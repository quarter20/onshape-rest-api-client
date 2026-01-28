from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_user_app_setting_operation_type import BTUserAppSettingOperationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_setting_param_value import BTSettingParamValue


T = TypeVar("T", bound="BTSettingParam")


@_attrs_define
class BTSettingParam:
    """
    Attributes:
        field (str | Unset):
        key (str | Unset):
        operation (BTUserAppSettingOperationType | Unset):
        value (BTSettingParamValue | Unset):
    """

    field: str | Unset = UNSET
    key: str | Unset = UNSET
    operation: BTUserAppSettingOperationType | Unset = UNSET
    value: BTSettingParamValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        key = self.key

        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if key is not UNSET:
            field_dict["key"] = key
        if operation is not UNSET:
            field_dict["operation"] = operation
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_setting_param_value import BTSettingParamValue

        d = dict(src_dict)
        field = d.pop("field", UNSET)

        key = d.pop("key", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: BTUserAppSettingOperationType | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = BTUserAppSettingOperationType(_operation)

        _value = d.pop("value", UNSET)
        value: BTSettingParamValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = BTSettingParamValue.from_dict(_value)

        bt_setting_param = cls(
            field=field,
            key=key,
            operation=operation,
            value=value,
        )

        bt_setting_param.additional_properties = d
        return bt_setting_param

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
