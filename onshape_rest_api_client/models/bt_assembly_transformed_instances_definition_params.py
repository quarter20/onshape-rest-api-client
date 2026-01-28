from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transform_group import TransformGroup


T = TypeVar("T", bound="BTAssemblyTransformedInstancesDefinitionParams")


@_attrs_define
class BTAssemblyTransformedInstancesDefinitionParams:
    """
    Attributes:
        transform_groups (list[TransformGroup] | Unset):
    """

    transform_groups: list[TransformGroup] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transform_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transform_groups, Unset):
            transform_groups = []
            for transform_groups_item_data in self.transform_groups:
                transform_groups_item = transform_groups_item_data.to_dict()
                transform_groups.append(transform_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transform_groups is not UNSET:
            field_dict["transformGroups"] = transform_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transform_group import TransformGroup

        d = dict(src_dict)
        _transform_groups = d.pop("transformGroups", UNSET)
        transform_groups: list[TransformGroup] | Unset = UNSET
        if _transform_groups is not UNSET:
            transform_groups = []
            for transform_groups_item_data in _transform_groups:
                transform_groups_item = TransformGroup.from_dict(transform_groups_item_data)

                transform_groups.append(transform_groups_item)

        bt_assembly_transformed_instances_definition_params = cls(
            transform_groups=transform_groups,
        )

        bt_assembly_transformed_instances_definition_params.additional_properties = d
        return bt_assembly_transformed_instances_definition_params

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
