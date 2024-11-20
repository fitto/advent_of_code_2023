from dataclasses import dataclass
from typing import ClassVar, List


@dataclass(frozen=True)
class CubeColor:
    color: str
    ALLOWED_COLORS: ClassVar[List[str]] = ['blue', 'green', 'red']

    def __post_init__(self):
        if self.color not in self.ALLOWED_COLORS:
            raise ValueError(f"Invalid color: {self.color}. Allowed colors are: {', '.join(self.ALLOWED_COLORS)}")

    def __repr__(self):
        return f"CubeColor({self.color})"

    def __str__(self):
        return f"{self.color}"