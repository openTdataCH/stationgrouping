from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CoordinatesStructure:
    """
    Type for GM Coordinates.
    """

    value: List[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
