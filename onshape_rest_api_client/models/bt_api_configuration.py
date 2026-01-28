from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_api_configuration_parameter_map import BTApiConfigurationParameterMap


T = TypeVar("T", bound="BTApiConfiguration")


@_attrs_define
class BTApiConfiguration:
    """
    Attributes:
        current (bool | Unset):
        default (bool | Unset):
        null (bool | Unset):
        parameter_map (BTApiConfigurationParameterMap | Unset):
        standard_content (bool | Unset):
        standard_content_parameters_id (str | Unset):
    """

    current: bool | Unset = UNSET
    default: bool | Unset = UNSET
    null: bool | Unset = UNSET
    parameter_map: BTApiConfigurationParameterMap | Unset = UNSET
    standard_content: bool | Unset = UNSET
    standard_content_parameters_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current = self.current

        default = self.default

        null = self.null

        parameter_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameter_map, Unset):
            parameter_map = self.parameter_map.to_dict()

        standard_content = self.standard_content

        standard_content_parameters_id = self.standard_content_parameters_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current is not UNSET:
            field_dict["current"] = current
        if default is not UNSET:
            field_dict["default"] = default
        if null is not UNSET:
            field_dict["null"] = null
        if parameter_map is not UNSET:
            field_dict["parameterMap"] = parameter_map
        if standard_content is not UNSET:
            field_dict["standardContent"] = standard_content
        if standard_content_parameters_id is not UNSET:
            field_dict["standardContentParametersId"] = standard_content_parameters_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_api_configuration_parameter_map import BTApiConfigurationParameterMap

        d = dict(src_dict)
        current = d.pop("current", UNSET)

        default = d.pop("default", UNSET)

        null = d.pop("null", UNSET)

        _parameter_map = d.pop("parameterMap", UNSET)
        parameter_map: BTApiConfigurationParameterMap | Unset
        if isinstance(_parameter_map, Unset):
            parameter_map = UNSET
        else:
            parameter_map = BTApiConfigurationParameterMap.from_dict(_parameter_map)

        standard_content = d.pop("standardContent", UNSET)

        standard_content_parameters_id = d.pop("standardContentParametersId", UNSET)

        bt_api_configuration = cls(
            current=current,
            default=default,
            null=null,
            parameter_map=parameter_map,
            standard_content=standard_content,
            standard_content_parameters_id=standard_content_parameters_id,
        )

        bt_api_configuration.additional_properties = d
        return bt_api_configuration

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
