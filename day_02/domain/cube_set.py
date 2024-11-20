from dataclasses import dataclass
from typing import Dict, Optional, List

from day_02.domain.cube_color import CubeColor


@dataclass(frozen=True)
class CubeSet:
    cubes: Dict[CubeColor, int]

    @staticmethod
    def new_from_text(input_string: str) -> Optional['CubeSet']:
        try:
            pairs = input_string.split(", ")
            new_cube_set = CubeSet.new_empty()

            for pair in pairs:
                number_str, color_name = pair.split()
                new_cube_set = new_cube_set.set_cubes(
                    CubeColor(color_name),
                    int(number_str)
                )
                if new_cube_set is None:
                    print('Unable to parse')
                    return None
            return new_cube_set
        except ValueError as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def new_empty() -> 'CubeSet':
        return CubeSet({CubeColor(color_name): 0 for color_name in CubeColor.ALLOWED_COLORS})

    def set_cubes(self,
                  cube_color: CubeColor,
                  number_of_cubes: int
                  ) -> Optional['CubeSet']:
        if number_of_cubes >= 0:
            new_dict = self.cubes.copy()
            new_dict[cube_color] = number_of_cubes
            return CubeSet(new_dict)
        else:
            print(f'Invalid inputs {cube_color} {number_of_cubes}')
            return None

    def has_less_or_equal_cubes_than(self,
                                     cube_color: CubeColor,
                                     number_of_cubes: int
                                     ) -> Optional[bool]:
        cubes_no = self.number_of_cubes(cube_color)
        if cubes_no is None:
            return None

        return cubes_no <= number_of_cubes

    def number_of_cubes(self,
                        cube_color: CubeColor,
                        ) -> Optional[int]:
        if cube_color not in self.cubes.keys():
            print('Invalid color')
            return None
        else:
            return self.cubes[cube_color]

    def within_cube_set(self,
                        cube_set: 'CubeSet'
                        ) -> bool:
        for cube_color, cube_number in cube_set.cubes.items():
            if self.number_of_cubes(cube_color) > cube_number:
                return False
        return True

    @property
    def all_cubes_numbers_list(self) -> List[int]:
        return [item for item in self.cubes.values()]

    def __repr__(self):
        return f"CubeSet({', '.join(f'{key}: {value}' for key, value in self.cubes.items())})"

    def __str__(self):
        return self.__repr__()



