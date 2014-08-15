import sublime
import sublime_plugin
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "libs"))

from pyslack import SlackClient

class Slackchat:
  def __init__(self):
    settings = sublime.load_settings("SubSlack.sublime-settings")
    token = settings.get('token')
    self.bot = settings.get('bot_name')
    self.room  = '#%s' % settings.get('default_chat')
    self.client = SlackClient(token)

  def post(self,text):
    self.client.chat_post_message(self.room, text,username=self.bot)


class SubSlackCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    def send_to_chat(text):
      chat = Slackchat()
      chat.post(text)
    for region in self.view.sel():
      if not region.empty():
        selection = self.view.substr(region)
        sublime.set_timeout_async(send_to_chat(selection),0)
