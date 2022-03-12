{
    'name': 'Module Custome Pembelian',
    'version': '15.0',
    'category': 'purchase',
    'summary': 'Module Custome Pembelian',
    'description': """
        Ini adalah module custom di Algoritma Channel
    """,
    'website': '',
    'author': 'Algoritma',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/algoritma_pembelian_view.xml',
        'views/algoritma_pembelian_action.xml',
        'views/algoritma_pembelian_menuitem.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
}