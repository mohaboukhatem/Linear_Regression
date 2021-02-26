from scipy import misc
import matplotlib.pyplot as plt
face = misc.face()

x = face.shape[0]
y = face.shape[1]

img = face[x//4 : -x//4, y //4: -y//4] 
zoom_face = img.copy()

for i in zoom_face :
    for k in i :
        j =0
        for j in range(3):
            if k[j] > 150 :
                k[j] = 255 
        
plt.imshow(zoom_face)
plt.show()