python -c "
content = '''# API Requirements - E-commerce Product API

## Domain
E-commerce product and order management system for an online retail platform.

## Target Users
- **Developers**: integrate product catalog and order management into frontend applications
- **Admins**: manage products, categories, inventory, and process orders
- **Analysts**: generate sales reports and monitor inventory levels
- **Customers**: browse products, place orders, and track order status

## Core Operations

### Product Operations
1. **Create Product** - Add a new product with name, price, category, stock, and description
2. **Get Product by ID** - Retrieve full product details including stock level
3. **Update Product** - Modify product details such as price, description, or category
4. **Delete Product** - Soft delete a product (mark as inactive)
5. **Search Products** - Search products by name, category, or price range with pagination
6. **List All Products** - Retrieve paginated list of all active products

### Inventory Operations
7. **Update Stock** - Increase or decrease product stock quantity
8. **Get Low Stock Products** - Retrieve products where stock is below a threshold

### Order Operations
9. **Create Order** - Place a new order with product ID, quantity, and customer info
10. **Get Order by ID** - Retrieve order details and current status
11. **Update Order Status** - Change order status (pending, processing, shipped, delivered, cancelled)
12. **List Customer Orders** - Retrieve all orders for a specific customer

## Data Rules
- Product SKU must be unique across all products
- Product price must be greater than 0
- Stock quantity must be a non-negative integer
- Product name must be between 3 and 100 characters
- Order quantity must be at least 1
- Customer email must be a valid email format
- Product category must match one of the predefined categories
- Orders cannot be placed for products with stock of 0
- Order status transitions must follow: pending -> processing -> shipped -> delivered

## Non-Functional Requirements
- Response time must be under 200ms for all GET endpoints
- Response time must be under 500ms for all POST and PUT endpoints
- JWT authentication required for all write operations (POST, PUT, DELETE)
- Public read access allowed for product listing and search endpoints
- Rate limiting: maximum 100 requests per minute per API key
- All responses must be in JSON format
- API must support pagination for all list endpoints with default page size of 20
- API versioning via URL prefix (e.g. /api/v1/)
- HTTPS required for all endpoints in production
'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\api_prototyper\api_requirements.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
"