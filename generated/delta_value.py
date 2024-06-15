from dataclasses import dataclass

from generated.delta_value_structure import DeltaValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeltaValue(DeltaValueStructure):
    """A  record of the detailed changes of a given ENTITY IN VERSION from one
    VERSION to the next one.

    A DELTA contains pairs of attributes' old values - new values.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
