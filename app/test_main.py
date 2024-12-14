import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,expected",
    [
        pytest.param(
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"],
            id="product is outdated when expiration date < today date"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 210
                }
            ],
            [],
            id="product is not outdated when expiration date = today date"
        ),
        pytest.param(
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 140
                }
            ],
            [], id="product is not outdated when expiration date > today date"
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mocked_datetime: mock.MagicMock,
        products: list,
        expected: list
) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == expected
