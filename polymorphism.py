class cat:
     def sound(self):
          print("meow!")

class dog:
     def sound(self):
          print("woof!")

def make_sound(animal):
     animal.sound()


my_cat = cat()
my_dog = dog()
make_sound(my_cat)
make_sound(my_dog)

