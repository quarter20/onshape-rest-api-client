from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTVersionOrWorkspaceParams")


@_attrs_define
class BTVersionOrWorkspaceParams:
    """
    Attributes:
        client_interaction_mode (str | Unset):
        description (str | Unset):
        document_id (str | Unset):
        from_history (bool | Unset):
        is_release (bool | Unset):
        microversion_id (str | Unset):
        missing_bom_table_template_id (str | Unset):
        name (str | Unset):
        publish_version (bool | Unset): Publish FeatureScript at this version. Default: False.
        purpose (int | Unset):
        read_only (bool | Unset):
        version_id (str | Unset):
        workspace_id (str | Unset):
    """

    client_interaction_mode: str | Unset = UNSET
    description: str | Unset = UNSET
    document_id: str | Unset = UNSET
    from_history: bool | Unset = UNSET
    is_release: bool | Unset = UNSET
    microversion_id: str | Unset = UNSET
    missing_bom_table_template_id: str | Unset = UNSET
    name: str | Unset = UNSET
    publish_version: bool | Unset = False
    purpose: int | Unset = UNSET
    read_only: bool | Unset = UNSET
    version_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_interaction_mode = self.client_interaction_mode

        description = self.description

        document_id = self.document_id

        from_history = self.from_history

        is_release = self.is_release

        microversion_id = self.microversion_id

        missing_bom_table_template_id = self.missing_bom_table_template_id

        name = self.name

        publish_version = self.publish_version

        purpose = self.purpose

        read_only = self.read_only

        version_id = self.version_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_interaction_mode is not UNSET:
            field_dict["clientInteractionMode"] = client_interaction_mode
        if description is not UNSET:
            field_dict["description"] = description
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if from_history is not UNSET:
            field_dict["fromHistory"] = from_history
        if is_release is not UNSET:
            field_dict["isRelease"] = is_release
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if missing_bom_table_template_id is not UNSET:
            field_dict["missingBomTableTemplateId"] = missing_bom_table_template_id
        if name is not UNSET:
            field_dict["name"] = name
        if publish_version is not UNSET:
            field_dict["publishVersion"] = publish_version
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_interaction_mode = d.pop("clientInteractionMode", UNSET)

        description = d.pop("description", UNSET)

        document_id = d.pop("documentId", UNSET)

        from_history = d.pop("fromHistory", UNSET)

        is_release = d.pop("isRelease", UNSET)

        microversion_id = d.pop("microversionId", UNSET)

        missing_bom_table_template_id = d.pop("missingBomTableTemplateId", UNSET)

        name = d.pop("name", UNSET)

        publish_version = d.pop("publishVersion", UNSET)

        purpose = d.pop("purpose", UNSET)

        read_only = d.pop("readOnly", UNSET)

        version_id = d.pop("versionId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_version_or_workspace_params = cls(
            client_interaction_mode=client_interaction_mode,
            description=description,
            document_id=document_id,
            from_history=from_history,
            is_release=is_release,
            microversion_id=microversion_id,
            missing_bom_table_template_id=missing_bom_table_template_id,
            name=name,
            publish_version=publish_version,
            purpose=purpose,
            read_only=read_only,
            version_id=version_id,
            workspace_id=workspace_id,
        )

        bt_version_or_workspace_params.additional_properties = d
        return bt_version_or_workspace_params

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
