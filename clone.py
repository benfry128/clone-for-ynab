import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()
YNAB_API_KEY = os.getenv('YNAB_API_KEY')
YNAB_URL = 'https://api.ynab.com/v1'
s = requests.Session()
s.headers.update({'Authorization': f'Bearer {YNAB_API_KEY}'})

old_id = '277f14e0-7fa0-4761-b14c-fbaa345e4175'
new_id = '27573c3a-9388-4e91-8098-4a786d13bcab'

budget = s.get(f'{YNAB_URL}/budgets/{old_id}').json()['data']['budget']
new_budget = s.get(f'{YNAB_URL}/budgets/{new_id}').json()['data']['budget']


# accounts = budget['accounts']

# for account in accounts:
#     acc = {
#         'account': {
#             'name': account['name'],
#             'type': account['type'],
#             'balance': 0
#         }
#     }
#     s.post(f'{YNAB_URL}/budgets/{new_id}/accounts', json=acc)



# first month, last month
# payees
# category groups
# categories
# months (budget info I think)
# transactions
# sub-transactions
# scheduled transactions (ignore?)

