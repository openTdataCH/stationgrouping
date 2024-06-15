from dataclasses import dataclass

from generated.authenticated_request_structure import (
    AuthenticatedRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AuthenticatedRequest(AuthenticatedRequestStructure):
    """
    Subsititutable type for an authenticated request Authenticated.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
