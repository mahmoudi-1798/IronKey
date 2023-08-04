from .rand import Random

class Generator:
    def __init__(self):
        self.random = Random()
    
    def generate(self, param):
        if param == "Very Strong":
            return self.random.very_strong()
        if param == "Strong":
            return self.random.strong()
        if param == "Medium":
            return self.random.medium()
        if param == "Weak":
            return self.random.weak()
        return None

