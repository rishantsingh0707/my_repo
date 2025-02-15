class Vehicle():

    def __init__(self):
        pass

    def get_veh_data(self, name:str, model:str, veh_type:str, n_seats:int):
        self.name = str(name)
        self.model = model
        self.veh_type = veh_type
        self.n_seats = n_seats

    def dims_weight(self, len_mm, brth_mm, ht_mm, wt_kg) -> float:
        self.length = len_mm
        self.breadth = brth_mm
        self.height = ht_mm
        self.weight = wt_kg

    def Core_components(self, chassis_type, suspension, axle, tyres, drivetrain):
        self.chassis_type = chassis_type
        self.suspension = suspension
        self.axle = axle
        self.tyres = tyres
        self.drivetrain = drivetrain

    def gas_fuel(self, cap:float, type:str, extra_tank:int = None):
        self.cap = cap
        self.fuel_type = type
        self.extra_tank = extra_tank

    def engine_spec(self, eng_cap:str, eng_type:str, turbo:str, torque:float):
        self.turbo = "Naturally aspirated"
        self.eng_cap = eng_cap
        self.eng_type = eng_type
        self.turbo = turbo
        self.torque = torque
    
    def transmission(self, trans_type, num_of_gears, oil_cap, clutch):
        self.transmission_type = trans_type
        self.num_gears = num_of_gears
        self.oil_cap = oil_cap
        self.clutch_disk = clutch

    def display_veh_details(self):
        print("~~~~~~~~~~~~~~ Vehicle Details ~~~~~~~~~~~~~~")
        print("Vehicle Name",self.name)
        print("Model name",self.model)
        print("Vehicle type",self.veh_type)
        print("Number of seats",self.n_seats)
    
class Truck(Vehicle):
    # Polymorphism concept
    def get_veh_data(self, name:str, model:str, n_seats:int, compartment:str):
        self.name = str(name)
        self.model = model
        self.n_seats = n_seats
        self.compartment = compartment

car = Vehicle()
car.get_veh_data()
car.display_veh_details()
car.engine_spec()