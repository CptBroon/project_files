from db.run_sql import run_sql
from models.species import Species
# import subcategory_repository as subcategory_repository
import repositories.subcategory_repository as subcategory_repository

# CRUD READ (ALL)
def select_all():
    species_list = []
    
    sql = "SELECT * FROM species"
    results = run_sql(sql)
    
    for row in results:
        species = Species(row["name"], subcategory_repository.select(row['subcategory_id']), row["difficulty"], row["stock_no"], row["buying_price"], row["selling_price"], row["active"], row["id"])
        species_list.append(species)
    return species_list

# READ (DISTINCT VALUES)
def select_distinct(column):
    column_options = []
    sql = f"SELECT DISTINCT {column} FROM species"
    results = run_sql(sql)
    for row in results:
        option = row[column]
        column_options.append(option)
    return column_options
        
# CRUD READ (SOME)
def select(column, value):
    species_list = []
    sql = f"SELECT * FROM species WHERE {column} = %s"
    values = [value]
    search_results = run_sql(sql, values)
    for row in search_results:
        species = Species(row['name'], subcategory_repository.select(row['subcategory_id']), row["difficulty"], row["stock_no"], row["buying_price"], row["selling_price"], row["active"], row["id"])
        species_list.append(species)
    return species_list

# CRUD CREATE
def save(species):
    sql = "INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [species.name, species.difficulty, species.stock_no, species.buying_price, species.selling_price, species.active, species.subcategory.id]
    results = run_sql(sql, values)
    species.id = results[0]['id']
    return species

# CRUD UPDATE
def update(species):
    sql = f"UPDATE species SET (name, difficulty, stock_no, buying_price, selling_price, active) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [species.name, species.difficulty, species.stock_no, species.buying_price, species.selling_price, species.active, species.id]
    run_sql(sql,values)
    
# CRUD DELETE (ALL)
def delete_all():
    sql = "DELETE FROM species"
    run_sql(sql)

# CRUD DELETE (SINGLE)

