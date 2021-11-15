from db.run_sql import run_sql
from models.species import Species

def select_all():
    species_list = []
    
    sql = "SELECT * FROM species"
    results = run_sql(sql)
    
    for row in results:
        species = Species(row["name"], row["subcategory_id"], row["difficulty"], row["stock_no"], row["buying_price"], row["selling_price"], row["active"], row["id"])
        species_list.append(species)
    return species_list

def select_single_species(species):
    species_list = []
    sql = "SELECT * FROM species WHERE name = %s"
    values = [species.name]
    result = run_sql(sql, values)
    for row in result:
        species = Species(row["name"], row["subcategory_id"], row["difficulty"], row["stock_no"], row["buying_price"], row["selling_price"], row["active"], row["id"])
        species_list.append(species)
    return species_list
    
    