from dataclasses import dataclass

from generated.branding_version_structure import BrandingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Branding(BrandingVersionStructure):
    """
    An arbitrary marketing classification.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
