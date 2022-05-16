
from turtle import *
from math import *
from time import sleep

setup()
up()
home()

tracer(0, 0)

bgcolor('lightblue')
hideturtle()
pos = [0.0, 0.0, 0.0]
rot = [0.0, 0.0, 0.0]
size = 20
Pos = pos
Rot = rot

verts = [[1.0 * size, 1.0 * size, 1.0 * size], [-1.0 * size, 1.0 * size, 1.0 * size],
         [-1.0 * size, -1.0 * size, 1.0 * size], [1.0 * size, -1.0 * size, 1.0 * size],
         [1.0 * size, 1.0 * size, -1.0 * size], [-1.0 * size, 1.0 * size, -1.0 * size],
         [-1.0 * size, -1.0 * size, -1.0 * size], [1.0 * size, -1.0 * size, -1.0 * size]]

faces = [[0, 1, 2, 3], [5, 4, 7, 6], [4, 0, 3, 7], [1, 5, 6, 2], [4, 5, 1, 0], [3, 2, 6, 7]]



def cull_faces(inverts=[], infaces=[]):
    return_faces = []

    for _ in range(len(infaces)):
        one = [verts[infaces[_][0]][0], verts[infaces[_][0]][1], verts[infaces[_][0]][2]]
        two = [verts[infaces[_][1]][0], verts[infaces[_][1]][1], verts[infaces[_][1]][2]]
        three = [verts[infaces[_][2]][0], verts[infaces[_][2]][1], verts[infaces[_][2]][2]]
        # calculate normals and normal lengths
        tempnorm = [(one[0] - two[0]), (one[1] - two[1]), (one[2] - two[2])]
        normlength = sqrt(((one[0] - two[0]) ** 2.0) + ((one[1] - two[1]) ** 2.0) + ((one[2] - two[2]) ** 2.0))
        norm1 = [tempnorm[0] / normlength, tempnorm[1] / normlength, tempnorm[2] / normlength]
        tempnorm = [(three[0] - two[0]), (three[1] - two[1]), (three[2] - two[2])]
        normlength = sqrt(((three[0] - two[0]) ** 2.0) + ((three[1] - two[1]) ** 2.0) + ((three[2] - two[2]) ** 2.0))
        norm2 = [tempnorm[0] / normlength, tempnorm[1] / normlength, tempnorm[2] / normlength]
        crossvec = [(norm1[1] * norm2[2]) - (norm1[2] * norm2[1]), (norm1[2] * norm2[0]) - (norm1[0] * norm2[2]),
                    (norm1[0] * norm2[1]) - (norm1[1] * norm2[0])]
        cameravec = [0.0, 0.0, 1.0]
        lightvec = [0, -0.45, 0.45]

        dot = (cameravec[0] * crossvec[0]) + (cameravec[1] * crossvec[1]) + (cameravec[2] * crossvec[2])
        if dot < -0.15:
            brightness = (lightvec[0] * crossvec[0]) + (lightvec[1] * crossvec[1]) + (lightvec[2] * crossvec[2])
            return_faces.append(infaces[_])
            return_faces.append(brightness)
    return return_faces


def draw(infaces):
    print(infaces, len(infaces) / 2)
    for _ in range(int(len(infaces) / 2)):
        color((0, 0.4 + (infaces[_ * 2 + 1]) * 0.4, 0))
        up()

        goto(verts[infaces[_ * 2][0]][0] * (5 + verts[infaces[_ * 2][0]][2] / 20.0),
             verts[infaces[_ * 2][0]][1] * (5 + verts[infaces[_ * 2][0]][2] / 20.0))
        begin_fill()
        down()
        goto(verts[infaces[_ * 2][1]][0] * (5 + verts[infaces[_ * 2][1]][2] / 20.0),
             verts[infaces[_ * 2][1]][1] * (5 + verts[infaces[_ * 2][1]][2] / 20.0))
        goto(verts[infaces[_ * 2][2]][0] * (5 + verts[infaces[_ * 2][2]][2] / 20.0),
             verts[infaces[_ * 2][2]][1] * (5 + verts[infaces[_ * 2][2]][2] / 20.0))
        goto(verts[infaces[_ * 2][3]][0] * (5 + verts[infaces[_ * 2][3]][2] / 20.0),
             verts[infaces[_ * 2][3]][1] * (5 + verts[infaces[_ * 2][3]][2] / 20.0))
        goto(verts[infaces[_ * 2][0]][0] * (5 + verts[infaces[_ * 2][0]][2] / 20.0),
             verts[infaces[_ * 2][0]][1] * (5 + verts[infaces[_ * 2][0]][2] / 20.0))
        end_fill()
        up()

    update()


def rotate(xAxis=0, yAxis=0, zAxis=0):
    # calculate for every angle
    thetaX = radians(xAxis)
    thetaY = radians(yAxis)
    thetaZ = radians(zAxis)
    csX = cos(thetaX)
    snX = sin(thetaX)
    csY = cos(thetaY)
    snY = sin(thetaY)
    csZ = cos(thetaZ)
    snZ = sin(thetaZ)
    for vert in range(len(verts)):
        # calculate changes to Y axis
        yx = float(verts[vert][0] * csY - verts[vert][2] * snY)
        yz = float(verts[vert][0] * snY + verts[vert][2] * csY)
        # rotate around Y axis
        verts[vert][0] = yx
        verts[vert][2] = yz
        # calculate changes to X axis
        xy = float(verts[vert][1] * csX - verts[vert][2] * snX)
        xz = float(verts[vert][1] * snX + verts[vert][2] * csX)
        verts[vert][1] = xy
        verts[vert][2] = xz
        # calculate changes to Z axis
        zx = float(verts[vert][0] * csZ - verts[vert][1] * snZ)
        zy = float(verts[vert][0] * snZ + verts[vert][1] * csZ)
        # rotate around Z axis
        verts[vert][0] = zx
        verts[vert][1] = zy


def L():
    clear()
    rotate(0, 5, 0)
    draw(cull_faces(verts, faces))


def R():
    clear()
    rotate(0, -5, 0)
    draw(cull_faces(verts, faces))


def U():
    clear()
    rotate(-5, 0, 0)
    draw(cull_faces(verts, faces))


def D():
    clear()
    rotate(5, 0, 0)
    draw(cull_faces(verts, faces))


onkey(L, "Left")
onkey(R, "Right")
onkey(U, "Up")
onkey(D, "Down")
listen()
rotate(0, 20, 20)
width(2)


draw(cull_faces(verts, faces))

for count in range(5000):
   clear()
   rotate(10,0,0)
   draw(cull_faces(verts,faces))
   sleep(0.09)

done()
