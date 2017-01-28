# -*- coding: utf-8 -*-
#################################################################################
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
#################################################################################


{
    "name": "Aloxa Ingalux",
    "version": "0.1",
    "category": "eiqui",
    "icon": "/aloxa_ingalux/static/src/img/logo.png",
    "author": "Solucións Aloxa S.L.",
    "description": "Módulo base para Ingalux",
    "init_xml": [],
    'external_dependencies': {
    },
    "depends": [
        'sale_order_chapters', 
        'sale_order_revision',
        'website_quote',
    ],
    "data": [
        'views/reports/inherit_sale_order_chapters_external_layout_header.xml',
        'views/reports/inherit_sale_order_chapters_external_layout_footer.xml',
        'views/reports/inherit_sale_order_chapters_report_sale_order_document.xml',
        'views/reports/inherit_sale_order_chapters_style.xml',
        'views/reports/inherit_website_quote_view_sale_quote_template_form.xml',
        'views/reports/inherit_description_stock_report_picking.xml',
        'views/reports/inherit_purchase_order_analytic_account.xml',
        'views/inherit_sale_order.xml',
        'views/inherit_res_partner.xml',
        'views/contract_contact.xml',
        'views/inherit_account_analytic_account.xml',
    ],
    
    "demo": [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
