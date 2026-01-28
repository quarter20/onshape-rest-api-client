from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_property_value_param_value import BTPropertyValueParamValue


T = TypeVar("T", bound="BTPropertyValueParam")


@_attrs_define
class BTPropertyValueParam:
    """
    Attributes:
        property_id (str | Unset): Id of the property to set.
        value (BTPropertyValueParamValue | Unset): Value to set for the property. User property values must be a list of
            `{ "id": "idValue" }` maps.
    """

    property_id: str | Unset = UNSET
    value: BTPropertyValueParamValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_id = self.property_id

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_property_value_param_value import BTPropertyValueParamValue

        d = dict(src_dict)
        property_id = d.pop("propertyId", UNSET)

        _value = d.pop("value", UNSET)
        value: BTPropertyValueParamValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = BTPropertyValueParamValue.from_dict(_value)

        bt_property_value_param = cls(
            property_id=property_id,
            value=value,
        )

        bt_property_value_param.additional_properties = d
        return bt_property_value_param

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
