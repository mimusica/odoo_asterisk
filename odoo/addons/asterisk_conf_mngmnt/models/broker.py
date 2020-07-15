# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Broker(models.Model):
    _name = 'broker.settings'
    _description = 'configuration of our broker'

    name = fields.Char(string="Broker Name",size=24, required=True, help="The name of the broker")
    ip = fields.Char(string="ip address", size=15, required=True, help="The ip address of the broker")
    port = fields.Char(string="server port",size=4, required=True, help="The server port that the broke uses")
    ssh_key = fields.Text(string="ssh key", required=False, help="The ssh key used to safely connect to the broker")
    description = fields.Text(string="description", required=False, help="The description of the broker")

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
