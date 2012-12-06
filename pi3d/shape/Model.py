from pi3d import *

from pi3d import Texture

from pi3d.context.TextureLoader import TextureLoader
from pi3d.loader import loaderEgg
from pi3d.loader import loaderObj
from pi3d.shape.Shape import Shape
from pi3d.util.RotateVec import rotate_vec
from pi3d.util.Matrix import Matrix

class Model(Shape):
  def __init__(self, camera, light, fileString, name="", x=0.0, y=0.0, z=0.0,
               rx=0.0, ry=0.0, rz=0.0, sx=1.0, sy=1.0, sz=1.0,
               cx=0.0, cy=0.0, cz=0.0):
    super(Model, self).__init__(camera, light, name, x, y, z, rx, ry, rz,
                                sx, sy, sz, cx, cy, cz)
    if("__clone__" in fileString): return #creating a copy but with pointer to buf
    self.exf = fileString[-3:].lower()
    if VERBOSE:
      print "Loading ",fileString

    if self.exf == 'egg':
      self.model = loaderEgg.loadFileEGG(self, fileString)
      return self.model
    elif self.exf == 'obj':
      self.model = loaderObj.loadFileOBJ(self, fileString)
      return self.model
    else:
      print self.exf, "file not supported"
      return None
      
  """
  def draw(self, texID=None, n=None):
    TODO need to do the child movements
    for c in self.childModel:
      relx, rely, relz = c.x, c.y, c.z
      relrotx, relroty, relrotz = c.rotx, c.roty, c.rotz
      rval = rotate_vec(self.rotx, self.roty, self.rotz, (c.x, c.y, c.z))
      c.x, c.y, c.z = self.x + rval[0], self.y + rval[1], self.z + rval[2]
      c.rotx, c.roty, c.rotz = (self.rotx + c.rotx, self.roty + c.roty,
                                self.rotz + c.rotz)
      c.draw() #should texture override be passed down to children?
      c.x, c.y, c.z = relx, rely, relz
      c.rotx, c.roty, c.rotz = relrotx, relroty, relrotz
  """
  
  def clone(self, camera, light):
    newModel = Model(camera, light, "__clone__." + self.exf)
    newModel.buf = self.buf
    newModel.vGroup = self.vGroup
    return newModel

  def reparentTo(self, parent):
    if not(self in parent.childModel):
      parent.childModel.append(self)

  def texSwap(self, texID, filename):
    return loaderEgg.texSwap(self, texID, filename)

