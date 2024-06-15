from dataclasses import dataclass, field

from generated.version_of_object_ref_structure import (
    VersionOfObjectRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllOrganisationsRefStructure(VersionOfObjectRefStructure):
    """
    Type for a reference tto all oranisationsORGANISATION.

    :ivar ref: Identifier of an ORGANISATION.
    """

    ref: str = field(
        init=False,
        default="All",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
