import os
import zeke.frontmatter as frontmatter
import sublime

class ZekeNote(object):
  """The model representation of a plain-text note format."""
  def __init__(self, path, note_string):
    super(ZekeNote, self).__init__()
    self.path = path
    post = frontmatter.loads(note_string)
    self.title = post['title']
    self.tags = post['tags']
    self.content = post.content


def load_the_notes(notes_dir):
  print(notes_dir)
  note_filenames = []
  for (root, dirs, files) in os.walk(notes_dir):
    note_filenames.extend(files)
  notes = []
  for filename in note_filenames:
    note_path = os.path.join(notes_dir, filename)
    print(note_path)
    with open(note_path) as f:
      contents = f.read()
      notes.append(ZekeNote(note_path, contents))
  return notes


def get_note_dir():
  plugin_settings = sublime.load_settings('zeke.sublime-settings')
  default_note_dir = plugin_settings.get('note_directory', '~/notes')
  note_dir = os.path.expanduser(default_note_dir)
  return note_dir
