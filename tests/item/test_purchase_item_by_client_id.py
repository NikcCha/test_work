import pytest
from methods.purchase_item_by_client_id import purchase_item_by_client_id
from datetime import date


@pytest.mark.parametrize(
    'client_id, item_id, expected_count',
    [
        ('94d0a63b-db2a-4da2-95e7-187f2d5459d4', '459672186', 5),
        ('94d0a63b-db2a-4da2-95e7-187f2d5459d4', '100883501248', 8)
    ]
)
def purchase_item_by_client_id(client_id, item_id, expected_count):
    response = purchase_item_by_client_id(client_id, item_id)
    today = date.today()
    assert response.status_code == 200
    assert response.items[0].item_id == item_id
    assert response.items[0].purchase_count == expected_count
    assert response.items[0].last_purchase_date == today
