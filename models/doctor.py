from odoo import models, fields, api, _

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string='name', required=True, track_visibility='always')

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default='male', string="Gender")

    related_user = fields.Many2one('res.users', string='Related User', help='Select the user with system admin access.')


