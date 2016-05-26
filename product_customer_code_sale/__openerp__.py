# -*- coding: utf-8 -*-
# © 2013 Agile Business Group sagl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Product Customer Code On Sale',
    'version': '8.0.1.0.0',
    'summary': 'Add product customer code on sale',
    'author': 'Agile Business Group,Odoo Community Association (OCA)',
    'website': 'http://www.agilebg.com',
    'category': 'Sales Management',
    'depends': [
        'base',
        'product',
        'sale',
        'product_customer_code'
    ],
    'data': ['views/sale_view.xml'],
    'installable': True,
    'license': 'AGPL-3',
}
