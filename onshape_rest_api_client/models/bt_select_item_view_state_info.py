from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_document_selector_info import BTDocumentSelectorInfo


T = TypeVar("T", bound="BTSelectItemViewStateInfo")


@_attrs_define
class BTSelectItemViewStateInfo:
    """
    Attributes:
        active_selector_id (str | Unset):
        document_selectors (list[BTDocumentSelectorInfo] | Unset):
        purpose (str | Unset):
    """

    active_selector_id: str | Unset = UNSET
    document_selectors: list[BTDocumentSelectorInfo] | Unset = UNSET
    purpose: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_selector_id = self.active_selector_id

        document_selectors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.document_selectors, Unset):
            document_selectors = []
            for document_selectors_item_data in self.document_selectors:
                document_selectors_item = document_selectors_item_data.to_dict()
                document_selectors.append(document_selectors_item)

        purpose = self.purpose

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_selector_id is not UNSET:
            field_dict["activeSelectorId"] = active_selector_id
        if document_selectors is not UNSET:
            field_dict["documentSelectors"] = document_selectors
        if purpose is not UNSET:
            field_dict["purpose"] = purpose

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_document_selector_info import BTDocumentSelectorInfo

        d = dict(src_dict)
        active_selector_id = d.pop("activeSelectorId", UNSET)

        _document_selectors = d.pop("documentSelectors", UNSET)
        document_selectors: list[BTDocumentSelectorInfo] | Unset = UNSET
        if _document_selectors is not UNSET:
            document_selectors = []
            for document_selectors_item_data in _document_selectors:
                document_selectors_item = BTDocumentSelectorInfo.from_dict(document_selectors_item_data)

                document_selectors.append(document_selectors_item)

        purpose = d.pop("purpose", UNSET)

        bt_select_item_view_state_info = cls(
            active_selector_id=active_selector_id,
            document_selectors=document_selectors,
            purpose=purpose,
        )

        bt_select_item_view_state_info.additional_properties = d
        return bt_select_item_view_state_info

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
