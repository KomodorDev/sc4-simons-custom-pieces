"""Finite identities for the original and opposite-direction DD RHW Y families."""
ORIGINAL = 'original'
REVERSED = 'reversed'
VARIANTS = (ORIGINAL, REVERSED)
ROLES = ('diagonal-stem-split', 'diagonal-branch', 'orthogonal-core')
ASSEMBLIES = {
    ORIGINAL: 'ddrhw-compact-diagonal-y-junction',
    REVERSED: 'ddrhw-compact-diagonal-y-junction-reversed',
}


def _variant(value):
    if not isinstance(value, str) or value not in VARIANTS:
        raise ValueError('Unknown DD RHW Y variant')
    return value


def records_for(variant=ORIGINAL):
    """Return exact source identities; geometry ownership is measured separately."""
    variant = _variant(variant)
    qualifier = '' if variant == ORIGINAL else 'reversed-'
    return [{'id': 'ddrhw-y-' + qualifier + role,
             'recipe': 'highway_ddrhw_y_' + ('' if variant == ORIGINAL else 'reversed_') + role.replace('-', '_'),
             'geometry_key': 'y-' + qualifier + role,
             'role': role, 'variant': variant}
            for role in ROLES]


def identities_for(variant=ORIGINAL):
    return {row['id']: row['geometry_key'] for row in records_for(variant)}


def assembly_for(variant=ORIGINAL):
    return ASSEMBLIES[_variant(variant)]


def variant_for_id(identifier):
    matches = [variant for variant in VARIANTS if identifier in identities_for(variant)]
    if len(matches) != 1:
        raise ValueError('Unknown DD RHW Y component identity')
    return matches[0]


def variant_of(piece):
    """Never admit a future recipe merely because it shares the Y prefix."""
    variant = variant_for_id(piece.get('id'))
    expected = next(row for row in records_for(variant) if row['id'] == piece['id'])
    if piece.get('recipe') != expected['recipe']:
        raise ValueError('Y component recipe disagrees with its exact variant identity')
    if piece.get('y_junction_variant', ORIGINAL) != variant:
        raise ValueError('Y component needs its exact explicit traffic variant')
    if 'geometry_key' in piece and piece['geometry_key'] != expected['geometry_key']:
        raise ValueError('Y component geometry key disagrees with its traffic variant')
    if piece.get('domain', 'highway') != 'highway':
        raise ValueError('Y components belong to the highway domain')
    return variant
