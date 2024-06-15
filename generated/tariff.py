from dataclasses import dataclass

from generated.tariff_version_structure import TariffVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Tariff(TariffVersionStructure):
    """
    A particular tariff, described by a combination of parameters.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
