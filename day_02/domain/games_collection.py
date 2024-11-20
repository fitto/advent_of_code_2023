from typing import List, Optional

from day_02.domain.cube_set import CubeSet
from day_02.domain.game import Game


class GamesCollection:
    def __init__(self,
                 games_list: List[Game]
                 ):
        self.games_list = games_list

    @staticmethod
    def new_from_text(file_name: str) -> Optional['GamesCollection']:
        try:
            games_list = []

            with open(file_name, "r") as file:
                for line in file:
                    games_list.append(Game.new_from_text(line))

            return GamesCollection(games_list)
        except ValueError as e:
            print(f"An error occurred: {e}")
            return None

    def games_with_possible_cube_sets(self,
                                      cube_set_to_check: CubeSet
                                      ) -> List[Game]:
        return [game for game in self.games_list if not game.possible_cube_sets(cube_set_to_check)]

    def min_cube_sets(self) -> List[CubeSet]:
        return [game.min_cube_set() for game in self.games_list]

    def __repr__(self):
        return f"GamesCollection({len(self.games_list)} games)"

    def __str__(self):
        return self.__repr__()
