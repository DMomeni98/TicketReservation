from vehicle import Vehicle

class Agancy:
    def __init__(self, agency_dic ):
        # super().__init__()
        self.name = agency_dic["name"]
        self.phone = agency_dic["phone"]
        self.email = agency_dic["email"]
        self.manager_name = agency_dic["manager_dic"]
        self.postal_code = agency_dic["postal_code"]
        self.email = agency_dic["agency"]
        self.vehicles = agency_dic["vehicles"]
    