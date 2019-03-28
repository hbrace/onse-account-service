from behave import given, when, then

from features.steps.get_account import get_account_by_context, \
    assert_account_details

CREATE_ACCOUNT_URL = f'/accounts/'


@when('I update the status of an account with id "{account_number}" to "{status}"')
def update_account(context, account_number, status):
    response = context.web_client.put(
        f'/accounts/{account_number}',
        json={'status': status})

    assert response.status_code == 200, response.status_code


@then('Account with id "{account_number}" should be "{status}"')
def get_account_status(context, account_number, status):
    response = context.web_client.get(f'/accounts/{account_number}')
    assert response.status_code == 200, response.status_code
    account = response.get_json()
    assert account['accountStatus'] == status, account
