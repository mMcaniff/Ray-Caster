import unittest
import data
import cast 
import vector_math

class Tests(unittest.TestCase):
   def test_cast_ray_1(self): 
      finish = data.Finish(.4,.4, .5, .05)
      one = data.Sphere(data.Point(2,2,0), 1.0, data.Color(.4,.2,.1), finish)
      two = data.Sphere(data.Point(6,6,0), 2.0, data.Color(.2,.3,.5), finish)
      three = data.Sphere(data.Point(-2,-2,0), 1.0, data.Color(1,1,1), finish)
      four = data.Sphere(data.Point(-6,-6,0), 15.0, data.Color(.5,.5,.5), finish)
      ray = data.Ray(data.Point(0,0,-14), data.Vector(0,0,1))
      l = [one,two,three,four]
      light = data.Light(data.Point(0,0,-14), data.Color(1.5,1.5,1.5))
      ambient_color = data.Color(.2,.2,.2)
      result = cast.cast_ray(ray,l,ambient_color, light, data.Point(0,0,-14))
      expected = data.Color(0.286793135633, 0.286793135633, 0.286793135633)
      self.assertEqual(result, expected)

   def test_cast_ray_2(self):
      finish = data.Finish(.4,.4, .5, .05)
      one = data.Sphere(data.Point(2,2,0), 1.0, data.Color(.1,.1,.1), finish)
      two = data.Sphere(data.Point(6,6,0), 2.0, data.Color(.2,.6,.5), finish)
      three = data.Sphere(data.Point(-2,-2,0), 15.0, data.Color(1,.5,1), finish)
      four = data.Sphere(data.Point(-6,-6,0), 1.0, data.Color(.75,.1,.9), finish)
      ray = data.Ray(data.Point(0,0,-14), data.Vector(0,0,1))
      l = [one,two,three,four]
      light = data.Light(data.Point(0,0,-14), data.Color(1.5,1.5,1.5))
      ambient_color = data.Color(.2,.2,.2)
      result = cast.cast_ray(ray,l,ambient_color, light, data.Point(0,0,-14))
      expected = data.Color(.08, 0.04, 0.08)
      self.assertEqual(result, expected)

   def test_get_color_1(self):    
      ambient = data.Color(.4,.4,.4)
      light = data.Light(data.Point(-100.0, 100.0,-100.0), data.Color(1.5,1.5,1.5))
      a = data.Sphere(data.Point(1.0,0.0,0.0), 2.0, data.Color(0.0,0.0,1.0), data.Finish(.2, .4, .5, .05))
      b = data.Sphere(data.Point(.5,1.5,-3.0), .5, data.Color(1.0,0.0,0.0), data.Finish(.4, .4, .5, .05))
      list = [a,b]
      t = (a, data.Point(2.0,0,0))
      result = cast.get_color(a.color, ambient, t, light, list)
      expected = data.Color(0,0,.08)
      self.assertEqual(result,expected)  
 
   def test_get_color_2(self):
      ambient = data.Color(.2,.2,.2)
      light = data.Light(data.Point(-100.0, 100.0,-100.0), data.Color(1.5,1.5,1.5))
      a = data.Sphere(data.Point(0,0,0), 2.0, data.Color(.5,0.3,.8), data.Finish(.2, .4, .5, .05))
      b = data.Sphere(data.Point(.5,1.5,-3.0), .5, data.Color(1.0,0.0,0.0), data.Finish(.4, .4, .5, .05))
      list = [a,b]
      t = (a, data.Point(2.0,0,0))
      result = cast.get_color(a.color, ambient, t, light, list)
      expected = data.Color(0.02, 0.012, 0.032)
      self.assertEqual(result,expected)     
 
   def test_get_difuse_color_1(self):
      light = data.Light(data.Point(-100.0, 100.0,-100.0), data.Color(1.5,1.5,1.5))
      a = data.Sphere(data.Point(0,0,0), 2.0, data.Color(.5,0.3,.8), data.Finish(.2, .4, .5, .05))
      b = data.Sphere(data.Point(.5,1.5,-3.0), .5, data.Color(1.0,0.0,0.0), data.Finish(.4, .4, .5, .05))
      list = [a,b]
      t = (a, data.Point(2.0,0,0))
      result = cast.get_diffuse_color(t, light, list)
      expected = data.Color(0,0,0)
      self.assertEqual(result, expected)

   def test_get_difuse_color_2(self):
      light = data.Light(data.Point(-5.0, 10.0,-10.0), data.Color(1.5,1.5,1.5))
      a = data.Sphere(data.Point(0,0,0), 4.0, data.Color(.5,0.3,.8), data.Finish(.2, .4, .5, .05))
      b = data.Sphere(data.Point(.5,1.5,-3.0), .5, data.Color(1.0,0.0,0.0), data.Finish(.4, .4, .5, .05))
      list = [a,b]
      t = (a, data.Point(2.0,0,0))
      result = cast.get_diffuse_color(t, light, list)
      expected = data.Color(0,0,0)
      self.assertEqual(result, expected)

   def test_get_specular_intensity_1(self):
      lDir = data.Vector(1,2,3)
      lDirection = 1.5
      N = data.Vector(1,2,3) 
      pE = data.Point(2,3,-3)
      light = data.Light(data.Point(0,0,-14), data.Color(1.5,1.5,1.5))
      sphere = data.Sphere(data.Point(0.0,0.0,0.0), 1.0, data.Color(0.0,0.0,1.0), data.Finish(.2, .4, .5, .05))
      result = cast.get_specular_intensity(lDir, lDirection,N,pE, light, sphere)
      expected = data.Color(0,0,0)
      self.assertEqual(result, expected)

   def test_get_specular_intensity_2(self):
      lDir = data.Vector(.5,10,3)
      lDirection = 3
      N = data.Vector(2,2,3)
      pE = data.Point(2,3,-3)
      light = data.Light(data.Point(0,0,-14), data.Color(1.5,1.5,1.5))
      sphere = data.Sphere(data.Point(0.0,0.0,0.0), 1.0, data.Color(1.0,.5,1.0), data.Finish(.2, .4, .5, .05))
      result = cast.get_specular_intensity(lDir, lDirection,N,pE, light, sphere)
      expected = data.Color(0,0,0) 
      self.assertEqual(result, expected)

   def test_get_pE_1(self):
      sphere = data.Sphere(data.Point(0.0,0.0,0.0), 1.0, data.Color(0.0,0.0,1.0), data.Finish(.2, .4, .5, .05))
      tuple = (sphere, data.Point(1,0,0))
      pe = cast.get_pe(tuple)
      expected = data.Point(1.01,0,0)
      self.assertEqual(pe,expected)


   def test_get_pE_2(self):
      sphere = data.Sphere(data.Point(0.0,0.0,0.0), 2.0, data.Color(0.0,0.0,1.0), data.Finish(.2, .4, .5, .05))
      tuple = (sphere, data.Point(0,2,0))
      pe = cast.get_pe(tuple)
      expected = data.Point(0,2.01,0)
      self.assertEqual(pe,expected)

   def test_light_direction_1(self):
      v1 = data.Vector(33,-2,1)
      v2 = data.Vector(1,3,38)
      product = vector_math.dot_vector(v1,v2)
      self.assertEqual(product, 65)

   def test_light_direction_2(self):
      v1 = data.Vector(1,2,3)
      v2 = data.Vector(5,6,7)
      product = vector_math.dot_vector(v1,v2)
      self.assertEqual(product, 38)

   def test_collides_with_spheres_1(self):
      s = data.Sphere(data.Point(0.0,0.0,0.0), 2.0, data.Color(1.0,0.0,0.0), data.Finish(.2, .4, .5, .05))
      s1 = data.Sphere(data.Point(5.0,5.0,5.0), 2.0, data.Color(1.0,0.0,0.0), data.Finish(.2, .4, .5, .05))
      ray = data.Ray(data.Point(-5,0,0), data.Vector(1,0,0))
      light = data.Light(data.Point(0,0,-14), data.Color(1,1,1))
      expected = False
      self.assertEqual(cast.collides_with_spheres(ray, [s,s1], data.Point(-3,-3,-3), light), expected)

   def test_collides_with_spheres_2(self):
      s = data.Sphere(data.Point(-5.0,-5.0,-5.0), 2.0, data.Color(1.0,0.0,0.0), data.Finish(.2, .4, .5, .05))
      s1 = data.Sphere(data.Point(5.0,5.0,5.0), 2.0, data.Color(1.0,0.0,0.0), data.Finish(.2, .4, .5, .05))
      s2 = data.Sphere(data.Point(0.0,0.0,0.0), 2.0, data.Color(1.0,0.0,0.0), data.Finish(.2, .4, .5, .05))
      s3 = data.Sphere(data.Point(100.0,100.0,100.0), 2.0, data.Color(1.0,0.0,0.0), data.Finish(.2, .4, .5, .05))
      ray = data.Ray(data.Point(0,0,0), data.Vector(1,0,0))
      light = data.Light(data.Point(0,0,-14), data.Color(1,1,1))
      expected = False
      self.assertEqual(cast.collides_with_spheres(ray, [s,s1,s2,s3], data.Point(-3,-3,-3), light), expected)

   def test_get_diffuse_1(self):
      lDir = 1.5
      light = data.Light(data.Point(-100.0, 100.0,-100.0), data.Color(2.0,2.0,2.0))
      s = data.Sphere(data.Point(1.0,1.0,0.0), 2.0, data.Color(1.0,0.0,0.0), data.Finish(.2, .4, .5, .05))
      diffuse = .2
      expected = data.Color(.6,0,0)
      self.assertEqual(cast.get_diffuse(lDir, light, s, diffuse), expected)

   def test_get_diffuse_2(self):
      lDir = 2
      light = data.Light(data.Point(-100.0, 100.0,-100.0), data.Color(1.5,1.5,1.5))
      s = data.Sphere(data.Point(1.0,1.0,0.0), 2.0, data.Color(0.0,0.0,1.0), data.Finish(.2, .4, .5, .05))
      diffuse = .4
      expected = data.Color(0,0,1.2) 
      self.assertEqual(cast.get_diffuse(lDir, light, s, diffuse), expected)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
