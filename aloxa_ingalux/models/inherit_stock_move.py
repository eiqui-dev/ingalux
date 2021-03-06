# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 Solucións Aloxa S.L. <info@aloxa.eu>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class StockMove(models.Model):
    _inherit = 'stock.move'

    contract_id = fields.Many2one('account.analytic.account', 'Contrato', related='purchase_line_id.order_id.contract_id')
    supplier_id = fields.Many2one('res.partner', 'Proveedor', related='purchase_line_id.partner_id')

    @api.v7
    def _get_invoice_line_vals(self, cr, uid, move, partner, inv_type, context=None):
        res = super(StockMove, self)._get_invoice_line_vals(
           cr, uid, move, partner, inv_type, context=context)
	_logger.info("ANTES")
	_logger.info(res)
	if move.purchase_line_id:
	        res.update({'analytics_id': move.purchase_line_id.analytics_id.id or False,})
	_logger.info("DESPOIS")
        _logger.info(res)
        return res

