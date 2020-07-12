import os
import sublime
import sublime_plugin
from datetime import datetime

class ZekeNewNoteCommand(sublime_plugin.WindowCommand):
  """
  Writes a new, empty note file to the notes directory
  """

  def run(self, *args):
    # Format today's date as a compact representation for new note name.
    now = datetime.now()
    note_name = now.strftime('%Y%m%d%H%M%S.zk')
    # What path will this note live in eventually?
    plugin_settings = sublime.load_settings('zeke.sublime-settings')
    default_note_dir = os.path.abspath(os.path.join(sublime.packages_path(), 'notes'))
    note_dir = plugin_settings.get('note_directory', default_note_dir)
    # TODO: Handle case where that directory doesn't exist yet!
    note_full_path = os.path.abspath(os.path.join(note_dir, note_name))
    # Write new note contents to the file.
    with open(note_full_path, mode = 'w', encoding = 'utf-8') as note_file:
      note_file.write('---\ntitle:\ntags:\n---\n\nContents go here.\n')
    # Open a view into that file.
    note_view = self.window.open_file(note_full_path)
