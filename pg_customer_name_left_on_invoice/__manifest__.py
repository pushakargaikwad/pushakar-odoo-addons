{
    'name' : 'Customer Name left side on invoice',
    'version' : '1.0.1',
    'summary': 'Displays Customer Name on the left side of invoice print',
    'sequence': 30,
    "category": "Accounting",
    'description': """
            This module displays the Customer Name, Address and other details on the left side of Invoice print
    """,
    'website': 'https://www.pushakar.com',
    'depends' : ['base','account','account_invoicing','web'],
    'data': ['views/pg_customer_name_left_on_invoice.xml',],
    'author': 'Pushakar Gaikwad',
    'license':'OPL-1',
    'price': 9.99,
    'currency': 'USD',
    'installable': True,
    'application': True,
    'auto_install': False,
}
