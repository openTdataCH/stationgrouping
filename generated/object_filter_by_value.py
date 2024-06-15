from dataclasses import dataclass

from generated.object_filter_by_value_structure import (
    ObjectFilterByValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ObjectFilterByValue(ObjectFilterByValueStructure):
    """
    Abstract Topic Filter.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
