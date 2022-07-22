# See LICENSE file for full copyright and licensing details.

{
    'name' : 'Development Tweaks and Tools to make life Easier',
    'version' : '1.0.4',
    'summary': 'A set of tools and tweaks to make Development easier and faster',
    'sequence': 31,
    "category": "Tools",
    'description': """
		A set of tools and tweaks to make Development easier and faster
    1. Added fields to view installed and latest versions
    1.1 If Installed and Latest versions are different, the line appears red in tree view
    2. Ability to search via Author, Summary Fields
            
    """,
    'website': 'https://pushakar.com/odoo-development/',
    'depends' : ['base'],
    'data': ['views/pg_developer_tools_view.xml'],
    'demo': [],
    'qweb': [ ],
    'author': 'Pushakar Gaikwad',
    'license':'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}

