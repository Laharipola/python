from abc import ABC
class mobiles(ABC):
    def color():
        pass
    def storage():
        pass
    def cost():
        print("clicks pictures")
class samsung(mobiles):
    def color():
        print('red')
    def storage():
        print('128gb')
    def cost():
        print('1200000')
class vivo(mobiles):
    def color():
        print('blue')
    def storage():
        print('120gb')
    def cost():
        print('1250000')
obj=vivo
vivo.cost()
obj1=vivo
vivo.color()
