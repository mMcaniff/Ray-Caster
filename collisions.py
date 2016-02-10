import data
import math
import vector_math 
def sphere_intersection_point(ray,sphere):
   a = vector_math.dot_vector(ray.dir, ray.dir)
   b = (2 * (vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center),  ray.dir)))
   c = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), (vector_math.difference_point(ray.pt, sphere.center))) - sphere.radius**2
   d = b**2 - 4*a*c 
   if d < 0: 
      return None 

   if d == 0:
      t1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
      if t1 > 0: 
         x = (t1 * ray.dir.x) + ray.pt.x
         y = (t1 * ray.dir.y) + ray.pt.y
         z = (t1 * ray.dir.z) + ray.pt.z
         return data.Point(x,y,z)
      else: 
         return None     
   
   if d > 0:
      t1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)   
      t2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
      if t2 < 0 and t1 < 0: 
         return None 
      elif t2 < 0: 
         x = (t1 * ray.dir.x) + ray.pt.x
         y = (t1 * ray.dir.y) + ray.pt.y
         z = (t1 * ray.dir.z) + ray.pt.z
         return data.Point(x,y,z) 
      else: 
         x = (t2 * ray.dir.x) + ray.pt.x
         y = (t2 * ray.dir.y) + ray.pt.y
         z = (t2 * ray.dir.z) + ray.pt.z
         return data.Point(x,y,z)
      
def find_intersection_points(sphere_list, ray):
   l = [] 
   for x in sphere_list:
      point = sphere_intersection_point(ray,x)
      if isinstance(point, data.Point): 
         l.append((x,point))
   return l

def sphere_normal_at_point(sphere,point):
   v = vector_math.difference_point(point, sphere.center)
   return vector_math.normalize_vector(v)
