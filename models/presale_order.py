from odoo import models, fields, api


class Order(models.Model):

    _name = 'presale.order'
    _description = 'Customers can preorder products'

    # Attributes #

    name = fields.Char(
        string='Order Reference',
        required=True,
        # readonly=True,
        copy=False,
        states={'draft': [('readonly', False)]},
        default=lambda self: ('New')
    )

    # Relations #

    customer_id = fields.Many2one('res.partner', required=True, string='Customer')
    # order_line_ids

    # Default fields #

    state = fields.Selection(
        selection=[('draft', 'Draft'), ('confirmed', 'Confirmed')],
        required=True,
        copy=False,
        string='Stage',
        readonly=True,
        default='draft',
    )
    active = fields.Boolean(default=True)

    # name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name') == 'New':
            vals['name'] = self.env['ir.sequence'].get('presale.order') or 'New'
        return super().create(vals)
