from rand import Random

class Generator:
    def __init__(self, very_strong=False, strong=False, 
                 medium=False, weak=False):
        self.very_strong = very_strong
        self.strong = strong
        self.medium = medium
        self.weak = weak
        self.random = Random()
    
    def generate(self):
        if self.very_strong is True:
            return self.random.very_strong()
        if self.strong is True:
            return self.random.strong()
        if self.medium is True:
            return self.random.medium()
        if self.weak is True:
            return self.random.weak()
        return None

