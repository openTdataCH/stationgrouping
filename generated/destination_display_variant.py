from dataclasses import dataclass

from generated.destination_display_variant_version_structure import (
    DestinationDisplayVariantVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayVariant(DestinationDisplayVariantVersionStructure):
    """
    A variant text of a DESTINATION DISPLAY for informational purposes.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
