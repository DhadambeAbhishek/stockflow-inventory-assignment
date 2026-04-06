# Part 1: Code Review & Debugging

## Issues Identified

### 1. No input validation
- Missing required fields can crash API

**Impact:**
- Application crashes
- Invalid data stored

---

### 2. No transaction handling
- Two separate commits used

**Impact:**
- Product created but inventory fails → inconsistent database

---

### 3. SKU uniqueness not enforced
- Duplicate SKUs possible

**Impact:**
- Business confusion and data inconsistency

---

### 4. Incorrect data modeling
- Product tied to one warehouse

**Impact:**
- Cannot support multiple warehouses

---

### 5. No error handling
- No try-catch blocks

**Impact:**
- Server crashes on failure

---

### 6. Price precision issue
- Float may cause inaccuracies

**Impact:**
- Financial errors

---

## Fixed Code

```python
# (paste your improved Flask code here)
