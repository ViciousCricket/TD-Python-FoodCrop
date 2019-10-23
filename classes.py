#Pour crÃ©er des classes abstraites
from abc import ABC, abstractmethod

# On dÃ©finit C comme une classe abstraite: elle hÃ©rite de ABC
from enum import Enum


class C(ABC):
    #Le constructeur est toujours __init__(self,...) et il faut
    #toujours faire figurer le self qui est Ã©quivalent au this de
    #Java
    def __init__(self):
        super().__init__()

    #On dÃ©finit une mÃ©thode abstraite
    @abstractmethod
    def methode_abstraite(self):
        pass #Si on met du code ici on aura une erreur d'execution

class A:
    #Constructeur de la classe A, on peut donner des indices au
    #sujet de types des paramÃ¨tres avec param: type et fixer des
    #valeurs par dÃ©faut avec param: type = valeur
    def __init__(self, param1: str, param2, param3: int = 0):
        #Attribut public
        self.attribut1 = param1

        #Attributs privÃ©s, toujours avec __ en prÃ©fixe
        self.__attrbutprive1 = param2

    #Une mÃ©thode privee
    def __ma_methode_privee(self):
        pass

    #Une mÃ©thode publique
    def methode1(self, param4: str):
        print(self.attribut1 + param4)

    #MÃ©thode qui retourne une valeur, on peut aussi indiquer le type
    #de retour
    def methode2(self, valeur: int) -> int:
        return valeur * 2

#HÃ©ritage multiple
class B(A, C):
    def __init__(self, param1):
        super().__init__(param1, "toto")

    #Surcharge de la mÃ©thode
    def methode1(self, param4):
        print(param4 + self.attribut1)

    def methode_abstraite(self):
        print("Ping")

class D(C):
    def __init__(self):
        super().__init__()

    def methode_abstraite(self):
        print("Pong")

    @staticmethod
    def ma_methode_statique(param1):
        pass


# Creer une Ã©numÃ©ration
class MyEnum(Enum):
    CONSTANTE_1 = 1
    CONSTANTE_2 = 2
    CONSTANTE_3 = 3


# C'est quoi le nil? -> En java c'est null et
# en python c'est None:
#Ici paramÃ¨tre avec None comme valeur par dÃ©faut
def methode(param1 =None):

    #Variable initialisÃ©e Ã  null
    ma_variable = None


