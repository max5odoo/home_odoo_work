# -*- coding: utf-8 -*-
# from odoo import http


# class NewModulePrac(http.Controller):
#     @http.route('/new_module_prac/new_module_prac/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_module_prac/new_module_prac/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_module_prac.listing', {
#             'root': '/new_module_prac/new_module_prac',
#             'objects': http.request.env['new_module_prac.new_module_prac'].search([]),
#         })

#     @http.route('/new_module_prac/new_module_prac/objects/<model("new_module_prac.new_module_prac"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_module_prac.object', {
#             'object': obj
#         })
