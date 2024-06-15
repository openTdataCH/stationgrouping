from dataclasses import dataclass

from generated.level_version_structure import LevelVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Level(LevelVersionStructure):
    """An identified storey (ground, first, basement, mezzanine, etc) within an
    interchange building or SITE on which SITE COMPONENTs reside.

    A PATH LINK may connect components on different levels.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
