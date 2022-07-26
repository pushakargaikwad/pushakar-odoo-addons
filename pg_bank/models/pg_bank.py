from odoo import api, fields, models, _


class pg_res_partner_bank(models.Model): 
    _inherit="res.partner.bank"

    x_account_name = fields.Char(string="Account Name",help="If the Account Name is not the same as the Account Holder Name, please specify here.")
    x_display_on_invoice_print = fields.Boolean(string="Display on Invoice Print?")


class pg_res_bank(models.Model): 
    _inherit="res.bank"

    x_branch_name = fields.Char(string="Branch Name")