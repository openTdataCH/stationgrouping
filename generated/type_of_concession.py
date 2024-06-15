from dataclasses import dataclass

from generated.type_of_concession_version_structure import (
    TypeOfConcessionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfConcession(TypeOfConcessionVersionStructure):
    """
    Category of concession user.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
