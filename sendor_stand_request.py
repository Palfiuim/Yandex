# Гришин Антон— Финальный проект. Инженер по тестированию плюс
import requests
import configuration

def create_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREAT_ORDERS,
        json=body
    )

def get_order_by_track(track_number):
    return requests.get(
        f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    )
