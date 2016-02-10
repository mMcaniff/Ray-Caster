import collisions
import vector_math
import data

def cast_ray(ray, sphere_list, am_color, light, point): 
   l = collisions.find_intersection_points(sphere_list, ray)   
   if len(l) > 0:
      tu = smallest_point_distance(ray,l)
      s = tu[0]
      p = tu[1]
      c = s.color
      return get_color(c, am_color, tu, light, sphere_list)
   else: 
      return data.Color(1.0,1.0,1.0)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient_color, light):
  
   f = open("image.ppm", 'w')

   f.write("P3\n")
   f.write("%d %d\n" % (width, height))
   f.write("255\n")

   w = max_x - min_x 
   h = max_y - min_y
   scale_x = w / width
   scale_y = h / height 
   
   total = width * height 
   percent = 0

   for i in range(height):
      print int(percent) 
      for j in range(width):
         position = width * i + j
         percent = float(position) / total * 100
         x = j * scale_x + min_x
         y = max_y - i * scale_y
         dir = vector_math.vector_from_to(eye_point, data.Point(x,y,0))
         ray = data.Ray(eye_point, dir)
         b = cast_ray(ray, sphere_list, ambient_color, light, eye_point)
         print_color(f,b)

def smallest_point_distance(ray, sphere_list):
   smallest = vector_math.distance(ray.pt, sphere_list[0][1])
   place = sphere_list[0]
   for x in sphere_list: 
      d = vector_math.distance(ray.pt, x[1])
      if d < smallest:
         smallest = d
         place = x

   return place

   
def get_color(c1,c2, tu, light, s_list):
   s = tu[0]
   p = tu[1]
   f = s.finish
   ambientColor = data.Color(c1.r * c2.r * f.ambient, c1.g * c2.g * f.ambient, c1.b * c2.b * f.ambient)
   diffuseColor = get_diffuse_color(tu, light, s_list)
   color = data.Color(ambientColor.r + diffuseColor.r, ambientColor.g + diffuseColor.g, ambientColor.b + diffuseColor.b)
   return color

def get_diffuse_color(tu, light, s_list):
   pE = get_pe(tu)
   N = collisions.sphere_normal_at_point(tu[0], tu[1])
   lDir = vector_math.vector_from_to(pE, light.pt)
   lDir = vector_math.normalize_vector(lDir)
   lDirection = vector_math.dot_vector(N, lDir)
   sI = get_specular_intensity(lDir, lDirection, N, pE, light, tu[0])
   ray = data.Ray(pE, lDir)
   if lDirection <= 0 or collides_with_spheres(ray, s_list, pE, light):
      return data.Color(0,0,0) 
   dif = get_diffuse(lDirection, light, tu[0], tu[0].finish.diffuse)
   finalColor = data.Color(sI.r + dif.r, sI.g + dif.g, sI.b + dif.b)
   return finalColor 
   

def get_specular_intensity(lDir, lDirection, N, pE, light, sphere):
   reflection_vector = vector_math.difference_vector(lDir, vector_math.scale_vector(N, lDirection * 2)) 
   vDir = vector_math.vector_from_to(data.Point(0.0,0.0,-14.0), pE)
   vDir = vector_math.normalize_vector(vDir)
   intensity = vector_math.dot_vector(reflection_vector, vDir)
   if intensity > 0: 
      r = light.color.r * sphere.finish.specular * intensity**(1 / sphere.finish.roughness)
      g = light.color.g * sphere.finish.specular * intensity**(1 / sphere.finish.roughness)
      b = light.color.b * sphere.finish.specular * intensity**(1 / sphere.finish.roughness)
      color = data.Color(r,g,b)
   else: 
      color = data.Color(0,0,0)

   return color

def get_pe(tu):
   vector = collisions.sphere_normal_at_point(tu[0], tu[1])
   sVector = vector_math.scale_vector(vector, .01)
   scaledPoint = vector_math.translate_point(tu[1], sVector)
   return scaledPoint

def light_direction(N, lDir): 
   return vector_math.dot_vector(N, lDir)

def collides_with_spheres(ray, list, pE, light):
   l = collisions.find_intersection_points(list, ray)
   d = vector_math.distance(pE, light.pt)
   s = False
   if len(l) > 0:
      for x in l:
         if vector_math.distance(x[1], pE) < d:
            s = True
   return s

def get_diffuse(lDirection, light, s, diffuse):
   r = lDirection * light.color.r * s.color.r * diffuse 
   g = lDirection * light.color.g * s.color.g * diffuse
   b = lDirection * light.color.b * s.color.b * diffuse
   return data.Color(r,g,b)

def print_color(f,b):
   if b.r > 1.0:
      b.r = 1.0
   if b.g > 1.0:
      b.g = 1.0
   if b.b > 1.0:
      b.b = 1.0

   f.write("%d %d %d\n" % (255 * b.r, 255 * b.g, 255 * b.b))
