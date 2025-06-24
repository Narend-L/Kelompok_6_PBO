from abc import ABC, abstractmethod

class cakeable(ABC):
    @abstractmethod
    def adon(self): pass

    @abstractmethod
    def panggang(self): pass

class Developable(ABC):
    @abstractmethod
    def kembangkan(self): pass

class Toppable(ABC):
    @abstractmethod
    def topping(self): pass
