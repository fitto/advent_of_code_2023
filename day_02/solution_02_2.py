from functools import reduce

from day_02.domain.games_collection import GamesCollection

# games_collection = GamesCollection.new_from_text('test2.txt')
games_collection = GamesCollection.new_from_text('task1.txt')

cube_sets = games_collection.min_cube_sets()
output = sum([reduce(lambda x, y: x * y, cube_set.all_cubes_numbers_list) for cube_set in cube_sets])

print(output)
