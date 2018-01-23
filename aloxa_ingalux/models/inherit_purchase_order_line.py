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
import logging
_logger = logging.getLogger(__name__)

class purchase_order_line(osv.osv):
    _inherit = 'purchase.order.line'
    

    _columns = {
	'partner_ref': fields.char('Supplier Reference', states={'confirmed':[('readonly',False)],'approved':[('readonly',False)],'done':[('readonly',False)]}),
	'uom_qty': fields.float('Qty by Uom'),
	'price_on_uom': fields.boolean('Price Based in Uom'),
	'price_by_uom': fields.float('Price in Uom'),
    }

    def onchange_product_id(self, cr, uid, ids, pricelist_id, product_id, qty, uom_id,
            partner_id, date_order=False, fiscal_position_id=False, date_planned=False,
            name=False, price_unit=False, state='draft', context=None):
	product = self.pool.get('product.product').browse(cr,uid,product_id,context=context)
	partner = self.pool.get('res.partner').browse(cr,uid,partner_id,context=context)
	res = super(purchase_order_line, self).onchange_product_id(cr, uid, ids, pricelist_id, product_id, qty, uom_id,
		partner_id, date_order=False, fiscal_position_id=False, date_planned=False,
                name=False, price_unit=False, state='draft', context=context)
	seller_price = context.get('price_unit')
	for seller in product.variant_seller_ids:
                        if seller.name.id == partner.id:
				qty_top = 0
				for pricelist_item in seller.pricelist_ids:
					_logger.info(pricelist_item)
					if qty >= pricelist_item.min_quantity and pricelist_item.min_quantity >= qty_top:
						qty_top = pricelist_item.min_quantity
						seller_price = pricelist_item.price
						_logger.info(qty_top)
   						_logger.info('A')
						res['value']['price_unit'] = seller_price
	if product and product.price_on_uom:
		if context.get('uom_qty') or context.get('price_by_uom'):
			if context.get('product_qty'): # If change the product qty we must recalcule the price based on pricelist 
				price_by_uom = res['value']['price_unit']
			else: # Else we use the price in form
				price_by_uom = context.get('price_by_uom')
			price_uom_calc = context.get('uom_qty') * price_by_uom
		else:
			price_uom_calc = product.uom_qty * res['value']['price_unit']
			price_by_uom = res['value']['price_unit']
			res['value'].update({
                         	'uom_qty' : product.uom_qty,
				'price_by_uom' : price_by_uom,
                		})
		res['value'].update({
			'price_on_uom' : product.price_on_uom,
			'price_unit' : price_uom_calc,
			'price_by_uom' : price_by_uom,
		})
	if product:
                name = product.with_context(display_default_code=False).display_name
                if product.description_purchase:
                        name += '\n' + product.description_purchase
		for seller in product.variant_seller_ids:
			_logger.info(seller.name)
                        if seller.name.id == partner.id and seller.product_name:
				_logger.info("DENTRO")
                                name = seller.product_name
                res['value'].update({'name': name})
	if product and not product.price_on_uom:
		res['value'].update({
			'price_on_uom' : product.price_on_uom,
			})
	return res

