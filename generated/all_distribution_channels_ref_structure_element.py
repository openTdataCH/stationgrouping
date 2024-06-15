from dataclasses import dataclass, field

from generated.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllDistributionChannelsRefStructureElement(TypeOfValueRefStructure):
    """
    Type for Reference to a DISTRIBUTION CHANNEL.

    :ivar ref: Identifier of a TYPE OF VALUE.
    """

    ref: str = field(
        init=False,
        default="All",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
