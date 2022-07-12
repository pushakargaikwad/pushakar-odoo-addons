# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"
    _description = "Purchase Order Line"

    @api.onchange('product_id')    
    def onchange_product_id(self): 
        res = super(PurchaseOrderLine,self).onchange_product_id()
        
        self.price_unit = float(self.product_id.standard_price)
        return res
