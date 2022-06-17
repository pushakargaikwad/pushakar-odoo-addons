# See LICENSE file for full copyright and licensing details.

{
    'name' : 'Company Details on Right Side of Header',
    'version' : '1.0.0',
    'summary': 'Displays Company details in Header with your company details on the right side',
    'sequence': 30,
    "category": "Extra Tools",
    'description': """
           This module changes the default location of your company information to the right side. This module updates it on all reports. 
           Note: This is just for your company details in header and not customer details. We have a separate module for that. 
    """,
    'website': 'https://www.pushakar.com',
    'depends' : ['base','account','l10n_in','web'],
    'images': ['static/description/assets/main_screenshot.png','static/description/banner.gif'],
    'data': ['views/pg_report_header_company_right_report.xml',],
    'author': 'Pushakar Gaikwad',
    'license':'AGPL-3',
    'price': 9.99,
    'currency': 'USD',
    'installable': True,
    'application': False,
    'auto_install': False,
}
