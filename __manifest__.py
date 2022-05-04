{
    'name': 'presale',
    'application': True,
    'depends': ['base', 'product', 'sale_management'],
    'data': [
        'data/mail_template_data.xml',
        'data/presale_order_sequence.xml',
        'views/presale_order_views.xml',
        'security/ir.model.access.csv',
        'views/presale_menus.xml',
    ],
}
