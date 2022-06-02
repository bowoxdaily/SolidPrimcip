from Interface.penjual_operation import PenjualOperation

class PenjualController(PenjualOperation):

    def menolak_pesanan(self)-> None:
        print ("Penjual Menolak Pesanan, Stok Habis")


    def menyiapkan_pesanan(self)-> None:
        print ("Penjual Menyiapkan pesanan Seusai Pilihan")    