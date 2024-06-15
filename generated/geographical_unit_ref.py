from dataclasses import dataclass

from generated.geographical_unit_ref_structure import (
    GeographicalUnitRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnitRef(GeographicalUnitRefStructure):
    """
    Reference to a GEOGRAPHICAL UNIT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
