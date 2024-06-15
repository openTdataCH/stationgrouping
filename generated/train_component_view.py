from dataclasses import dataclass

from generated.train_component_derived_view_structure import (
    TrainComponentDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentView(TrainComponentDerivedViewStructure):
    """
    Simplified view of TRAIN COMPONENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
