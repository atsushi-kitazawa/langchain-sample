class Person:
    company = 'abc_company'

    @classmethod
    def c_method(cls):
        return cls

    def __init__(self, name, age):
        # インスタンス変数はここで定義する
        self.name = name
        self.age = age

if __name__ == '__main__':
    print(Person.c_method().company)
    Person.c_method().company = 'ABC_company'

    bob = Person('bob', 20)
    print(bob.name)
    print(bob.age)
    print(bob.company)
    bob.company = 'def_company'
    print(bob.company)
    
    alice = Person('alice', 30)
    print(alice.name)
    print(alice.age)
    print(alice.company)