# -*- coding: utf-8 -*-
{
    'name': "Saldo APP",

    'summary': """Aplicacion WEB para registrar ingresos y egresos""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Camilo T.",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded

    'data': [
		'security/res_groups.xml',
		'security/ir_rule.xml',
        'security/ir_model_access.xml',
		'report/templates.xml',
		'report/report.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
   
}
