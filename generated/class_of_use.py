from dataclasses import dataclass

from generated.class_of_use_value_structure import ClassOfUseValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassOfUse(ClassOfUseValueStructure):
    """
    Defines an Classification of users who may make use of a component or amenity.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
