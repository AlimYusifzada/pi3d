from pi3d import *
from pi3d.Texture import Texture
from pi3d.Buffer import Buffer
from pi3d.shape.Shape import Shape
from pi3d.util.Loadable import Loadable

class Sprite(Shape):
  """ 3d model inherits from Shape, differs from Plane in being single sided"""
  def __init__(self, camera=None, light=None, w=1.0, h=1.0, name="",
               x=0.0, y=0.0, z=20.0,
               rx=0.0, ry=0.0, rz=0.0,
               sx=1.0, sy=1.0, sz=1.0,
               cx=0.0, cy=0.0, cz=0.0):
    """uses standard constructor for Shape extra Keyword arguments:
    w -- width
    h -- height
    """  
    super(Sprite, self).__init__(camera, light, name, x, y, z, rx, ry, rz,
                                sx, sy, sz, cx, cy, cz)
    self.width = w
    self.height = h
    self.ttype = GL_TRIANGLES
    self.verts = []
    self.norms = []
    self.texcoords = []
    self.inds = []

    ww = w / 2.0
    hh = h / 2.0

    self.verts = ((-ww, hh, 0.0), (ww, hh, 0.0), (ww, -hh, 0.0), (-ww,-hh, 0.0))
    self.norms = ((0, 0, -1), (0, 0, -1),  (0, 0, -1), (0, 0, -1))
    self.texcoords = ((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0 ,1.0))

    self.inds = ((0, 1, 3), (1, 2, 3))

    self.buf = []
    self.buf.append(Buffer(self, self.verts, self.texcoords, self.inds, self.norms))


class ImageSprite(Sprite, Loadable): #TODO is Loadable needed?
  """for 2D sprites"""
  def __init__(self, texture, shader, **kwds):
    Sprite.__init__(self, **kwds)
    Loadable.__init__(self) #TODO need this? as Loadable->Shape->Sprite->ImageSprite
    if not isinstance(texture, Texture):
      texture = Texture(texture)
    self.buf[0].set_draw_details(shader, [texture])
    self.set_2d_size() # default full window size

  def _load_opengl(self):
    self.buf[0].textures[0].load_opengl()
