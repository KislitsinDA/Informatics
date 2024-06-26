def find_farthest_orbit(list_of_orbits):
    max_area = max([3.14 * orbit[0] * orbit[1] for orbit in list_of_orbits if orbit[0] != orbit[1]])
    for orbit in list_of_orbits:
        if max_area == 3.14 * orbit[0] * orbit[1]:
            return orbit


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
