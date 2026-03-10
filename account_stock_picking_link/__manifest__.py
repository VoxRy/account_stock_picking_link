# -*- coding: utf-8 -*-
{
    'name': "Invoice Stock Picking Link",
    'summary': """
        Link Invoices and Stock Pickings manually.""",
    'description': """
        This module allows users to manually link independent Invoices and Stock Pickings
        that are not created from a Sales Order.
    """,
    'author': "Antigravity",
    'website': "https://www.yourcompany.com",
    'category': 'Inventory',
    'version': '15.0.1.0.0',
    'depends': ['account', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
        'views/stock_picking_views.xml',
    ],
    'license': 'LGPL-3',
}
