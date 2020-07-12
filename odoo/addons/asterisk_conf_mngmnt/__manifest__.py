{
    'name': 'Odoo Asterisk configuration management',
    'summary': 'base module for Asterisk management',
    'description':
        """
        This module let's you manage and configure your remote Asterisk PBX's
        """,
    'version': '0.0.1',
    'category': 'Telephony',
    'author': 'Christophe Langenberg',
    'website': 'http://christophe.langenberg.be',
    'depends': ['web', 'bus'],
    'data': [
        'views/menu.xml',
    ],
    'demo': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
}
