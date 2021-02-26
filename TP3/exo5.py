import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(0, 2, 10)
print(X)
plt.figure() # Création d'une figure
plt.plot(X, X, label='quadratique') # premiere courbe
plt.plot(X, X**3, label='cubique') # deuxieme courbe
# Extra information
plt.title('figure 1') # titre
plt.xlabel('axe x') # axes
plt.ylabel('axe y') # axes
plt.legend() # legend
plt.savefig('figure.png') # sauvegarde la figure dans le repertoire de

plt.show() # affiche la figure'''