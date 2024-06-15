from dataclasses import dataclass

from generated.control_centre_version_structure import (
    ControlCentreVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControlCentre(ControlCentreVersionStructure):
    """
    An ORGANISATION PART for an operational team who are responsible for issuing
    commands to control the services.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
