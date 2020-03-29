"""Test plugins"""

import os
import sys

if 'MEG_PLUGINS_PATH' not in os.environ:
    os.environ['MEG_PLUGINS_PATH'] = os.path.dirname(sys.path[0])

from meg_runtime import PluginManager

# Test plugins
def test_plugins():
    """Test plugins"""
    assert PluginManager.update()
    assert PluginManager.load_all()
    assert PluginManager.unload_all()
