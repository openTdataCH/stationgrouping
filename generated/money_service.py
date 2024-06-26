from dataclasses import dataclass

from generated.money_service_version_structure import (
    MoneyServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MoneyService(MoneyServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE dedicated to money services.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
