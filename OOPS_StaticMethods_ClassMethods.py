class Router():
    update_vlan = 100

    def __init__(self, intname, speed, vlan):
        self.intname = intname
        self.speed = speed
        self.vlan = vlan

    def fullname(self):
        return 'The interface name is {} of speed {} with vlan{}'.format(self.intname, self.speed, self.vlan)

    def update_details(self):
        self.vlan = Router.update_vlan
        return self.vlan

    @classmethod
    def setvlan(cls,update_vlan):
        cls.setvlan = update_vlan


int1 = Router('Fa0/0', 100, 10)

print(int1.setvlan)