# See LICENSE file for full copyright and licensing details.

{
    'name' : 'Remove time on quotation print',
    'version' : '1.0.0',
    'summary': 'Removes time from datetime fields of Quotation and Sales Order Print',
    'sequence': 31,
    'category': 'Sales',
    'description': """
      Sometimes you just want to display date (and not exact time) on Quotation. This is particularly required for fields like Confirmation Date, Order Date and Validity date. This module removes the time information of these fields from the Quotation and Sales Order Print Documents 
            
    """,
    'website': 'https://www.pushakar.com',
    'depends' : ['base','mail','sale','sale_management'],
    'data': ['views/pg_remove_time_on_quotation_print.xml'],
    'author': 'Pushakar Gaikwad',
    'license':'AGPL-3',
    'price': 9.99,
    'currency': 'USD',
    'installable': True,
    'application': True,
    'auto_install': False,
}

