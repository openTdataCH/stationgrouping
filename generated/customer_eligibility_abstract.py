from dataclasses import dataclass

from generated.entity_in_version_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerEligibilityAbstract(VersionedChildStructure):
    """
    Dummy Type for Customer Eligibility.
    """

    class Meta:
        name = "CustomerEligibility_"
        namespace = "http://www.netex.org.uk/netex"
