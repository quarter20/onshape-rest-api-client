from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_metadata_value_type import BTMetadataValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTSimplePropertyInfo")


@_attrs_define
class BTSimplePropertyInfo:
    """
    Attributes:
        display_name (str | Unset):
        frozen (bool | Unset):
        property_id (str | Unset):
        publish_state (int | Unset):
        value_type (BTMetadataValueType | Unset):
    """

    display_name: str | Unset = UNSET
    frozen: bool | Unset = UNSET
    property_id: str | Unset = UNSET
    publish_state: int | Unset = UNSET
    value_type: BTMetadataValueType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        frozen = self.frozen

        property_id = self.property_id

        publish_state = self.publish_state

        value_type: str | Unset = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if frozen is not UNSET:
            field_dict["frozen"] = frozen
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if publish_state is not UNSET:
            field_dict["publishState"] = publish_state
        if value_type is not UNSET:
            field_dict["valueType"] = value_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        frozen = d.pop("frozen", UNSET)

        property_id = d.pop("propertyId", UNSET)

        publish_state = d.pop("publishState", UNSET)

        _value_type = d.pop("valueType", UNSET)
        value_type: BTMetadataValueType | Unset
        if isinstance(_value_type, Unset):
            value_type = UNSET
        else:
            value_type = BTMetadataValueType(_value_type)

        bt_simple_property_info = cls(
            display_name=display_name,
            frozen=frozen,
            property_id=property_id,
            publish_state=publish_state,
            value_type=value_type,
        )

        bt_simple_property_info.additional_properties = d
        return bt_simple_property_info

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
