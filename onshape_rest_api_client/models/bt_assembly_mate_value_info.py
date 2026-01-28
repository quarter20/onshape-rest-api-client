from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAssemblyMateValueInfo")


@_attrs_define
class BTAssemblyMateValueInfo:
    """Quantities for length are specified in meters, and quantities for angles are specified in radians.

    Attributes:
        json_type (str):
        feature_id (str | Unset): The ID of the assembly mate feature.
        mate_name (str | Unset): The name of the assembly mate feature.
    """

    json_type: str
    feature_id: str | Unset = UNSET
    mate_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_type = self.json_type

        feature_id = self.feature_id

        mate_name = self.mate_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonType": json_type,
            }
        )
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if mate_name is not UNSET:
            field_dict["mateName"] = mate_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        json_type = d.pop("jsonType")

        feature_id = d.pop("featureId", UNSET)

        mate_name = d.pop("mateName", UNSET)

        bt_assembly_mate_value_info = cls(
            json_type=json_type,
            feature_id=feature_id,
            mate_name=mate_name,
        )

        bt_assembly_mate_value_info.additional_properties = d
        return bt_assembly_mate_value_info

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
