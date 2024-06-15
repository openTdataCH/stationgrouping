from dataclasses import dataclass

from generated.left_luggage_service_version_structure import (
    LeftLuggageServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LeftLuggageService(LeftLuggageServiceVersionStructure):
    """
    Specialisation of CUSTOMER SERVICE for left luggage (provides left luggage
    information like self service locker, locker free, etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
