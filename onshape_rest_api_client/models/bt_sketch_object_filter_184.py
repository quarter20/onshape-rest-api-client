from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sketch_object_type import GBTSketchObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTSketchObjectFilter184")


@_attrs_define
class BTSketchObjectFilter184:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        is_sketch_object (bool | Unset):
        object_type (GBTSketchObjectType | Unset):
    """

    bt_type: str | Unset = UNSET
    is_sketch_object: bool | Unset = UNSET
    object_type: GBTSketchObjectType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        is_sketch_object = self.is_sketch_object

        object_type: str | Unset = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if is_sketch_object is not UNSET:
            field_dict["isSketchObject"] = is_sketch_object
        if object_type is not UNSET:
            field_dict["objectType"] = object_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        is_sketch_object = d.pop("isSketchObject", UNSET)

        _object_type = d.pop("objectType", UNSET)
        object_type: GBTSketchObjectType | Unset
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = GBTSketchObjectType(_object_type)

        bt_sketch_object_filter_184 = cls(
            bt_type=bt_type,
            is_sketch_object=is_sketch_object,
            object_type=object_type,
        )

        bt_sketch_object_filter_184.additional_properties = d
        return bt_sketch_object_filter_184

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
