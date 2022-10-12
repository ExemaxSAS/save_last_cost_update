# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    cost_date = fields.Datetime('Fecha de Actualización Costo')

    @api.onchange('list_price', 'standard_price')
    def update_cost_date(self):
        self.cost_date = datetime.now()