from odoo import models, fields, api

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    custom_field_char = fields.Char(string="Additional Details")
    custom_field_int = fields.Integer(string="Age")
    custom_field_many2one = fields.Many2one('res.partner', string="User Details")
    status = fields.Selection(
        [
            ("yes", "Yes"),
            ("no", "No")
        ],
        string="Status",
        store=True,
    )

    def _prepare_opportunity_quotation_context(self):
        quotation_context = super(CrmLeadInherit, self)._prepare_opportunity_quotation_context()
        quotation_context.update({
            'default_custom_field_char': self.custom_field_char,
            'default_custom_field_int': self.custom_field_int,
            #'default_custom_field_many2one': self.custom_field_many2one.id if self.custom_field_many2one else False,
            'default_status': self.status,
        })
        return quotation_context

