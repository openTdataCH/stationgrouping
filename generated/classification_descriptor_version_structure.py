from dataclasses import dataclass

from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassificationDescriptorVersionStructure(TypeOfValueVersionStructure):
    """
    Type for a Descriptor for a POINT OF INTEREST CLASSIFICATION.
    """

    class Meta:
        name = "ClassificationDescriptor_VersionStructure"
