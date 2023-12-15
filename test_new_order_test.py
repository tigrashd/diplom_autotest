import request_order
import pytest


def test_order_info ():
    track = request_order.ceate_new_order()
    requests = request_order.order_track_info(str(track)).status_code
    exp = 200
    assert requests == exp

#  Игорь Ченчик, 11-я когорта — Финальный проект. Инженер по тестированию плюс



