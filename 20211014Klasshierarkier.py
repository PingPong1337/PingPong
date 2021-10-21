class Computer(object):
    def __init__(self, name, cpu):
        self.name = name
        self.cpu = cpu

class Laptop(Computer):
    def __init__(self, name, cpu, manufacturer):
        super(Laptop, self).__init__(name, cpu)
        self.manufacturer = manufacturer

class AutomatedTellerMachine(Computer):
    def __init__(self, name, cpu, bank):
        super(AutomatedTellerMachine, self).__init__(name, cpu)
        self.bank = bank