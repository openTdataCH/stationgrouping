from dataclasses import dataclass

from generated.crew_base_version_structure import CrewBaseVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CrewBase(CrewBaseVersionStructure):
    """
    A place where operating EMPLOYEEs (e.g. drivers) report on and register their
    worK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
