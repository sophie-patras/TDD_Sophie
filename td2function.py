#td2.function - modif depuis doc tp2.py de Lucille

__author__="Sophie Pat"
__date__="$Date:17/04/2020$"

"""
ex function

def toRoman(n):
    #""convert integer to Roman numeral""
    if not (0 < n < 4000):
        raise OutOfRangeError, "number out of range (must be 1..3999)"
    if int(n) <> n:
        raise NotIntegerError, "non-integers can not be converted"

    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result
"""

import td2_classes

#Define exceptions

#class AgeOutOfRange(AgeError): pass
#class NotIntegerError(RomanError): pass
#class InvalidRomanNumeralError(RomanError): pass

def sameSchool(Prenom1,Prenom2):

  """ détermine si les deux personnes sont dans la même école
   il faut un test pour vérifier que ces écoles existent bien"""

  pass

def knowEachOther(Prenom1, Prenom2):

"""
La fonction établit en fonction de l'age, la ville l'école de fréquentation si deux enfants ou un professeur et un enfant se connaissent.

Prenom est un object de la classe Person
"""

""" A partir des infos de Prenomi, test si classe est correcte :
     - test sur les ages (negatif, trop grand, trop petit)
     - test sur les ecoles
"""

  pass



#Main function

if __name__ == '__main__':

  Robert=Person("Robert",40,'American')
  Leo=Person('Leo',7,'British')
  Robert=Adult("Teacher",3)
  Leo=Child("The Great School", "blue")

  KnowEachOther(Leo, Robert)
