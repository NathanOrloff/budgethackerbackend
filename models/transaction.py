from schema import Schema, And, Use, SchemaError

class TransactionException(Exception):
    pass


class Transaction:

    SCHEMA = Schema({
        'version': And(Use(int)),
        'info': {
            "account_id": And(Use(str), None),
            "account_owner": And(Use(str), None),
            "amount": And(Use(float), None),
            "iso_currency_code": And(Use(str), None),
            "unofficial_currency_code": And(Use(str), None),
            "category": And(Use(list), None),
            "category_id": And(Use(str), None),
            "check_number": And(Use(str), None),
            "counterparties": [
                {
                    "name": And(Use(str), None),
                    "type": And(Use(str), None),
                    "logo_url": And(Use(str), None),
                    "website": And(Use(str), None),
                    "entity_id": And(Use(str), None),
                    "confidence_level": And(Use(str), None),
                }
            ],
            "date": And(Use(str), None),
            "datetime": And(Use(str), None),
            "authorized_date": And(Use(str), None),
            "authorized_datetime": And(Use(str), None),
            "location": {
                "address": And(Use(str), None),
                "city": And(Use(str), None),
                "region": And(Use(str), None),
                "postal_code": And(Use(str), None),
                "country": And(Use(str), None),
                "lat": And(Use(float), None),
                "lon": And(Use(float), None),
                "store_number": And(Use(str), None),
            },
            "name": And(Use(str), None),
            "merchant_name": And(Use(str), None),
            "merchant_entity_id": And(Use(str), None),
            "logo_url": And(Use(str), None),
            "website": And(Use(str), None),
            "payment_meta": {
                "by_order_of": And(Use(str), None),
                "payee": And(Use(str), None),
                "payer": And(Use(str), None),
                "payment_method": And(Use(str), None),
                "payment_processor": And(Use(str), None),
                "ppd_id": And(Use(str), None),
                "reason": And(Use(str), None),
                "reference_number": And(Use(str))
            },
            "payment_channel": And(Use(str), None),
            "pending": And(Use(bool), None),
            "pending_transaction_id": And(Use(str), None),
            "personal_finance_category": {
                "primary": And(Use(str), None),
                "detailed": And(Use(str), None),
                "confidence_level": And(Use(str), None),
            },
            "personal_finance_category_icon_url": And(Use(str), None),
            "transaction_id": And(Use(str), None),
            "transaction_code": And(Use(str), None),
            "transaction_type": And(Use(str), None),
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
