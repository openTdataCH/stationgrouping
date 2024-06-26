from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Organisation2(DataManagedObjectStructure):
    """
    Dummy supertype for ORGANISATION.
    """

    class Meta:
        name = "Organisation_"
        namespace = "http://www.netex.org.uk/netex"
