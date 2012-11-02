from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("kalkulator.glade")

window = builder.get_object("window_kalkulator")
window.connect("delete-event", Gtk.main_quit)
window.show_all()

Gtk.main()

