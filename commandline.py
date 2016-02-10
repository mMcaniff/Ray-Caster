import data

def get_eye_point(l, eye_point):
   result = []
   for i in range(1, len(l)):
      try:
         result.append(float(l[i]))
      except: 
         print "ERROR-- parsing eye_point"   
         result.append(eye_point[i])

   return data.Point(result[0],result[1], result[2])

def get_view(l, view):
   result = []
   for i in range(1, len(l)):
      try: 
         result.append(float(l[i]))
      except:
         print "ERROR-- parsing view"
         result.append(view[i])

   return [result[0],result[1],result[2],result[3],result[4],result[5]]
    
def get_ambient_light(l, ambient_light):
   result = []
   for i in range(1, len(l)):
      try:
         result.append(float(l[i]))
      except: 
         print "ERROR-- parsing ambient light"
         result.append(ambient_light[i])
   return data.Color(result[0], result[1], result[2])
     
def get_light(l, light):
   result = []
   for i in range(1, len(l)):
      try: 
         result.append(float(l[i]))
      except:
         print "ERROR-- parsing light"
         result.append(light[i])

   position = data.Point(result[0],result[1],result[2])
   color = data.Color(result[3], result[4], result[5])

   return data.Light(position, color)
