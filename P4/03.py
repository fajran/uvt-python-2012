try:
    print 1 / 0
except ZeroDivisionError:
    print "Tidak boleh ada pembagian dengan nol"
except OSError:
    print "Terjadi masalah saat mengakses berkas"
except (ValueError, TypeError), e:
    print "Terjadi masalah: ", e

