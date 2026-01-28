from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_configured_value import BTConfiguredValue


T = TypeVar("T", bound="BTOptionallyConfiguredValue")


@_attrs_define
class BTOptionallyConfiguredValue:
    """Optional map of configuration parameter id to value

    Attributes:
        configured_value (BTConfiguredValue | Unset): Configured variable description, if configured
        value (str | Unset): The string value, if not configured
    """

    configured_value: BTConfiguredValue | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configured_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configured_value, Unset):
            configured_value = self.configured_value.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configured_value is not UNSET:
            field_dict["configuredValue"] = configured_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_configured_value import BTConfiguredValue

        d = dict(src_dict)
        _configured_value = d.pop("configuredValue", UNSET)
        configured_value: BTConfiguredValue | Unset
        if isinstance(_configured_value, Unset):
            configured_value = UNSET
        else:
            configured_value = BTConfiguredValue.from_dict(_configured_value)

        value = d.pop("value", UNSET)

        bt_optionally_configured_value = cls(
            configured_value=configured_value,
            value=value,
        )

        bt_optionally_configured_value.additional_properties = d
        return bt_optionally_configured_value

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
