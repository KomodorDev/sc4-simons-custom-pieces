#!/usr/bin/env python3
"""Report complete-boundary candidates across fresh registered library exports."""
import argparse
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
PLANNER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLANNER / 'src'))

from scp_planner._source import configured_root
from scp_planner.discovery import discover_compatibility


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--custom-pieces-root', type=Path,
                        help='Data root; must match SCP_CUSTOM_PIECES_ROOT or the configured library code root')
    parser.add_argument('--domain', default='high-speed-rail', help='Exact registered transport-domain ID')
    parser.add_argument('--piece', help='Keep this registered piece fixed and search every eligible candidate type')
    parser.add_argument('--boundary', help='Exact complete boundary ID on --piece; never an individual service group')
    parser.add_argument('--report', type=Path, default=PLANNER / 'local/compatibility/report.json')
    args = parser.parse_args(argv)
    destination = args.report.expanduser().resolve()
    if not destination.is_relative_to((PLANNER / 'local').resolve()):
        parser.error('Generated compatibility reports must stay below scp-planner/local')
    try:
        report = discover_compatibility(args.custom_pieces_root or configured_root(),
                                        domain_id=args.domain, query_piece_id=args.piece,
                                        query_boundary_id=args.boundary)
    except (ValueError, OSError, ImportError) as error:
        parser.error(str(error))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
    print(json.dumps({'status': report['status'], 'domain': report['domain_id'],
                      'query': report['query'], 'counts': report['counts'],
                      'unverified': report['checks_not_established'],
                      'report': str(destination)}, indent=2))


if __name__ == '__main__':
    main()
