from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Interchange2(DataManagedObjectStructure):
    """
    Dummy supertype for INTERCHANGe.
    """

    class Meta:
        name = "Interchange_"
        namespace = "http://www.netex.org.uk/netex"
