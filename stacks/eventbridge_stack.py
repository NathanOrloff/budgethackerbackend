from aws_solutions_constructs.aws_eventbridge_lambda import EventbridgeToLambda
from aws_cdk import (
    Stack,
   aws_events as events,
   aws_lambda as _lambda,
)
from constructs import Construct

class EventbridgeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id)
        self.stage = kwargs.get('stage', 'alpha')

        EventbridgeToLambda(self, f'budgethacker-Eventbridgelambda-{self.stage}',
            lambda_function_props=_lambda.FunctionProps(
                code=_lambda.Code.from_asset('./compute'),
                runtime=_lambda.Runtime.PYTHON_3_10,
                handler='test_api.hello_world'
            ),
            event_rule_props=events.RuleProps(
                schedule=events.Schedule.cron(
                        day="*",
                        hour="0",
                        minute="0",
                        month="*"
            ))
        )
        