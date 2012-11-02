from gi.repository import Gtk

class Jendela(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        self.set_title("Hello World!")
        self.connect("delete-event", Gtk.main_quit)
        self.resize(100, 50)

        self.angka = 0

        self.tombol = Gtk.Button("Halo!")
        self.tombol.connect("clicked", self.cetak_halo)
        self.add(self.tombol)

    def cetak_halo(self, sender):
        self.angka += 1
        self.tombol.set_label("Angka: %d" % self.angka)

jendela = Jendela()
jendela.show_all()

Gtk.main()

