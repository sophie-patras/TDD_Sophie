# test_td2classes.py

"""
Unit test for td2function.py

Ligne de commande : $ python3 -m unittest discover
"""

__author__="Sophie Pat"
__date__="$Date:17/04/2020$"


import td2classes
import td2function
import unittest

  Robert=td2classes.Person("Robert",40,'American')
Robert=td2classes.Adult("Les Copains",3)
#Tests sur les classes

class KnownChild(unittest.TestCase):
  

  Leo=td2classes.Person('Leo',7,'British')
  Leo=td2classes.Child("Moneghetti", "blue")
  Remi=td2classes.Person('Remi',5,'Italiano')
  Remi=td2classes.Child('Les Copains', 'blue')
  
  """ Comme dans l'exemple Roman, il faudrait définir beaucoup plus de profil d'individus pour pouvoir tester les fonctions defeinies plus tard sur un nb représentatifs de cas
  """
   
  knownIndiv = ( Leo, Remi)

  knownSchools = (("Les Copains",3,11), ("Tenao",6,11),("Paul Doumer",3,6),("Les Cigales",6,12),("Moneghetti",3,6))

 
  def testSchoolsExist (self): 
  """On ne sait traiter que les cas d'eleve des ecoles de Beausoleil"""

     for prenom in self.knownIndiv:
         a=prenom.school
         self.assertIn(a, (self.knownSchools[0][i] for i in range 5))
  
   """ On verifie que l'enfant peut effectivement etre dans cette ecole etant donne son age"""

  def testChildInSchool (self):
     for prenom in self.knownIndiv:
         age=prenom.age
         

class BadIndividu(unittest.TestCase):
  
  def testAge(self):
      self.assertRaises(td2classes.OutOfRangeError, td2.egvhqsb, 77)

class (unittest.TestCase):

   def testNegative(self):
       




if __name__=="__main__":
   unittest.main()
