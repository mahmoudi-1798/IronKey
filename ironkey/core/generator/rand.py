import random

class Random:
    def __init__(self):
        self.number = "0123456789"
        self.lowercase_string = "qwertyuiopasdfghjklzxcvbnm"
        self.uppercase_string = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.less_symbol = "@#$%&"
        self.all_symbol = "~`!^&*()_-+=}{][|\:;?/<>,."
    
    def rand(self, variable, number):
        return ''.join(random.sample(variable, number))
    
    def shuffle(self, parameter, len_of_variable):
        return ''.join(random.sample(parameter, len_of_variable))
        
    def weak(self):
        result = self.rand(self.number, 7) + self.rand(self.lowercase_string, 7)
        return self.shuffle(result, len(result))
    
    def medium(self):
        result = self.weak() + self.rand(self.uppercase_string, 7)
        return self.shuffle(result, len(result))
    
    def strong(self):
        result = self.medium() + self.rand(self.less_symbol, 5)
        return self.shuffle(result, len(result))
        
    def very_strong(self):
        result = self.strong() + self.rand(self.all_symbol, 7)
        return self.shuffle(result, len(result))


