from dataclasses import dataclass

from generated.delta_structure import DeltaStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Delta(DeltaStructure):
    """A  record of the detailed changes of a given ENTITY IN VERSION from one
    VERSION to the next one.

    A DELTA contains pairs of attributes' old values - new values.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
