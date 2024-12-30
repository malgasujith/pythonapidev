from abc import ABC,abstractmethod


class Reg_base(ABC):

    @abstractmethod
    def has_value(self, password):
        pass

    @abstractmethod
    def user_registration(self, request, count: int = 0):
        pass      