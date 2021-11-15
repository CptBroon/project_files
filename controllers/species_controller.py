from flask import Flask, Blueprint, render_template
import repositories.species_repository as species_repository

species_blueprint = Blueprint("species", __name__)

@species_blueprint.route('/stocklist')
def stocklist():
    stocklist = species_repository.select_all()
    return render_template("stocklist/index.html", title = "SMS - Stocklist")
