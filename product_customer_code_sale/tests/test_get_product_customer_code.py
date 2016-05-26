# -*- coding: utf-8 -*-
# © 2013 Agile Business Group sagl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class GetProductCustomerCode(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(GetProductCustomerCode, self).setUp(*args, **kwargs)
        # Objects
        self.obj_product = self.env['product.product']
        self.obj_sale_order = self.env['sale.order']
        self.obj_prod_cust_code = self.env['product.customer.code']

        # Data Category Product
        self.categ = self.ref('product.accessories')

        # Data UOM
        self.uom = self.ref('product.product_uom_unit')

        # Data Partner
        self.partner = self.ref('base.res_partner_3')

    def _prepare_product_data(self):
        data = {
            'name': 'Test Product - 1',
            'categ_id': self.categ,
            'standard_price': 500.0,
            'list_price': 150.5,
            'type': 'consu',
            'uom_id': self.uom,
            'uom_po_id': self.uom,
            'default_code': 'TST001',
            'product_customer_code_ids': [
                (0, 0, {'product_name': 'Test Product - 1',
                        'product_code': 'CUST001',
                        'partner_id': self.partner})
            ]
        }

        return data

    def _create_product(self):
        data = self._prepare_product_data()
        product = self.obj_product.create(data)

        return product

    def _prepare_sale_order_data(
            self, product_id, product_name, product_lst_price):
        data = {
            'partner_id': self.partner,
            'order_line': [
                (0, 0, {'product_id': product_id,
                        'name': product_name,
                        'product_uom_qty': 1.0,
                        'price_unit': product_lst_price})
            ]
        }

        return data

    def _create_sale_order(
            self, product_id, product_name, product_lst_price):
        data = self._prepare_sale_order_data(
            product_id, product_name, product_lst_price)
        sale_order = self.obj_sale_order.create(data)

        return sale_order

    def test_get_product_cust_code(self):
        # Create Product
        prod_id = self._create_product()
        # Check Create Product
        self.assertIsNotNone(prod_id)
        # Create SO
        so_id = self._create_sale_order(
            prod_id.id, prod_id.name, prod_id.lst_price)
        # Check Create SO
        self.assertIsNotNone(so_id)

        # Check Get Product Customer Code
        for line in so_id.order_line:
            partner_id = line.order_id.partner_id.id
            product_id = line.product_id.id
            if product_id and partner_id:
                code_ids = self.obj_prod_cust_code.search([
                    ('product_id', '=', product_id),
                    ('partner_id', '=', partner_id),
                ], limit=1)
                self.assertEqual(
                    line.product_customer_code, code_ids.product_code)
