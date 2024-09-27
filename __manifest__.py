{
    'name': 'Graduados lista',
    'version': '1.0',
    'summary': 'Registro de graduados',
    'author': 'Juan Jose Benites Coronel',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/carrera_graduado_views.xml',
        'views/graduado_report.xml',
        'views/menu.xml',
        # Incluir archivos de vistas y otros datos si los añades más adelante
    ],
    'installable': True,
    'application': True,
}