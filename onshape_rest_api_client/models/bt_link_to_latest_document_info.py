from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTLinkToLatestDocumentInfo")


@_attrs_define
class BTLinkToLatestDocumentInfo:
    """
    Attributes:
        changed_elements (list[str] | Unset):
    """

    changed_elements: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed_elements: list[str] | Unset = UNSET
        if not isinstance(self.changed_elements, Unset):
            changed_elements = self.changed_elements

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changed_elements is not UNSET:
            field_dict["changedElements"] = changed_elements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        changed_elements = cast(list[str], d.pop("changedElements", UNSET))

        bt_link_to_latest_document_info = cls(
            changed_elements=changed_elements,
        )

        bt_link_to_latest_document_info.additional_properties = d
        return bt_link_to_latest_document_info

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
