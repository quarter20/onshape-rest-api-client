from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_value_use import GBTValueUse
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btfs_value_1888 import BTFSValue1888


T = TypeVar("T", bound="BTValueAndUse4696")


@_attrs_define
class BTValueAndUse4696:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        use (GBTValueUse | Unset):
        value (BTFSValue1888 | Unset):
    """

    bt_type: str | Unset = UNSET
    use: GBTValueUse | Unset = UNSET
    value: BTFSValue1888 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        use: str | Unset = UNSET
        if not isinstance(self.use, Unset):
            use = self.use.value

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if use is not UNSET:
            field_dict["use"] = use
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btfs_value_1888 import BTFSValue1888

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _use = d.pop("use", UNSET)
        use: GBTValueUse | Unset
        if isinstance(_use, Unset):
            use = UNSET
        else:
            use = GBTValueUse(_use)

        _value = d.pop("value", UNSET)
        value: BTFSValue1888 | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = BTFSValue1888.from_dict(_value)

        bt_value_and_use_4696 = cls(
            bt_type=bt_type,
            use=use,
            value=value,
        )

        bt_value_and_use_4696.additional_properties = d
        return bt_value_and_use_4696

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
