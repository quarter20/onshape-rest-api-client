from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_configured_value import BTConfiguredValue


T = TypeVar("T", bound="BTVariableParams")


@_attrs_define
class BTVariableParams:
    """
    Attributes:
        name (str): Variable name
        type_ (str): VariableType name, from FeatureScript VariableType
        configured_description (BTConfiguredValue | Unset): Configured variable description, if configured
        configured_expression (BTConfiguredValue | Unset): Configured variable description, if configured
        description (str | Unset): Variable description, if not configured
        expression (str | Unset): Variable definition expression, if not configured
    """

    name: str
    type_: str
    configured_description: BTConfiguredValue | Unset = UNSET
    configured_expression: BTConfiguredValue | Unset = UNSET
    description: str | Unset = UNSET
    expression: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        configured_description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configured_description, Unset):
            configured_description = self.configured_description.to_dict()

        configured_expression: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configured_expression, Unset):
            configured_expression = self.configured_expression.to_dict()

        description = self.description

        expression = self.expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if configured_description is not UNSET:
            field_dict["configuredDescription"] = configured_description
        if configured_expression is not UNSET:
            field_dict["configuredExpression"] = configured_expression
        if description is not UNSET:
            field_dict["description"] = description
        if expression is not UNSET:
            field_dict["expression"] = expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_configured_value import BTConfiguredValue

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        _configured_description = d.pop("configuredDescription", UNSET)
        configured_description: BTConfiguredValue | Unset
        if isinstance(_configured_description, Unset):
            configured_description = UNSET
        else:
            configured_description = BTConfiguredValue.from_dict(_configured_description)

        _configured_expression = d.pop("configuredExpression", UNSET)
        configured_expression: BTConfiguredValue | Unset
        if isinstance(_configured_expression, Unset):
            configured_expression = UNSET
        else:
            configured_expression = BTConfiguredValue.from_dict(_configured_expression)

        description = d.pop("description", UNSET)

        expression = d.pop("expression", UNSET)

        bt_variable_params = cls(
            name=name,
            type_=type_,
            configured_description=configured_description,
            configured_expression=configured_expression,
            description=description,
            expression=expression,
        )

        bt_variable_params.additional_properties = d
        return bt_variable_params

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
