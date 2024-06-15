from dataclasses import dataclass

from generated.open_transport_mode_value_structure import (
    OpenTransportModeValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OpenTransportMode(OpenTransportModeValueStructure):
    """Open values TRANSPORT MODE.

    Allows additional named modes to be created. A mode is a
    characterisation of the operation according to the means of
    transport (bus, tram, metro, train, ferry, ship). NOTE : To enforce
    standardisation, enumerated values are generally used in references.
    In The schema.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
