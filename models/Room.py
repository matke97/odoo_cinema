from odoo import models, fields


class Room(models.Model):
    _name = "cinema_management.room"
    _description = 'Room'
    timetable_ids = fields.One2many('cinema_management.timetable', 'room_id')
    capacity = fields.Integer(required = True)
