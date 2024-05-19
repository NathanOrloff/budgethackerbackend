from aws_cdk import (
    Stack,
    aws_cognito as cognito,
    RemovalPolicy
)
from constructs import Construct

class CognitoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id)
        self.stage = kwargs.get('stage', 'alpha')

        userpool = cognito.UserPool(self, f"budgethacker-userpool-{self.stage}", 
            user_pool_name=f'budgethacker-{self.stage}-user-pool',
            sign_in_aliases={
                'username': True,
                'email': True
            },
            self_sign_up_enabled=True,
            auto_verify={
                'email': True
            },
            user_verification={
                'email_subject': 'You need to verify your email',
                'email_body': 'Thanks for signing up Your verification code is {####}',
                'email_style': cognito.VerificationEmailStyle.CODE, 
            },
            account_recovery=cognito.AccountRecovery.EMAIL_ONLY,
            removal_policy=RemovalPolicy.DESTROY,
        )

        client = userpool.add_client(f"budgerhacker-client-{self.stage}",
            o_auth=cognito.OAuthSettings(
                flows=cognito.OAuthFlows(
                    implicit_code_grant=True
                ),
                callback_urls=[
                    "https://example.com/"
                ],
                scopes=[
                    cognito.OAuthScope.OPENID,
                    cognito.OAuthScope.EMAIL,
                    cognito.OAuthScope.PHONE,
                    cognito.OAuthScope.PROFILE
                ]
            )
        )

        domain = userpool.add_domain(f"budgethacker-domain-{self.stage}", 
            cognito_domain={
                'domain_prefix': "budgethacker"
            }                                     
        )
        sign_in_url = domain.sign_in_url(client,
            redirect_uri="https://example.com/"    
        )




       