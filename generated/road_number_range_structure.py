from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadNumberRangeStructure:
    """
    Type for a range of numbers.
    """

    from_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "FromNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
