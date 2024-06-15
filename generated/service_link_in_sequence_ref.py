from dataclasses import dataclass

from generated.service_link_in_sequence_ref_structure import (
    ServiceLinkInSequenceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLinkInSequenceRef(ServiceLinkInSequenceRefStructure):
    """Reference to a SERVICE LINK IN SEQUENCE.

    If given by context does not need to be stated.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
