# percabangan II

nilai = raw_input("masukkan nilai 1-10: ")
nilai = int(nilai)

if nilai <= 0:
    print "Terlalu kecil"
elif nilai > 10:
    print "Terlalu besar"
else:
    if nilai % 2 == 0:
        print "genap"
    else:
        print "ganjil"

