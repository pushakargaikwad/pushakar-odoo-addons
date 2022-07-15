# See LICENSE file for full copyright and licensing details.


{
    'name' : 'PO Cost Price onchange Product',
    'version' : '1.0.0',
    'summary': 'Updates Product Cost Price when Product is changed.',
    'sequence': 30,
    'category': 'Purchases',
    'description': """
            When we add or change a product on Purchase Order, the cost price of the product is updated. 
                
    """,
    'website': 'https://pushakar.com/odoo-development/',
    'depends' : ['base','purchase'],
    'data': [],
    'demo': [],
    'qweb': [],
    'author': 'Pushakar Gaikwad',
    'license':'AGPL-3',
    'price': 9.99,
    'installable': True,
    'application': True,
    'auto_install': False,
}
