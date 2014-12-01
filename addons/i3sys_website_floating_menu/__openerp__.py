# -*- coding: utf-8 -*-
{
    'name': 'Floating Menu',
    'category': 'Website',
    'website': 'http://i3rendszerhaz.hu',
    'summary': 'Changes the menu to be floating',
    'version': '1.0',
    'description': """
Floating Menu on Website
========================

It will only work for logged out users, because the floating menu hides
the top editor bar.
        """,
    'author': 'i3 Rendszerház Kft.',
    'depends': ['website'],
    'data': [
        'views/floating_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
