# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class WarningNullOrderPurchase(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def create(self, vals):
        print('Hit')
        print(vals)
        if vals['order_line'][0][2]['price_unit'] == 0:
            raise UserError(
                _('Price Unit cannot be 0!')
            )

        return super(WarningNullOrderPurchase, self).create(vals)

    @api.multi
    def write(self, vals):
        print(vals)
        print(self.order_line.price_unit)
        if 'order_line' in vals and 'price_unit' in vals['order_line'][0][2] and vals['order_line'][0][2]['price_unit'] == 0:
            raise UserError(
                _('Price Unit cannot be 0!')
            )
        elif 'order_line' in vals and 'price_unit' not in vals['order_line'][0][2] and self.order_line.price_unit == 0.0:
            raise UserError(
                _('Price Unit cannot be 0!')
            )

        return super(WarningNullOrderPurchase, self).write(vals)
