from gi.repository import Gtk

class Aksi:
    def __init__(self, entry_satu, entry_dua, label_hasil):
        self.entry_satu = entry_satu
        self.entry_dua = entry_dua
        self.label_hasil = label_hasil

    def tambah(self, sender):
        a = float(self.entry_satu.get_text())
        b = float(self.entry_dua.get_text())
        hasil = a + b
        self.label_hasil.set_label(str(hasil))

    def kurang(self, sender):
        a = float(self.entry_satu.get_text())
        b = float(self.entry_dua.get_text())
        hasil = a - b
        self.label_hasil.set_label(str(hasil))

    def kali(self, sender):
        a = float(self.entry_satu.get_text())
        b = float(self.entry_dua.get_text())
        hasil = a * b
        self.label_hasil.set_label(str(hasil))

    def bagi(self, sender):
        a = float(self.entry_satu.get_text())
        b = float(self.entry_dua.get_text())
        hasil = a / b
        self.label_hasil.set_label(str(hasil))

builder = Gtk.Builder()
builder.add_from_file("kalkulator.glade")

entry_satu = builder.get_object("entry_satu")
entry_dua = builder.get_object("entry_dua")
label_hasil = builder.get_object("label_hasil")

aksi = Aksi(entry_satu, entry_dua, label_hasil)
builder.connect_signals(aksi)

window = builder.get_object("window_kalkulator")
window.connect("delete-event", Gtk.main_quit)
window.show_all()

Gtk.main()

