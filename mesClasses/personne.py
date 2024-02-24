from abc import ABC, abstractmethod
from tkinter.messagebox import showinfo,showerror
import pickle

class Personne(ABC):
    def __init__(self, num, nom, sexe, ville):
        self.num = num
        self.nom = nom
        self.sexe = sexe
        self.ville = ville

    @abstractmethod
    def methodAA(self):
        pass

    def __str__(self):
        return f'{self.num}, {self.nom}'

class Client(Personne):
    def methodAA(self):
        print("je suis plus abstraite")

class Clients:
    __mesClients = []

    @classmethod
    def getClients(cls):
        return cls.__mesClients

    @classmethod
    def getCount(cls):
        return len(cls.__mesClients)

    @classmethod
    def chercherClient(cls, num):
        pos = -1
        for i in range(cls.getCount()):
            if cls.__mesClients[i].num == num:
                pos = i
                break
        return pos

    @classmethod
    def addClient(cls, cl):
        pos = cls.chercherClient(cl.num)
        if pos == -1:
            cls.__mesClients.append(cl)
        else :
            showinfo(title='Alert',message="Client existe déjà!!!!")

    @classmethod
    def updateClient(cls, cl):
        pos = cls.chercherClient(cl.num)
        if pos != -1:
            cls.__mesClients[pos]=cl
        else :
            showerror(title='Alert',message="le Client n'existe pas!!!!")

    @classmethod
    def deleteClient(cls, num):
        pos = cls.chercherClient(num)
        if pos != -1:
            cls.__mesClients.pop(pos)
        else :
            showerror(title='Alert',message="le Client n'existe pas!!!!")

    @classmethod
    def enregistrer(cls, nomFichier):
        with open(nomFichier, "wb") as pointf:
            pickle.dump(cls.__mesClients, pointf)
            pointf.close()
            showinfo(title='Alert',message="Fichier enregistré avec succés")


    @classmethod
    def charger(cls, nomFichier):
        with open(nomFichier, "rb") as pointf:
            cls.__mesClients = pickle.load(pointf)
            pointf.close()
            showinfo(title='Alert',message="Fichier charger avec succés")


    # def __init__(self, mesClients: list):
    #     self.__mesClients = mesClients
    #
    # def __getitem__(self, item):
    #     return self.__mesClients[item]
    #
    # def __setitem__(self, key, value):
    #     self.__mesClients[key] = value
    #
    # def __add__(self, other):
    #     self.__mesClients.append(other)
    #
    # def __len__(self):
    #     return len(self.__mesClients)
    #
    # def tri(self):
    #     print("kkkkkkkkkk")