from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
# from datetime import datetime
import datetime, time
from datetime import timedelta, date
import math
import sys

sys.setrecursionlimit(2000)


class Students(models.Model):
    _name = 'student.student'
    _description = 'student description'
    _inherit = ['website.published.mixin', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char('name', required=False)
    address = fields.Text('address',placeholder='enter your address')
    rollno = fields.Integer('Roll No')
    student_fees=fields.Float('Fess',digits=(6,2))
    dob=fields.Date()
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ], 'Gender', default='male')
    student_profile=fields.Binary('Profile Picture')
    student_reference=fields.Reference(selection=[('sale.order','Sale Order'),('purchase.order','Purchase Order')])
    student_html=fields.Html('Student Html Page')