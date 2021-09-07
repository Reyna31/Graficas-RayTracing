from gl import Raytracer, V3, _color
from Obj import Obj, Texture

from figure import Sphere, Material

width = 512
height = 512

brick = Material(diffuse = _color(0.8,0.25,0.25))
stone = Material(diffuse = _color(0.4,0.4,0.4))
grass = Material(diffuse = _color(0.4,1,0))
wood = Material(diffuse = _color(0.5,0.5,0.1))
snow = Material(diffuse= _color(0.9,0.9,0.9))
nara = Material(diffuse=_color(0.9,0.3,0))
black = Material(diffuse=_color(0,0,0))
yellow = Material(diffuse=_color(0.95,0.92,0.03))



rtx = Raytracer(width,height)

rtx.scene.append( Sphere(V3(0,3.5,-10), 1.5, snow))
rtx.scene.append( Sphere(V3(0,0.5,-10), 2, snow))
rtx.scene.append( Sphere(V3(0,-2.5,-10), 2.5, snow))
rtx.scene.append(Sphere(V3(2,-4.5,-10),1,snow))
rtx.scene.append(Sphere(V3(-2,-4.5,-10),1,snow))

rtx.scene.append(Sphere(V3(0,2.05,-6),0.2,nara))

rtx.scene.append(Sphere(V3(-0.3,2.5,-6),0.1,black))
rtx.scene.append(Sphere(V3(0.3,2.5,-6),0.1,black))

rtx.scene.append(Sphere(V3(0,-1.6,-6),0.2, yellow))
rtx.scene.append(Sphere(V3(0,-0.6,-6),0.2, yellow))
rtx.scene.append(Sphere(V3(0,0.4,-6),0.2, yellow))

rtx.scene.append(Sphere(V3(0.4,1.7,-6),0.05,black))
rtx.scene.append(Sphere(V3(0.2,1.5,-6),0.05,black))
rtx.scene.append(Sphere(V3(-0.2,1.5,-6),0.05,black))
rtx.scene.append(Sphere(V3(-0.4,1.7,-6),0.05,black))


rtx.glRender()

rtx.glFinish('output.bmp')
