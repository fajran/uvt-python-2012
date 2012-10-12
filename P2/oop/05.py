class SegiEmpat(object):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * self.panjang + 2 * self.lebar

class Persegi(SegiEmpat):
    def __init__(self, sisi):
        super(Persegi, self).__init__(sisi, sisi)

kotak = Persegi(5)
print 'Panjang:', kotak.panjang
print 'Lebar:', kotak.lebar
print 'Luas:', kotak.luas()
print 'Keliling:', kotak.keliling()

