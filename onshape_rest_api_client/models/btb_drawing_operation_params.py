from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btb_drawing_operation_params_other_fields import BTBDrawingOperationParamsOtherFields


T = TypeVar("T", bound="BTBDrawingOperationParams")


@_attrs_define
class BTBDrawingOperationParams:
    """A single drawing entity creation or modification definition

    Attributes:
        format_version (str): Version of drawing entity format. Example: 2021-01-01.
        message_name (str): Type of drawing modification operation: `onshapeCreateAnnotations` |
            `onshapeEditAnnotations` Example: onshapeCreateAnnotations.
        description (str | Unset): Operation description Example: Replicate annotations.
        other_fields (BTBDrawingOperationParamsOtherFields | Unset): Other entity creation or modification parameters.
    """

    format_version: str
    message_name: str
    description: str | Unset = UNSET
    other_fields: BTBDrawingOperationParamsOtherFields | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_version = self.format_version

        message_name = self.message_name

        description = self.description

        other_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_fields, Unset):
            other_fields = self.other_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formatVersion": format_version,
                "messageName": message_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if other_fields is not UNSET:
            field_dict["otherFields"] = other_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btb_drawing_operation_params_other_fields import BTBDrawingOperationParamsOtherFields

        d = dict(src_dict)
        format_version = d.pop("formatVersion")

        message_name = d.pop("messageName")

        description = d.pop("description", UNSET)

        _other_fields = d.pop("otherFields", UNSET)
        other_fields: BTBDrawingOperationParamsOtherFields | Unset
        if isinstance(_other_fields, Unset):
            other_fields = UNSET
        else:
            other_fields = BTBDrawingOperationParamsOtherFields.from_dict(_other_fields)

        btb_drawing_operation_params = cls(
            format_version=format_version,
            message_name=message_name,
            description=description,
            other_fields=other_fields,
        )

        btb_drawing_operation_params.additional_properties = d
        return btb_drawing_operation_params

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
