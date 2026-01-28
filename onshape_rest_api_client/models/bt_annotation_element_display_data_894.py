from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_annotation_element_display_data_894_annotation_id_to_display_object import (
        BTAnnotationElementDisplayData894AnnotationIdToDisplayObject,
    )


T = TypeVar("T", bound="BTAnnotationElementDisplayData894")


@_attrs_define
class BTAnnotationElementDisplayData894:
    """
    Attributes:
        annotation_id_to_display_object (BTAnnotationElementDisplayData894AnnotationIdToDisplayObject | Unset):
        annotation_ids (list[str] | Unset):
        bt_type (str | Unset): Type of JSON object.
    """

    annotation_id_to_display_object: BTAnnotationElementDisplayData894AnnotationIdToDisplayObject | Unset = UNSET
    annotation_ids: list[str] | Unset = UNSET
    bt_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotation_id_to_display_object: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotation_id_to_display_object, Unset):
            annotation_id_to_display_object = self.annotation_id_to_display_object.to_dict()

        annotation_ids: list[str] | Unset = UNSET
        if not isinstance(self.annotation_ids, Unset):
            annotation_ids = self.annotation_ids

        bt_type = self.bt_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotation_id_to_display_object is not UNSET:
            field_dict["annotationIdToDisplayObject"] = annotation_id_to_display_object
        if annotation_ids is not UNSET:
            field_dict["annotationIds"] = annotation_ids
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_annotation_element_display_data_894_annotation_id_to_display_object import (
            BTAnnotationElementDisplayData894AnnotationIdToDisplayObject,
        )

        d = dict(src_dict)
        _annotation_id_to_display_object = d.pop("annotationIdToDisplayObject", UNSET)
        annotation_id_to_display_object: BTAnnotationElementDisplayData894AnnotationIdToDisplayObject | Unset
        if isinstance(_annotation_id_to_display_object, Unset):
            annotation_id_to_display_object = UNSET
        else:
            annotation_id_to_display_object = BTAnnotationElementDisplayData894AnnotationIdToDisplayObject.from_dict(
                _annotation_id_to_display_object
            )

        annotation_ids = cast(list[str], d.pop("annotationIds", UNSET))

        bt_type = d.pop("btType", UNSET)

        bt_annotation_element_display_data_894 = cls(
            annotation_id_to_display_object=annotation_id_to_display_object,
            annotation_ids=annotation_ids,
            bt_type=bt_type,
        )

        bt_annotation_element_display_data_894.additional_properties = d
        return bt_annotation_element_display_data_894

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
