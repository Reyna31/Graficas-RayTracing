from gl import Raytracer, V3, _color
from Obj import *

from figure import *

width = 1080
height = 720


Black = Material(diffuse = _color(0,0,0),spec = 128)
brick = Material(diffuse = _color(0.8,0.25,0.25),spec = 64)
stone = Material(diffuse = _color(0.4,0.4,0.4), spec = 64)

wood = Material(diffuse = _color(0.5,0.5,0.1))
snow = Material(diffuse= _color(0.9,0.9,0.9))

gold = Material(diffuse = (1,0.8,0), spec = 32, matType = REFLECTIVE)
mirror = Material(spec = 128, matType = REFLECTIVE)

water = Material(spec = 64, ior = 1.33, matType = TRANSPARENT)
glass = Material(spec = 64, ior = 1.5, matType = TRANSPARENT)

grass = Material(texture = Texture('Models/Yerba.bmp'))
redM = Material(texture = Texture('Models/Rojo Metal.bmp'))



rtx = Raytracer(width,height)
rtx.envmap = EnvMap('Models/monbachtal_riverbank_2k.bmp')

rtx.ambLight = AmbientLight(strength = 0.1)
rtx.dirLight = DirectionalLight(direction = V3(2,-1,2), intensity = 0.5)
rtx.dirLight = DirectionalLight(direction = V3(-2,2,3), intensity = 1)
rtx.pointLights.append(PointLight(position = V3(0,2,0), intensity = 0.5))

#Gusano primera parte
rtx.scene.append(Sphere(V3(-6,-3,-8),0.4,gold))
rtx.scene.append(Sphere(V3(-5.5,-2.5,-8),0.4,gold))
rtx.scene.append(Sphere(V3(-5,-2,-8),0.4,glass))
rtx.scene.append(Sphere(V3(-4.5,-2.5,-8),0.4,gold))
rtx.scene.append(Sphere(V3(-4,-3,-8),0.4,gold))

#Gusano 2
rtx.scene.append(Sphere(V3(-3.5,-3,-8),0.4,gold))
rtx.scene.append(Sphere(V3(-3,-2.5,-8),0.4,gold))
rtx.scene.append(Sphere(V3(-2.5,-2,-8),0.4,glass))
rtx.scene.append(Sphere(V3(-2,-2.5,-8),0.4,gold))
rtx.scene.append(Sphere(V3(-1.5,-3,-8),0.4,redM))

#Gusano Cuello
rtx.scene.append(Sphere(V3(-1,-2.5,-8),0.4,gold))
rtx.scene.append(Sphere(V3(-0.5,-2,-8),0.4,gold))
rtx.scene.append(Sphere(V3(0,-1.5,-8),0.4,gold))
rtx.scene.append(Sphere(V3(0.5,-1,-8),0.4,gold))

#Cabeza
rtx.scene.append(Sphere(V3(1,0,-8),0.8,gold))
rtx.scene.append(Sphere(V3(1.15,0.2,-7),0.1,Black))
rtx.scene.append(Sphere(V3(1.1,0.2,-6.7),0.3,wood))


#piso
rtx.scene.append(AABB(V3(0,-4,-8),V3(25,1,0.5),grass))

rtx.glRender()

rtx.glFinish('output.bmp')
