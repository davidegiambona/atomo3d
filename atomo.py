import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Funzione per generare la posizione di un elettrone in orbita
def electron_orbit(radius, num_points=100):
    # Angoli di 0 a 2*pi
    theta = np.linspace(0, 2 * np.pi, num_points)
    # Orbite circolari (X, Y, Z)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.zeros_like(x)
    return x, y, z

# Parametri per la rappresentazione dell'atomo
nucleus_position = (0, 0, 0)  # Nucleo centrale
electron_orbit_radii = [1, 2, 3]  # Diverse orbite degli elettroni

# Creazione del grafico 3D
fig = plt.figure(figsize=(8, 8))  # Aumenta la dimensione della finestra
ax = fig.add_subplot(111, projection='3d')

# Impostiamo il colore di sfondo dell'intera finestra (sfondo nero)
fig.patch.set_facecolor('black')
ax.set_facecolor('black')  # Sfondo del grafico stesso

# Posizione del nucleo (un punto rosso brillante)
ax.scatter(nucleus_position[0], nucleus_position[1], nucleus_position[2], color='red', s=300, label='Nucleo', marker='o')

# Disegnare orbite degli elettroni come sfere per una resa migliore
for radius in electron_orbit_radii:
    # Creiamo una "orbita" come una serie di sfere distribuite lungo la circonferenza
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.zeros_like(x)

    # Aggiungere sfere rappresentando gli elettroni
    ax.scatter(x, y, z, color='cyan', s=50, alpha=0.8)

# Estendiamo la visualizzazione in 3D per dare un buon effetto spaziale
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-1, 1)

# Etichette e personalizzazioni
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Struttura di un Atomo (Nucleo + Elettroni)', color='white')

# Rimuoviamo gli assi cartesiani
ax.axis('off')

# Rimuovere i ticks sugli assi
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Estendere lo spazio vuoto attorno alla grafica (bordi neri)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)  # Ridurre i margini per espandere l'area visibile

# Visualizzare il grafico
plt.show()
