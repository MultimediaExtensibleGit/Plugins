"""Test plugins"""

# Import the runtime after setting the plugin path
from meg_runtime import PluginManager


# Test plugins
def test_plugins():
    """Test plugins"""
    assert PluginManager.update()
    assert PluginManager.load_all()
    assert PluginManager.unload_all()
