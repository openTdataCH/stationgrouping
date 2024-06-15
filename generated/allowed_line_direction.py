from dataclasses import dataclass

from generated.allowed_line_direction_version_structure import (
    AllowedLineDirectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllowedLineDirection(AllowedLineDirectionVersionStructure):
    """
    A set of allowed DIRECTIONs that can be used on a given ROUTE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
