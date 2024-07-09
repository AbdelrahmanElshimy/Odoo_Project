from odoo import http
from odoo.http import request
import json

class ShopifyApiController(http.Controller):

    @http.route('/shopify/webhook', type='http', auth='public', methods=['POST'], csrf=False)
    def shopify_webhook(self, **post):
        request.env['shopify.integration'].sudo().search([])  # Access Shopify integration settings
        # Parse the incoming webhook data
        webhook_data = json.loads(request.httprequest.data)
        # Perform actions based on the webhook type (e.g., order creation)
        if webhook_data.get('type') == 'order_created':
            # Process order creation webhook
            # Create a sale order in Odoo
            # Example:
            order_data = webhook_data.get('order')
            order_vals = {
                'name': order_data.get('order_number'),
                'partner_id': order_data.get('customer_id'),
                # Add more fields as needed
            }
            request.env['sale.order'].sudo().create(order_vals)
        return 'Webhook received and processed successfully'
