from aws_cdk import (
    Stack,
   aws_lambda,
   aws_apigateway,
   aws_apigatewayv2
)
from constructs import Construct

class ApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id)
        self.stage = kwargs.get('stage', 'alpha')

        register_new_user_lambda = aws_lambda.Function(
            self,
            id=f"budgethacker-RegisterNewUser-{self.stage}",
            code=aws_lambda.Code.from_asset("./compute"),
            handler="test_api.hello_world",
            runtime=aws_lambda.Runtime.PYTHON_3_10
        )
        set_user_budget_lambda = aws_lambda.Function(
            self,
            id=f"budgethacker-SetUserBudget-{self.stage}",
            code=aws_lambda.Code.from_asset("./compute"),
            handler="test_api.hello_world",
            runtime=aws_lambda.Runtime.PYTHON_3_10
        )
        get_transactions_by_date_lambda = aws_lambda.Function(
            self,
            id=f"budgethacker-GetTransactionsByDate-{self.stage}",
            code=aws_lambda.Code.from_asset("./compute"),
            handler="test_api.hello_world",
            runtime=aws_lambda.Runtime.PYTHON_3_10
        )
        get_transactions_by_type_lambda = aws_lambda.Function(
            self,
            id=f"budgethacker-GetTransactionsByType-{self.stage}",
            code=aws_lambda.Code.from_asset("./compute"),
            handler="test_api.hello_world",
            runtime=aws_lambda.Runtime.PYTHON_3_10
        )
        get_user_budget_lambda = aws_lambda.Function(
            self,
            id=f"budgethacker-GetUserBudget-{self.stage}",
            code=aws_lambda.Code.from_asset("./compute"),
            handler="test_api.hello_world",
            runtime=aws_lambda.Runtime.PYTHON_3_10
        )