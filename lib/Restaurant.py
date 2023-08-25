class Restaurant:
    def __init__(self, name:str):
        self._name = ""
        self.name = name 

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Restaurant name should be a string!")

    name = property(get_name, set_name)

kfc = Restaurant("7")
print(kfc.name)