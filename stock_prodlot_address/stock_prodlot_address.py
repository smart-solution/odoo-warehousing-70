# -*- coding: utf-8 -*-
##############################################################################
#
#    Smart Solution bvba
#    Copyright (C) 2010-Today Smart Solution BVBA (<http://www.smartsolution.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################## 

from osv import osv, fields
from openerp.tools.translate import _

class stock_production_lot(osv.osv):

    _inherit = "stock.production.lot"

    def _address_get(self, cr, uid, ids, field_name, args, context=None):
        """Get the last assigned destination address for that producion lot"""
        result = {}

        lots = self.browse(cr, uid, ids)
        for lot in lots:
            lot_moves = self.pool.get('stock.move').search(cr, uid, [('prodlot_id','=',lot.id)])
            if lot_moves:
                result[lot.id] = self.pool.get('stock.move').browse(cr, uid, max(lot_moves)).partner_id.id
            else:
                result[lot.id] = False
        return result

    _columns = { 
            'last_address_id': fields.function(_address_get, method=True, type='many2one', relation='res.partner', readonly=True, string="Address"),
    }   

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
