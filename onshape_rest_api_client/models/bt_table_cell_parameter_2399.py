from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_parameter_spec_6 import BTParameterSpec6
    from ..models.btm_parameter_1 import BTMParameter1


T = TypeVar("T", bound="BTTableCellParameter2399")


@_attrs_define
class BTTableCellParameter2399:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        is_ever_visible (bool | Unset):
        is_read_only (bool | Unset):
        error (str | Unset):
        info (str | Unset):
        override_spec (BTParameterSpec6 | Unset):
        parameter (BTMParameter1 | Unset): A list of parameter values for instantiation of the feature spec. Parameters
            are present for all defined parameters, even if not used in a specific instantiation.
    """

    bt_type: str | Unset = UNSET
    is_ever_visible: bool | Unset = UNSET
    is_read_only: bool | Unset = UNSET
    error: str | Unset = UNSET
    info: str | Unset = UNSET
    override_spec: BTParameterSpec6 | Unset = UNSET
    parameter: BTMParameter1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        is_ever_visible = self.is_ever_visible

        is_read_only = self.is_read_only

        error = self.error

        info = self.info

        override_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override_spec, Unset):
            override_spec = self.override_spec.to_dict()

        parameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameter, Unset):
            parameter = self.parameter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if is_ever_visible is not UNSET:
            field_dict["isEverVisible"] = is_ever_visible
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if error is not UNSET:
            field_dict["error"] = error
        if info is not UNSET:
            field_dict["info"] = info
        if override_spec is not UNSET:
            field_dict["overrideSpec"] = override_spec
        if parameter is not UNSET:
            field_dict["parameter"] = parameter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_parameter_spec_6 import BTParameterSpec6
        from ..models.btm_parameter_1 import BTMParameter1

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        is_ever_visible = d.pop("isEverVisible", UNSET)

        is_read_only = d.pop("isReadOnly", UNSET)

        error = d.pop("error", UNSET)

        info = d.pop("info", UNSET)

        _override_spec = d.pop("overrideSpec", UNSET)
        override_spec: BTParameterSpec6 | Unset
        if isinstance(_override_spec, Unset):
            override_spec = UNSET
        else:
            override_spec = BTParameterSpec6.from_dict(_override_spec)

        _parameter = d.pop("parameter", UNSET)
        parameter: BTMParameter1 | Unset
        if isinstance(_parameter, Unset):
            parameter = UNSET
        else:
            parameter = BTMParameter1.from_dict(_parameter)

        bt_table_cell_parameter_2399 = cls(
            bt_type=bt_type,
            is_ever_visible=is_ever_visible,
            is_read_only=is_read_only,
            error=error,
            info=info,
            override_spec=override_spec,
            parameter=parameter,
        )

        bt_table_cell_parameter_2399.additional_properties = d
        return bt_table_cell_parameter_2399

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
