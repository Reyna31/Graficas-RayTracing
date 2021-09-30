from gl import Raytracer, V3, _color
from Obj import *

from figure import *

width = 720
height = 540

brick = Material(diffuse = _color(0.8,0.25,0.25),spec = 64)
stone = Material(diffuse = _color(0.4,0.4,0.4), spec = 64)

wood = Material(diffuse = _color(0.5,0.5,0.1))
snow = Material(diffuse= _color(0.9,0.9,0.9))
grass = Material(diffuse = _color(0.3,0.5,0.3), spec = 128)

gold = Material(diffuse = (1,0.8,0), spec = 32, matType = REFLECTIVE)
mirror = Material(spec = 128, matType = REFLECTIVE)

water = Material(spec = 64, ior = 1.33, matType = TRANSPARENT)
glass = Material(spec = 64, ior = 1.5, matType = TRANSPARENT)



rtx = Raytracer(width,height)
rtx.envmap = EnvMap('evening_meadow_4k.bmp')

rtx.ambLight = AmbientLight(strength = 0.1)
rtx.dirLight = DirectionalLight(direction = V3(1,-1,-2), intensity = 0.5)
rtx.pointLights.append(PointLight(position = V3(0,2,0), intensity = 0.5))

#Opacas
rtx.scene.append(Sphere(V3(-4,0,-8),1,snow))
rtx.scene.append(Sphere(V3(-4,-3,-8),1,wood))

#reflectivas
rtx.scene.append(Sphere(V3(0,0,-8),1,gold))
rtx.scene.append(Sphere(V3(0,-3,-8),1,mirror))

#transparentes
rtx.scene.append(Sphere(V3(4,0,-8),1,water))
rtx.scene.append(Sphere(V3(4,-3,-8),1,glass))

rtx.glRender()

rtx.glFinish('output.bmp')
