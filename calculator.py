class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multip(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b == 0:
            return None
        return a / b
