{
    'name': 'presale',
    'application': True,
    'depends': ['base', 'product', 'sale_management'],
    'data': [
        'security/security.xml',
        'data/presale_order_sequence.xml',
        'views/presale_order_views.xml',
        'views/sale_order_views.xml',
        'views/presale_menus.xml',
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
    ],
    'category': 'Presale/Presale',
}
