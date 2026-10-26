"""Explicit human layout-review flags, separate from binary correctness.

An encoded route can be connected and clear while still being a poor design.
Flags do not rename a permanent piece or change its saved-city model assets.
"""
from .dbpf import require

LABELS = {
    'needs-redesign': 'NEEDS REDESIGN',
    'review-needed': 'REVIEW NEEDED',
}


def validate_review(piece):
    review = piece.get('design_review')
    if review is None:
        return
    require(isinstance(review, dict) and review.get('status') in LABELS,
            f'{piece.get("id")}: invalid design review status')
    require(isinstance(review.get('summary'), str) and review['summary'].strip(),
            f'{piece.get("id")}: design review needs a plain-language summary')
    reasons = review.get('reasons')
    require(isinstance(reasons, list) and reasons and
            all(isinstance(reason, str) and reason.strip() for reason in reasons),
            f'{piece.get("id")}: design review needs specific reasons')


def review_label(piece):
    review = piece.get('design_review')
    return LABELS[review['status']] if review else ''


def review_note(piece):
    review = piece.get('design_review')
    if not review:
        return ''
    return review_label(piece) + ': ' + review['summary']
