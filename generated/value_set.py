from dataclasses import dataclass

from generated.value_set_version_structure import ValueSetVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValueSet(ValueSetVersionStructure):
    """
    An extensible set of code values   which may be added to by user applications
    and is used to validate the properties of Entities.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
