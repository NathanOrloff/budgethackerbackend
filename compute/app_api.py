import boto3
from botocore.exceptions import ClientError
import jwt
import logging
import constants
import utils


def get_transactions_by_date():
    '''
    Returns json of transactions from supplied date till current.
    If date is further back than last transaction, returns all transactions
    '''

def get_transactions_by_pfc():
    '''
    Returns json of all transactions that match the personal finance category
    provided.
    '''

def update_transactions():
    '''
    Updates transaction in database for any transactions that have been modified.
    Pass in list of modified transactions, returns success or failure.
    '''

def add_transactions():
    '''
    Adds new transactions to the database. Pass in a list of transactions,
    returns success or failure.
    '''

def remove_transactions():
    '''
    Remove transactions from the database. Pass in list of transaction ids,
    returns success or failure.
    '''

def update_database():
    '''
    Automated job called nightly to retrieve recent transactions from bank, and
    update the datebase with the changes [added, modified, removed].
    '''

def create_user():
    '''
    Create a user and add them to the User Info DB
    '''
    # user cognito token to get username and email, generate unique key, store access token in secrets manager
    # inputs are cookie token and public_token - should exchange public_token for access token

def delete_user():
    '''
    Remove a user from the User Info DB. (Maybe should remove their transaction info too).
    '''

def _get_user():
    '''
    Get user by using the log in token from Cognito.
    '''

def _get_access_token():
    '''
    Retrieve access token stored in secrets manager.
    '''

def get_user_budget():
    '''
    Get user budget stored in User Info DB
    '''


if __name__=="__main__":
    id_token = 'eyJraWQiOiJnbzNFVXdpZXdQWCtmRGp3MEh1NEVod0JlOFhvTHRKQ2FJYTVVcEZiOWNnPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiMm4tcS1kY0R6SlVyb3JxXzdHVF80ZyIsInN1YiI6IjNiNjRlNzg4LTA5NTYtNGQ1My05ZTQ2LWYzODQyY2M0NjJkNiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb21cL3VzLXdlc3QtMl91dkNxR0xPSjEiLCJjb2duaXRvOnVzZXJuYW1lIjoidGVzdF9uYXRoYW40IiwiYXVkIjoiM25jYXFnZ2MzaDVzOWo5a25sZnYxOWpyOGEiLCJldmVudF9pZCI6ImIzMmI5OWYyLTQ3YzQtNDYyNi1iOWJiLTk3MDI3NmVjZGRkNCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzE0OTU4NDU0LCJleHAiOjE3MTQ5NjIwNTQsImlhdCI6MTcxNDk1ODQ1NCwianRpIjoiNWVkYWRhODYtNzg3OC00YTFmLTg4NzUtNWM1YjQzYTMyMzg4IiwiZW1haWwiOiJuYXRoYW5jb3Jsb2ZmK3Rlc3Rjb2duaXRvNkBnbWFpbC5jb20ifQ.o_SLaT8KsyyWKB5D63HkPLocssA9hH--6g5IcPOc-TfBflfs-id8kPlrHdfp8YYnJar7vVHyo6L0Yk9lXy2-h3HBuYHvCV6Av3v2DQYzcPQU58cNak14ABI5A7c4G3LUIvnLDq0fJF_slXCl-eOmaBuWm3MdPc5eb0nkjB1NexQ7cRo4YCttAtns7TnuyofLxJOpU4jMilZ65f7mpAVbrr4M89hdK78ALTivkAs1YCUgesW_yovMCU36myO-j0lQ_Ah1vyxTyYDkS7eaKAaRSk2a0uKvnIfGVvXoxkT_UHZoSYofhYOQcqKIjjPInMaUoi7PRxXTphFNKZqyK7e2Cg'
    decoded_data = jwt.decode(jwt=id_token,
                              options={"verify_signature": False})
    import pprint
    pprint.pprint(decoded_data)

    # use scope openID /oauth2/userInfo to get user info,
    # no need to decode id token. just pass access token