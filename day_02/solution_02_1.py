from day_02.domain.cube_color import CubeColor
from day_02.domain.cube_set import CubeSet
from day_02.domain.games_collection import GamesCollection

# games_collection = GamesCollection.new_from_text('test1.txt')
games_collection = GamesCollection.new_from_text('task1.txt')

cubes_set_shown = CubeSet(
    {
        CubeColor('red'): 12,
        CubeColor('green'): 13,
        CubeColor('blue'): 14,
    }
)

games = games_collection.games_with_possible_cube_sets(cubes_set_shown)
output = sum(game.game_no for game in games)

print(output)


