# -*- coding: utf-8 -*-
{
    'name': "cinema_management",

    'summary': """
        Module for cinema company managment""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Milos Matic",
    'website': "http://www.modoolar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'product'
                ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/movie_view.xml',
        'views/sell_tickets_view.xml',
        'views/timetable_view.xml',
        'views/room_view.xml',
        'views/product_inherit_view.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
