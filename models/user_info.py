from schema import Schema, And, Use, Optional, SchemaError
from models.budget import Budget

class UserInfoException(Exception):
    pass


class UserInfo:

    SCHEMA = Schema({
        'version': And(Use(int)),
        'info': {
            'uuid': And(Use(str)),
            'email': And(Use(str)),
            'username': And(Use(str)),
            'secret': And(Use(str)),
            Optional('budget'): And(
                Use(dict),
                lambda d: Budget.check_schema(d)      
            )
        }
    })


    def __init__(self, data):
        if not UserInfo.check_schema(data):
            raise UserInfoException("Invalid user info data")
        self.data = data

    
    @staticmethod
    def check_schema(data):
        try:
            UserInfo.SCHEMA.validate(data)
            return True
        except SchemaError:
            return False
