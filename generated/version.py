from dataclasses import dataclass

from generated.version_version_structure import VersionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Version(VersionVersionStructure):
    """A group of operational data instances which share the same VALIDITY
    CONDITIONs.

    A VERSION belongs to a unique VERSION FRAME and is characterized by
    a unique TYPE OF VERSION. E.g.  NETWORK VERSION for Line 12 starting
    from 2000-01-01.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
