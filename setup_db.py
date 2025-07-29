import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Drop old products table if exists
c.execute("DROP TABLE IF EXISTS products")

# Create new products table
c.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    price REAL,
    image TEXT
)
""")

# Insert sample products
products = [
    ('Laptop', 'High-performance laptop with 16GB RAM', 1299.99, 'laptop.png'),
    ('Mouse', 'Ergonomic wireless mouse', 29.99, 'mouse.png'),
    ('Keyboard', 'Mechanical RGB keyboard', 79.99, 'keyboard.png'),
    ('Monitor', '27″ Full HD display', 199.99, 'monitor.png'),
    ('Webcam', '1080p webcam with mic', 49.99, 'webcam.png'),
    ('Smartphone', 'Latest-gen smartphone with AMOLED screen', 899.99, 'smartphone.png'),
    ('Charger', 'Fast charger 65W', 19.99, 'charger.png'),
    ('Headphones', 'Noise-cancelling over-ear headphones', 149.99, 'headphones.png'),
    ('USB Cable', 'Durable USB‑C to USB‑A cable', 9.99, 'cable.png'),
    ('Gaming Chair', 'Ergonomic chair with lumbar support', 249.99, 'chair.png'),
]

c.executemany("INSERT INTO products (name, description, price, image) VALUES (?, ?, ?, ?)", products)
conn.commit()
conn.close()

print("✅ Product database setup complete.")
