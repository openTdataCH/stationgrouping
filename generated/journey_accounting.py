from dataclasses import dataclass

from generated.journey_accounting_version_structure import (
    JourneyAccountingVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyAccounting(JourneyAccountingVersionStructure):
    """
    Parameters characterizing VEHICLE JOURNEYs or SPECIAL SERVICEs used for
    accounting purposes in particular in contracts between ORGANISATIONs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
