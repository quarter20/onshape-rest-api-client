from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_metadata_state_type import BTMetadataStateType
from ..models.btapi_workflowable_type import BTAPIWorkflowableType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTObjectWorkflowInfo")


@_attrs_define
class BTObjectWorkflowInfo:
    """An workflowable object like Release or Task that supports states and transitions.

    Attributes:
        can_be_discarded (bool | Unset): Whether workflowable object can be discarded.
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        is_discarded (bool | Unset): Whether workflowable object has been discarded.
        is_frozen (bool | Unset): Whether workflowable object has reached terminal state and is frozen.
        metadata_state (BTMetadataStateType | Unset): The current state metadata values if applicable.
        name (str | Unset): Name of the resource.
        object_type (BTAPIWorkflowableType | Unset): All workflowable types that can be enumerated.
        state_id (str | Unset): The current state of object like SETUP, REJECTED etc. Custom workflows can have any
            declared state.
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        workflow_id (str | Unset): The workflow definition id that governs this object's states and transitions.
    """

    can_be_discarded: bool | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    is_discarded: bool | Unset = UNSET
    is_frozen: bool | Unset = UNSET
    metadata_state: BTMetadataStateType | Unset = UNSET
    name: str | Unset = UNSET
    object_type: BTAPIWorkflowableType | Unset = UNSET
    state_id: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_be_discarded = self.can_be_discarded

        href = self.href

        id = self.id

        is_discarded = self.is_discarded

        is_frozen = self.is_frozen

        metadata_state: str | Unset = UNSET
        if not isinstance(self.metadata_state, Unset):
            metadata_state = self.metadata_state.value

        name = self.name

        object_type: str | Unset = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        state_id = self.state_id

        view_ref = self.view_ref

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_be_discarded is not UNSET:
            field_dict["canBeDiscarded"] = can_be_discarded
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if is_discarded is not UNSET:
            field_dict["isDiscarded"] = is_discarded
        if is_frozen is not UNSET:
            field_dict["isFrozen"] = is_frozen
        if metadata_state is not UNSET:
            field_dict["metadataState"] = metadata_state
        if name is not UNSET:
            field_dict["name"] = name
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if state_id is not UNSET:
            field_dict["stateId"] = state_id
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_be_discarded = d.pop("canBeDiscarded", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        is_discarded = d.pop("isDiscarded", UNSET)

        is_frozen = d.pop("isFrozen", UNSET)

        _metadata_state = d.pop("metadataState", UNSET)
        metadata_state: BTMetadataStateType | Unset
        if isinstance(_metadata_state, Unset):
            metadata_state = UNSET
        else:
            metadata_state = BTMetadataStateType(_metadata_state)

        name = d.pop("name", UNSET)

        _object_type = d.pop("objectType", UNSET)
        object_type: BTAPIWorkflowableType | Unset
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = BTAPIWorkflowableType(_object_type)

        state_id = d.pop("stateId", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        workflow_id = d.pop("workflowId", UNSET)

        bt_object_workflow_info = cls(
            can_be_discarded=can_be_discarded,
            href=href,
            id=id,
            is_discarded=is_discarded,
            is_frozen=is_frozen,
            metadata_state=metadata_state,
            name=name,
            object_type=object_type,
            state_id=state_id,
            view_ref=view_ref,
            workflow_id=workflow_id,
        )

        bt_object_workflow_info.additional_properties = d
        return bt_object_workflow_info

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
