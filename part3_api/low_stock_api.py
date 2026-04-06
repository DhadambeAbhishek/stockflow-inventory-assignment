from flask import jsonify

def get_low_stock_alerts(company_id):
    alerts = []

    # Dummy logic (replace with DB queries)
    products = [
        {
            "product_id": 1,
            "name": "Widget A",
            "sku": "WID-001",
            "quantity": 5,
            "threshold": 20,
            "warehouse_id": 101,
            "warehouse_name": "Main Warehouse",
            "supplier": {
                "id": 201,
                "name": "Supplier Corp",
                "contact_email": "orders@supplier.com"
            }
        }
    ]

    for p in products:
        if p["quantity"] < p["threshold"]:
            alerts.append({
                "product_id": p["product_id"],
                "product_name": p["name"],
                "sku": p["sku"],
                "warehouse_id": p["warehouse_id"],
                "warehouse_name": p["warehouse_name"],
                "current_stock": p["quantity"],
                "threshold": p["threshold"],
                "days_until_stockout": 10,
                "supplier": p["supplier"]
            })

    return jsonify({
        "alerts": alerts,
        "total_alerts": len(alerts)
    })
