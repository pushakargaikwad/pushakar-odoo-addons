# See LICENSE file for full copyright and licensing details.

{
    'name' : 'Bank Module Improvements',
    'version' : '1.2.1',
    'summary': 'Bank Module Improvements',
    'sequence': 30,
    'description': """
            1. Option to display bank details on invoice.
            2. Extra fields: Account Name, Branch Name
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://pushakar.com/odoo-development/',
    'depends' : ['base','account','web'],
    'data': ['views/pg_bank_details_on_invoice.xml','views/pg_bank.xml',],
    'images': ['static/description/banner.png'],
    'demo': [],
    'qweb': [ ],
    'author': 'Pushakar Gaikwad',
    'license':'AGPL-3',
    'price': 9.99,
    'installable': True,
    'application': True,
    'auto_install': False,
}
