from os import name
from flask import Flask, Blueprint, render_template, request, redirect
from models.category import Category
from models.subcategory import Subcategory
import repositories.species_repository as species_repository
import repositories.subcategory_repository as subcategory_repository
import repositories.category_repository as category_repository
from models.species import Species

new_blueprint = Blueprint("new", __name__)

@new_blueprint.route('/new')
def new():
    return render_template('new/new.html', title = "SMS - Add new details")

@new_blueprint.route('/new/category')
def new_category():
    categories = category_repository.select_all()
    return render_template('new/new_category.html', title="SMS -Add new Category", categories=categories)

@new_blueprint.route('/new/category', methods=['POST'])
def create_new_category():
    new_category = Category(request.form['name'])
    category_repository.save(new_category)
    return redirect ('/new')

@new_blueprint.route('/new/subcategory')
def new_subcategory():
    categories = category_repository.select_all()
    subcategories = subcategory_repository.select_all()
    return render_template('new/new_subcategory.html', title="SMS - Add new Subcategory", categories = categories, subcategories=subcategories)

@new_blueprint.route('/new/subcategory', methods=['POST'])
def create_new_subcategory():
    category = category_repository.select(request.form['category'])
    new_subcategory = Subcategory(request.form['name'], category)
    subcategory_repository.save(new_subcategory)
    return redirect ('/new')

@new_blueprint.route('/new/species')
def new_species():
    categories = category_repository.select_all()
    subcategories = subcategory_repository.select_all()
    all_species = species_repository.select_all()
    possible_difficulties = species_repository.select_distinct("difficulty")
    return render_template('new/new_species.html', title="SMS - Add new Species", categories=categories, subcategories=subcategories, species=all_species, possible_difficulties=possible_difficulties)

@new_blueprint.route('/new/species', methods=['POST'])
def create_new_species():
    subcategory = subcategory_repository.select(request.form['subcategory'])
    new_species = Species(request.form['name'], subcategory, request.form['difficulty'], request.form['stock_no'], request.form['buying_price'], request.form['selling_price'], request.form['active'])
    species_repository.save(new_species)
    return redirect('/new')