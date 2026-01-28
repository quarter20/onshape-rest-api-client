from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_parameter_visibility_logical_op import GBTParameterVisibilityLogicalOp
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_parameter_visibility_condition_177 import BTParameterVisibilityCondition177


T = TypeVar("T", bound="BTParameterVisibilityLogical178")


@_attrs_define
class BTParameterVisibilityLogical178:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        self_or_child_always_visible (bool | Unset):
        children (list[BTParameterVisibilityCondition177] | Unset):
        operation (GBTParameterVisibilityLogicalOp | Unset):
    """

    bt_type: str | Unset = UNSET
    self_or_child_always_visible: bool | Unset = UNSET
    children: list[BTParameterVisibilityCondition177] | Unset = UNSET
    operation: GBTParameterVisibilityLogicalOp | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        self_or_child_always_visible = self.self_or_child_always_visible

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if self_or_child_always_visible is not UNSET:
            field_dict["selfOrChildAlwaysVisible"] = self_or_child_always_visible
        if children is not UNSET:
            field_dict["children"] = children
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_parameter_visibility_condition_177 import BTParameterVisibilityCondition177

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        self_or_child_always_visible = d.pop("selfOrChildAlwaysVisible", UNSET)

        _children = d.pop("children", UNSET)
        children: list[BTParameterVisibilityCondition177] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = BTParameterVisibilityCondition177.from_dict(children_item_data)

                children.append(children_item)

        _operation = d.pop("operation", UNSET)
        operation: GBTParameterVisibilityLogicalOp | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = GBTParameterVisibilityLogicalOp(_operation)

        bt_parameter_visibility_logical_178 = cls(
            bt_type=bt_type,
            self_or_child_always_visible=self_or_child_always_visible,
            children=children,
            operation=operation,
        )

        bt_parameter_visibility_logical_178.additional_properties = d
        return bt_parameter_visibility_logical_178

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
