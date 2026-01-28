from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_diff_info_collection_type import BTDiffInfoCollectionType
from ..models.gbt_node_change import GBTNodeChange
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_root_diff_info_changes import BTRootDiffInfoChanges
    from ..models.bt_root_diff_info_collection_changes import BTRootDiffInfoCollectionChanges


T = TypeVar("T", bound="BTRootDiffInfo")


@_attrs_define
class BTRootDiffInfo:
    """
    Attributes:
        changes (BTRootDiffInfoChanges | Unset):
        collection_changes (BTRootDiffInfoCollectionChanges | Unset):
        entity_type (BTDiffInfoCollectionType | Unset):
        geometry_change_messages (list[str] | Unset):
        source_configuration (str | Unset):
        source_id (str | Unset):
        source_microversion_id (str | Unset):
        source_value (str | Unset):
        source_version_id (str | Unset):
        source_workspace_id (str | Unset):
        target_configuration (str | Unset):
        target_id (str | Unset):
        target_microversion_id (str | Unset):
        target_value (str | Unset):
        target_version_id (str | Unset):
        target_workspace_id (str | Unset):
        type_ (GBTNodeChange | Unset):
    """

    changes: BTRootDiffInfoChanges | Unset = UNSET
    collection_changes: BTRootDiffInfoCollectionChanges | Unset = UNSET
    entity_type: BTDiffInfoCollectionType | Unset = UNSET
    geometry_change_messages: list[str] | Unset = UNSET
    source_configuration: str | Unset = UNSET
    source_id: str | Unset = UNSET
    source_microversion_id: str | Unset = UNSET
    source_value: str | Unset = UNSET
    source_version_id: str | Unset = UNSET
    source_workspace_id: str | Unset = UNSET
    target_configuration: str | Unset = UNSET
    target_id: str | Unset = UNSET
    target_microversion_id: str | Unset = UNSET
    target_value: str | Unset = UNSET
    target_version_id: str | Unset = UNSET
    target_workspace_id: str | Unset = UNSET
    type_: GBTNodeChange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = self.changes.to_dict()

        collection_changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.collection_changes, Unset):
            collection_changes = self.collection_changes.to_dict()

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        geometry_change_messages: list[str] | Unset = UNSET
        if not isinstance(self.geometry_change_messages, Unset):
            geometry_change_messages = self.geometry_change_messages

        source_configuration = self.source_configuration

        source_id = self.source_id

        source_microversion_id = self.source_microversion_id

        source_value = self.source_value

        source_version_id = self.source_version_id

        source_workspace_id = self.source_workspace_id

        target_configuration = self.target_configuration

        target_id = self.target_id

        target_microversion_id = self.target_microversion_id

        target_value = self.target_value

        target_version_id = self.target_version_id

        target_workspace_id = self.target_workspace_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changes is not UNSET:
            field_dict["changes"] = changes
        if collection_changes is not UNSET:
            field_dict["collectionChanges"] = collection_changes
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if geometry_change_messages is not UNSET:
            field_dict["geometryChangeMessages"] = geometry_change_messages
        if source_configuration is not UNSET:
            field_dict["sourceConfiguration"] = source_configuration
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if source_microversion_id is not UNSET:
            field_dict["sourceMicroversionId"] = source_microversion_id
        if source_value is not UNSET:
            field_dict["sourceValue"] = source_value
        if source_version_id is not UNSET:
            field_dict["sourceVersionId"] = source_version_id
        if source_workspace_id is not UNSET:
            field_dict["sourceWorkspaceId"] = source_workspace_id
        if target_configuration is not UNSET:
            field_dict["targetConfiguration"] = target_configuration
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if target_microversion_id is not UNSET:
            field_dict["targetMicroversionId"] = target_microversion_id
        if target_value is not UNSET:
            field_dict["targetValue"] = target_value
        if target_version_id is not UNSET:
            field_dict["targetVersionId"] = target_version_id
        if target_workspace_id is not UNSET:
            field_dict["targetWorkspaceId"] = target_workspace_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_root_diff_info_changes import BTRootDiffInfoChanges
        from ..models.bt_root_diff_info_collection_changes import BTRootDiffInfoCollectionChanges

        d = dict(src_dict)
        _changes = d.pop("changes", UNSET)
        changes: BTRootDiffInfoChanges | Unset
        if isinstance(_changes, Unset):
            changes = UNSET
        else:
            changes = BTRootDiffInfoChanges.from_dict(_changes)

        _collection_changes = d.pop("collectionChanges", UNSET)
        collection_changes: BTRootDiffInfoCollectionChanges | Unset
        if isinstance(_collection_changes, Unset):
            collection_changes = UNSET
        else:
            collection_changes = BTRootDiffInfoCollectionChanges.from_dict(_collection_changes)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: BTDiffInfoCollectionType | Unset
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = BTDiffInfoCollectionType(_entity_type)

        geometry_change_messages = cast(list[str], d.pop("geometryChangeMessages", UNSET))

        source_configuration = d.pop("sourceConfiguration", UNSET)

        source_id = d.pop("sourceId", UNSET)

        source_microversion_id = d.pop("sourceMicroversionId", UNSET)

        source_value = d.pop("sourceValue", UNSET)

        source_version_id = d.pop("sourceVersionId", UNSET)

        source_workspace_id = d.pop("sourceWorkspaceId", UNSET)

        target_configuration = d.pop("targetConfiguration", UNSET)

        target_id = d.pop("targetId", UNSET)

        target_microversion_id = d.pop("targetMicroversionId", UNSET)

        target_value = d.pop("targetValue", UNSET)

        target_version_id = d.pop("targetVersionId", UNSET)

        target_workspace_id = d.pop("targetWorkspaceId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GBTNodeChange | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GBTNodeChange(_type_)

        bt_root_diff_info = cls(
            changes=changes,
            collection_changes=collection_changes,
            entity_type=entity_type,
            geometry_change_messages=geometry_change_messages,
            source_configuration=source_configuration,
            source_id=source_id,
            source_microversion_id=source_microversion_id,
            source_value=source_value,
            source_version_id=source_version_id,
            source_workspace_id=source_workspace_id,
            target_configuration=target_configuration,
            target_id=target_id,
            target_microversion_id=target_microversion_id,
            target_value=target_value,
            target_version_id=target_version_id,
            target_workspace_id=target_workspace_id,
            type_=type_,
        )

        bt_root_diff_info.additional_properties = d
        return bt_root_diff_info

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
