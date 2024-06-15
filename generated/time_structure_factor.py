from dataclasses import dataclass

from generated.priceable_object_version_structure import (
    TimeStructureFactorVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeStructureFactor(TimeStructureFactorVersionStructure):
    """
    The value of a TIME INTERVAL or a DISTANCE MATRIX ELEMENT expressed by a TIME
    UNIT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
