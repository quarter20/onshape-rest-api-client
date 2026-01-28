from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_constraint_type import GBTConstraintType
from ..models.gbt_sketch_entity_type import GBTSketchEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CombinedSketchEntityType")


@_attrs_define
class CombinedSketchEntityType:
    """
    Attributes:
        constraint_type (GBTConstraintType | Unset):
        entity_type (GBTSketchEntityType | Unset):
    """

    constraint_type: GBTConstraintType | Unset = UNSET
    entity_type: GBTSketchEntityType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constraint_type: str | Unset = UNSET
        if not isinstance(self.constraint_type, Unset):
            constraint_type = self.constraint_type.value

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constraint_type is not UNSET:
            field_dict["constraintType"] = constraint_type
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _constraint_type = d.pop("constraintType", UNSET)
        constraint_type: GBTConstraintType | Unset
        if isinstance(_constraint_type, Unset):
            constraint_type = UNSET
        else:
            constraint_type = GBTConstraintType(_constraint_type)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: GBTSketchEntityType | Unset
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = GBTSketchEntityType(_entity_type)

        combined_sketch_entity_type = cls(
            constraint_type=constraint_type,
            entity_type=entity_type,
        )

        combined_sketch_entity_type.additional_properties = d
        return combined_sketch_entity_type

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
