from Interface.penolakan_operation import PenolakanOperation
from abc import ABC, abstractmethod

class DriverOperation(PenolakanOperation, ABC):
    def menolak_pesanan(self) -> None:
        pass


@abstractmethod
def mengantarkan_pesanan(self)-> None:
    pass

