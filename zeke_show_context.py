import sublime
import sublime_plugin

class ZekeShowContextListener(sublime_plugin.ViewEventListener):
  @classmethod
  def is_applicable(self, settings):
    is_zekenote = settings.get('is_zekenote', False)
    return is_zekenote


  def on_post_save(self):
    # Display the context for the zekenote.
    window = self.view.window()
    context_panel = window.create_output_panel('zeke_context')
    context_panel.set_read_only(True)
    context_panel.set_scratch(True)
    # self.window.run_command('show_panel', {
    #   'panel': 'output.zeke_context'
    # })
