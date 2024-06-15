from dataclasses import dataclass

from generated.commercial_profile_version_structure import (
    CommercialProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommercialProfile(CommercialProfileVersionStructure):
    """
    A category of users depending on their commercial relations with the operator
    (frequency of use, amount of purchase etc.), often used for allowing discounts.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
