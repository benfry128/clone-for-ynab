# Clone For Ynab

Clone for Ynab is a project that can be used to clone a budget into a new budget.
The copy will include accounts, categories, transactions, and previously budgeted amounts.

## Installation and Usage

Clone the repo to your local machine.
Log into YNAB and navigate to the budget you'd like to copy, then hit Make a Fresh Start.
Add a category called 'Transfers' somewhere in the new budget (see why [below](#things-this-software-does-and-doesnt-do)).
Copy the budget ids from the URLs of the original (archived) budget as well as the new (Fresh Start) budget.
Create a .env file in the folder and add `OLD_BUDGET_ID=<your old budget id>` and `NEW_BUDGET_ID=<your new budget id>`. 
Run copy_transactions.py, then copy_months.py, creating YNAB API keys and inputting them into the terminal as needed.
If your budget is large enough, you may see errors about network throttling after running copy_months.py for a while.
If this happens, follow the instructions near the top of copy_months.py to continue the process.

## Things This Software Does and Doesn't Do

The YNAB API doesn't currently let you add transactions with 'internal' payee names like Transfers and Starting Balances.
This software turns the `s`'s in `Transfer` and `Starting` into dollar signs to get around this requirement. 
It also adds and subtracts transfers from the new 'Transfers' category. 
However, if you have any Transfer transactions that also have a Category, you'll have to track those down and edit them.
In addition, subtransactions will be split into separate transactions in the new budget due to quirks with adding Split transactions via the API.
This may cause some subtransactions to be unexpectedly uncategorized. 
This software was developed expressly for a specific budget, so using it on yours may or may not work. 

## License

[MIT](https://choosealicense.com/licenses/mit/)