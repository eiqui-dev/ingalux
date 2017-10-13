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
from openerp.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class sale_order(osv.osv):
    _inherit = 'sale.order'

    def onchange_template_id(self, cr, uid, ids, template_id, partner=False, fiscal_position=False, context=None):
        res = super(sale_order, self).onchange_template_id(cr,
                                                           uid,
                                                           ids,
                                                           template_id,
                                                           partner=partner,
                                                           fiscal_position=fiscal_position,
                                                           context=context)
        if not template_id:
            return True

        if context is None:
            context = {}
        context = dict(context,
                       lang=self.pool.get('res.partner').browse(cr,
                                                                uid,
                                                                partner,
                                                                context).lang)

        quote_template = self.pool.get('sale.quote.template').browse(cr,
                                                                     uid,
                                                                     template_id,
                                                                     context=context)
        cont = 1
        lines = quote_template.quote_line[1::]
        for line in lines:
            res['value']['order_line'][cont][2].update({
                'chapter_id': line.chapter_id.id
            })
            cont = cont + 1
        cont = 0
        for option in quote_template.options:
            res['value']['options'][cont][2].update({
                'chapter_id': option.chapter_id.id
            })
            cont = cont + 1
        return res


    def onchange_title(self, cr, uid, ids, title, context=None):
	if title and len(title.split('\n')) > 4:
        	raise ValidationError('El titulo no debe sobrepasar de 4 lineas')

    def write(self, cr, uid, ids, vals, context={}):
	res = super(sale_order, self).write(cr, uid, ids, vals, context=context)
	order = self.browse(cr, uid, ids, context=context)
	chapters = self.pool.get('sale_order_chapters.chapter').search(cr,uid,[('id', 'in', order.order_line.mapped('chapter_id.id'))], order='seq ASC')
	c = 1
	for chapter in chapters:
		chapter_obj = self.pool.get('sale_order_chapters.chapter').browse(cr,uid,chapter,context=None) 
		order_lines = self.pool.get('sale.order.line').search(cr,uid,[('order_id', '=', order.id),('chapter_id','=',chapter_obj.id)])	
		l = 1
		for line in order_lines:
			order_line_obj = self.pool.get('sale.order.line').browse(cr,uid,line,context=None)
			order_line_obj.numeration = str(c)+'.'+str(l)
			l += 1
		c += 1
	return res

    def copy_quotation(self, cr, uid, ids, context=None):
        action = super(sale_order, self).copy_quotation(cr, uid, ids, context=None)
	sale = self.browse(cr, uid, ids, context=context)
	old_revision = self.pool.get('sale.order').browse(cr,uid,sale.old_revision_ids[0].id,context=context)
	date = sale.date_order
	sale.date_order = old_revision.date_order
	old_revision.date_order = date
        return action

    _columns = {
        'title': fields.text('Title'),
        'unrevisioned_name' : fields.char('Order Reference', copy=False, readonly=True), #FIX https://github.com/OCA/sale-workflow/issues/210
    }
