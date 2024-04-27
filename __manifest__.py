
{
    'name': 'My Hospital',
    'version': '1.0',
    'author': 'Abdelrahman',
    'category': 'Uncategorized',
    'depends': ['base','mail','sale'],
    'data': [
    'security/ir.model.access.csv',
    'security/security.xml',
    'data/sequence.xml',
    'data/data.xml',
    'wizards/create_appointment.xml',
    'views/patient.xml',
    'views/appointment.xml',
    'views/doctor.xml',
    'reports/report.xml',
    'reports/patient_card.xml',
    ],
    'images': [
    'static/description/icon.png',
    ],
    'installable': True,
    'application': True,
}