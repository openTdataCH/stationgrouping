from dataclasses import dataclass

from generated.operating_day_ref_structure import OperatingDayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingDayRef(OperatingDayRefStructure):
    """
    Reference to an OPERATING DAY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
