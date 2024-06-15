from dataclasses import dataclass

from generated.transfer_restriction_version_structure import (
    TransferRestrictionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransferRestriction(TransferRestrictionVersionStructure):
    """
    A CONSTRAINT that can be applied on a CONNECTION or INTERCHANGE between two
    SCHEDULED STOP POINT, preventing or forbidding the passenger to use it.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
