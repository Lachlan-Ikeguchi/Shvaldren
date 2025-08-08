#!/usr/bin/env python3
from gi.repository import GLib, Gtk
import sys
import gi

gi.require_version("Gtk", "4.0")


class ShvaldrenGenerator(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.shvaldren.generator")
        GLib.set_application_name("Shvaldren Generator")

    def do_activate(self):
        window = Gtk.ApplicationWindow(
            application=self, title="Shvaldren Generator")
        window.present()


if __name__ == "__main__":
    gui = ShvaldrenGenerator()
    exit_status = gui.run(sys.argv)
    sys.exit(exit_status)
