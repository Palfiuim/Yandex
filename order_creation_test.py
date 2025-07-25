# Гришин Антон,  — Финальный проект.
from sendor_stand_request import create_order, get_order_by_track
import data

def test_order_creation():
    response = create_order(data.order_body)
    assert response.status_code == 201

    track = response.json()["track"]
    order_response = get_order_by_track(track)
    assert order_response.status_code == 200
