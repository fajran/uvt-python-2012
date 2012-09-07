# return

def jumlah_detik(detik, menit=0, jam=0, hari=0):
    return detik + menit * 60 + jam * 3600 + hari * 86400

print "Durasi:", jumlah_detik(45, 50, 2)

