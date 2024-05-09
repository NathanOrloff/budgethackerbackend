from schema import Schema, And, Use, SchemaError

class BudgetException(Exception):
    pass


class Budget:

    SCHEMA = Schema({
        'version': And(Use(int)),
        'info': {
            'budget': And(Use(list))
        }
    })


    def __init__(self, data):
        if not Budget.check_schema(data):
            raise BudgetException("Invalid budget data")
        self.data = data


    @staticmethod
    def check_schema(data):
        try:
            Budget.SCHEMA.validate(data)
            return True
        except SchemaError:
            return False

