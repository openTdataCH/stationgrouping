from dataclasses import dataclass

from generated.train_element_version_structure import (
    TrainElementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainElement(TrainElementVersionStructure):
    """
    An elementary component of a TRAIN (e.g. wagon, locomotive).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
