from os import name
from flask import Flask, Blueprint, render_template, request, redirect
import repositories.species_repository as species_repository
import repositories.subcategory_repository as subcategory_repository
from models.species import Species

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

@species_blueprint.route('/species/<name>')
def show_species_info(name):
    species = species_repository.select("name", name)[0]
    return render_template('species/show.html', title = 'SMS - View Species Details', species = species)

@species_blueprint.route('/species/change_stock_form')
def stock_increase_form():
    species_list = species_repository.select_all()
    return render_template('species/change_stock_form.html', results=species_list)

@species_blueprint.route('/species/change_stock_form', methods=['POST'])
def change_stock():
    stock_change_type = request.form['log_type']
    stock_change_value = int(request.form['stock_value'])
    species_name = request.form['species_name']
    species_to_change = species_repository.select("name", species_name)[0]
    if stock_change_type == "sale":
        species_to_change.reduce_stock(stock_change_value)
        species_repository.update(species_to_change)
    else:
        species_to_change.increase_stock(stock_change_value)
        species_repository.update(species_to_change)
    return redirect('/species')
    