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
new_id = '8d414a6a-5201-469b-b5a8-a4e42afefe5e'

new_budget = s.get(f'{YNAB_URL}/budgets/{new_id}').json()['data']['budget']

new_cat_dict = {cat['name']: cat['id'] for cat in new_budget['categories'] if not cat['deleted']}
new_acc_dict = {acc['name']: acc['id'] for acc in new_budget['accounts']}

transactions_dict = {'transactions': []}

transactions = s.get(f'{YNAB_URL}/budgets/{old_id}/transactions').json()['data']['transactions']
print(len(transactions))
for t in transactions:
    if not t['transfer_transaction_id'] and not t['subtransactions'] and not t['payee_name'] == 'Starting Balance':
        continue
        transactions_dict['transactions'].append({
            'account_id': new_acc_dict[t['account_name']],
            'date': t['date'],
            'amount': t['amount'],
            'payee_name': t['payee_name'],
            'category_id': new_cat_dict[t['category_name']],
            'memo': t['memo'],
            'cleared': t['cleared'],
            'approved': t['approved'],
            'flag_color': t['flag_color']
        })
    if not t['subtransactions'] and t['payee_name'] != 'Starting Balance' and 'Discover' not in t['payee_name'] and 'Quicksilver' not in t['payee_name'] and 'Discover' not in t['account_name'] and 'Quicksilver' not in t['account_name']:
        transactions_dict['transactions'].append({
            'account_id': new_acc_dict[t['account_name']],
            'date': t['date'],
            'amount': t['amount'],
            'payee_name': t['payee_name'],
            'category_id': new_cat_dict[t['category_name']],
            'memo': t['memo'],
            'cleared': t['cleared'],
            'approved': t['approved'],
            'flag_color': t['flag_color']
        })
        print(transactions_dict)
        result = s.post(f'{YNAB_URL}/budgets/{new_id}/transactions', json=transactions_dict)
        print(result.json())
        # for row in result:
        #     print(result[row])
        pprint(t)

        input("HI")
        # input("HI")

print(len(transactions_dict['transactions']))

print(result)

# first month, last month
# months (budget info I think)
# transactions
# sub-transactions
