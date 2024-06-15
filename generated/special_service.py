from dataclasses import dataclass

from generated.special_service_version_structure import (
    SpecialServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpecialService(SpecialServiceVersionStructure):
    """A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE.

    The pattern of working is in principle defined by a SERVICE JOURNEY
    PATTERN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
