from dataclasses import dataclass

from generated.country_version_structure import CountryVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Country(CountryVersionStructure):
    """
    A sovereign COUNTRY.where entities may be located or domiciled.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
