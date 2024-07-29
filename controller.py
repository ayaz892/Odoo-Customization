from odoo import http
from odoo.http import request


class OeOdooDevTraining(http.Controller):
    @http.route('/oe_odoo_dev_training', website=True, auth='public', type='http')
    def oe_odoo_dev_training(self):
        return request.render("oe_odoo_dev_training.oe_odoo_dev_training_page", {})

    @http.route('/create_progress', website=True, auth='public', type='http', methods=['POST'], csrf=False)

    def create_progress(self, **kwargs):
        student_name = kwargs.get('student_name')
        age = kwargs.get('age')
        date_created = kwargs.get('date_created')
        details = kwargs.get('details')

        request.env['oe_odoo_dev_training.oe_odoo_dev_training'].sudo().create({
            'student_name': student_name,
            'age': age,
            'date_created': date_created,
            'details': details,
        })
        return request.redirect('/oe_odoo_dev_training')

    @http.route('/oe_odoo_dev_training/records', website=True, auth='public', type='http')
    def list_students(self):
        students = request.env['oe_odoo_dev_training.oe_odoo_dev_training'].sudo().search([])
        return request.render("oe_odoo_dev_training.records_page", {
            'students': students,
        })
