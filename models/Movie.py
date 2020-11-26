from odoo import models, fields, api

OPTIONS = [
    ('Comedy', 'Comedy'),
    ('Action', 'Action'),
    ('Animated', 'Animated'),
    ('Horror', 'Horror')
]

class Movie(models.Model):
    _name = "cinema_management.movie"
    _description = "Movie"

    name         = fields.Char(required=True)
    genre        = fields.Selection(OPTIONS, default=OPTIONS[0][0])
    release_year = fields.Integer(required=True)
    description  = fields.Text()
    image        = fields.Binary()

