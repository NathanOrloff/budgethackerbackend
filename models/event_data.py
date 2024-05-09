from schema import Schema, And, Use, SchemaError
from models.transaction import Transaction
from models.user_info import UserInfo

class EventDataException(Exception):
    pass


class EventData:

    SCHEMA = Schema({
        'version': And(Use(int)),
        'info': {
            'type': And(
                Use(str),
                lambda t: t in ['user_info', 'transaction']
            ),
            'time': And(Use(str)),
            'event': And(
                Use(dict),
                lambda d: (UserInfo.check_schema(d) or Transaction.check_schema(d))
            )
        }
    })


    def __init__(self, data):
        if not EventData.check_schema(data):
            raise EventDataException("Invalid event data")
        self.data = data

    
    @staticmethod
    def check_schema(data):
        try:
            EventData.SCHEMA.validate(data)
            return True
        except SchemaError:
            return False
