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

class sale_quote_line(osv.osv):
    _inherit = 'sale.quote.line'
    
    def on_change_product_id(self, cr, uid, ids, product, context=None):
        product_obj = self.pool.get('product.product').browse(cr, uid, product, context=context)
        res = super(sale_quote_line, self).on_change_product_id(cr, uid, ids, product, context=context)
        if product_obj.chapter_id:
            res['value'].update({'chapter_id': product_obj.chapter_id.id})
        return res
    
    _columns = {
        'chapter_id': fields.many2one('sale_order_chapters.chapter', 'Chapter', required=True)
    }