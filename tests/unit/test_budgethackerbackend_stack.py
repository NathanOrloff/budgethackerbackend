import aws_cdk as core
import aws_cdk.assertions as assertions

from budgethackerbackend.budgethackerbackend_stack import BudgethackerbackendStack

# example tests. To run these tests, uncomment this file along with the example
# resource in budgethackerbackend/budgethackerbackend_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BudgethackerbackendStack(app, "budgethackerbackend")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
