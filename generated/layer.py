from dataclasses import dataclass

from generated.layer_version_structure import LayerVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Layer(LayerVersionStructure):
    """
    A user-defined GROUP OF ENTITies, specified for a particular functional
    purpose, associating data referring to a particular LOCATING SYSTEM.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
