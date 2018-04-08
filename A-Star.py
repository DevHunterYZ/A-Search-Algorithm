# Kütüphaneleri çağıralım.
import numpy
from heapq import *

# Sezgisel Fonksiyonumuzu oluşturalım.
def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def astar(array, start, goal):
# Komşuları tanımla. 0,0 kendisidir, alınmaz.
    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    # Daha önce değerlendirilen düğüm kümesi.
    close_set = set()
    # Boş harita // Gezinmiş düğümlerin haritası.
    came_from = {}
    # En iyi bilinen yol boyunca başlangıçtan itibaren maliyet.
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    #İlk olarak başlangıç düğümünü içeren, değerlendirilecek geçici düğümler kümesi.
    oheap = []

    heappush(oheap, (fscore[start], start))

    while oheap:
        # En düşük f_score [] değerine sahip olan openset içindeki düğüm.
        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j     
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # dizi y duvarlarına bağlı
                    continue
            else:
                # dizi x duvarlarına bağlı
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))

    return False
#Labirenti oluştur.
nmap = numpy.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,0,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

print (astar(nmap, (10,13), (0,0)))
