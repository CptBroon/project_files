import pdb
from models.category import Category
from models.subcategory import Subcategory
from models.species import Species

import repositories.species_repository as species_repository
import repositories.subcategory_repository as subcategory_repository
import repositories.category_repository as category_repository

# CLEAR ALL TABLES
species_repository.delete_all()
subcategory_repository.delete_all()
category_repository.delete_all()

# CREATE DUMMY DATA
category1 = Category("Dog")
category2 = Category("Cat")
category3 = Category("Bird")
category4 = Category("Reptile")
category_repository.save(category1)
category_repository.save(category2)
category_repository.save(category3)
category_repository.save(category4)

subcategory1 = Subcategory("Large dog", 1)
subcategory2 = Subcategory("Medium dog", 1)
subcategory3 = Subcategory("Small dog", 1)
subcategory4 = Subcategory("Haired cat", 2)
subcategory5 = Subcategory("Hairless cat", 2)
subcategory6 = Subcategory("Tropical bird", 3)
subcategory7 = Subcategory("Native bird", 3)
subcategory8 = Subcategory("Snake", 4)
subcategory9 = Subcategory("Gecko", 4)
subcategory10 = Subcategory("Pogona", 4)
subcategory_repository.save(subcategory1)
subcategory_repository.save(subcategory2)
subcategory_repository.save(subcategory3)
subcategory_repository.save(subcategory4)
subcategory_repository.save(subcategory5)
subcategory_repository.save(subcategory6)
subcategory_repository.save(subcategory7)
subcategory_repository.save(subcategory8)
subcategory_repository.save(subcategory9)
subcategory_repository.save(subcategory10)

species1 = Species('Labrador', 1, 'Beginner', 3, 500, 800, True)
species2 = Species('Husky', 1, 'Expert', 1, 700, 1000, True)
species3 = Species('Border Collie', 2, 'Intermediate', 1, 800, 1400, True)
species4 = Species('Chihuahua', 3, 'Intermediate', 1, 450, 750, True)
species5 = Species('Dachshund', 3, 'Beginner', 2, 600, 900, True)

species6 = Species('Persian', 4, 'Beginner', 2, 900, 1500, True)
species7 = Species('Bengal', 4, 'Expert', 1, 1200, 1700, True)
species8 = Species('Sphynx', 5, 'Intermediate', 1, 1000, 1600, True)

species9 = Species('Parrot', 6, 'Beginner', 1, 450, 800, True)
species10 = Species('Robin', 7, 'Beginner', 0, 100, 200, False)

species11 = Species('Boa', 8, 'Intermediate', 5, 20, 50, True)
species12 = Species('Bearded Dragon', 10, 'Beginner', 6, 25, 80, True)
species13 = Species('Crested Gecko', 9, 'Intermediate', 3, 30, 75, True)
species14 = Species('Leopard Gecko', 9, 'Intermediate', 2, 30, 75, True)

species_repository.save(species1)
species_repository.save(species2)
species_repository.save(species3)
species_repository.save(species4)
species_repository.save(species5)
species_repository.save(species6)
species_repository.save(species7)
species_repository.save(species8)
species_repository.save(species9)
species_repository.save(species10)
species_repository.save(species11)
species_repository.save(species12)
species_repository.save(species13)
species_repository.save(species14)





