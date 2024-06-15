from dataclasses import dataclass, field
from typing import Optional

from generated.info_links_rel_structure import InfoLinksRelStructure
from generated.priceable_object_version_structure import (
    PriceableObjectVersionStructure,
)
from generated.private_code import PrivateCode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceAccessRightVersionStructure(PriceableObjectVersionStructure):
    """
    Type for  SERVICE ACCESS RIGHT.

    :ivar private_code:
    :ivar info_url: URL for further information.
    :ivar document_links: Timetable documents associated with the
        Product e.g pdf files
    """

    class Meta:
        name = "ServiceAccessRight_VersionStructure"

    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    info_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfoUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    document_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "documentLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
