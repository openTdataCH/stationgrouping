from dataclasses import dataclass

from generated.entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageParameter2(DataManagedObjectStructure):
    """Dummy Supertype: A parameter used to specify the use of a fare system."""

    class Meta:
        name = "UsageParameter_"
        namespace = "http://www.netex.org.uk/netex"
