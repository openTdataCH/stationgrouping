from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from generated.data_objects_rel_structure import DataObjectsRelStructure
from generated.multilingual_string import MultilingualString
from generated.participant_ref import ParticipantRef
from generated.publication_request_structure import PublicationRequestStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PublicationDeliveryStructure:
    """
    Type for Publication Delivery.

    :ivar publication_timestamp: Time of output of data.
    :ivar participant_ref:
    :ivar publication_request: Echo Request used to create bulk
        response.
    :ivar publication_refresh_interval: How often data in publication is
        refreshed.
    :ivar description: Description of contents.
    :ivar data_objects: NeTEx Entities of any type.
    :ivar version:
    """

    publication_timestamp: XmlDateTime = field(
        metadata={
            "name": "PublicationTimestamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    participant_ref: ParticipantRef = field(
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    publication_request: Optional[PublicationRequestStructure] = field(
        default=None,
        metadata={
            "name": "PublicationRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    publication_refresh_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PublicationRefreshInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    data_objects: Optional[DataObjectsRelStructure] = field(
        default=None,
        metadata={
            "name": "dataObjects",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    version: str = field(
        default="1.0",
        metadata={
            "type": "Attribute",
        },
    )
