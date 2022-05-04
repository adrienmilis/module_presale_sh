{
    'name': 'presale',
    'application': True,
    'depends': ['base', 'product', 'sale_management'],
    'data': [
        'data/presale_order_sequence.xml',
        'views/presale_order_views.xml',
        'views/sale_order_views.xml',
        'security/ir.model.access.csv',
        'views/presale_menus.xml',
        'data/ir_cron_data.xml',
    ],
}
