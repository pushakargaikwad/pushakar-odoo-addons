# See LICENSE file for full copyright and licensing details.

{
    'name' : 'Invoice Cancellation Group',
    'version' : '1.0.0',
    'summary': 'New group for "Cancel Invoice" button',
    'sequence': 30,
    'category': 'Accounting/Accounting',
    'description': """
            Invoice Cancellation Group

            1. Created new group named as "Invoice Cancel Rights" Under "Allow to cancel invoice" group category.
            2. This group basically assigned to user who has an authority to cancel the invoice. 
            3. "Cancel Invoice" button will be visible to this group only. 
            
            "Account Cancel" which is a free module is required to be installed and configured for this module to work. 
            After Installation, To view cancel buttons on Invoice and Payment, the user should be assigned to the group "Invoice Cancel Rights"
            Be careful with this module as it has audit implications. Cancelling accounting entries is not authorized in all countries.
            As "admin" has highest access rights, admin user still has direct access to cancel button without explicitly assigning this group.

    """,
    'website': 'https://pushakar.com/odoo-development/',
    'depends' : ['base','account','account_cancel'],
    'data': ['views/pg_invoice_cancellation.xml','views/pg_invoice_cancellation_group.xml'],
    'images': ['static/description/assets/main_screenshot.png'],
    'demo': [],
    'qweb': [ ],
    'author': 'Pushakar Gaikwad',
    'license':'AGPL-3',
    'price': 19.99,
    'installable': True,
    'application': True,
    'auto_install': False,
}
