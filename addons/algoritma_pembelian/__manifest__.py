{
    'name' : 'Module Pembelian Terbaru',
    'version' : '15.0',
    'category' : 'purchase',
    'summary' : 'Module Pembelian Terbaru',
    'description' : 'Ini adalh module custom',
    'website' : '',
    'author' : 'stefabus',
    'depends' : ['web', 'base'],
    'data' : [
        'security/ir.model.access.csv',
        'views/algoritma_pembelian_actions.xml',
        'views/algoritma_pembelian_menuitem.xml',
        'views/algoritma_pembelian_view.xml'
    ],
    'installable' : True,
    'application' : True,
    'license' : 'OEEL-1',

}