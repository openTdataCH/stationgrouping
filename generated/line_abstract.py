from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineAbstract(DataManagedObjectStructure):
    """
    Dummy Supertype for LINE &amp; FLEXIBLE LINe.
    """

    class Meta:
        name = "Line_"
        namespace = "http://www.netex.org.uk/netex"
