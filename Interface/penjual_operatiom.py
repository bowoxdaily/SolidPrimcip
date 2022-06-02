from ast import Pass
from Interface.penolakan_operation import PenolakanOperation
from abc import ABC , abstractmethod    


class PenjualOperation(PenolakanOperation, ABC):

    @abstractmethod
    def menolak_pesanan(self):
        super().menolak_pesanan()

    @abstractmethod
    def menyiapkan_pesanan(self) -> None:
        pass

