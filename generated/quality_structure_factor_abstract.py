from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QualityStructureFactorAbstract(DataManagedObjectStructure):
    """
    Dummy type.
    """

    class Meta:
        name = "QualityStructureFactor_"
        namespace = "http://www.netex.org.uk/netex"
