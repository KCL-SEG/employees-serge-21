"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, hours=0, rate=0, bonus=0, commision=0, contract_number=1):
        self.name = name
        self.contract = not salary
        self.salary = salary or hours*rate
        self.hours = hours
        self.rate = rate
        self.bonus = bonus
        self.commision = commision
        self.contract_number = contract_number

    def get_pay(self):
        return self.salary + self.bonus +(self.commision * self.contract_number)

    def __str__(self):
        explanation = ''

        if self.contract:
            explanation += f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour'
        else:
            explanation += f'{self.name} works on a monthly salary of {self.salary}'
        
        if self.bonus:
            explanation += f' and receives a bonus commission of {self.bonus}'
        elif self.commision:
            explanation += f' and receives a commission for {self.contract_number} contract(s) at {self.commision}/contract'

        explanation += f'.  Their total pay is {self.get_pay()}.'

        return explanation

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, rate=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, contract_number=4, commision=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, rate=25, contract_number=3, commision=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, rate=30, bonus=600)

print(billie.get_pay(), billie)
print(charlie.get_pay(), charlie)
print(renee.get_pay(), renee)
print(jan.get_pay(), jan)
print(robbie.get_pay(), robbie)
print(ariel.get_pay(), ariel)
