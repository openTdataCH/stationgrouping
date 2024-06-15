from dataclasses import dataclass

from generated.fare_unit_ref_structure import FareUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareUnitRef(FareUnitRefStructure):
    """
    Reference to a FARE UNIT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
