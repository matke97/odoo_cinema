from odoo import models,fields,api

class Timetable(models.Model):
    _name        = 'cinema_management.timetable'
    _description = 'Timetable'

    date     = fields.Datetime(required=True)
    movie    = fields.Many2one("cinema_management.movie", required=True)
    premiere = fields.Boolean()
    room_id  = fields.Many2one("cinema_management.room")


    sold_seats      = fields.Integer(default=0)
    total_seats     = fields.Integer(compute='_compute_total_seats')
    remaining_seats = fields.Integer(compute="_compute_remaining_seats")


    """Method to compute remaining seats field in Timtablemodel"""
    @api.depends('total_seats', 'sold_seats')
    def _compute_remaining_seats(self):
        for record in self:
            record.remaining_seats = record.total_seats - record.sold_seats

    """Method to get total seats field in Timtablemodel from Room model"""
    @api.depends('room_id')
    def _compute_total_seats(self):
        for record in self:
            record.total_seats = record.room_id.capacity


