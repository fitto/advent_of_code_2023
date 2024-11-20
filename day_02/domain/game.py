from typing import List, Optional

from day_02.domain.cube_set import CubeSet


class Game:
    def __init__(self,
                 game_no: int,
                 cube_sets: List[CubeSet]
                 ):
        self.game_no = game_no
        self.cube_sets = cube_sets

    @staticmethod
    def new_from_text(input_string: str) -> Optional['Game']:
        try:
            game_name_data, cube_sets_data = input_string.split(": ")

            game_no = int(game_name_data.split()[-1])
            cube_sets = []

            for cube_set_text in cube_sets_data.split('; '):
                cube_sets.append(CubeSet.new_from_text(cube_set_text))

            return Game(
                game_no,
                cube_sets
            )
        except ValueError as e:
            print(f"An error occurred: {e}")
            return None

    def possible_cube_sets(self,
                           cube_set_to_check: CubeSet
                           ) -> List[CubeSet]:
        return [cube_set for cube_set in self.cube_sets if not cube_set.within_cube_set(cube_set_to_check)]

    def min_cube_set(self) -> CubeSet:
        min_dict = {}

        for cub_set in self.cube_sets:
            for cube_color, num in cub_set.cubes.items():
                min_dict[cube_color] = max(min_dict.get(cube_color, 0), num)

        return CubeSet(min_dict)

    def __repr__(self):
        return f"Game(no = {self.game_no}, cube_sets_no = {len(self.cube_sets)})"

    def __str__(self):
        return self.__repr__()
