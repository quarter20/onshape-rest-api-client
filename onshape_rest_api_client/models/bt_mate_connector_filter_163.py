from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMateConnectorFilter163")


@_attrs_define
class BTMateConnectorFilter163:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        allow_implicit_mate_connector (bool | Unset):
        is_mate_connector_inference_enabled_by_default (bool | Unset):
        requires_occurrence (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    allow_implicit_mate_connector: bool | Unset = UNSET
    is_mate_connector_inference_enabled_by_default: bool | Unset = UNSET
    requires_occurrence: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        allow_implicit_mate_connector = self.allow_implicit_mate_connector

        is_mate_connector_inference_enabled_by_default = self.is_mate_connector_inference_enabled_by_default

        requires_occurrence = self.requires_occurrence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if allow_implicit_mate_connector is not UNSET:
            field_dict["allowImplicitMateConnector"] = allow_implicit_mate_connector
        if is_mate_connector_inference_enabled_by_default is not UNSET:
            field_dict["isMateConnectorInferenceEnabledByDefault"] = is_mate_connector_inference_enabled_by_default
        if requires_occurrence is not UNSET:
            field_dict["requiresOccurrence"] = requires_occurrence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        allow_implicit_mate_connector = d.pop("allowImplicitMateConnector", UNSET)

        is_mate_connector_inference_enabled_by_default = d.pop("isMateConnectorInferenceEnabledByDefault", UNSET)

        requires_occurrence = d.pop("requiresOccurrence", UNSET)

        bt_mate_connector_filter_163 = cls(
            bt_type=bt_type,
            allow_implicit_mate_connector=allow_implicit_mate_connector,
            is_mate_connector_inference_enabled_by_default=is_mate_connector_inference_enabled_by_default,
            requires_occurrence=requires_occurrence,
        )

        bt_mate_connector_filter_163.additional_properties = d
        return bt_mate_connector_filter_163

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
