# On détermine un nombre pivot
# On compare ce nombre pivot aux éléments:
#   - si l'élément est plus grand on le met à droite
#   - si l'élément est plus petit on le met à gauche
#   - on donne la position finale du pivot
# On fait une fonction récursive sur les sous liste à gauche et à droite jusqu'à ce que chaque sous liste ne contiennent qu'un seul élément ou soient vide

import random

my_list = [45, 12, 25, 125, 10, 0, 36, 42, 130, 66]

def quicksort(list):

    if len(list) <= 1:
        return list

    pivot_index = random.randint(0, len(list) - 1)
    pivot = list[pivot_index]

    left = []
    middle = []
    right = []

    for element in list:

        if element > pivot:
            right.append(element)
        elif element < pivot:
            left.append(element)
        else:
            middle.append(element)

    sorted_left = quicksort(left)
    sorted_right = quicksort(right)

    return sorted_left + middle + sorted_right
    
print(quicksort(my_list))