from dataclasses import dataclass

from generated.other_error_structure import OtherErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class OtherError(OtherErrorStructure):
    """Error: Error type other than the well defined codes."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
