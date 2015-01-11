#Here elements get deleted

from math import sqrt


def asteroid(mouse_pos, asteroids):
    for i, j in zip(asteroids, range(0, len(asteroids))):
        distance = sqrt((mouse_pos[0] - (i["pos"][0]+11.5))**2 + (mouse_pos[1] - (i["pos"][1]+11.5))**2)
        if distance <= 11.5:
            del asteroids[j]

    return asteroids