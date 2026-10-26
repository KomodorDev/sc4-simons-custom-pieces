"""Common menu resource addresses and registered-domain menu dispatch."""
MENU_EXEMPLAR = (0x6534284A, 0x2A3858E4)
ICON = (0x856DDBAC, 0x6A386D26)
TITLE = (0x2026960B, 0x123007BB)
DESCRIPTION = (0x2026960B, 0x123006AA)


def build_menu_resources(donor, spec):
    from .providers import domain_module
    return domain_module(spec, 'menu').build_menu_resources(donor, spec)


def validate_menu_resources(resources, donor_exemplar, spec):
    from .providers import domain_module
    return domain_module(spec, 'menu').validate_menu_resources(resources, donor_exemplar, spec)
