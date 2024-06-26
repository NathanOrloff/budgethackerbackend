from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    RemovalPolicy
)
from constructs import Construct

class DatabaseStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id)
        self.stage = kwargs.get('stage', 'alpha')

        event_store = dynamodb.TableV2(self, f"budgethacker-EventStore-{self.stage}",
                                       partition_key=dynamodb.Attribute(name="pk", type=dynamodb.AttributeType.STRING),
                                       sort_key=dynamodb.Attribute(name="sk", type=dynamodb.AttributeType.STRING),
                                       removal_policy=RemovalPolicy.DESTROY
                                    )

        transactions_db = dynamodb.TableV2(self, f"budgethacker-Transactions-{self.stage}",
                                       partition_key=dynamodb.Attribute(name="pk", type=dynamodb.AttributeType.STRING),
                                       sort_key=dynamodb.Attribute(name="sk", type=dynamodb.AttributeType.STRING),
                                       removal_policy=RemovalPolicy.DESTROY
                                    )

        user_info_db = dynamodb.TableV2(self, f"budgethacker-UserInfo-{self.stage}",
                                       partition_key=dynamodb.Attribute(name="pk", type=dynamodb.AttributeType.STRING),
                                       sort_key=dynamodb.Attribute(name="sk", type=dynamodb.AttributeType.STRING),
                                       removal_policy=RemovalPolicy.DESTROY
                                    )