#Елена Парахина, кагорта 22, 11 спринт Диплом
import data
import sender_stand_request

def create_order():
    current_body = data.order_body.copy()
    track_num = sender_stand_request.post_new_order(current_body)
    return str(track_num.json()["track"])

def positive_assert():
    track_num = create_order()
    current_params = data.param_get.copy()
    current_params["t"] = track_num
    response = sender_stand_request.get_order(current_params)
    assert response.status_code == 200
    print("Заказ успешно создан. Номер трека заказа:" +track_num)

def test_order():
    positive_assert()