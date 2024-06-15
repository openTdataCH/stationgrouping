from dataclasses import dataclass

from generated.destination_display_variant_ref_structure import (
    DestinationDisplayVariantRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayVariantRef(DestinationDisplayVariantRefStructure):
    """
    Reference to a DESTINATION DISPLAY VARIANT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
