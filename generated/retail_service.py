from dataclasses import dataclass

from generated.retail_service_version_structure import (
    RetailServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailService(RetailServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE dedicated to retail services.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
