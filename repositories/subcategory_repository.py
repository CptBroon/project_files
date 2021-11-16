from db.run_sql import run_sql
from models.subcategory import Subcategory

def delete_all():
    sql = "DELETE FROM subcategory"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE FROM subcategory WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def save(subcategory):
    sql = "INSERT INTO subcategory (name) VALUES (%s) RETURNING *"
    values = [subcategory.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    subcategory.id = id
    return subcategory

def select_all():
    subcategories = []
    sql = "SELECT * FROM subcategory"
    results = run_sql(sql)
    
    for row in results:
        subcategory = Subcategory(row['name'], row['category_id'], row['id'])
        subcategories.append(subcategory)
    return subcategories

def select_distinct(column):
    column_options = []
    sql = f"SELECT DISTINCT {column} FROM subcategory"
    results = run_sql(sql)
    for row in results:
        option = row[column]
        column_options.append(option)
    return column_options

def select(id):
    sql = "SELECT * FROM subcategory WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    subcategory = Subcategory(result['name'], result['category_id'], result['id'])
    return subcategory

def select_by_name(name):
    sql = "SELECT * FROM subcategory WHERE name = %s"
    values = [name]
    print(values)
    result = run_sql(sql, values)[0]
    subcategory = Subcategory(result['name'], result['category_id'], result['id'])
    return subcategory

def update(subcategory):
    sql = "UPDATE subcategory SET (name, category_id) = (%s, %s) WHERE id = %s"
    values = [subcategory.name, subcategory.category_id, subcategory.id]
    run_sql(sql, values)