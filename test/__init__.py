"""Test plugin"""

from meg_runtime import Config, Logger, Plugin, PluginManager

# TODO: Create plugin decorator functions for testing
plugin = PluginManager.get_current()
Logger.info(f'MEG Plugins: {plugin.name()} {plugin.version()}')
