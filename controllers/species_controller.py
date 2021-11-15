from flask import Flask, Blueprint, render_template
import repositories.species_repository as species_repository

species_blueprint = Blueprint("species", __name__)

@species_blueprint.route('/stocklist')
def stocklist():
    stocklist = species_repository.select_all()
    return render_template("stocklist/index.html", title = "SMS - Stocklist", results=stocklist)

@species_blueprint.route('/stocklist/search')
def search_list():
    return render_template("stocklist/search.html", title = "SMS - Search Stock")

# @species_blueprint.route('stocklist/search', method= ['POST'])
# def search_single_item():
    