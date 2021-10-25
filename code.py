def cuboid_volume(l):
     if type(l) not in [int, float]:
     		raise TypeError('The length of the cuboid can only vaild integer or float')
     return (l*l*l)
length = [2,1.1, -2.5, 2, 3]
for i in range(len(length)):
    print ("The volume of cuboid:",cuboid_volume(length[i]))
