import os
from dotenv import load_dotenv
import requests

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
for t in transactions:
    starting_balance = t['payee_name'] == 'Starting Balance'
    transfer = 'Transfer' in t['payee_name']
    if not t['subtransactions']:
        transactions_dict['transactions'].append({
            'account_id': new_acc_dict[t['account_name']],
            'date': t['date'],
            'amount': t['amount'],
            'payee_name': t['payee_name'] if not starting_balance and not transfer else t['payee_name'].replace('a', '@', 1),
            'category_id': new_cat_dict[t['category_name']] if not transfer else new_cat_dict['Transfers'],
            'memo': t['memo'],
            'cleared': t['cleared'],
            'approved': t['approved'],
            'flag_color': t['flag_color']
        })
    for sub in t['subtransactions']:
        transactions_dict['transactions'].append({
            'account_id': new_acc_dict[t['account_name']],
            'date': t['date'],
            'amount': sub['amount'],
            'payee_name': sub['payee_name'],
            'category_id': new_cat_dict[sub['category_name']],
            'memo': sub['memo'],
            'cleared': t['cleared'],
            'approved': t['approved'],
            'flag_color': t['flag_color']
        })

result = s.post(f'{YNAB_URL}/budgets/{new_id}/transactions', json=transactions_dict)

# first month, last month
# months (budget info I think)
# transactions
# sub-transactions
