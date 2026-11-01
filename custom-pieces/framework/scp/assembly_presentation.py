"""Canonical assembly button names with an explicit presentation-only label."""
from .dbpf import require


def validate_variant_label(value):
    """Require a short label without a second title separator or hidden text."""
    require(isinstance(value, str) and 1 <= len(value) <= 64
            and value == value.strip() and value.isprintable()
            and '  ' not in value and '|' not in value and '—' not in value,
            'Assembly variant_label must be plain single-line text of one to 64 characters')
    return value


def canonical_cycle_title(scene_title, *, variant_label=None):
    """Preserve the canonical name, then append an explicitly declared label."""
    require(isinstance(scene_title, str) and scene_title.strip(),
            'Assembly cycle needs its canonical scene title')
    result = 'SCP | ASSEMBLY | ' + scene_title
    if variant_label is not None:
        label = validate_variant_label(variant_label)
        require(scene_title != label and not scene_title.endswith(' — ' + label),
                'Assembly variant_label duplicates the canonical scene title suffix')
        result += ' — ' + label
    return result


def validate_cycle_title(scene, cycle_button):
    """Require the exact canonical title and its optional declared qualifier."""
    require(isinstance(scene, dict) and isinstance(cycle_button, dict),
            'Assembly title validation needs a scene and cycle button')
    if 'variant_label' in cycle_button:
        validate_variant_label(cycle_button['variant_label'])
    expected = canonical_cycle_title(scene.get('title'),
                                     variant_label=cycle_button.get('variant_label'))
    require(cycle_button.get('title') == expected,
            'Assembly cycle title differs from its canonical scene title and explicit variant_label')
    return expected
