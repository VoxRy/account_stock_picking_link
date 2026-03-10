# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    invoice_ids = fields.Many2many(
        'account.move',
        'account_invoice_picking_rel',
        'stock_picking_id',
        'account_move_id',
        string="Faturalar"
    )
    invoice_count = fields.Integer(compute='_compute_invoice_count', string="Fatura Sayısı")

    @api.depends('invoice_ids')
    def _compute_invoice_count(self):
        for picking in self:
            picking.invoice_count = len(picking.invoice_ids)

    def action_view_invoice(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("account.action_move_out_invoice_type")
        if len(self.invoice_ids) > 1:
            action['domain'] = [('id', 'in', self.invoice_ids.ids)]
        elif self.invoice_ids:
            form_view = [(self.env.ref('account.view_move_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = self.invoice_ids.id
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action
