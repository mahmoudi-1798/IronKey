from .rand import Random

class Generator:
    def __init__(self):
        self.random = Random()
    
    def generate(self, param):
        if param == "very_strong":
            return self.random.very_strong()
        if param == "strong":
            return self.random.strong()
        if param == "medium":
            return self.random.medium()
        if param == "weak":
            return self.random.weak()
        return None

