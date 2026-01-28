from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_app_element_error_code import BTAppElementErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_app_element_content_entry_info import BTAppElementContentEntryInfo


T = TypeVar("T", bound="BTAppElementContentInfo")


@_attrs_define
class BTAppElementContentInfo:
    """
    Attributes:
        change_id (str | Unset):
        data (list[BTAppElementContentEntryInfo] | Unset):
        error_code (int | Unset): `0: OK (healthy) | 1: INFO | 2: WARNING | 3: ERROR (dangling or view generation call
            failed) | 4: UNKNOWN`
        error_description (str | Unset): A human-readable value for the error that occurred, if one occurred.
        error_value (BTAppElementErrorCode | Unset):
    """

    change_id: str | Unset = UNSET
    data: list[BTAppElementContentEntryInfo] | Unset = UNSET
    error_code: int | Unset = UNSET
    error_description: str | Unset = UNSET
    error_value: BTAppElementErrorCode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_id = self.change_id

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        error_code = self.error_code

        error_description = self.error_description

        error_value: str | Unset = UNSET
        if not isinstance(self.error_value, Unset):
            error_value = self.error_value.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change_id is not UNSET:
            field_dict["changeId"] = change_id
        if data is not UNSET:
            field_dict["data"] = data
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if error_value is not UNSET:
            field_dict["errorValue"] = error_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_app_element_content_entry_info import BTAppElementContentEntryInfo

        d = dict(src_dict)
        change_id = d.pop("changeId", UNSET)

        _data = d.pop("data", UNSET)
        data: list[BTAppElementContentEntryInfo] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = BTAppElementContentEntryInfo.from_dict(data_item_data)

                data.append(data_item)

        error_code = d.pop("errorCode", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        _error_value = d.pop("errorValue", UNSET)
        error_value: BTAppElementErrorCode | Unset
        if isinstance(_error_value, Unset):
            error_value = UNSET
        else:
            error_value = BTAppElementErrorCode(_error_value)

        bt_app_element_content_info = cls(
            change_id=change_id,
            data=data,
            error_code=error_code,
            error_description=error_description,
            error_value=error_value,
        )

        bt_app_element_content_info.additional_properties = d
        return bt_app_element_content_info

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
