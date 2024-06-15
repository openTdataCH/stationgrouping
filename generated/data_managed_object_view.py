from dataclasses import dataclass

from generated.data_managed_object_view_structure import (
    DataManagedObjectViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataManagedObjectView(DataManagedObjectViewStructure):
    """
    Abstract derived view of a MANAGED OBJECT for general purpose use.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
