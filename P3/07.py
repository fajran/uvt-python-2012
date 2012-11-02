from gi.repository import Gtk

class Aksi:
    def tambah(self, sender):
        print 'tambah'

    def kurang(self, sender):
        print 'kurang'

    def kali(self, sender):
        print 'kali'

    def bagi(self, sender):
        print 'bagi'

builder = Gtk.Builder()
builder.add_from_file("kalkulator.glade")

aksi = Aksi()
builder.connect_signals(aksi)

window = builder.get_object("window_kalkulator")
window.connect("delete-event", Gtk.main_quit)
window.show_all()

Gtk.main()

