# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FboProject(models.Model):
    _name ="fbo.project"
    _inherit = 'res.partner'
    begin_date = fields.Date(string="Begin Date")
    end_date = fields.Date(default="12/31/2050")

class FboContact(models.Model):
    _inherit = 'res.partner'


