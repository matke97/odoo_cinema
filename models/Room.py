from odoo import models, fields


class Room(models.Model):
    _name = "cinema_management.room"

    timetable_ids = fields.One2many("cinema_management.timetable", required=True)
    capacity = fields.Integer(required = True)
