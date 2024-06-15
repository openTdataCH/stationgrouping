from dataclasses import dataclass

from generated.fare_day_type_ref_structure import FareDayTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareDayTypeRef(FareDayTypeRefStructure):
    """
    Reference to a FARE DAY TYPE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
