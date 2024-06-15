from dataclasses import dataclass

from generated.timeband_ref_structure import TimebandRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimebandRef(TimebandRefStructure):
    """
    Reference to a TIME BAND.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
