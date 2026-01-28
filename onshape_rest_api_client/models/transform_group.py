from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_instance_definition_params import BTAssemblyInstanceDefinitionParams


T = TypeVar("T", bound="TransformGroup")


@_attrs_define
class TransformGroup:
    """
    Attributes:
        instances (list[BTAssemblyInstanceDefinitionParams] | Unset):
        transform (list[float] | Unset):
    """

    instances: list[BTAssemblyInstanceDefinitionParams] | Unset = UNSET
    transform: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()
                instances.append(instances_item)

        transform: list[float] | Unset = UNSET
        if not isinstance(self.transform, Unset):
            transform = self.transform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instances is not UNSET:
            field_dict["instances"] = instances
        if transform is not UNSET:
            field_dict["transform"] = transform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_instance_definition_params import BTAssemblyInstanceDefinitionParams

        d = dict(src_dict)
        _instances = d.pop("instances", UNSET)
        instances: list[BTAssemblyInstanceDefinitionParams] | Unset = UNSET
        if _instances is not UNSET:
            instances = []
            for instances_item_data in _instances:
                instances_item = BTAssemblyInstanceDefinitionParams.from_dict(instances_item_data)

                instances.append(instances_item)

        transform = cast(list[float], d.pop("transform", UNSET))

        transform_group = cls(
            instances=instances,
            transform=transform,
        )

        transform_group.additional_properties = d
        return transform_group

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
