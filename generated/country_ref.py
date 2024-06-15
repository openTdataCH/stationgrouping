from dataclasses import dataclass

from generated.country_ref_structure import CountryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CountryRef(CountryRefStructure):
    """Reference to a country ISO 3166-1 Note that GB is used for UK .

    May be qualified with a 3166-2 subdivision e.g. gb +m ENG, GB + SCT, GB See www.iso.org/iso/country_codes/iso_3166_code_lists.htm.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
