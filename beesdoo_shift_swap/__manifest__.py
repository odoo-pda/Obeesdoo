# -*- coding: utf-8 -*-
{
    'name': "beesdoo_shift_swap",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Coop It Easy SCRLfs",
    'website': "https://github.com/beescoop/Obeesdoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Cooperative Management',
    'version': '12.0.1.0.2',

    # any module necessary for this one to work correctly
    'depends': [
        "base",
        "beesdoo_base",
        "beesdoo_shift",
    ],

    # always loaded
    'data': [
        'security/shift_swap_group.xml',
        'security/ir.model.access.csv',
        'views/shift_swap.xml',
        'views/shift_swap_subscribe.xml',
        'views/shift_swap_timeslot.xml',
        'views/shift_swap_proposale.xml',
        'views/shift_swap_set.xml',
        'wizard/Subscribe_shift_swap.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}