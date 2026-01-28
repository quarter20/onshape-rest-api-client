from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_variable_info import BTVariableInfo
    from ..models.bt_variable_studio_reference_info import BTVariableStudioReferenceInfo


T = TypeVar("T", bound="BTVariableTableInfo")


@_attrs_define
class BTVariableTableInfo:
    """
    Attributes:
        variables (list[BTVariableInfo]): Variables in the VariableTable
        variable_studio_reference (BTVariableStudioReferenceInfo | Unset): List of variable studio references
    """

    variables: list[BTVariableInfo]
    variable_studio_reference: BTVariableStudioReferenceInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        variable_studio_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variable_studio_reference, Unset):
            variable_studio_reference = self.variable_studio_reference.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variables": variables,
            }
        )
        if variable_studio_reference is not UNSET:
            field_dict["variableStudioReference"] = variable_studio_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_variable_info import BTVariableInfo
        from ..models.bt_variable_studio_reference_info import BTVariableStudioReferenceInfo

        d = dict(src_dict)
        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = BTVariableInfo.from_dict(variables_item_data)

            variables.append(variables_item)

        _variable_studio_reference = d.pop("variableStudioReference", UNSET)
        variable_studio_reference: BTVariableStudioReferenceInfo | Unset
        if isinstance(_variable_studio_reference, Unset):
            variable_studio_reference = UNSET
        else:
            variable_studio_reference = BTVariableStudioReferenceInfo.from_dict(_variable_studio_reference)

        bt_variable_table_info = cls(
            variables=variables,
            variable_studio_reference=variable_studio_reference,
        )

        bt_variable_table_info.additional_properties = d
        return bt_variable_table_info

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
