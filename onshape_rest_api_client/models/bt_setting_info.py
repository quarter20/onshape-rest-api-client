from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_setting_info_value import BTSettingInfoValue


T = TypeVar("T", bound="BTSettingInfo")


@_attrs_define
class BTSettingInfo:
    """
    Attributes:
        key (str | Unset):
        value (BTSettingInfoValue | Unset):
    """

    key: str | Unset = UNSET
    value: BTSettingInfoValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_setting_info_value import BTSettingInfoValue

        d = dict(src_dict)
        key = d.pop("key", UNSET)

        _value = d.pop("value", UNSET)
        value: BTSettingInfoValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = BTSettingInfoValue.from_dict(_value)

        bt_setting_info = cls(
            key=key,
            value=value,
        )

        bt_setting_info.additional_properties = d
        return bt_setting_info

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
