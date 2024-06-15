from dataclasses import dataclass

from generated.connection_version_structure import ConnectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Connection(ConnectionVersionStructure):
    """The physical (spatial) possibility for a passenger to change from one public
    transport vehicle to another to continue the trip.

    Different times may be necessary to cover this link, depending on
    the kind of passenger.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
