"""Test plugins configuration"""

import os
import sys


# Set the plugin path to be the parent directory of tests where all the plugins are
if 'MEG_PLUGINS_PATH' not in os.environ:
    os.environ['MEG_PLUGINS_PATH'] = os.path.dirname(sys.path[0])
