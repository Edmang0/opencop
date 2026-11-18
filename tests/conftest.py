from __future__ import annotations

from pathlib import Path

import pytest

# TODO(Milestone 1): restore these imports and _make_point once opencop.domain exists.
# from opencop.domain import Domain, Source, TrackPoint
# from opencop.geo import Position

FIXTURES = Path(__file__).parent / "fixtures"

# MakePoint = Callable[..., TrackPoint]


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES


# def _make_point(
#     ident: str = "D1",
#     ts: float = 1_000.0,
#     lat: float = 40.6,
#     lon: float = -74.0,
#     domain: Domain = Domain.DRONE,
#     speed_mps: float | None = 10.0,
#     course_deg: float | None = 90.0,
#     alt_m: float | None = 100.0,
#     label: str | None = None,
# ) -> TrackPoint:
#     return TrackPoint(
#         domain=domain,
#         ident=ident,
#         ts=ts,
#         pos=Position(lat, lon),
#         speed_mps=speed_mps,
#         course_deg=course_deg,
#         alt_m=alt_m,
#         source=Source.SIM,
#         label=label,
#     )
#
#
# @pytest.fixture
# def make_point() -> MakePoint:
#     """Factory fixture: call make_point(ident="X", ts=5.0, ...) inside a test."""
#     return _make_point
