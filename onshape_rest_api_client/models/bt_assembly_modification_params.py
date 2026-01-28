from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_transform_definition_params import BTAssemblyTransformDefinitionParams


T = TypeVar("T", bound="BTAssemblyModificationParams")


@_attrs_define
class BTAssemblyModificationParams:
    """
    Attributes:
        delete_instances (list[str] | Unset):
        edit_description (str | Unset):
        suppress_instances (list[str] | Unset):
        transform_definitions (list[BTAssemblyTransformDefinitionParams] | Unset):
        unsuppress_instances (list[str] | Unset):
    """

    delete_instances: list[str] | Unset = UNSET
    edit_description: str | Unset = UNSET
    suppress_instances: list[str] | Unset = UNSET
    transform_definitions: list[BTAssemblyTransformDefinitionParams] | Unset = UNSET
    unsuppress_instances: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_instances: list[str] | Unset = UNSET
        if not isinstance(self.delete_instances, Unset):
            delete_instances = self.delete_instances

        edit_description = self.edit_description

        suppress_instances: list[str] | Unset = UNSET
        if not isinstance(self.suppress_instances, Unset):
            suppress_instances = self.suppress_instances

        transform_definitions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transform_definitions, Unset):
            transform_definitions = []
            for transform_definitions_item_data in self.transform_definitions:
                transform_definitions_item = transform_definitions_item_data.to_dict()
                transform_definitions.append(transform_definitions_item)

        unsuppress_instances: list[str] | Unset = UNSET
        if not isinstance(self.unsuppress_instances, Unset):
            unsuppress_instances = self.unsuppress_instances

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_instances is not UNSET:
            field_dict["deleteInstances"] = delete_instances
        if edit_description is not UNSET:
            field_dict["editDescription"] = edit_description
        if suppress_instances is not UNSET:
            field_dict["suppressInstances"] = suppress_instances
        if transform_definitions is not UNSET:
            field_dict["transformDefinitions"] = transform_definitions
        if unsuppress_instances is not UNSET:
            field_dict["unsuppressInstances"] = unsuppress_instances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_transform_definition_params import BTAssemblyTransformDefinitionParams

        d = dict(src_dict)
        delete_instances = cast(list[str], d.pop("deleteInstances", UNSET))

        edit_description = d.pop("editDescription", UNSET)

        suppress_instances = cast(list[str], d.pop("suppressInstances", UNSET))

        _transform_definitions = d.pop("transformDefinitions", UNSET)
        transform_definitions: list[BTAssemblyTransformDefinitionParams] | Unset = UNSET
        if _transform_definitions is not UNSET:
            transform_definitions = []
            for transform_definitions_item_data in _transform_definitions:
                transform_definitions_item = BTAssemblyTransformDefinitionParams.from_dict(
                    transform_definitions_item_data
                )

                transform_definitions.append(transform_definitions_item)

        unsuppress_instances = cast(list[str], d.pop("unsuppressInstances", UNSET))

        bt_assembly_modification_params = cls(
            delete_instances=delete_instances,
            edit_description=edit_description,
            suppress_instances=suppress_instances,
            transform_definitions=transform_definitions,
            unsuppress_instances=unsuppress_instances,
        )

        bt_assembly_modification_params.additional_properties = d
        return bt_assembly_modification_params

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
