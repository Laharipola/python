class menu():
    def starter():
        print('Manchurian')
    def main_course():
        print('Biryani')
    def desserts():
        print('Gulab jamun')
class starters(menu):
    def manchurian():
        print('VEG,CHICKEN')
sobj=starters
sobj.starter()
sobj.main_course()
sobj.desserts()
sobj.manchurian()    
    
    

