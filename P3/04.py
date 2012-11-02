from gi.repository import Gtk

class Jendela(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World!")

        self.connect("delete-event", Gtk.main_quit)
        self.resize(200, 50)

        kotak = Gtk.Box()
        self.add(kotak)

        self.isian = Gtk.Entry()
        kotak.pack_start(self.isian, True, True, 5)

        tombol = Gtk.Button("Cetak")
        tombol.connect("clicked", self.cetak)
        kotak.add(tombol)

    def cetak(self, sender):
        print 'Teks:', self.isian.get_text()

jendela = Jendela()
jendela.show_all()

Gtk.main()

