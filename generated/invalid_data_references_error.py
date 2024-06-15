from dataclasses import dataclass

from generated.invalid_data_references_error_structure import (
    InvalidDataReferencesErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InvalidDataReferencesError(InvalidDataReferencesErrorStructure):
    """Error: Request contains references to  identifiers that are not known.  +SIRI v2.0."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
