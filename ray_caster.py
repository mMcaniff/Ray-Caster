import sys
import data
import commandline
import cast 
 
def main():
   args = sys.argv
   sphere_list = get_sphere_list(args[1])
   eye_point = data.Point(0.0,0.0,-14.0)
   view = [-10.0, 10.0, -7.5,7.5, 1024, 768]
   ambient_light = data.Color(1.0,1.0,1.0)
   light = data.Light(data.Point(-100.0, 100.0,-100.0), data.Color(1.5,1.5,1.5))

   if len(args) > 2: 
      try:
         for i in range(2,len(args)):
            if args[i] == "-eye":
               l = args[i:i+4]
               eye_point = commandline.get_eye_point(l, [0.0,0.0,-14.0])
            elif args[i] == "-view":
               l = args[i:i+7]
               view = commandline.get_view(l, view)
            elif args[i] == "-light":
               l = args[i:i+7]
               light = commandline.get_light(l, [-100.0,100.0,-100.0,1.5,1.5,1.5])
            elif args[i] == "-ambient":
               l = args[i:i+4]
               ambient_light = commandline.get_ambient_light(l, [1.0,1.0,1.0])
             
      except: 
         print "Something went horribly wrong"

   cast.cast_all_rays(view[0],view[1],view[2],view[3], view[4], view[5], eye_point, sphere_list, ambient_light, light)

def get_sphere_list(file): 
   sphere_list = []
   try:
      f = open(file, 'r')
      for line in f:
         try:
            components = line.split()
            sphere_list.append(get_sphere(components))
         except:
            print "ERROR-- cannot read line: " + line
   except:
      print "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"
      exit()

   return sphere_list

def get_sphere(l):
   if not len(l) == 11:
      print "ERROR-- Number of arugements is incorrect: ", len(l)
   else: 
      try: 
         point = data.Point(float(l[0]), float(l[1]), float(l[2]))
         radius = float(l[3])
         color = data.Color(float(l[4]), float(l[5]), float(l[6]))
         finish = data.Finish(float(l[7]), float(l[8]), float(l[9]), float(l[10]))
      except: 
         print "ERROR-- Something went wrong while parsing spheres"
   return data.Sphere(point, radius, color, finish)

if __name__ == "__main__":
    main()
