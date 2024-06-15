from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountStatusVersionStructure(TypeOfEntityVersionStructure):
    """
    Type for CUSTOMER ACCOUNT STATUS.
    """

    class Meta:
        name = "CustomerAccountStatus_VersionStructure"
