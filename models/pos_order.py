# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PosOrder(models.Model):
    _name = 'pos.order'
    _inherit = ['pos.order','mail.thread', 'mail.activity.mixin']



