from odoo import _, models, fields, api

from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    patient_name = fields.Char(string='Patient Name')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'patient Record'
    _rec_name = 'patient_name'

    # error message shown for incorrect age
    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5:
                raise ValidationError(_('the age must be over than 5'))

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    @api.multi
    def open_hospital_appointment(self):
        return {
            'name': _('Appointment'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

    @api.onchange('doctor_id')
    def set_doctor_gender(self):
        for rec in self:
            if rec.doctor_id:
                rec.doctor_gender = rec.doctor_id.gender

    Gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], default='male', string="Gender")

    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor')],
        string="age Group", compute='set_age_group')

    patient_name = fields.Char(string='name', required=True, track_visibility='always')
    patient_age = fields.Integer('Age', track_visibility='always')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='image')
    name = fields.Char(string='Test')

    # doctor = fields.Many2one('doctor_name', string='Doctor', help='Select the doctor for this patient.')
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")

    doctor_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Doctor Gender")

    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    appointment_count = fields.Integer(string='Appointment', compute='get_appointment_count')
    active = fields.Boolean("Active", default=True)

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result