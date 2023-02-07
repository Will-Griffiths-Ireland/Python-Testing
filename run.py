import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')
data = sales.get_all_values()

def get_sales_data():
    """
    Get sales figures from user
    """
    print('Please input sales figures')
    print('6 numbers separated by commas\n')
    data_str = input('Enter your data here: ')
    print(f'The data provided is {data_str}')
    sales_data = data_str.split(',')
    validate_data(sales_data)



def validate_data(values):
    """
    validate data
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f'I said you need 6 numbers! You gave {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, try again bozo. \n')

get_sales_data()