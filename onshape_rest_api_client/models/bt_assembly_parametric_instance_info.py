from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_parametric_instance_child_info import BTAssemblyParametricInstanceChildInfo


T = TypeVar("T", bound="BTAssemblyParametricInstanceInfo")


@_attrs_define
class BTAssemblyParametricInstanceInfo:
    """Parametric instance description.

    Attributes:
        children (list[BTAssemblyParametricInstanceChildInfo] | Unset): Child instances.
        id (str | Unset): Id of the Part Studio instance.
        name (str | Unset): Name of the parametric instance.
        suppressed (bool | Unset): If the parametric is suppressed.
        type_ (str | Unset): Type of parametric instance.
    """

    children: list[BTAssemblyParametricInstanceChildInfo] | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    suppressed: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        id = self.id

        name = self.name

        suppressed = self.suppressed

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if children is not UNSET:
            field_dict["children"] = children
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_parametric_instance_child_info import BTAssemblyParametricInstanceChildInfo

        d = dict(src_dict)
        _children = d.pop("children", UNSET)
        children: list[BTAssemblyParametricInstanceChildInfo] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = BTAssemblyParametricInstanceChildInfo.from_dict(children_item_data)

                children.append(children_item)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        suppressed = d.pop("suppressed", UNSET)

        type_ = d.pop("type", UNSET)

        bt_assembly_parametric_instance_info = cls(
            children=children,
            id=id,
            name=name,
            suppressed=suppressed,
            type_=type_,
        )

        bt_assembly_parametric_instance_info.additional_properties = d
        return bt_assembly_parametric_instance_info

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
