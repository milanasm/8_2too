import numpy as np
import matplotlib.pyplot as plt

"""
Этот код:
    - Читает данные о горах из текстового файла maed.txt.
    - Вычисляет среднюю, самую высокую, самую низкую гору и общую высоту всех гор.
    - Показывает это на экране.
    - Строит столбчатый график, где видно, какая гора какая по высоте.
"""

#4tenie iz faila
with open("maed.txt", "r") as fail:
    """
    Что такое with open(...) as ...?
        ✅ Открывает файл
        ✅ Делает с ним что-то (чтение, запись и т.д.)
        ✅ Автоматически закрывает файл, даже если произойдёт ошибка

    as fail — даёт этому открытому файлу имя fail, чтобы можно было его использовать.
    """

    read=[rida.split() for rida in fail.readlines()]
    """
    Каждую строку разбиваем на части, чтобы получить имя горы и её высоту
    """

nimed=[rida[0] for rida in read]
korgused=np.array([int(rida[1]) for rida in read])
"""
np.array превращает его в массив, для подсчёта среднего, максимума, суммы и других операций.
"""

#Stat
keskmine=np.mean(korgused)
max_indeks=np.argmax(korgused)
min_indeks=np.argmin(korgused)
kogusumma=np.sum(korgused)
"""
Считаем среднюю высоту.

Находим, какая гора самая высокая и самая низкая.

Считаем общую высоту всех гор.
"""

print(f"Keskmine: {keskmine:.1f} m")
print(f"Kõrgeim: {nimed[max_indeks]} ({korgused[max_indeks]} m)")
print(f"Madalim: {nimed[min_indeks]} ({korgused[min_indeks]} m)")
print(f"Kogusumma: {kogusumma} m")

#Grafik
plt.bar(nimed, korgused)           # Создаём столбчатую диаграмму
plt.xticks(rotation=45)            # Поворачиваем подписи по X (чтобы влезли)
plt.title('Mäed')                  # Заголовок графика
plt.tight_layout()                 # Автоматически настраивает поля, чтобы всё влезло
plt.savefig('maed_graafik.png')    # Сохраняем график в файл
plt.show()                         # Показываем график на экране



