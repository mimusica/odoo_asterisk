# -*- coding: utf-8 -*-
{
    'name': "Odoo Asterisk configuration manager",

    'summary': """
        base module for working with Asterisk modules created by the author of this module""",

    'description': """
        This module let's you manage and configure your remote Asterisk PBX's
    """,

    'author': "Christophe Langenberg",
    'website': "https://christophe.langenberg.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Telephony',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'bus'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
            'static/src/xml/*.xml',
        ],
}
