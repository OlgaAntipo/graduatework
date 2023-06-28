#Ольга Антипова, 5-я когорта - Финальный проект. Инженер по тестированию плюс
import requests
import data
import configuration


# 1. Create order
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=data.headers)


response = post_new_order(data.order_body)


# 2. Save order number
def post_track_number(order_track):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_track,
                         headers=data.headers)


response = post_track_number(data.order_track)
print(response.json())
