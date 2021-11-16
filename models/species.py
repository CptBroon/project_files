class Species:
    
    def __init__(self, name, subcategory, difficulty, stock_no, buying_price, selling_price, active, id=None):
        self.name = name
        self.subcategory = subcategory
        self.difficulty = difficulty
        self.stock_no = stock_no
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.active = active
        self.id = id
        
    def increase_stock(self, delivery_amount):
        self.stock_no += delivery_amount
        
    def reduce_stock(self, sale_amount):
        if self.stock_no >= sale_amount:
            self.stock_no -= sale_amount
        else:
            pass