class PengirimPenerimaSama(Exception):
    def __init__(self, nama):
        super(PengirimPenerimaSama, self).__init__()

        self.nama = nama

    def __str__(self):
        return 'Pengirim dan penerima sama, yaitu %s' % self.nama

def kirim_lagu(pengirim, penerima):
    if pengirim == penerima:
        raise PengirimPenerimaSama(pengirim)
    print 'lagu dikirim dari', pengirim, 'ke', penerima

print 'Pengirim lagu:',
pengirim = raw_input()

print 'Penerima:',
penerima = raw_input()

try:
    kirim_lagu(pengirim, penerima)
except PengirimPenerimaSama, e:
    print 'Masalah terjadi:', e

