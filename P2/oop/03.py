class SegiEmpat(object):
    panjang = 10
    lebar = 20
    
    def luas(self):
        return self.panjang * self.lebar

kotak = SegiEmpat()
print 'Panjang:', kotak.panjang
print 'Lebar:', kotak.lebar
print 'Luas:', kotak.luas()

