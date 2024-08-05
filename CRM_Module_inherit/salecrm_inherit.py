from odoo import fields, models, api


class SaleCrmInherit(models.Model):

    _inherit = 'sale.order'

    custom_field_char = fields.Char(string="Additional Details")
    custom_field_int = fields.Integer(string="age")
    custom_field_many2one = fields.Many2one('res.partner', string="User Details")
    status = fields.Selection(
        [
            ("yes", "Yes"),
            ("no", "No")
        ],
        string="Status ",
        store=True,
    )


