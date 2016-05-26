# -*- coding: utf-8 -*-
# © 2013 Agile Business Group sagl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    def _get_product_customer_code(self):
        product_customer_code_obj = self.env['product.customer.code']
        for line in self:
            partner_id = line.order_id.partner_id.id
            product_id = line.product_id.id
            if product_id and partner_id:
                code_ids = product_customer_code_obj.search([
                    ('product_id', '=', product_id),
                    ('partner_id', '=', partner_id),
                ], limit=1)
                if code_ids:
                    line.product_customer_code = code_ids.product_code
                else:
                    line.product_customer_code = ''

    product_customer_code = fields.Char(
        string='Product Customer Code',
        size=64,
        compute='_get_product_customer_code'
    )
