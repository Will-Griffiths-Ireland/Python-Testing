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
    while True:
        print('Please input sales figures')
        print('6 numbers separated by commas\n')
        data_str = input('Enter your data here: ')
        print(f'The data provided is {data_str}')
        sales_data = data_str.split(',')
        if validate_data(sales_data):
            print('Data is valid!')
            break
    return sales_data        


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
        return False

    return True




def update_sales_worksheet(data):
    """
        Update sales worksheet with a new line and data provided
    """
    print('Updating sales worksheet.../n')
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('Sales worksheet updated successfully!/n')


data = get_sales_data()
sales_data = [int(num) for num in data]
print(sales_data)
update_sales_worksheet(sales_data)    