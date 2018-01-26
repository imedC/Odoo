# -*- coding: utf-8 -*-
from odoo import http

# class Fbo(http.Controller):
#     @http.route('/fbo/fbo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fbo/fbo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fbo.listing', {
#             'root': '/fbo/fbo',
#             'objects': http.request.env['fbo.fbo'].search([]),
#         })

#     @http.route('/fbo/fbo/objects/<model("fbo.fbo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fbo.object', {
#             'object': obj
#         })