from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationPartAbstract(DataManagedObjectStructure):
    """
    Dummy supertype for ORGANISATION PART.
    """

    class Meta:
        name = "OrganisationPart_"
        namespace = "http://www.netex.org.uk/netex"
