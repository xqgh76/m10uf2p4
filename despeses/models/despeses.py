# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Despeses(models.Model):
    _name = "despeses.despeses"

    data = fields.Datetime(string = "Data", default=datetime.today(), help='Data')
    total = fields.Float(string = "Total", compute="_calcula_cost_total_despesa", help='Preu total', store=True)
    id_despesa = fields.One2many('despeses.linies', 'id_despesa', string="Ticket")

    def name_get(self):
        nom_modificat = []
        for despesa in self:
            name = "Despesa " + str(despesa.id)
            nom_modificat.append((despesa.id, name))
        return nom_modificat

    @api.depends('id_despesa')
    def _calcula_cost_total_despesa(self):
        preuTotal = 0.0
        for despesa in self:
            for linia in despesa.id_despesa:
                preuTotal = preuTotal + linia.preu 
        self.total = preuTotal
        

