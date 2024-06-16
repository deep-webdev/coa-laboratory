# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE for full copyright and licensing details.

from odoo import models, fields
from datetime import datetime


def get_years():
    years_list = []
    curr_year = datetime.today().year
    for i in range(curr_year, curr_year+10):
        years_list.append((str(i), str(i)))
    return years_list


class CoaMeasure(models.Model):
    _name = "coa.measure"
    _description = "Certificate of Analysis Measures"
    _rec_name = 'product_id'

    product_id = fields.Many2one(
        'product.product', string="Product", domain="[('is_sample_product', '=', True)]")
    batch_no = fields.Char(string="Batch No.")
    chemical_formula = fields.Char(string="Chemical Formula")
    date = fields.Date(string="Date", default=datetime.today())
    company_id = fields.Many2one(
        'res.company', required=True, readonly=True, default=lambda self: self.env.company)
    purity = fields.Char(string="Purity")
    copper = fields.Char(string="Copper (as Cu)")
    acidity = fields.Char(string="Acidity (Free H2So4)")
    ph = fields.Char(string="pH (5% Solution)")
    lead = fields.Char(string="Lead (as Pb)")
    cadmium = fields.Char(string="Cadmium (as Cd)")
    iron = fields.Char(string="Iron (as Fe)")
    free_moisture = fields.Char(string="Free Moisture")
    mfg_month = fields.Selection([('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), (
        '06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], string="Mfg Month")
    mfg_year = fields.Selection(get_years(), string="Mfg Year")
    exp_month = fields.Selection([('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), (
        '06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], string="Exp Month")
    exp_year = fields.Selection(get_years(), string="Exp Year")
    partner_id = fields.Many2one('res.partner', string="Vendor")
