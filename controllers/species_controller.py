from flask import Flask, Blueprint, render_template, request
import repositories.species_repository as species_repository
import repositories.subcategory_repository as subcategory_repository

species_blueprint = Blueprint("species", __name__)

@species_blueprint.route('/species')
def species_list():
    species = species_repository.select_all()
    return render_template("species/index.html", title = "SMS - Stocklist", results=species)

@species_blueprint.route('/species', methods=['POST'])
def species_list_single():
    criteria = request.form['criteria_option']
    if criteria == "subcategory":
        results = subcategory_repository.select_distinct('name')
    else:
        results = species_repository.select_distinct(criteria)
    return render_template("species/search.html", title = f'SMS - Search species by {criteria.capitalize()}', criteria = criteria, results=results)

@species_blueprint.route('/species/results', methods=['POST'])
def search_results():
    criteria = request.form['search_criteria']
    print(criteria)
    result = request.form['search_options']
    print(result)
    if criteria == "subcategory":
        subcat = subcategory_repository.select_by_name(result)
        print(subcat)
        results = species_repository.select("subcategory_id", subcat.id)
        print(results)
    else:
        results = species_repository.select(criteria, result)
    return render_template("species/index.html", title = "SMS - Search Results", results=results)