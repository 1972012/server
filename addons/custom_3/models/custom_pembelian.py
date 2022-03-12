from odoo import models, fields

class custom_pembelian(models.Model):
    _name = 'custom.pembelian'

    name = fields.Char(string="Name")
    tanggal = fields.Date(string="Tanggal")
    status = fields.Selection(
        [('draft', 'Draft'), ('to_approve', 'To Approve'), ('approved', 'Approved'), ('done', 'Done')], default="draft")
