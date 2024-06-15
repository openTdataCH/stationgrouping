from dataclasses import dataclass

from generated.duty_part_version_structure import DutyPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DutyPart(DutyPartVersionStructure):
    """A continuous part of a driver DUTY during which (s)he is under the
    management of the company.

    A DUTY PART may include BREAKs. .
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
