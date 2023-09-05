from odoo import fields,models,api

class quickcreate(models.Model):
    _inherit = 'crm.lead'

    user_id=fields.Many2one(
        'res.users', string='Salesperson', default=lambda self: self.env.user,
        domain="['&', ('share', '=', False), ('company_ids', 'in', user_company_ids)]",
        check_company=True, index=True, tracking=True)