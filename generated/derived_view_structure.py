from dataclasses import dataclass, field
from typing import Optional

from generated.branding_ref import BrandingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DerivedViewStructure:
    """
    Type for MANAGED OBJECT VIEW.

    :ivar branding_ref:
    :ivar id: Identifier of Object of which this is a view.
    """

    branding_ref: Optional[BrandingRef] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
