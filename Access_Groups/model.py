from odoo import models, fields, api


class my_ustom_security_module(models.Model):
    _name = 'my_ustom_security_module.my_ustom_security_module'
    _description = 'my_ustom_security_module.my_ustom_security_module'

    name = fields.Char()
    age = fields.Integer()
    salary = fields.Float()
    description = fields.Text()

    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting for department approval', 'Waiting For Department Approval'),
        ('waiting for finance approval', 'Waiting For Finance Approval'),
        ('waiting for gm approval', 'Waiting For GM Approval'),
        ('approved', 'Approved')
    ], string='Status', default='draft')

    department_approved_by = fields.Many2one('res.users', string="Department Approved By")
    finance_approved_by = fields.Many2one('res.users', string="Finance Approved By")
    gm_approved_by = fields.Many2one('res.users', string="GM Approved By")

    def action_confirm(self):
        print("Clicked on Button")
        self.state = 'waiting for department approval'

    def action_depart(self):
        self.state = 'waiting for finance approval'
        self.department_approved_by = self.env.user

    def action_fn(self):
        self.state = 'waiting for gm approval'
        self.finance_approved_by = self.env.user

    def action_gm(self):
        self.state = 'approved'
        self.gm_approved_by = self.env.user

