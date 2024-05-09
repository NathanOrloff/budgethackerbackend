from aws_solutions_constructs.aws_eventbridge_lambda import EventbridgeToLambda
from aws_cdk import (
    Stack,
   aws_events as events,
   aws_lambda as _lambda,
)
from constructs import Construct

class ApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        EventbridgeToLambda(self, 'test-eventbridge-lambda',
            lambda_function_props=_lambda.FunctionProps(
                code=_lambda.Code.from_asset('./compute'),
                runtime=_lambda.Runtime.PYTHON_3_10,
                id="EventBridge Lambda",
                handler='index.handler'
            ),
            event_rule_props=events.RuleProps(
                schedule=events.Schedule.expression(
                    'cron(0 0 0 * * ?)'
            ))
        )
        