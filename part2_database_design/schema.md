# Part 2: Database Design

## Tables

### Companies
- id (PK)
- name
- created_at

### Warehouses
- id (PK)
- company_id (FK)
- name
- location

### Products
- id (PK)
- company_id (FK)
- name
- sku (UNIQUE)
- price (DECIMAL)

### Inventory
- id (PK)
- product_id (FK)
- warehouse_id (FK)
- quantity

### Suppliers
- id (PK)
- name
- contact_email

---

## Relationships
- One company → many warehouses
- One product → many warehouses (via inventory)
- Products ↔ Suppliers (many-to-many)

---

## Design Decisions
- Separate inventory table for multi-warehouse support
- Decimal used for price to avoid precision issues
- Unique constraint on SKU

---

## Missing Requirements
- SKU uniqueness scope (global or per company?)
- Definition of recent sales
- Supplier relationships
- Bundle structure rules
