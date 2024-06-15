from dataclasses import dataclass

from generated.fare_request_ref_structure import FareRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareRequestRef(FareRequestRefStructure):
    """
    Reference to a FARE REQUEST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
