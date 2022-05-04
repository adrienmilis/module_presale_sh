from odoo import models, fields, api, Command


class Order(models.Model):

    _name = 'presale.order'
    _description = 'Customers can preorder products'

    # Attributes #

    name = fields.Char(
        string='Order Reference',
        required=True,
        # readonly=True,
        copy=False,
        default='New',
    )

    # Relations #

    customer_id = fields.Many2one('res.partner', required=True, string='Customer')
    order_line_ids = fields.One2many('presale.order.line', 'order_id', string='Order Lines')

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

    # Overrides #

    @api.model
    def create(self, vals):
        if vals.get('name') == 'New':
            vals['name'] = self.env['ir.sequence'].get('presale.order') or 'New'
        return super().create(vals)

    # Buttons #

    def _get_product_description(self, product):
        default_code = f'[{product.default_code}]' if product.default_code else ""
        description_sale = f'\n{product.description_sale}' if product.description_sale else ""
        return '{} {}{}'.format(default_code, product.name, description_sale)

    def _get_sale_order_line_values(self):
        return [{
            'product_id': order_line_id.product_id.id,
            'name': self._get_product_description(order_line_id.product_id),
            'price_unit': order_line_id.price,
            'product_uom_qty': order_line_id.quantity,
        } for order_line_id in self.order_line_ids]

    def action_validate_order(self):

        self.ensure_one()
        self.env['sale.order'].create({
            'partner_id': self.customer_id.id,
            'order_line': [
                Command.create(vals) for vals in self._get_sale_order_line_values()
            ],
        })
        self.state = 'confirmed'
