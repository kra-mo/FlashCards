# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gtk

@Gtk.Template(resource_path='/io/github/fkinoshita/FlashCards/ui/deck_row.ui')
class DeckRow(Adw.ActionRow):
    __gtype_name__ = 'DeckRow'

    revealer = Gtk.Template.Child()
    checkbox = Gtk.Template.Child()
    deck_icon = Gtk.Template.Child()
    edit_button = Gtk.Template.Child()
    next_icon = Gtk.Template.Child()

    def __init__(self, deck, **kwargs):
        super().__init__(**kwargs)

        self.deck = deck

        self.set_title(deck.name)
        self.deck_icon.set_label(deck.icon)

