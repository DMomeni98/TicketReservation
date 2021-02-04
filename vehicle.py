class Vehicle:

    def __init__(self, vehicle_dic):
        # super().__init__()
        self.identifier = vehicle_dic["identifier"]
        self.manufacturer = vehicle_dic["manufacturer"]
        self.model = vehicle_dic["model"]
        self.build_year = vehicle_dic["build_year"]
        self.type = vehicle_dic["type"]
        self.capacity = vehicle_dic["capacity"]


