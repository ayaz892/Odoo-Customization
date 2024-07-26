# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class OeOdooDevTraining(models.Model):
    _name = 'oe_odoo_dev_training.oe_odoo_dev_training'
    _description = 'This module is for Task 1'

    student_name = fields.Char(string="Student Name")
    age = fields.Integer(string="Student Age")
    date_created = fields.Date(string="Date Created")
    date_ended = fields.Date(string="Expected End Date")


    img = fields.Image(string="Image")
    details = fields.Text(string="Additional Detail")
    # time_created = fields.Datetime(string="Time Created", readonly=True)
    phone_no = fields.Integer(string="Phone No")
    active = fields.Boolean(string="Active", default=True)

    total_fees = fields.Float(string="Total Course Fees" ,compute='_compute_total_fees', store=True)

    oe_travel_sequence = fields.Char(string=" Students ID", required=True, readonly=True,
                                     default=lambda self: _('New'))

    leave_details_id = fields.One2many(comodel_name="training.progress", inverse_name="trainee_id")

    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Canceled'),


    ], string='Status', default='draft')

    gender =fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    def create_rec(self):
        for rec in self:
            students = self.env['oe_odoo_dev_training.oe_odoo_dev_training'].create({

                'student_name': rec.student_name or 'Ayaz Odoo developer',
                'age': rec.age or '25',
                'phone_no':rec.phone_no or '0334678643'
            })

    def search_rec(self):
        for rec in self:
            students = self.env['oe_odoo_dev_training.oe_odoo_dev_training'].search([])
            print("List of all the search record", students)

    def copy_rec(self):

        for rec in self:
            students = self.env['oe_odoo_dev_training.oe_odoo_dev_training'].browse([48])
            if not students:
                print("Record not found",students)
            else:
                students.copy()

    def search_count_rec(self):

        for rec in self:
            check = self.env['oe_odoo_dev_training.oe_odoo_dev_training'].search_count([
                '|',('age', '=' , '22'), ('gender', '=' , 'female'),


            ])
            print("Total record with this domain is:", check)





    @api.model
    def create(self, vals):
        if vals.get('oe_travel_sequence', 'New') == 'New':
            vals['oe_travel_sequence'] = (
                        self.env['ir.sequence'].next_by_code('oe_odoo_dev_training.oe_odoo_dev_training') or 'New')
        res = super(OeOdooDevTraining, self).create(vals)
        return res

    @api.onchange('date_created')
    def _onchange_date_creation(self):
        if self.date_created:
            self.details = f"Date Created: {self.date_created} - Student Register Successfully"
        else:
            self.details = ""


    @api.depends('leave_details_id.course_fee')
    def _compute_total_fees(self):
        for record in self:
            record.total_fees=sum(line.course_fee for line in record.leave_details_id)


    # @api.model
    # def get_report_action(self, record_ids):
    #     return self.env.ref('oe_odoo_dev_training.action_student_report').report_action(record_ids)

    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
    #         record.value2 = float(record.value) / 100
