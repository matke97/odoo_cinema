from odoo import models,fields


class Product(models.Model):
    _inherit = "product.product"

    eTicket = fields.Boolean(string = "eTicket")

