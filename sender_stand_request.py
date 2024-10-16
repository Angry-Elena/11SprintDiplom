import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_POST,
                         json=body,
                         headers=data.headers)


def get_order(parameters):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_GET,
                        params=parameters)