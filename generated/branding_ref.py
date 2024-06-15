from dataclasses import dataclass

from generated.branding_ref_structure import BrandingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BrandingRef(BrandingRefStructure):
    """
    Reference to a BRANDING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
