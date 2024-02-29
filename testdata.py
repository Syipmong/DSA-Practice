class TestData:
    def __init__(self):
        return self

    def setName(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return f'My name is {self.name} and i am {self.age} years old'
    
    def __repr__(self) -> str:
        return self.getName()
    

test = TestData()

test.setName("Shehu", 20)

print(test())