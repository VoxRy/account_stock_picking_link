# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    picking_ids = fields.Many2many(
        'stock.picking',
        'account_move_stock_picking_rel',
        'move_id',
        'picking_id',
        string="Transferler"
    )
    picking_count = fields.Integer(compute='_compute_picking_count', string="Transfer Sayısı")

    @api.depends('picking_ids')
    def _compute_picking_count(self):
        for move in self:
            move.picking_count = len(move.picking_ids)

    def action_view_picking(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("stock.action_picking_tree_all")
        if len(self.picking_ids) > 1:
            action['domain'] = [('id', 'in', self.picking_ids.ids)]
        elif self.picking_ids:
            form_view = [(self.env.ref('stock.view_picking_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = self.picking_ids.id
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action
