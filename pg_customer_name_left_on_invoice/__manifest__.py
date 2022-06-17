# See LICENSE file for full copyright and licensing details.

{
    'name' : 'Customer Details left side of invoice',
    'version' : '1.0.1',
    'summary': 'Displays Customer Name and details on the left side of invoice print',
    'sequence': 30,
    "category": "Accounting",
    'description': """
            This module displays the Customer Name, Address and other details on the left side of Invoice print
    """,
    'website': 'https://pushakar.com/odoo-development/',
    'depends' : ['base','account','account_invoicing','web'],
    'data': ['views/pg_customer_name_left_on_invoice.xml',],
    'images': ['static/description/assets/main_screenshot.png','static/description/assets/screenshot_invoice.png'],
    'author': 'Pushakar Gaikwad',
    'license':'AGPL-3',
    'price': 9.99,
    'currency': 'USD',
    'installable': True,
    'application': True,
    'auto_install': False,
}
