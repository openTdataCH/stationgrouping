from dataclasses import dataclass

from generated.residential_qualification_version_structure import (
    ResidentialQualificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResidentialQualification(ResidentialQualificationVersionStructure):
    """
    The number and characteristics (weight, volume) of luggage that a holder of an
    access right is entitled to carry.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
