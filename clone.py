import os
from dotenv import load_dotenv
import ynab_api
from pprint import pprint
from ynab_api.api import accounts_api
from ynab_api.model.save_account_wrapper import SaveAccountWrapper
from ynab_api.model.save_account import SaveAccount

load_dotenv()
YNAB_API_KEY = os.getenv('YNAB_API_KEY')

configuration = ynab_api.Configuration(
    host="https://api.youneedabudget.com/v1"
)

configuration.api_key['bearer'] = YNAB_API_KEY
configuration.api_key_prefix['bearer'] = 'Bearer'


# Enter a context with an instance of the API client
with ynab_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    budget_id = "budget_id_example"  # str, none_type | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
    data = SaveAccountWrapper(
        account=SaveAccount(
            name="name_example",
            type="checking",
            balance=1,
        ),
    )  # SaveAccountWrapper | The account to create.

    try:
        # Create a new account
        api_response = api_instance.create_account(budget_id, data)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling AccountsApi->create_account: %s\n" % e)
