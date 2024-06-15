from dataclasses import dataclass

from generated.type_of_service_structure import TypeOfServiceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfService(TypeOfServiceStructure):
    """
    Classification of a Service.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
