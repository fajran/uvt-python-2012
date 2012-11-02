from gi.repository import Gtk

def cetak_halo(sender):
    print "Halo!"

window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)
window.set_title("Hello World!")
window.resize(100, 50)

tombol = Gtk.Button("Halo!")
tombol.connect("clicked", cetak_halo)
tombol.show()
window.add(tombol)

window.show()

Gtk.main()

