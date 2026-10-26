"""Preserve source-backed endpoint occurrences without inferring game tolerance.

The SC4PATH byte fixtures below are artificial routes. They establish extraction
behavior for coincident directions, geometries, and engine classes, not a tested
Street contract or evidence of operation inside SimCity 4.
"""
import unittest

from scp.connectivity import PATH, _routes, piece_connectivity


def encoded(routes):
    lines = ['SC4PATHS', '1.2', str(len(routes)), '0', '0']
    for engine, entry, exit_, points in routes:
        lines += [str(engine), '0', str(entry), str(exit_), '0', str(len(points))]
        lines += [','.join(str(value) for value in point) for point in points]
    return ('\n'.join(lines)+'\n').encode('ascii')


def subject(cells=((0, 0),)):
    return {'id': 'synthetic-endpoints', 'footprint': [1, len(cells)],
            'cells': [list(cell) for cell in cells],
            'tile_ids': [f'{0x7f500000+16*index:08x}' for index in range(len(cells))]}


def extract(routes):
    piece = subject()
    return piece_connectivity(piece, {(*PATH, 0x7f500000): encoded(routes)})


class EndpointOccurrenceTests(unittest.TestCase):
    def test_one_bidirectional_channel_retains_both_flows_at_each_position(self):
        west, east = (-8., 0., 15.5), (8., 0., 15.5)
        result = extract([(7, 0, 2, [west, east]), (7, 2, 0, [east, west])])
        self.assertEqual(len(result['ports']), 4)
        for point in (west, east):
            self.assertEqual({p['direction'] for p in result['ports'] if p['endpoint_m'] == list(point)}, {'in', 'out'})
        self.assertEqual(len(result['journeys']), 2)
        ports = {p['id']: p for p in result['ports']}
        for journey in result['journeys']:
            self.assertNotEqual(ports[journey['entry_port']]['endpoint_m'], ports[journey['exit_port']]['endpoint_m'])

    def test_shared_entry_position_keeps_distinct_heading_and_journey(self):
        south = (0., -8., 15.5)
        result = extract([(7, 3, 2, [south, (0., -4., 15.5), (8., 0., 15.5)]),
                          (7, 3, 0, [south, (4., -4., 15.5), (-8., 0., 15.5)])])
        entries = [p for p in result['ports'] if p['direction'] == 'in']
        self.assertEqual(len(entries), 2)
        self.assertEqual(len({tuple(p['tangent']) for p in entries}), 2)
        self.assertEqual(len({p['id'] for p in result['ports']}), 4)
        for port in entries:
            journeys = [j for j in result['journeys'] if j['entry_port'] == port['id']]
            self.assertEqual(len(journeys), 1)
            target = next(p for p in result['ports'] if p['id'] == journeys[0]['exit_port'])
            self.assertEqual(target['endpoint_m'][0], 8. if port['tangent'] == [0., 1.] else -8.)

    def test_shared_entry_position_keeps_distinct_grade(self):
        south = (0., -8., 15.5)
        result = extract([(7, 3, 2, [south, (0., -4., 15.5), (8., 0., 15.5)]),
                          (7, 3, 0, [south, (0., -4., 16.5), (-8., 0., 17.5)])])
        entries = [p for p in result['ports'] if p['direction'] == 'in']
        self.assertEqual({p['grade'] for p in entries}, {0., .25})
        self.assertEqual(len(result['journeys']), 2)

    def test_coincident_engine_classes_remain_separate_movements(self):
        west, east = (-8., 0., 0.), (8., 0., 0.)
        result = extract([(1, 0, 2, [west, east]), (2, 0, 2, [west, east])])
        self.assertEqual(len(result['ports']), 4)
        self.assertEqual({tuple(j['engine_transport_classes']) for j in result['journeys']}, {(1,), (2,)})
        ports = {p['id']: p for p in result['ports']}
        for journey in result['journeys']:
            self.assertEqual(ports[journey['entry_port']]['engine_transport'], ports[journey['exit_port']]['engine_transport'])

    def test_bidirectional_internal_tile_seam_does_not_become_a_uturn(self):
        piece = subject(((0, 0), (0, 1)))
        routes = [(7, 3, 1, [(0., -8., 15.5), (0., 8., 15.5)]),
                  (7, 1, 3, [(0., 8., 15.5), (0., -8., 15.5)])]
        result = piece_connectivity(piece, {(*PATH, int(tile, 16)): encoded(routes) for tile in piece['tile_ids']})
        self.assertEqual(len(result['ports']), 4)
        self.assertEqual(len(result['journeys']), 2)
        ports = {p['id']: p for p in result['ports']}
        for journey in result['journeys']:
            self.assertEqual(abs(ports[journey['entry_port']]['endpoint_m'][1]-ports[journey['exit_port']]['endpoint_m'][1]), 32.)

    def test_raw_route_identity_references_saved_tile_and_record(self):
        piece = subject()
        raw = encoded([(7, 0, 2, [(-8., 0., 15.5), (8., 0., 15.5)])])
        route = _routes(piece, {(*PATH, 0x7f500000): raw})[0]
        self.assertEqual(route['id'], 'path-7f500000-route-000')
        self.assertEqual(route['source_route_index'], 0)
        self.assertEqual(route['source_class'], 0)
        self.assertEqual(route['compatibility'], 0)
        self.assertEqual(route['cell'], [0, 0])


if __name__ == '__main__':
    unittest.main()
