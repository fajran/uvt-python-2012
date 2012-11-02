from gi.repository import Gtk
from gi.repository import WebKit

class Jendela(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World!")

        self.connect("delete-event", Gtk.main_quit)
        self.resize(400, 300)
        
        kotak = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        kotak_atas = Gtk.Box()
        kotak.pack_start(kotak_atas, False, True, 0)

        self.alamat = Gtk.Entry()
        kotak_atas.pack_start(self.alamat, True, True, 5)

        tombol = Gtk.Button("Buka")
        tombol.connect("clicked", self.buka)
        kotak_atas.add(tombol)


        self.browser = WebKit.WebView()
        kotak.pack_start(self.browser, True, True, 0)

        self.add(kotak)

    def buka(self, sender):
        self.browser.open(self.alamat.get_text())

jendela = Jendela()
jendela.show_all()

Gtk.main()

