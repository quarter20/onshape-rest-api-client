from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_annotation_type import GBTAnnotationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAnnotationFilter4841")


@_attrs_define
class BTAnnotationFilter4841:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        annotation_type (GBTAnnotationType | Unset):
    """

    bt_type: str | Unset = UNSET
    annotation_type: GBTAnnotationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        annotation_type: str | Unset = UNSET
        if not isinstance(self.annotation_type, Unset):
            annotation_type = self.annotation_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if annotation_type is not UNSET:
            field_dict["annotationType"] = annotation_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _annotation_type = d.pop("annotationType", UNSET)
        annotation_type: GBTAnnotationType | Unset
        if isinstance(_annotation_type, Unset):
            annotation_type = UNSET
        else:
            annotation_type = GBTAnnotationType(_annotation_type)

        bt_annotation_filter_4841 = cls(
            bt_type=bt_type,
            annotation_type=annotation_type,
        )

        bt_annotation_filter_4841.additional_properties = d
        return bt_annotation_filter_4841

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
