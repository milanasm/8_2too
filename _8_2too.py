import numpy as np
import matplotlib.pyplot as plt

#4tenie iz faila
with open("maed.txt", "r") as fail:
    read=[rida.split() for rida in fail.readlines()]

nimed=[rida[0] for rida in read]
korgused=np.array([int(rida[1]) for rida in read])

#Stat
keskmine=np.mean(korgused)
max_indeks=np.argmax(korgused)
min_indeks=np.argmin(korgused)
kogusumma=np.sum(korgused)

print(f"Keskmine: {keskmine:.1f} m")
print(f"Kõrgeim: {nimed[max_indeks]} ({korgused[max_indeks]} m)")
print(f"Madalim: {nimed[min_indeks]} ({korgused[min_indeks]} m)")
print(f"Kogusumma: {kogusumma} m")

#Grafik
plt.bar(nimed, korgused)
plt.xticks(rotation=45)
plt.title('Mäed')
plt.tight_layout()
plt.savefig('maed_graafik.png')
plt.show()