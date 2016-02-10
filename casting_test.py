import data
import cast

eyePoint = data.Point(0.0, 0.0, -14.0)
ambient_light = data.Color(1.0,1.0,1.0)
light = data.Light(data.Point(-100.0, 100.0,-100.0), data.Color(1.5,1.5,1.5))
a = data.Sphere(data.Point(1.0,1.0,0.0), 2.0, data.Color(0.0,0.0,1.0), data.Finish(.2, .4, .5, .05))
b = data.Sphere(data.Point(.5,1.5,-3.0), .5, data.Color(1.0,0.0,0.0), data.Finish(.4, .4, .5, .05))
cast.cast_all_rays(-10.0,10.0,-7.5,7.5, 1024, 768, eyePoint, [a,b], ambient_light, light) 
