class Restaurant:
    # Initialize a Restaurant object with an empty name
    def __init__(self, name:str):
        self._name = ""
        self.name = name 

    # Getter method to retrieve the restaurant's name
    def get_name(self):
        return self._name
    
    # Setter method to set the restaurant's name with input validation
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Restaurant name should be a string!")

    # Name property created using get_name and set_name
    name = property(get_name, set_name)

