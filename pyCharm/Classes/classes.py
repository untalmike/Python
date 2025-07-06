class Vehicle: # La clase define la especificación
    def __init__(self, make, model): # Definimos los atributos
        self.make = make
        self.model = model
        
    def moves(self): # la función lo mueve
        print('Moves along...')

    def get_make_model(self):
        print(f"i'm a {self.make} {self.model}")

my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade') # It's an object using the class get_make_model and moves
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id): # Definimos los atributos
        super().__init__(make, model) # call the parents
        self.faa_id = faa_id

    def moves(self):
        print('Flies along...')

class Truck(Vehicle):
    def __init__(self, make, model): # Definimos los atributos
        self.make = make
        self.model = model

    def moves(self):
        print('Rumbles along...')

class GolfCart(Vehicle):
    def moves(self):
        pass

cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')

for v in (my_car, your_car, cessna, mack, golfwagon): # It return the same methods 
    v.get_make_model()
    v.moves()
