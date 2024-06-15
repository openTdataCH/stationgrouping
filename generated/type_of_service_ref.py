from dataclasses import dataclass

from generated.type_of_service_ref_structure import TypeOfServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfServiceRef(TypeOfServiceRefStructure):
    """
    Reference to a TYPE OF SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
