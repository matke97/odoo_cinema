from odoo import models,fields,exceptions
from datetime import date


class SellTickets(models.TransientModel):
    _name = "cinema_management.sell_wizard"

    def _default_timetable_id(self):
        return self.env['cinema_management.timetable'].browse(self._context.get('active_id'))

    timetable_id = fields.Many2one('cinema_management.timetable', required=True, default=_default_timetable_id)
    tickets = fields.Integer(required = True)

    partner_id = fields.Many2one('res.partner', required=True)
    product_id = fields.Many2one('product.product', required=True, domain = [('eTicket', '=', 'True')])


    def sell_submit(self):
        if self.tickets <= self.timetable_id.remaining_seats:
            if self.tickets == 0:
                return {}
            self.timetable_id.sold_seats += self.tickets
            product = self.env['product.product'].search([('id', '=', self.product_id.id)])
            pdv = self.env['account.tax'].search([('name', '=', 'PDV')])
            record = self.env['account.move'].create({
                'move_type'       : 'out_invoice',
                #'journal_id': journal.id,
                'partner_id'      : self.partner_id.id,
                'invoice_date'    : date.today(),
                'invoice_line_ids': [(0, 0, {
                        'product_id'  : self.product_id.id,
                        'quantity'    : self.tickets,
                        'discount'    : 0,
                        'price_unit'  : product.lst_price,
                        'tax_ids'     : [pdv.id]
                })]
            })
            return {record}

        else:
            raise exceptions.AccessDenied("Error. You try to reserve more seats that there are available")
        return {}

    def sell_cancel(self):
        return {}
