from __future__ import absolute_import, division, print_function, unicode_literals

from pi3d import Display
from pi3d.util import Log

LOGGER = Log.logger(__name__)

class Loadable(object):
  def __init__(self):
    self.disk_loaded = False
    self.opengl_loaded = False

  def __del__(self):
    if not self.unload_opengl(False):
      Display.display.unload_opengl(self)

  def load_disk(self):
    if not self.disk_loaded:
      self._load_disk()
      self.disk_loaded = True

  def load_opengl(self):
    self.load_disk()
    if not self.opengl_loaded:
      if Display.is_display_thread():
        self._load_opengl()
        self.opengl_loaded = True
      else:
        LOGGER.error('load_opengl must be called on main thread for %s', self)

  def unload_opengl(self, report_error=True):
    if not self.opengl_loaded:
      return True

    elif Display.is_display_thread():
      self._unload_opengl()
      self.opengl_loaded = False
      return True

    elif report_error:
      LOGGER.error('unload_opengl must be called on main thread for %s', self)
      return False

  def _load_disk(self):
    """Override this to load assets from disk."""
    pass

  def _load_opengl(self):
    """Override this to load assets into Open GL."""
    pass

  def _unload_opengl(self):
    """Override this to load assets into Open GL."""
    pass
