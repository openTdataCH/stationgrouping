from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.control_centre import ControlCentre
from generated.control_centre_ref import ControlCentreRef
from generated.department import Department
from generated.department_ref import DepartmentRef
from generated.operating_department import OperatingDepartment
from generated.organisation_part import OrganisationPart
from generated.organisation_part_ref import OrganisationPartRef
from generated.organisational_unit import OrganisationalUnit
from generated.organisational_unit_ref import OrganisationalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationPartsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ORGANISATION PARTs.
    """

    class Meta:
        name = "organisationParts_RelStructure"

    choice: List[
        Union[
            ControlCentreRef,
            OrganisationalUnitRef,
            DepartmentRef,
            OrganisationPartRef,
            ControlCentre,
            OperatingDepartment,
            OrganisationalUnit,
            Department,
            OrganisationPart,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControlCentreRef",
                    "type": ControlCentreRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnitRef",
                    "type": OrganisationalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DepartmentRef",
                    "type": DepartmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationPartRef",
                    "type": OrganisationPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControlCentre",
                    "type": ControlCentre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatingDepartment",
                    "type": OperatingDepartment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationalUnit",
                    "type": OrganisationalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Department",
                    "type": Department,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationPart",
                    "type": OrganisationPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
