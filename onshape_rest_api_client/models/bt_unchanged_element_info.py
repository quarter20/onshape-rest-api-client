from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_unchanged_reference_info import BTUnchangedReferenceInfo


T = TypeVar("T", bound="BTUnchangedElementInfo")


@_attrs_define
class BTUnchangedElementInfo:
    """
    Attributes:
        connection_id (str | Unset):
        element_id (str | Unset):
        unchanged_references (list[BTUnchangedReferenceInfo] | Unset):
    """

    connection_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    unchanged_references: list[BTUnchangedReferenceInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        element_id = self.element_id

        unchanged_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unchanged_references, Unset):
            unchanged_references = []
            for unchanged_references_item_data in self.unchanged_references:
                unchanged_references_item = unchanged_references_item_data.to_dict()
                unchanged_references.append(unchanged_references_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if unchanged_references is not UNSET:
            field_dict["unchangedReferences"] = unchanged_references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_unchanged_reference_info import BTUnchangedReferenceInfo

        d = dict(src_dict)
        connection_id = d.pop("connectionId", UNSET)

        element_id = d.pop("elementId", UNSET)

        _unchanged_references = d.pop("unchangedReferences", UNSET)
        unchanged_references: list[BTUnchangedReferenceInfo] | Unset = UNSET
        if _unchanged_references is not UNSET:
            unchanged_references = []
            for unchanged_references_item_data in _unchanged_references:
                unchanged_references_item = BTUnchangedReferenceInfo.from_dict(unchanged_references_item_data)

                unchanged_references.append(unchanged_references_item)

        bt_unchanged_element_info = cls(
            connection_id=connection_id,
            element_id=element_id,
            unchanged_references=unchanged_references,
        )

        bt_unchanged_element_info.additional_properties = d
        return bt_unchanged_element_info

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
