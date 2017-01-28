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

'''                                                                                                                                                                
Modelo que sobreescribe res_partner

'''                                                                                     
class res_partner(models.Model):
    _inherit='res.partner'
    
    homologated = fields.Boolean('Homologated')
    homologated_description = fields.Char('Homologated Description')
#   contracs_contact_ids = fields.One2many('ingalux.contract.contact', 'partner_id ', string='Contracts')
    
    