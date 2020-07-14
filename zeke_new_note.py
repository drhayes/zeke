import os
import sublime
import sublime_plugin
from datetime import datetime
import re

def slugify(text):
  # re.sub(pattern, repl, string, count=0, flags=0)
  text = str.lower(text)
  text = re.sub(r'[-_]+', '-', text)
  text = re.sub(r'\W+', '-', text)
  text = text.rstrip('-')
  return text

class ZekeNewNoteCommand(sublime_plugin.WindowCommand):
  """
  Prompts user for a title for the new note. Creates it.
  """

  def run(self, title):
    # Format today's date as a compact representation for new note name.
    now = datetime.now()
    note_date_stamp = now.strftime('%Y%m%d%H%M%S')
    note_name = now.strftime('{0}-{1}.zk'.format(note_date_stamp, slugify(title)))
    # What path will this note live in eventually?
    plugin_settings = sublime.load_settings('zeke.sublime-settings')
    default_note_dir = plugin_settings.get('note_directory', '~/notes')
    note_dir = os.path.expanduser(default_note_dir)
    # TODO: Handle case where that directory doesn't exist yet!
    note_full_path = os.path.abspath(os.path.join(note_dir, note_name))
    # Write some default content in there.
    with open(note_full_path, mode = 'w', encoding = 'utf-8') as note_file:
      note_file.write('---\ntitle: {0}\ntags:\n---\n\n'.format(title))
    # Open a view into that file.
    note_view = self.window.open_file(note_full_path)
    settings = note_view.settings()
    settings.set('is_zekenote', True)
    settings.set('zeke_to_the_end', True)


  def input(self, args):
    return ZekeNoteTitleInputHandler()


class ZekeNoteTitleInputHandler(sublime_plugin.TextInputHandler):
  def name(self):
    return 'title'

  def placeholder(self):
    return 'Enter your title here'
