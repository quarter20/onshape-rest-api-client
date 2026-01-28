from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_property_value_param import BTPropertyValueParam


T = TypeVar("T", bound="BTReleasePackageItemParams")


@_attrs_define
class BTReleasePackageItemParams:
    """
    Attributes:
        configuration (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        element_type (int | Unset):
        flat_part_id (str | Unset):
        href (str | Unset):
        id (str | Unset):
        is_included (bool | Unset):
        parent_id (str | Unset):
        part_id (str | Unset):
        part_identity (str | Unset):
        part_number (str | Unset):
        properties (list[BTPropertyValueParam] | Unset):
        revision_id (str | Unset):
        version_id (str | Unset):
        workspace_id (str | Unset):
    """

    configuration: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: int | Unset = UNSET
    flat_part_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    is_included: bool | Unset = UNSET
    parent_id: str | Unset = UNSET
    part_id: str | Unset = UNSET
    part_identity: str | Unset = UNSET
    part_number: str | Unset = UNSET
    properties: list[BTPropertyValueParam] | Unset = UNSET
    revision_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration

        document_id = self.document_id

        element_id = self.element_id

        element_type = self.element_type

        flat_part_id = self.flat_part_id

        href = self.href

        id = self.id

        is_included = self.is_included

        parent_id = self.parent_id

        part_id = self.part_id

        part_identity = self.part_identity

        part_number = self.part_number

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        revision_id = self.revision_id

        version_id = self.version_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if flat_part_id is not UNSET:
            field_dict["flatPartId"] = flat_part_id
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if is_included is not UNSET:
            field_dict["isIncluded"] = is_included
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_identity is not UNSET:
            field_dict["partIdentity"] = part_identity
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if properties is not UNSET:
            field_dict["properties"] = properties
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_property_value_param import BTPropertyValueParam

        d = dict(src_dict)
        configuration = d.pop("configuration", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_type = d.pop("elementType", UNSET)

        flat_part_id = d.pop("flatPartId", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        is_included = d.pop("isIncluded", UNSET)

        parent_id = d.pop("parentId", UNSET)

        part_id = d.pop("partId", UNSET)

        part_identity = d.pop("partIdentity", UNSET)

        part_number = d.pop("partNumber", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[BTPropertyValueParam] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = BTPropertyValueParam.from_dict(properties_item_data)

                properties.append(properties_item)

        revision_id = d.pop("revisionId", UNSET)

        version_id = d.pop("versionId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_release_package_item_params = cls(
            configuration=configuration,
            document_id=document_id,
            element_id=element_id,
            element_type=element_type,
            flat_part_id=flat_part_id,
            href=href,
            id=id,
            is_included=is_included,
            parent_id=parent_id,
            part_id=part_id,
            part_identity=part_identity,
            part_number=part_number,
            properties=properties,
            revision_id=revision_id,
            version_id=version_id,
            workspace_id=workspace_id,
        )

        bt_release_package_item_params.additional_properties = d
        return bt_release_package_item_params

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
