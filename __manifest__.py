{
    'name': 'presale',
    'application': True,
    'depends': ['base', 'product', 'sales'],
    'data': [
        'data/presale_order_sequence.xml',
        'views/presale_order_views.xml',
        'security/ir.model.access.csv',
        'views/presale_menus.xml',
    ],
}
