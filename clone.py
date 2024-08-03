import os
from dotenv import load_dotenv
import ynab_api
from ynab_api.api import budgets_api

load_dotenv()
YNAB_API_KEY = os.getenv('YNAB_API_KEY')

configuration = ynab_api.Configuration(
    host="https://api.youneedabudget.com/v1"
)

configuration.api_key['bearer'] = YNAB_API_KEY
configuration.api_key_prefix['bearer'] = 'Bearer'


# Enter a context with an instance of the API client
with ynab_api.ApiClient(configuration) as api_client:

    api_instance = budgets_api.BudgetsApi(api_client)

    budget_id = "budget_id_example"
    include_accounts = True

    api_response = api_instance.get_budgets(include_accounts=include_accounts)
    print(api_response)
