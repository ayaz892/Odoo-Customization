
display_currency_id = fields.Many2one(
        'res.currency',
        string="Display Currency",
        default=lambda self: self.env.ref('base.AED')  # Ensure AED currency exists in the system
    )
    display_amount_total = fields.Monetary(
        compute="_compute_display_amount_total",
        currency_field="display_currency_id",
        string="Total in Display Currency"
    )
 
    @api.depends('amount_total', 'display_currency_id')
    def _compute_display_amount_total(self):
 
        for record in self:
            if record.display_currency_id:
                record.display_amount_total = record.currency_id._convert(
                    record.amount_total,
                    record.display_currency_id,
                    record.company_id,
                    record.invoice_date or fields.Date.today()
                )
            else:
                record.display_amount_total = record.amount_total
