-- Assumed tables:
-- customers(id, name, city)
-- orders(id, customer_id, amount, created_at)
-- products(id, name, category, price)
-- order_items(order_id, product_id, quantity)

-- Q1: Total order amount per customer
SELECT
    c.id AS customer_id,
    c.name,
    SUM(o.amount) AS total_spent
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name
ORDER BY total_spent DESC;

-- Q2: Number of orders per customer
SELECT
    customer_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
ORDER BY order_count DESC;

-- Q3: Top 5 highest revenue customers
SELECT
    c.name,
    SUM(o.amount) AS total_spent
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 5;

-- Q4: Monthly revenue
SELECT
    DATE_TRUNC('month', created_at) AS month,
    SUM(amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;

-- Q5: Products with total quantity sold
SELECT
    p.name,
    SUM(oi.quantity) AS total_sold
FROM products p
JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.name
ORDER BY total_sold DESC;

-- Q6: Customers who never placed orders
SELECT
    c.id,
    c.name
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.id IS NULL;