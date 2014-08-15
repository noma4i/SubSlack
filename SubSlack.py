import sublime
import sublime_plugin

sys.path.append(os.path.join(os.path.dirname(__file__), "libs"))


class SubSlackCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print('Cool!')