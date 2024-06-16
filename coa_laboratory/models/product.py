# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE for full copyright and licensing details.

from odoo import models, fields, api


class ProductTemplate(models.Model):
	_inherit = "product.template"

	is_sample_product = fields.Boolean(string="Sample Product", compute='_compute_sample_product',
        inverse='_set_compute_product', store=True)
	coa_ids = fields.Many2many('coa.measure', compute="_compute_all_coa_per_template")
	coa_product_count = fields.Integer(compute="_compute_coas")

	def _compute_coas(self):
		for rec in self:
			rec.coa_product_count = len(rec.coa_ids.ids)

	@api.depends('product_variant_ids.is_sample_product')
	def _compute_sample_product(self):
		self._compute_template_field_from_variant_field('is_sample_product')

	def _set_compute_product(self):
		self._set_product_variant_field('is_sample_product')

	@api.depends('product_variant_ids.coa_ids')
	def _compute_all_coa_per_template(self):
		for rec in self:
			rec.coa_ids = False
			if len(rec.product_variant_ids.ids) == 1:
				rec.coa_ids = rec.product_variant_ids.coa_ids.ids

	def action_view_coa(self):
		return {
	        'name': 'COA',
	        'view_type': 'tree',
	        "view_mode": 'tree,form',
	        'res_model': 'coa.measure',
	        'type': 'ir.actions.act_window',
	        'domain': [('id', 'in', self.coa_ids.ids)],
	    }


class ProductProduct(models.Model):
	_inherit = "product.product"

	is_sample_product = fields.Boolean(string="Sample Product")
	coa_ids = fields.One2many('coa.measure', 'product_id')
	coa_product_count = fields.Integer(compute="_compute_coas")

	def _compute_coas(self):
		for rec in self:
			rec.coa_product_count = len(rec.coa_ids.ids)

	def action_view_coa(self):
		return {
	        'name': 'COA',
	        'view_type': 'tree',
	        "view_mode": 'tree,form',
	        'res_model': 'coa.measure',
	        'type': 'ir.actions.act_window',
	        'domain': [('id', 'in', self.coa_ids.ids)],
	    }