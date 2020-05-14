class Dog:
    species='mammal'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def description(self):
        return "{} is {} years old".format(self.name,self.age)
    def speak(self,sound):
        return "{} says {} ".format(self.name,sound)
    
Mikey=Dog("Mikey",6)
print(Mikey.description())
print(Mikey.speak("BOw Bow"))

class RussellTerrie(Dog):
    def dogtype(self):
        return "{} is a Russell Terrie".format(self.name)
    def run(self,speed):
        return"{} runs {} miles per hour".format(self.name,speed)

class bulldog(Dog):
    def dogtype(self):
        return "{} is a Bull Dog".format(self.name)
    
Tom=bulldog("Tom",12)
print(Tom.dogtype())

jim=RussellTerrie("Jim",11)
print(jim.run(15))
print(jim.dogtype())

class person():
    species='HOOMAN'
    def __init__(self,name,age,tel,gender):
        self.name=name
        self.age=age
        self.tel=tel
        self.gender=gender
        
    def fullname(self):
        return "{} is {} years old and his phone number is {} and he is {}".format(self.name,self.age,self.tel,self.gender)

ud=person("Usharbudha Dev",23,9833196769,"Male")
print(ud.fullname())


class Pizza:
    def __init__(self,ingredients):
        self.ingredients=ingredients
    def __repr__(self):
        return f'Pizza((self.ingredients!r))'
    #class method
    def margherita(cls):
        return cls(['Mozella','Tomatoes'])
    def prosciutto(cls):
        return cls(['Mozzarella','Tomatoes'])

veggie=Pizza.margherita()
veggie1=Pizza(['Mozeralla','Tomatoes'])
veggie1