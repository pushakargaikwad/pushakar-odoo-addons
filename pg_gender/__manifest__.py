# See LICENSE file for full copyright and licensing details.

{
    'name' : 'Gender Module',
    'version' : '1.0.0',
    'summary': 'Dedicated module for Gender',
    'sequence': 30,
    'description': """
            This module solves the problem of code duplication which occurs when creating a gender field in every module that needs it. 
            This module will allow configuring gender model once which can be referred in Many2one in other modules as required.
    """,
    'category': 'Tools',
    'website': 'https://pushakar.com/odoo-development/',
    'depends' : ['base','web'],
    'data': ['security/ir.model.access.csv','views/res_gender_view.xml','data/res_gender_data.xml'],
    'images': [],
    'demo': [],
    'qweb': [ ],
    'author': 'Pushakar Gaikwad',
    'license':'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
