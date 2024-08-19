from odoo import models, fields, api


class CustomEmployees(models.Model):
    _name = 'custom_employees.custom_employees'
    _description = 'Custom Employees'

    name = fields.Char(required=True)
    img = fields.Image()
    position = fields.Text()
    tags = fields.Many2one("hr.employee.category", string="")
    work_mobile = fields.Char(string="Work Mobile")
    work_phone = fields.Char(string="Work Phone")
    work_email = fields.Char(string="Work Email")
    company = fields.Many2one('res.company', string="Company")
    department = fields.Many2one("hr.department", string="Department")
    manager = fields.Many2one("hr.employee", string="Manager")
    jobposition = fields.Char(string="Job Position")
    coach = fields.Many2one('res.users', string="Coach")
    employee_type = fields.Selection([
        ('employee', 'Employee'),
        ('student', 'Student'),
        ('trainee', 'Trainee'),
        ('contractor', 'Contractor'),
        ('freelance', 'Freelancer'),
    ], string='Employee Type')
    related_user = fields.Many2one('res.users', string='Related User')
    pin_code = fields.Char(string='Pin Code')
    badge_id = fields.Char(string='Badge Id')

    def action_view_documents(self):
        print("meeting")

    def action_view_contacts(self):
        print("meeting")

    def action_view_loans(self):
        print("meeting")

    def action_view_equipment(self):
        print("meeting")

    def action_schedule_meeting(self):
        print("meeting")

    def action_quotation_meeting(self):
        print("quotation")
