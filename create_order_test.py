#Ольга Антипова, 5-я когорта - Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import sender_stand_request
import data


def test_get_order_body(track):
    current_body = data.order_body.copy()
    current_body["track"] = track
    return current_body


# Get order track
def test_get_order_track():
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TABLE_PATH)


response = data.order_track()
print(response.text)


# Get order
def test_get_order_by_track():
    order_body = test_get_order_track("track")
    order_response = sender_stand_request.post_new_order(order_body)
    assert order_response.status_code == 200

