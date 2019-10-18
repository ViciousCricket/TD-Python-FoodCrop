#Pour créer des classes abstraites
from abc import ABC, abstractmethod

# On définit C comme une classe abstraite: elle hérite de ABC
class C(ABC):
    #Le constructeur est toujours __init__(self,...) et il faut
    #toujours faire figurer le self qui est équivalent au this de
    #Java
    def __init__(self):
        super().__init__()

    #On définit une méthode abstraite
    @abstractmethod
    def methode_abstraite(self):
        pass #Si on met du code ici on aura une erreur d'execution

class A:
    #Constructeur de la classe A, on peut donner des indices au
    #sujet de types des paramètres avec param: type et fixer des
    #valeurs par défaut avec param: type = valeur
    def __init__(self, param1: str, param2, param3: int = 0):
        #Attribut public
        self.attribut1 = param1

        #Attributs privés, toujours avec __ en préfixe
        self.__attrbutprive1 = param2

    #Une méthode privee
    def __ma_methode_privee(self):
        pass

    #Une méthode publique
    def methode1(self, param4: str):
        print(self.attribut1 + param4)

    #Méthode qui retourne une valeur, on peut aussi indiquer le type
    #de retour
    def methode2(self, valeur: int) -> int:
        return valeur * 2

#Héritage multiple
class B(A, C):
    def __init__(self, param1):
        super().__init__(param1, "toto")

    #Surcharge de la méthode
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
