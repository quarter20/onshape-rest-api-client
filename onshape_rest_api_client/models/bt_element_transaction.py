from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTElementTransaction")


@_attrs_define
class BTElementTransaction:
    """
    Attributes:
        description (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        id (str | Unset):
        microbranch_id (str | Unset):
        workspace_id (str | Unset):
    """

    description: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    id: str | Unset = UNSET
    microbranch_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        document_id = self.document_id

        element_id = self.element_id

        id = self.id

        microbranch_id = self.microbranch_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if id is not UNSET:
            field_dict["id"] = id
        if microbranch_id is not UNSET:
            field_dict["microbranchId"] = microbranch_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        id = d.pop("id", UNSET)

        microbranch_id = d.pop("microbranchId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_element_transaction = cls(
            description=description,
            document_id=document_id,
            element_id=element_id,
            id=id,
            microbranch_id=microbranch_id,
            workspace_id=workspace_id,
        )

        bt_element_transaction.additional_properties = d
        return bt_element_transaction

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
