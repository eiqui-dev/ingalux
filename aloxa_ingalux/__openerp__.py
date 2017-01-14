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
    ],
    "data": [
        'views/inherit_sale_order_chapters_external_layout_header.xml',
        'views/inherit_sale_order_chapters_report_sale_order_document.xml',
    ],
    
    "demo": [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
