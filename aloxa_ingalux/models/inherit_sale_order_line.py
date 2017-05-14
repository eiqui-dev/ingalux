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
import html2text

class sale_order_line(models.Model):
    _inherit = 'sale.order.line'

    
    @api.depends('name')
    def _compute_name_text(self):
        for l in self:
		text = html2text.HTML2Text()
		text.ignore_links = True
	        l.name_text = text.handle(l.name)

    name= fields.Html('Description', required=True, readonly=True, states={'draft': [('readonly', False)]})
    name_text= fields.Text('Description', readonly=True, compute='_compute_name_text')
    
