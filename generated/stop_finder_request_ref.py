from dataclasses import dataclass

from generated.stop_finder_request_ref_structure import (
    StopFinderRequestRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopFinderRequestRef(StopFinderRequestRefStructure):
    """
    Reference to a STOP FINDER REQUEST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
