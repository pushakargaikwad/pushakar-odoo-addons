# See LICENSE file for full copyright and licensing details.

{
    'name' : 'Remove Salesperson from Quotation Print',
    'version' : '1.0.0',
    'summary': 'Removes the Salesperson field from Quotation and Sales Order',
    'sequence': 31,
    'category': 'Sales',
    'description': """
            If you don't want the Salesperson field to appear on the Print of Quotation and Sales Order, then this module is for you. 
    """,
    'website': 'https://www.pushakar.com',
    'depends' : ['base','mail','sale','sale_management'],
    'data': ['views/pg_remove_sales_person_from_quotation_print.xml'],
    'author': 'Pushakar Gaikwad',
    'license':'AGPL-3',
    'price': 9.99,
    'currency': 'USD',
    'installable': True,
    'application': True,
    'auto_install': False,
}
