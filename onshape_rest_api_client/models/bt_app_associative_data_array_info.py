from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_app_element_error_code import BTAppElementErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_associative_data_info import BTAssociativeDataInfo


T = TypeVar("T", bound="BTAppAssociativeDataArrayInfo")


@_attrs_define
class BTAppAssociativeDataArrayInfo:
    """
    Attributes:
        change_id (str | Unset):
        error_code (int | Unset): `0: OK (healthy) | 1: INFO | 2: WARNING | 3: ERROR (dangling or view generation call
            failed) | 4: UNKNOWN`
        error_description (str | Unset): A human-readable value for the error that occurred, if one occurred.
        error_value (BTAppElementErrorCode | Unset):
        items (list[BTAssociativeDataInfo] | Unset):
        parent_change_id (str | Unset):
    """

    change_id: str | Unset = UNSET
    error_code: int | Unset = UNSET
    error_description: str | Unset = UNSET
    error_value: BTAppElementErrorCode | Unset = UNSET
    items: list[BTAssociativeDataInfo] | Unset = UNSET
    parent_change_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_id = self.change_id

        error_code = self.error_code

        error_description = self.error_description

        error_value: str | Unset = UNSET
        if not isinstance(self.error_value, Unset):
            error_value = self.error_value.value

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        parent_change_id = self.parent_change_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change_id is not UNSET:
            field_dict["changeId"] = change_id
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if error_value is not UNSET:
            field_dict["errorValue"] = error_value
        if items is not UNSET:
            field_dict["items"] = items
        if parent_change_id is not UNSET:
            field_dict["parentChangeId"] = parent_change_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_associative_data_info import BTAssociativeDataInfo

        d = dict(src_dict)
        change_id = d.pop("changeId", UNSET)

        error_code = d.pop("errorCode", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        _error_value = d.pop("errorValue", UNSET)
        error_value: BTAppElementErrorCode | Unset
        if isinstance(_error_value, Unset):
            error_value = UNSET
        else:
            error_value = BTAppElementErrorCode(_error_value)

        _items = d.pop("items", UNSET)
        items: list[BTAssociativeDataInfo] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = BTAssociativeDataInfo.from_dict(items_item_data)

                items.append(items_item)

        parent_change_id = d.pop("parentChangeId", UNSET)

        bt_app_associative_data_array_info = cls(
            change_id=change_id,
            error_code=error_code,
            error_description=error_description,
            error_value=error_value,
            items=items,
            parent_change_id=parent_change_id,
        )

        bt_app_associative_data_array_info.additional_properties = d
        return bt_app_associative_data_array_info

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
