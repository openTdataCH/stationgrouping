from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceableObject2(DataManagedObjectStructure):
    """
    Dummy Abstract price.
    """

    class Meta:
        name = "PriceableObject_"
        namespace = "http://www.netex.org.uk/netex"
