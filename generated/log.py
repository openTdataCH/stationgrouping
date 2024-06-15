from dataclasses import dataclass

from generated.log_version_structure import LogVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Log(LogVersionStructure):
    """A Collection of LOG ENTRIES grouped together in a file or any other kind of
    storage.

    +v1.1.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
