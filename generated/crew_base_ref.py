from dataclasses import dataclass

from generated.crew_base_ref_structure import CrewBaseRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CrewBaseRef(CrewBaseRefStructure):
    """
    Reference to a CREW BASE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
