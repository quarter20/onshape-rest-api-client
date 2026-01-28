from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTCopyElementParams")


@_attrs_define
class BTCopyElementParams:
    """
    Attributes:
        anchor_element_id (str | Unset):
        document_id_source (str | Unset):
        element_id_source (str | Unset):
        is_group_anchor (bool | Unset):
        workspace_id_source (str | Unset):
    """

    anchor_element_id: str | Unset = UNSET
    document_id_source: str | Unset = UNSET
    element_id_source: str | Unset = UNSET
    is_group_anchor: bool | Unset = UNSET
    workspace_id_source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anchor_element_id = self.anchor_element_id

        document_id_source = self.document_id_source

        element_id_source = self.element_id_source

        is_group_anchor = self.is_group_anchor

        workspace_id_source = self.workspace_id_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anchor_element_id is not UNSET:
            field_dict["anchorElementId"] = anchor_element_id
        if document_id_source is not UNSET:
            field_dict["documentIdSource"] = document_id_source
        if element_id_source is not UNSET:
            field_dict["elementIdSource"] = element_id_source
        if is_group_anchor is not UNSET:
            field_dict["isGroupAnchor"] = is_group_anchor
        if workspace_id_source is not UNSET:
            field_dict["workspaceIdSource"] = workspace_id_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        anchor_element_id = d.pop("anchorElementId", UNSET)

        document_id_source = d.pop("documentIdSource", UNSET)

        element_id_source = d.pop("elementIdSource", UNSET)

        is_group_anchor = d.pop("isGroupAnchor", UNSET)

        workspace_id_source = d.pop("workspaceIdSource", UNSET)

        bt_copy_element_params = cls(
            anchor_element_id=anchor_element_id,
            document_id_source=document_id_source,
            element_id_source=element_id_source,
            is_group_anchor=is_group_anchor,
            workspace_id_source=workspace_id_source,
        )

        bt_copy_element_params.additional_properties = d
        return bt_copy_element_params

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
