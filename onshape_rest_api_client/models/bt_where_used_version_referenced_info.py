from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_base_info import BTBaseInfo
    from ..models.bt_document_base_summary_info import BTDocumentBaseSummaryInfo
    from ..models.config_info import ConfigInfo


T = TypeVar("T", bound="BTWhereUsedVersionReferencedInfo")


@_attrs_define
class BTWhereUsedVersionReferencedInfo:
    """List of document versions in which the queried item is referenced. Each entry contains the version info, referring
    document and element details, configuration, revision, and part identifiers. Only populated when includeVersionInfo
    is true.

        Attributes:
            configuration (list[ConfigInfo] | Unset): The configuration parameters of the referenced item in this version.
            created_at (datetime.datetime | Unset): The timestamp when this version was created.
            document (BTDocumentBaseSummaryInfo | Unset): Summary information about the document containing the reference.
            element_id (str | Unset): The element ID of the referring element in this version.
            element_type (int | Unset): The element type ordinal of the referring element.
            part_id (str | Unset): The part ID of the referenced item.
            part_name (str | Unset): The part name of the referenced item.
            part_number (str | Unset): The part number of the referenced item.
            revision (str | Unset): The revision id of the referenced item.
            revision_obsolete (bool | Unset): Whether the revision of this item is obsolete.
            version (BTBaseInfo | Unset):
    """

    configuration: list[ConfigInfo] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    document: BTDocumentBaseSummaryInfo | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: int | Unset = UNSET
    part_id: str | Unset = UNSET
    part_name: str | Unset = UNSET
    part_number: str | Unset = UNSET
    revision: str | Unset = UNSET
    revision_obsolete: bool | Unset = UNSET
    version: BTBaseInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = []
            for configuration_item_data in self.configuration:
                configuration_item = configuration_item_data.to_dict()
                configuration.append(configuration_item)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        document: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        element_id = self.element_id

        element_type = self.element_type

        part_id = self.part_id

        part_name = self.part_name

        part_number = self.part_number

        revision = self.revision

        revision_obsolete = self.revision_obsolete

        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if document is not UNSET:
            field_dict["document"] = document
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_name is not UNSET:
            field_dict["partName"] = part_name
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if revision is not UNSET:
            field_dict["revision"] = revision
        if revision_obsolete is not UNSET:
            field_dict["revisionObsolete"] = revision_obsolete
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_base_info import BTBaseInfo
        from ..models.bt_document_base_summary_info import BTDocumentBaseSummaryInfo
        from ..models.config_info import ConfigInfo

        d = dict(src_dict)
        _configuration = d.pop("configuration", UNSET)
        configuration: list[ConfigInfo] | Unset = UNSET
        if _configuration is not UNSET:
            configuration = []
            for configuration_item_data in _configuration:
                configuration_item = ConfigInfo.from_dict(configuration_item_data)

                configuration.append(configuration_item)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _document = d.pop("document", UNSET)
        document: BTDocumentBaseSummaryInfo | Unset
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = BTDocumentBaseSummaryInfo.from_dict(_document)

        element_id = d.pop("elementId", UNSET)

        element_type = d.pop("elementType", UNSET)

        part_id = d.pop("partId", UNSET)

        part_name = d.pop("partName", UNSET)

        part_number = d.pop("partNumber", UNSET)

        revision = d.pop("revision", UNSET)

        revision_obsolete = d.pop("revisionObsolete", UNSET)

        _version = d.pop("version", UNSET)
        version: BTBaseInfo | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = BTBaseInfo.from_dict(_version)

        bt_where_used_version_referenced_info = cls(
            configuration=configuration,
            created_at=created_at,
            document=document,
            element_id=element_id,
            element_type=element_type,
            part_id=part_id,
            part_name=part_name,
            part_number=part_number,
            revision=revision,
            revision_obsolete=revision_obsolete,
            version=version,
        )

        bt_where_used_version_referenced_info.additional_properties = d
        return bt_where_used_version_referenced_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
