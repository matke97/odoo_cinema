from odoo import models,fields,exceptions


class Sell_tickets(models.TransientModel):
    _name = "cinema_management.sell_wizard"

    def _default_timetable_id(self):
        return self.env['cinema_management.timetable'].browse(self._context.get('active_id'))

    timetable_id = fields.Many2one('cinema_management.timetable', required=True, default=_default_timetable_id)
    tickets = fields.Integer(required = True)



    def sell_tickets_submit(self):
        if self.tickets <= self.timetable_id.remaining_seats:
            self.timetable_id.sold_seats += self.tickets
        else:
            raise exceptions.AccessDenied("Error. You try to reserve more seats that are available")
        return {}
