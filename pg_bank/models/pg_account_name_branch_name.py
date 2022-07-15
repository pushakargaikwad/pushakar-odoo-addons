from odoo import api, fields, models, _


class pg_account_name(models.Model): 
    _inherit="res.partner.bank"

    x_account_name = fields.Char(string="Account Name")


class pg_branch_name(models.Model): 
    _inherit="res.bank"

    x_branch_name = fields.Char(string="Branch Name")