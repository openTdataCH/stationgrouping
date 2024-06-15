from dataclasses import dataclass

from generated.flexible_area_version_structure import (
    FlexibleAreaVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleArea(FlexibleAreaVersionStructure):
    """Specialisation of a FLEXIBLE QUAY (which is abstract) to identify what is
    the catchment area for a flexible service (so that a stop finder can find  the
    nearest available types of transport).

    It is a named zone visited by a particular mode of transport.  It is
    part of the SITE data set rather than the service data set, since it
    can be defined and exists independently of an actual service.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
