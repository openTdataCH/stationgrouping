from dataclasses import dataclass, field
from typing import Optional

from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataSourceVersionStructure(TypeOfValueVersionStructure):
    """
    Type for DATA SOURCE.

    :ivar email: Contact email for data queries.
    """

    class Meta:
        name = "DataSource_VersionStructure"

    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
