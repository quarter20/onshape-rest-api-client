from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_metadata_property_update_params_value import BTMetadataPropertyUpdateParamsValue


T = TypeVar("T", bound="BTMetadataPropertyUpdateParams")


@_attrs_define
class BTMetadataPropertyUpdateParams:
    """
    Attributes:
        property_id (str | Unset): The id of the property that should be edited. This can be retrieved from
            MetadataCategory:getCategoryProperties.
        value (BTMetadataPropertyUpdateParamsValue | Unset): The new value for the property.
    """

    property_id: str | Unset = UNSET
    value: BTMetadataPropertyUpdateParamsValue | Unset = UNSET
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
        from ..models.bt_metadata_property_update_params_value import BTMetadataPropertyUpdateParamsValue

        d = dict(src_dict)
        property_id = d.pop("propertyId", UNSET)

        _value = d.pop("value", UNSET)
        value: BTMetadataPropertyUpdateParamsValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = BTMetadataPropertyUpdateParamsValue.from_dict(_value)

        bt_metadata_property_update_params = cls(
            property_id=property_id,
            value=value,
        )

        bt_metadata_property_update_params.additional_properties = d
        return bt_metadata_property_update_params

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
