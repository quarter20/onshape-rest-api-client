from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_app_element_view_geometry_properties_1100_property_to_value import (
        BTAppElementViewGeometryProperties1100PropertyToValue,
    )


T = TypeVar("T", bound="BTAppElementViewGeometryProperties1100")


@_attrs_define
class BTAppElementViewGeometryProperties1100:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        property_to_value (BTAppElementViewGeometryProperties1100PropertyToValue | Unset):
    """

    bt_type: str | Unset = UNSET
    property_to_value: BTAppElementViewGeometryProperties1100PropertyToValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        property_to_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_to_value, Unset):
            property_to_value = self.property_to_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if property_to_value is not UNSET:
            field_dict["propertyToValue"] = property_to_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_app_element_view_geometry_properties_1100_property_to_value import (
            BTAppElementViewGeometryProperties1100PropertyToValue,
        )

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _property_to_value = d.pop("propertyToValue", UNSET)
        property_to_value: BTAppElementViewGeometryProperties1100PropertyToValue | Unset
        if isinstance(_property_to_value, Unset):
            property_to_value = UNSET
        else:
            property_to_value = BTAppElementViewGeometryProperties1100PropertyToValue.from_dict(_property_to_value)

        bt_app_element_view_geometry_properties_1100 = cls(
            bt_type=bt_type,
            property_to_value=property_to_value,
        )

        bt_app_element_view_geometry_properties_1100.additional_properties = d
        return bt_app_element_view_geometry_properties_1100

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
