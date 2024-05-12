import pytest
import datetime
from models import budget, event_data, transaction, user_info


def test_budget_model():
    good_budget = {
        'version': 1,
        'info': {
            'budget': {
                'category1': 10.5,
                'category2': 50.2,
                'category3': 300.1,
                'category4': 2
            }
        }
    }
    obj = budget.Budget(good_budget)
    assert budget.Budget.check_schema(good_budget)


def test_bad_budget():
    bad_budget = {
        'version': "string",
        'info': {
            'budget': [
                ('category1', 10.5),
                ('category2', 50.2),
                ('category3', 300.1),
                ('category4', 2)
            ]
        }
    }
    assert not budget.Budget.check_schema(bad_budget)


def test_transaction_model():
    good_transaction = {
        'version': 1,
        'info': {
            "account_id": "BxBXxLj1m4HMXBm9WZZmCWVbPjX16EHwv99vp",
            "account_owner": None,
            "amount": 72.1,
            "iso_currency_code": "USD",
            "unofficial_currency_code": None,
            "category": [
                "Shops",
                "Supermarkets and Groceries"
            ],
            "category_id": "19046000",
            "check_number": None,
            "counterparties": [
                {
                    "name": "Walmart",
                    "type": "merchant",
                    "logo_url": "https://plaid-merchant-logos.plaid.com/walmart_1100.png",
                    "website": "walmart.com",
                    "entity_id": "O5W5j4dN9OR3E6ypQmjdkWZZRoXEzVMz2ByWM",
                    "confidence_level": "VERY_HIGH"
                }
            ],
            "date": "2023-09-24",
            "datetime": "2023-09-24T11:01:01Z",
            "authorized_date": "2023-09-22",
            "authorized_datetime": "2023-09-22T10:34:50Z",
            "location": {
                "address": "13425 Community Rd",
                "city": "Poway",
                "region": "CA",
                "postal_code": "92064",
                "country": "US",
                "lat": 32.959068,
                "lon": -117.037666,
                "store_number": "1700"
            },
            "name": "PURCHASE WM SUPERCENTER #1700",
            "merchant_name": "Walmart",
            "merchant_entity_id": "O5W5j4dN9OR3E6ypQmjdkWZZRoXEzVMz2ByWM",
            "logo_url": "https://plaid-merchant-logos.plaid.com/walmart_1100.png",
            "website": "walmart.com",
            "payment_meta": {
                "by_order_of": None,
                "payee": None,
                "payer": None,
                "payment_method": None,
                "payment_processor": None,
                "ppd_id": None,
                "reason": None,
                "reference_number": None
            },
            "payment_channel": "in store",
            "pending": False,
            "pending_transaction_id": "no86Eox18VHMvaOVL7gPUM9ap3aR1LsAVZ5nc",
            "personal_finance_category": {
                "primary": "GENERAL_MERCHANDISE",
                "detailed": "GENERAL_MERCHANDISE_SUPERSTORES",
                "confidence_level": "VERY_HIGH"
            },
            "personal_finance_category_icon_url": "https://plaid-category-icons.plaid.com/PFC_GENERAL_MERCHANDISE.png",
            "transaction_id": "lPNjeW1nR6CDn5okmGQ6hEpMo4lLNoSrzqDje",
            "transaction_code": None,
            "transaction_type": "place"
        }
    }
    obj = transaction.Transaction(good_transaction)
    assert transaction.Transaction.check_schema(good_transaction)


def test_transaction_bad():
    bad_transaction = {
        'version': 1,
        'info': {
            "account_id": "BxBXxLj1m4HMXBm9WZZmCWVbPjX16EHwv99vp",
            "account_owner": None,
            "amount": 72.1,
            "iso_currency_code": "USD",
            "unofficial_currency_code": None,
            "category": [
                "Shops",
                "Supermarkets and Groceries"
            ],
            "category_id": "19046000",
            "check_number": None,
            "counterparties": [
                {
                    "name": "Walmart",
                    "type": "merchant",
                    "logo_url": "https://plaid-merchant-logos.plaid.com/walmart_1100.png",
                    "website": "walmart.com",
                    "entity_id": "O5W5j4dN9OR3E6ypQmjdkWZZRoXEzVMz2ByWM",
                    "confidence_level": "VERY_HIGH"
                }
            ],
            "date": "2023-09-24",
            "datetime": "2023-09-24T11:01:01Z",
            "authorized_date": "2023-09-22",
        }
    }
    assert not transaction.Transaction.check_schema(bad_transaction)


def test_user_info_model():
    good_user_info = {
        'version': 1,
        'info': {
            'uuid': 'aaaa-bbbb-cccc-dddd',
            'email': 'example_email@gmail.com',
            'username': 'example',
            'secret': 'asddfhujkds;fl28364;sdafg12!!'
        }
    }
    obj = user_info.UserInfo(good_user_info)
    assert user_info.UserInfo.check_schema(good_user_info)


def test_user_info_bad():
    bad_user_info = {
        'version': 1,
        'info': {
            'uuid': 'aaaa-bbbb-cccc-dddd',
            'email': 'example_email@gmail.com',
            'secret': 'asddfhujkds;fl28364;sdafg12!!'
        }
    }
    assert not user_info.UserInfo.check_schema(bad_user_info)


def test_event_data_model():
    good_user_info = {
        'version': 1,
        'info': {
            'uuid': 'aaaa-bbbb-cccc-dddd',
            'email': 'example_email@gmail.com',
            'username': 'example',
            'secret': 'asddfhujkds;fl28364;sdafg12!!'
        }
    }
    good_event_data = {
        'version': 1,
        'info': {
            'type': 'user_info',
            'time': datetime.datetime.now().isoformat(),
            'event': good_user_info
        }
    }
    obj = event_data.EventData(good_event_data)
    assert event_data.EventData.check_schema(good_event_data)


def test_event_data_bad():
    good_user_info = {
        'version': 1,
        'info': {
            'uuid': 'aaaa-bbbb-cccc-dddd',
            'email': 'example_email@gmail.com',
            'username': 'example',
            'secret': 'asddfhujkds;fl28364;sdafg12!!'
        }
    }
    bad_event_data = {
        'version': 1,
        'info': {
            'type': 'budget',
            'time': datetime.datetime.now().isoformat(),
            'event': good_user_info
        }
    }
    assert not event_data.EventData.check_schema(bad_event_data)
