from db.run_sql import run_sql
from models.category import Category

def delete_all():
    sql = "DELETE FROM category"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE FROM category WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def save(category):
    sql = "INSERT INTO category (name) VALUES (%s) RETURNING *"
    values = [category.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    category.id = id
    return category

def select_all():
    categories = []
    sql = "SELECT * FROM category"
    results = run_sql(sql)
    
    for row in results:
        category = Category(row['name'], row['id'])
        categories.append(category)
    return categories

def select(id):
    sql = "SELECT * FROM category WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    category = Category(result['name'], result['id'])
    return category

def update(category):
    sql = "UPDATE category SET (name) = (%s) WHERE id = %s"
    values = [category.name, category.id]
    run_sql(sql, values)