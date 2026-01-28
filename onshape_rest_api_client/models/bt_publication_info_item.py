from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_element_type import GBTElementType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_application_target_info import BTApplicationTargetInfo


T = TypeVar("T", bound="BTPublicationInfoItem")


@_attrs_define
class BTPublicationInfoItem:
    """
    Attributes:
        json_type (str):
        application_target (BTApplicationTargetInfo | Unset):
        data_type (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        element_type (GBTElementType | Unset):
        encoded_configuration (str | Unset):
        id (str | Unset):
        part_id (str | Unset):
        part_name (str | Unset):
        part_number (str | Unset):
        revision (str | Unset):
        revision_id (str | Unset):
        state (int | Unset):
        version_id (str | Unset):
        version_name (str | Unset):
    """

    json_type: str
    application_target: BTApplicationTargetInfo | Unset = UNSET
    data_type: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: GBTElementType | Unset = UNSET
    encoded_configuration: str | Unset = UNSET
    id: str | Unset = UNSET
    part_id: str | Unset = UNSET
    part_name: str | Unset = UNSET
    part_number: str | Unset = UNSET
    revision: str | Unset = UNSET
    revision_id: str | Unset = UNSET
    state: int | Unset = UNSET
    version_id: str | Unset = UNSET
    version_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_type = self.json_type

        application_target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application_target, Unset):
            application_target = self.application_target.to_dict()

        data_type = self.data_type

        document_id = self.document_id

        element_id = self.element_id

        element_type: str | Unset = UNSET
        if not isinstance(self.element_type, Unset):
            element_type = self.element_type.value

        encoded_configuration = self.encoded_configuration

        id = self.id

        part_id = self.part_id

        part_name = self.part_name

        part_number = self.part_number

        revision = self.revision

        revision_id = self.revision_id

        state = self.state

        version_id = self.version_id

        version_name = self.version_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonType": json_type,
            }
        )
        if application_target is not UNSET:
            field_dict["applicationTarget"] = application_target
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if encoded_configuration is not UNSET:
            field_dict["encodedConfiguration"] = encoded_configuration
        if id is not UNSET:
            field_dict["id"] = id
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_name is not UNSET:
            field_dict["partName"] = part_name
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if revision is not UNSET:
            field_dict["revision"] = revision
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if state is not UNSET:
            field_dict["state"] = state
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if version_name is not UNSET:
            field_dict["versionName"] = version_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_application_target_info import BTApplicationTargetInfo

        d = dict(src_dict)
        json_type = d.pop("jsonType")

        _application_target = d.pop("applicationTarget", UNSET)
        application_target: BTApplicationTargetInfo | Unset
        if isinstance(_application_target, Unset):
            application_target = UNSET
        else:
            application_target = BTApplicationTargetInfo.from_dict(_application_target)

        data_type = d.pop("dataType", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        _element_type = d.pop("elementType", UNSET)
        element_type: GBTElementType | Unset
        if isinstance(_element_type, Unset):
            element_type = UNSET
        else:
            element_type = GBTElementType(_element_type)

        encoded_configuration = d.pop("encodedConfiguration", UNSET)

        id = d.pop("id", UNSET)

        part_id = d.pop("partId", UNSET)

        part_name = d.pop("partName", UNSET)

        part_number = d.pop("partNumber", UNSET)

        revision = d.pop("revision", UNSET)

        revision_id = d.pop("revisionId", UNSET)

        state = d.pop("state", UNSET)

        version_id = d.pop("versionId", UNSET)

        version_name = d.pop("versionName", UNSET)

        bt_publication_info_item = cls(
            json_type=json_type,
            application_target=application_target,
            data_type=data_type,
            document_id=document_id,
            element_id=element_id,
            element_type=element_type,
            encoded_configuration=encoded_configuration,
            id=id,
            part_id=part_id,
            part_name=part_name,
            part_number=part_number,
            revision=revision,
            revision_id=revision_id,
            state=state,
            version_id=version_id,
            version_name=version_name,
        )

        bt_publication_info_item.additional_properties = d
        return bt_publication_info_item

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
