from methods.order import create_order


def test_create_order():
    response = create_order()
    assert response.status_code == 200
    assert isinstance(response.json()['order_id'], str)
    assert isinstance(response.json()['order_number'], str)
