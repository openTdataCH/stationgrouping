from dataclasses import dataclass, field
from typing import Optional, Union

from generated.access_not_allowed_error import AccessNotAllowedError
from generated.allowed_resource_usage_exceeded_error import (
    AllowedResourceUsageExceededError,
)
from generated.beyond_data_horizon import BeyondDataHorizon
from generated.capability_not_supported_error import (
    CapabilityNotSupportedError,
)
from generated.endpoint_denied_access_error import EndpointDeniedAccessError
from generated.endpoint_not_available_access_error import (
    EndpointNotAvailableAccessError,
)
from generated.error_description_structure import ErrorDescriptionStructure
from generated.invalid_data_references_error import InvalidDataReferencesError
from generated.no_info_for_topic_error import NoInfoForTopicError
from generated.other_error import OtherError
from generated.parameters_ignored_error import ParametersIgnoredError
from generated.service_not_available_error import ServiceNotAvailableError
from generated.unapproved_key_access_error import UnapprovedKeyAccessError
from generated.unknown_endpoint_error import UnknownEndpointError
from generated.unknown_extensions_error import UnknownExtensionsError
from generated.unknown_participant_error import UnknownParticipantError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceDeliveryErrorConditionStructure:
    """
    Type for Standard ErrorConditiosn for Service request.

    :ivar choice:
    :ivar description: Text description of error.
    """

    choice: Optional[
        Union[
            UnapprovedKeyAccessError,
            UnknownParticipantError,
            UnknownEndpointError,
            EndpointDeniedAccessError,
            EndpointNotAvailableAccessError,
            ServiceNotAvailableError,
            CapabilityNotSupportedError,
            AccessNotAllowedError,
            InvalidDataReferencesError,
            BeyondDataHorizon,
            NoInfoForTopicError,
            ParametersIgnoredError,
            UnknownExtensionsError,
            AllowedResourceUsageExceededError,
            OtherError,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "UnapprovedKeyAccessError",
                    "type": UnapprovedKeyAccessError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "UnknownParticipantError",
                    "type": UnknownParticipantError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "UnknownEndpointError",
                    "type": UnknownEndpointError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "EndpointDeniedAccessError",
                    "type": EndpointDeniedAccessError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "EndpointNotAvailableAccessError",
                    "type": EndpointNotAvailableAccessError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ServiceNotAvailableError",
                    "type": ServiceNotAvailableError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "CapabilityNotSupportedError",
                    "type": CapabilityNotSupportedError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AccessNotAllowedError",
                    "type": AccessNotAllowedError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "InvalidDataReferencesError",
                    "type": InvalidDataReferencesError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "BeyondDataHorizon",
                    "type": BeyondDataHorizon,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "NoInfoForTopicError",
                    "type": NoInfoForTopicError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ParametersIgnoredError",
                    "type": ParametersIgnoredError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "UnknownExtensionsError",
                    "type": UnknownExtensionsError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AllowedResourceUsageExceededError",
                    "type": AllowedResourceUsageExceededError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "OtherError",
                    "type": OtherError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    description: Optional[ErrorDescriptionStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
