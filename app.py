from flask import Flask, render_template
app = Flask(__name__)
from controllers.species_controller import species_blueprint
from controllers.new_controller import new_blueprint
app.register_blueprint(species_blueprint)
app.register_blueprint(new_blueprint)

@app.route('/')
def splash():
    return render_template('splash.html', title='SMS - Stock Management System')

@app.route('/home')
def home():
    return render_template('index.html', title = 'SMS - Home')

if __name__=='__main__':
    app.run(debug=True)