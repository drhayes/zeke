import sublime
import sublime_plugin

class ZekeEventListener(sublime_plugin.EventListener):
  def on_load(self, view):
    # Is this view a zeke note?
    # 1. Find scope at beginning of file.
    scope_name = view.scope_name(0)
    # 2. Does the scope contain the text 'zekenote'
    if 'zekenote' in scope_name:
      # 3. Set the 'is_zekenote' flag for our other commands and things.
      settings = view.settings()
      settings.set('is_zekenote', True)
      if settings.get('zeke_to_the_end', False):
        sel = view.sel()
        sel.clear()
        sel.add(sublime.Region(view.size(), view.size()))

