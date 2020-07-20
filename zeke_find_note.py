import sublime
import sublime_plugin
from .zeke import notes_index

class ZekeFindNoteCommand(sublime_plugin.WindowCommand):
  def run(self):
    note_dir = notes_index.get_note_dir()
    self.notes = notes_index.load_the_notes(note_dir)
    titles = [note.title for note in self.notes]
    self.window.show_quick_panel(titles, self.on_done)

  def on_done(self, index):
    # Which note are we loading?
    note = self.notes[index]
    note_view = self.window.open_file(note.path)
    settings = note_view.settings()
    settings.set('is_zekenote', True)

