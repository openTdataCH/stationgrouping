from dataclasses import dataclass, field
from typing import Optional

from generated.multilingual_string import MultilingualString
from generated.sign_content_enumeration import SignContentEnumeration
from generated.sign_equipment_version_structure import (
    SignEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralSignStructure(SignEquipmentVersionStructure):
    """
    Type for an GENERAL SIGN.

    :ivar content: Content of Sign.
    :ivar sign_content_type: Classification of content as standard
        category.
    """

    content: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sign_content_type: Optional[SignContentEnumeration] = field(
        default=None,
        metadata={
            "name": "SignContentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
