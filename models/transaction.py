from schema import Schema, And, Or, Use, SchemaError

class TransactionException(Exception):
    pass


class Transaction:

    SCHEMA = Schema({
        'version': And(Use(int)),
        'info': {
            "account_id": Or(Use(str), None),
            "account_owner": Or(Use(str), None),
            "amount": Or(Use(float), None),
            "iso_currency_code": Or(Use(str), None),
            "unofficial_currency_code": Or(Use(str), None),
            "category": Or(Use(list), None),
            "category_id": Or(Use(str), None),
            "check_number": Or(Use(str), None),
            "counterparties": [
                {
                    "name": Or(Use(str), None),
                    "type": Or(Use(str), None),
                    "logo_url": Or(Use(str), None),
                    "website": Or(Use(str), None),
                    "entity_id": Or(Use(str), None),
                    "confidence_level": Or(Use(str), None),
                }
            ],
            "date": Or(Use(str), None),
            "datetime": Or(Use(str), None),
            "authorized_date": Or(Use(str), None),
            "authorized_datetime": Or(Use(str), None),
            "location": {
                "address": Or(Use(str), None),
                "city": Or(Use(str), None),
                "region": Or(Use(str), None),
                "postal_code": Or(Use(str), None),
                "country": Or(Use(str), None),
                "lat": Or(Use(float), None),
                "lon": Or(Use(float), None),
                "store_number": Or(Use(str), None),
            },
            "name": Or(Use(str), None),
            "merchant_name": Or(Use(str), None),
            "merchant_entity_id": Or(Use(str), None),
            "logo_url": Or(Use(str), None),
            "website": Or(Use(str), None),
            "payment_meta": {
                "by_order_of": Or(Use(str), None),
                "payee": Or(Use(str), None),
                "payer": Or(Use(str), None),
                "payment_method": Or(Use(str), None),
                "payment_processor": Or(Use(str), None),
                "ppd_id": Or(Use(str), None),
                "reason": Or(Use(str), None),
                "reference_number": And(Use(str))
            },
            "payment_channel": Or(Use(str), None),
            "pending": Or(Use(bool), None),
            "pending_transaction_id": Or(Use(str), None),
            "personal_finance_category": {
                "primary": Or(Use(str), None),
                "detailed": Or(Use(str), None),
                "confidence_level": Or(Use(str), None),
            },
            "personal_finance_category_icon_url": Or(Use(str), None),
            "transaction_id": Or(Use(str), None),
            "transaction_code": Or(Use(str), None),
            "transaction_type": Or(Use(str), None),
        }
    })


    def __init__(self, data):
        if not Transaction.check_schema(data):
            raise TransactionException("Invalid transaction data")
        self.data = data

    
    @staticmethod
    def check_schema(data):
        try:
            Transaction.SCHEMA.validate(data)
            return True
        except SchemaError:
            return False
