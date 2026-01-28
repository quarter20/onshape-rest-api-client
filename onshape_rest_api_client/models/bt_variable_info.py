from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_variable_type import GBTVariableType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTVariableInfo")


@_attrs_define
class BTVariableInfo:
    """Variables in the VariableTable

    Attributes:
        expression (str): Variable expression
        name (str): Variable name
        type_ (GBTVariableType): Variable type name, from FeatureScript VariableType
        value (str): Variable formatted value
        description (str | Unset): Variable description
    """

    expression: str
    name: str
    type_: GBTVariableType
    value: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expression = self.expression

        name = self.name

        type_ = self.type_.value

        value = self.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expression": expression,
                "name": name,
                "type": type_,
                "value": value,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expression = d.pop("expression")

        name = d.pop("name")

        type_ = GBTVariableType(d.pop("type"))

        value = d.pop("value")

        description = d.pop("description", UNSET)

        bt_variable_info = cls(
            expression=expression,
            name=name,
            type_=type_,
            value=value,
            description=description,
        )

        bt_variable_info.additional_properties = d
        return bt_variable_info

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
