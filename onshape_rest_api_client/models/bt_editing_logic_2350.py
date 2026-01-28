from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTEditingLogic2350")


@_attrs_define
class BTEditingLogic2350:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        function_name (str | Unset):
        wants_clicked_button (bool | Unset):
        wants_hidden_bodies (bool | Unset):
        wants_is_creating (bool | Unset):
        wants_specified_parameters (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    function_name: str | Unset = UNSET
    wants_clicked_button: bool | Unset = UNSET
    wants_hidden_bodies: bool | Unset = UNSET
    wants_is_creating: bool | Unset = UNSET
    wants_specified_parameters: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        function_name = self.function_name

        wants_clicked_button = self.wants_clicked_button

        wants_hidden_bodies = self.wants_hidden_bodies

        wants_is_creating = self.wants_is_creating

        wants_specified_parameters = self.wants_specified_parameters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if function_name is not UNSET:
            field_dict["functionName"] = function_name
        if wants_clicked_button is not UNSET:
            field_dict["wantsClickedButton"] = wants_clicked_button
        if wants_hidden_bodies is not UNSET:
            field_dict["wantsHiddenBodies"] = wants_hidden_bodies
        if wants_is_creating is not UNSET:
            field_dict["wantsIsCreating"] = wants_is_creating
        if wants_specified_parameters is not UNSET:
            field_dict["wantsSpecifiedParameters"] = wants_specified_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        function_name = d.pop("functionName", UNSET)

        wants_clicked_button = d.pop("wantsClickedButton", UNSET)

        wants_hidden_bodies = d.pop("wantsHiddenBodies", UNSET)

        wants_is_creating = d.pop("wantsIsCreating", UNSET)

        wants_specified_parameters = d.pop("wantsSpecifiedParameters", UNSET)

        bt_editing_logic_2350 = cls(
            bt_type=bt_type,
            function_name=function_name,
            wants_clicked_button=wants_clicked_button,
            wants_hidden_bodies=wants_hidden_bodies,
            wants_is_creating=wants_is_creating,
            wants_specified_parameters=wants_specified_parameters,
        )

        bt_editing_logic_2350.additional_properties = d
        return bt_editing_logic_2350

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
