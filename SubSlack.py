import sublime
import sublime_plugin
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "libs"))

from pyslack import SlackClient

class Slackchat:
  def __init__(self):
    settings = sublime.load_settings("SubSlack.sublime-settings")
    token  = settings.get('token')
    self.room  = '#%s' % settings.get('default_chat')
    self.client = SlackClient(token)

  def post(self,text):
    self.client.chat_post_message(self.room, "testing, testing...",username='alex')


class SubSlackCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    chat = Slackchat()
    chat.post("dddd")