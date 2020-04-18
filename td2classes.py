#td2.classes - modif depuis doc de Lulu


class Person:

  def __init__(self,name,age,nationality):
    self.name=name
    self.age=age
    self.nationality=nationality


class Child(Person):

  def __init__(self,school,favorite_color):
    self.school=school
    self.favorite_color=favorite_color

  def whichSchool(self):
    print("I go to",self.school)

  def presentation(self):
    print("My favorite color is",self.favorite_color)
 
  
class Adult(Person):


  def __init__(self,school,nb_children):
    self.job="teacher"
    self.nb_children=nb_children
    self.school=school

  def working(self):
    print("I work as a teacher at", self.school)

  def children(self):
      print("I have",self.nb_children,"children")
 
