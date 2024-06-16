# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE for full copyright and licensing details.

{
    'name' : 'COA Laboratory',
    'version' : '17.0.0.0.0',
    'summary': 'Sample prducts for Laboratory and measure COA for Products',
    'category': 'Inventory',
    'description': """
        Sample prducts for Laboratory and measure COA for Products
    """,
    'images' : [],
    'depends' : ['base', 'web','stock'],
    'author': 'Deep Panchal',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/view_product.xml',
        'views/view_coa.xml',
        'views/menuitems.xml',
        'report/report_coa.xml'
    ],
    'assets': {

    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
