from gi.repository import Gtk

window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)
window.set_title("Hello World!")
window.show()

Gtk.main()

