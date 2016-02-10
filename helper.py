import unittest
import data
import cast
import collisions
import vector_math

a = data.Sphere(data.Point(0.0,0.0,0.0), 2.0, data.Color(0.0,0.0,1.0), data.Finish(.2, .4, .5, .05))
t = (a, data.Point(0,2,0))
pe = cast.get_pe(t)
sphere = data.Sphere(data.Point(0,0,0), 2.0, data.Color(0,0,0), data.Finish(.2,.4,.5,.05))
N = data.Vector(0,0,0)
V = data.Vector(5,5,5)
s = vector_math.dot_vector(N,V)
print s
print "%f %f %f" % (pe.x,pe.y,pe.z)
