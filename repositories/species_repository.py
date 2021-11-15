from db.run_sql import run_sql
from models.species import Species

# CRUD READ (ALL)
def select_all():
    species_list = []
    
    sql = "SELECT * FROM species"
    results = run_sql(sql)
    
    for row in results:
        species = Species(row["name"], row["subcategory_id"], row["difficulty"], row["stock_no"], row["buying_price"], row["selling_price"], row["active"], row["id"])
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
        species = Species(row['name'], row['subcategory_id'], row["difficulty"], row["stock_no"], row["buying_price"], row["selling_price"], row["active"], row["id"])
        species_list.append(species)
    return species_list

# CRUD CREATE
def save(species):
    sql = "INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [species.name, species.difficulty, species.stock_no, species.buying_price, species.selling_price, species.active, species.subcategory]
    result = run_sql(sql, values)
    new_species_db = result[0]
    new_species = Species(new_species_db['name'], new_species_db['subcategory_id'], new_species_db['difficulty'], new_species_db['stock_no'], new_species_db['buying_price'], new_species_db['selling_price'], new_species_db['active'])
    return new_species

# CRUD UPDATE
def update(species):
    sql = f"UPDATE species SET (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [species.name, species.difficulty, species.stock_no, species.buying_price, species.selling_price, species.active, species.subcategory, species.id]
    run_sql(sql,values)
    
# CRUD DELETE (ALL)
def delete_all():
    sql = "DELETE FROM species"
    run_sql(sql)

# CRUD DELETE (SINGLE)

