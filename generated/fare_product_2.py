from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareProduct2(DataManagedObjectStructure):
    """
    An immaterial marketable element (access rights, discount rights etc), specific
    to a CHARGING MOMENT.
    """

    class Meta:
        name = "FareProduct_"
        namespace = "http://www.netex.org.uk/netex"
