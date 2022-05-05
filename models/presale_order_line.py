from odoo import fields, models, api


class OrderLine(models.Model):

    _name = "presale.order.line"
    _description = "Line in a presale order"

    # Attributes #

    quantity = fields.Integer(required=True, default=1)
    price = fields.Float(required=True)  # from the product

    # Relations #

    order_id = fields.Many2one('presale.order', string='Order', required=True)
    product_id = fields.Many2one('product.product', required=True, string="Product")

    @api.onchange('product_id')
    def _onchange_price(self):
        for record in self:
            record.price = record.product_id.list_price

    # Constraints #

    _sql_constraints = [
        ('quantity_strictly_positive', 'CHECK(quantity > 0)', 'The quantity must be strictly positive.'),
        ('price_positive', 'CHECK(price >= 0)', 'The unit price must be positive.')
    ]
