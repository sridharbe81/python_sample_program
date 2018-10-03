class Router():
    update_vlan = 100
    def __init__(self, intname, speed, vlan):
        self.intname = intname
        self.speed = speed
        self.vlan = vlan

    def fullname(self):
        return 'The Interface name is {} of speed {} with vlan {}'.format(self.intname, self.speed, self.vlan)

    def update_details(self):
        self.vlan = self.update_vlan
        return self.vlan

int1 = Router('fa0/1',1000, 10)
int2 = Router('fa1/1', 1000, 20)

print(int1.fullname())
#print(int1.update_vlan)
Router.update_details(int2)
print(int1.fullname())
print(int2.fullname())


# class Router:
#
#     change_vlaninfo = 40
#
#     def __init__(self,intname,vlan):
#         self.intname = intname
#         self.vlan = vlan
#
#     def fullname(self):
#         return '{}@{}'.format(self.intname,self.vlan)
#
#     def change_vlan(self):
#         self.vlan=Router.change_vlaninfo
#         return self.vlan
#
#
# int1 = Router('intfa0/0',20)
# int2 = Router('intfa1/0', 30)
#
# print(int1.change_vlan())
# #Router.change_vlan(int1)
# print(int1.fullname())
# print(int2.fullname())
#
# #
# # print(int1.__dict__)
# # print(int1.change_vlaninfo)
# # print(int2.change_vlaninfo)




