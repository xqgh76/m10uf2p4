# -*- coding: utf-8 -*-

from odoo import models, fields, api


class liniadespesa(models.Model):
    _name = "despeses.linies"

    id_despesa = fields.Many2one('despeses.despeses', string="Despesa", help='Id despesa', ondelete='cascade')
    concepte = fields.Char(string = "Concepte", size = 50, required = True)
    preu = fields.Float(string = "Preu", store=True)
    
   
        

