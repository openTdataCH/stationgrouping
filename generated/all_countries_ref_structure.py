from dataclasses import dataclass, field

from generated.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllCountriesRefStructure(TypeOfValueRefStructure):
    """
    Type for a reference All Countries.

    :ivar ref: Iso 3166-1 Two Character country code.
    """

    ref: str = field(
        init=False,
        default="All",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
