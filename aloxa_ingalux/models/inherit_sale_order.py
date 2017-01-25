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
from openerp.osv import fields, osv

class sale_order(osv.osv):
    _inherit = 'sale.order'
    
    def onchange_template_id(self, cr, uid, ids, template_id, partner=False, fiscal_position=False, context=None):
        res = super(sale_order, self).onchange_template_id(cr, uid, ids, template_id, partner=partner, fiscal_position=fiscal_position, context=context)
        if not template_id:
            return True

        if context is None:
            context = {}
        context = dict(context, lang=self.pool.get('res.partner').browse(cr, uid, partner, context).lang)
        
        quote_template = self.pool.get('sale.quote.template').browse(cr, uid, template_id, context=context)
        cont = 1
        lines = quote_template.quote_line[1::]
        for line in lines:
            res['value']['order_line'][cont][2].update({'chapter_id': line.chapter_id.id})
            cont=cont+1
        cont = 0
        for option in quote_template.options:
            res['value']['options'][cont][2].update({'chapter_id': option.chapter_id.id})
            cont=cont+1
        return res
    
    _columns = {
        'title': fields.char('Title')
    }