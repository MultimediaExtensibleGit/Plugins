"""Test plugin"""

from kivy.logger import Logger
from meg_runtime import Config, Plugin, PluginManager

# TODO: Create plugin decorator functions for testing
plugin = PluginManager.get_current()
Logger.info(f'MEG Plugins: {plugin.name()} {plugin.version()}')
