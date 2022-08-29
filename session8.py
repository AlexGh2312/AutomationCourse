# create a class which has 2 class atr and 3 constr atr
# class atr #1 = model, #2 = manufacturer
# constr var1 = engine, var2 = colour, var3 = is running
# create a method which sets a model and manufacturer
# create another method which prints both model and manufacturer

class Car:
    __model = 'Rav 4'
    __manufacturer = 'Toyota'

    def __init__(self, engine, colour, is_running: bool):
        self.engine = engine
        self.colour = colour
        self.is_running = is_running

    def set_new_model(self, model):
        self.__model = model

    def set_manuf(self, manufacturer):
        self.__manufacturer = manufacturer

    def get_model_and_manuf(self):
        print(f'This model is {self.__model} and the manufacturer is {self.__manufacturer}.')

obj1 = Car(engine="TKO", colour="yellow", is_running= True)
obj1.get_model_and_manuf()
obj1.set_new_model("Logan")
obj1.set_manuf("Dacia")
obj1.get_model_and_manuf()