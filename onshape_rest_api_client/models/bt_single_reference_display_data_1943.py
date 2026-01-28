from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_error_string_enum import GBTErrorStringEnum
from ..models.gbtbs_feature_visibility import GBTBSFeatureVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_full_element_id_756 import BTFullElementId756


T = TypeVar("T", bound="BTSingleReferenceDisplayData1943")


@_attrs_define
class BTSingleReferenceDisplayData1943:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        context_workspace_id (str | Unset):
        document_id (str | Unset):
        error (GBTErrorStringEnum | Unset):
        error_message (str | Unset):
        full_element_id (BTFullElementId756 | Unset):
        is_transient (bool | Unset):
        name (str | Unset):
        reference_name (str | Unset):
        reference_node_id (str | Unset):
        visibility (GBTBSFeatureVisibility | Unset):
    """

    bt_type: str | Unset = UNSET
    context_workspace_id: str | Unset = UNSET
    document_id: str | Unset = UNSET
    error: GBTErrorStringEnum | Unset = UNSET
    error_message: str | Unset = UNSET
    full_element_id: BTFullElementId756 | Unset = UNSET
    is_transient: bool | Unset = UNSET
    name: str | Unset = UNSET
    reference_name: str | Unset = UNSET
    reference_node_id: str | Unset = UNSET
    visibility: GBTBSFeatureVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        context_workspace_id = self.context_workspace_id

        document_id = self.document_id

        error: str | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.value

        error_message = self.error_message

        full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id, Unset):
            full_element_id = self.full_element_id.to_dict()

        is_transient = self.is_transient

        name = self.name

        reference_name = self.reference_name

        reference_node_id = self.reference_node_id

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if context_workspace_id is not UNSET:
            field_dict["contextWorkspaceId"] = context_workspace_id
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if error is not UNSET:
            field_dict["error"] = error
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if full_element_id is not UNSET:
            field_dict["fullElementId"] = full_element_id
        if is_transient is not UNSET:
            field_dict["isTransient"] = is_transient
        if name is not UNSET:
            field_dict["name"] = name
        if reference_name is not UNSET:
            field_dict["referenceName"] = reference_name
        if reference_node_id is not UNSET:
            field_dict["referenceNodeId"] = reference_node_id
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_full_element_id_756 import BTFullElementId756

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        context_workspace_id = d.pop("contextWorkspaceId", UNSET)

        document_id = d.pop("documentId", UNSET)

        _error = d.pop("error", UNSET)
        error: GBTErrorStringEnum | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = GBTErrorStringEnum(_error)

        error_message = d.pop("errorMessage", UNSET)

        _full_element_id = d.pop("fullElementId", UNSET)
        full_element_id: BTFullElementId756 | Unset
        if isinstance(_full_element_id, Unset):
            full_element_id = UNSET
        else:
            full_element_id = BTFullElementId756.from_dict(_full_element_id)

        is_transient = d.pop("isTransient", UNSET)

        name = d.pop("name", UNSET)

        reference_name = d.pop("referenceName", UNSET)

        reference_node_id = d.pop("referenceNodeId", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: GBTBSFeatureVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = GBTBSFeatureVisibility(_visibility)

        bt_single_reference_display_data_1943 = cls(
            bt_type=bt_type,
            context_workspace_id=context_workspace_id,
            document_id=document_id,
            error=error,
            error_message=error_message,
            full_element_id=full_element_id,
            is_transient=is_transient,
            name=name,
            reference_name=reference_name,
            reference_node_id=reference_node_id,
            visibility=visibility,
        )

        bt_single_reference_display_data_1943.additional_properties = d
        return bt_single_reference_display_data_1943

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
