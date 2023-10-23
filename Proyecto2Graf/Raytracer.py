import pygame as pg
from pygame.locals import *
from rt import Raytracer
from figures import *
from materials import *
from lights import *

width = 1000
height = 1000

pg.init()

screen = pg.display.set_mode((width, height), pg.DOUBLEBUF | pg.HWACCEL | pg.HWSURFACE)
screen.set_alpha(None)

raytracer = Raytracer(screen=screen)
raytracer.envMap = pg.image.load("fondo_1.jpg")

white = Material(diffuse=(1, 1, 1))
ball1 = pg.image.load("ball1.png")
ball1 = Material(texture=ball1)
ball2 = pg.image.load("ball2.png")
ball2 = Material(texture=ball2)
ball3 = pg.image.load("ball3.png")
ball3 = Material(texture=ball3)
ball4 = pg.image.load("ball4.png")
ball4 = Material(texture=ball4)
ball5 = pg.image.load("ball5.png")
ball5 = Material(texture=ball5)
ball6 = pg.image.load("ball6.png")
ball6 = Material(texture=ball6)
ball7 = pg.image.load("ball7.png")
ball7 = Material(texture=ball7)
ball8 = pg.image.load("ball8.png")
ball8 = Material(texture=ball8)
ball9 = pg.image.load("ball9.png")
ball9 = Material(texture=ball9)
ball10 = pg.image.load("ball10.png")
ball10 = Material(texture=ball10)
ball11 = pg.image.load("ball11.png")
ball11 = Material(texture=ball11)
ball12 = pg.image.load("ball12.png")
ball12 = Material(texture=ball12)
ball13 = pg.image.load("ball13.png")
ball13 = Material(texture=ball13)
ball14 = pg.image.load("ball14.png")
ball14 = Material(texture=ball14)
fondo = pg.image.load("fondo.jpg")
fondo = Material(texture=fondo)
wood = pg.image.load("wood.jpg")
wood = Material(texture=wood)
lwood = pg.image.load("light_wood.jpg")
lwood = Material(texture=lwood)
trian = pg.image.load("triang.jpg")
trian = Material(texture=trian)
green = Material(diffuse=(0, 1, 0))
black = Material(diffuse=(0, 0, 0), specular=10, ks=0.2, ior=1.5, matType=REFLECTIVE)
vaso = Material(diffuse=(0.9, 0.9, 0.9), specular=64, ks=0.2, ior=1.5, matType=REFLECTIVE)
refract = Material(
    diffuse=(0.9, 0.9, 0.9),
    specular=32,
    ks=0.2,
    ior=1.33,
    matType=TRANSPARENT
)

sizeDimA = 2
sizeDimB = 4
sizeDimC = 0.5
sizeDimD = 2.6
sizeDimE = 1
raytracer.scene.append(Sphere(position=(0,0,-3), radius=(0.1), material=ball1))
raytracer.scene.append(Sphere(position=(0,1,-3), radius=(0.1), material=refract))
raytracer.scene.append(Sphere(position=(0,0.8,-3), radius=(0.1), material=ball3))
raytracer.scene.append(Sphere(position=(0.6,0.8,-3), radius=(0.1), material=ball4))
raytracer.scene.append(Sphere(position=(0,-1,-3), radius=(0.1), material=ball5))
raytracer.scene.append(Sphere(position=(0.3,-0.6,-3), radius=(0.1), material=ball6))
raytracer.scene.append(Sphere(position=(-0.6,-1.1,-3), radius=(0.1), material=ball7))
raytracer.scene.append(Sphere(position=(0.6,-1,-3), radius=(0.1), material=ball8))
raytracer.scene.append(Sphere(position=(-0.5,-1,-3), radius=(0.1), material=ball9))
raytracer.scene.append(Sphere(position=(0,-1.5,-3), radius=(0.1), material=ball10))
raytracer.scene.append(Sphere(position=(-0.5,1,-3), radius=(0.1), material=ball11))
raytracer.scene.append(Sphere(position=(0.3,-1,-3), radius=(0.1), material=ball12))
raytracer.scene.append(Sphere(position=(0.4,0.4,-3), radius=(0.1), material=ball13))
raytracer.scene.append(Sphere(position=(-0.6,0.9,-3), radius=(0.1), material=ball14))
cilindro_x = -0.6
cilindro_y = 1
cilindro_z = -4.2
cilindro_height = 0.4
raytracer.scene.append(Cilindro(material=vaso, v0=(cilindro_x, cilindro_z, cilindro_y), v1=(cilindro_x, cilindro_z + cilindro_height, cilindro_y), radius=0.2))
raytracer.scene.append(Cubo(position=(-0.2,0,-4), size=(sizeDimD,sizeDimB,sizeDimC), material=wood))
raytracer.scene.append(Cubo(position=(0.2,0,-4), size=(sizeDimD,sizeDimB,sizeDimC), material=wood))
raytracer.scene.append(Cubo(position=(0,1.3,-3), size=(sizeDimA,0.2,sizeDimC), material=wood))
raytracer.scene.append(Cubo(position=(0,-1.3,-3), size=(sizeDimA,0.2,sizeDimC), material=wood))
raytracer.scene.append(Cubo(position=(0,0,-4), size=(sizeDimA,sizeDimB,sizeDimA), material=fondo))
sizeDim = 0.2
raytracer.scene.append(Cilindro(material=lwood, v0=(1,-3,5), v1=(-0.4,4,-3), radius=0.02))
triangulo_x = -1.8
triangulo_x = -1.8
triangulo_y = 0.6
triangulo_z = -3.2
lado_del_triángulo = 0.5

triangulo_x2 = -1.7
triangulo_y2 = 0.6
triangulo_z2 = -3.1
lado_triangulo_2 = 0.4
v0_0 = (triangulo_x, triangulo_y, triangulo_z)
v1_1 = (triangulo_x + lado_del_triángulo, triangulo_y, triangulo_z)
v2_2 = (triangulo_x + lado_del_triángulo / 2, triangulo_y + 2 * (lado_del_triángulo * (3 ** 0.5)) / 2, triangulo_z)


v0 = (triangulo_x2, triangulo_y2, triangulo_z2)
v1 = (triangulo_x2 + lado_triangulo_2, triangulo_y2, triangulo_z2)
v2 = (triangulo_x2 + lado_triangulo_2 / 2, triangulo_y2 + 2 * (lado_triangulo_2 * (3 ** 0.5)) / 2, triangulo_z2)
raytracer.scene.append(Triangulo(material=black, v0=v0_0, v1=v1_1, v2=v2_2))
raytracer.scene.append(Triangulo(material=trian, v0=v0, v1=v1, v2=v2))

raytracer.lights.append(AmbientLight(0.4    ))
raytracer.lights.append(PointLight(point=(0,0,0), intensity=0.2))
raytracer.lights.append(DirectionalLight(direction=(0,0,-3), intensity=0.1, color=(1,1,0)))

isRunning = True
while(isRunning):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                isRunning = False
            elif event.key == pg.K_s:
                pg.image.save(screen, "image.bmp")
    raytracer.rtClear()
    raytracer.rtRender()
    pg.display.flip()



pg.quit()