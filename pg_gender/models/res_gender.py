from odoo import models, fields, api, _

class ResGender(models.Model):
    _name = 'res.gender'
    _description = 'Gender'

    name = fields.Char(string='Name',required=True)