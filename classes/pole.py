class pole():

    def __init__(self,front_pole= None, behind_pole= None, battary=None, temperature=None, ip_addr=None) -> None:
        self.battary= battary
        self.temperature= temperature
        self.front_pole:pole= front_pole
        self.behind_pole:pole= behind_pole
        self.ip_addr= ip_addr

    def send_alarm(self):
        pass
    
    def test_connectivity(self):
        pass

    def update_info(self):
        pass

    def get_poles(self):
        return (self.front_pole, self.behind_pole)

    def get_battary(self):
        return self.battary
    
    def get_temperature(self):
        return self.temperature
    