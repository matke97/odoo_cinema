from odoo import models,fields

class Timetable(models.Model):
    _name        = 'cinema_management.timetable'
    _description = 'Timetable'

    date     = fields.Datetime(required=True)
    movie    = fields.Many2one("cinema_management.movie", required=True)
    premiere = fields.Boolean()
    room_id  = fields.Many2one("cinema_management.room")


