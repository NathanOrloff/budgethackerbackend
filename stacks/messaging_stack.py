from aws_cdk import (
    Stack,
   aws_sns as sns,
   aws_sns_subscriptions as subscriptions,
   aws_sqs as sqs,
   aws_lambda as _lambda,
   aws_lambda_event_sources
)
from constructs import Construct

class MessagingStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id)
        self.stage = kwargs.get('stage', 'alpha')

        topic = sns.Topic(self, f"budgethacker-EventDistribution-{self.stage}",
            content_based_deduplication=True,
            display_name="Event distribution topic",
            fifo=True
        )

        transactions_queue = sqs.Queue(self, f"budgethacker-Transactions-{self.stage}",
            fifo=True
        )
        user_info_queue = sqs.Queue(self, f"budgethacker-UserInfo-{self.stage}",
            fifo=True
        )


        topic.add_subscription(subscriptions.SqsSubscription(transactions_queue,
            filter_policy={
                "type": sns.SubscriptionFilter.string_filter(
                    allowlist=["transactions"]
                ),
            }
        ))

        topic.add_subscription(subscriptions.SqsSubscription(user_info_queue,
            filter_policy={
                "type": sns.SubscriptionFilter.string_filter(
                    allowlist=["user_info"]
                ),
            }
        ))

        update_transactions_db = _lambda.Function(
                                        self,
                                        id=f"budgethacker-UpdateTransactionsDb-{self.stage}",
                                        code=_lambda.Code.from_asset("./compute"),
                                        handler="test_api.hello_world",
                                        runtime=_lambda.Runtime.PYTHON_3_10
                                    )
        
        transactions_lambda_event_src = aws_lambda_event_sources.SqsEventSource(
            transactions_queue
        )

        update_transactions_db.add_event_source(transactions_lambda_event_src)

        update_user_info_db = _lambda.Function(
                                    self,
                                    id=f"budgethacker-UpdateUserInfo-{self.stage}",
                                    code=_lambda.Code.from_asset("./compute"),
                                    handler="test_api.hello_world",
                                    runtime=_lambda.Runtime.PYTHON_3_10
                                )
        
        user_info_lambda_event_src = aws_lambda_event_sources.SqsEventSource(
            user_info_queue
        )

        update_user_info_db.add_event_source(user_info_lambda_event_src)

