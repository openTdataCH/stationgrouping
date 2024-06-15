from dataclasses import dataclass

from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingAlgorithmTypeValueStructure(TypeOfValueVersionStructure):
    """
    Type for a TIMING ALGORITHM TYPE.
    """

    class Meta:
        name = "TimingAlgorithmType_ValueStructure"
