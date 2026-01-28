from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_error_string_enum import GBTErrorStringEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_value_and_use_4696 import BTValueAndUse4696


T = TypeVar("T", bound="BTParameterExpressionErrorInfo2037")


@_attrs_define
class BTParameterExpressionErrorInfo2037:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        error_message_identifier (GBTErrorStringEnum | Unset):
        message_arguments (list[BTValueAndUse4696] | Unset):
    """

    bt_type: str | Unset = UNSET
    error_message_identifier: GBTErrorStringEnum | Unset = UNSET
    message_arguments: list[BTValueAndUse4696] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        error_message_identifier: str | Unset = UNSET
        if not isinstance(self.error_message_identifier, Unset):
            error_message_identifier = self.error_message_identifier.value

        message_arguments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.message_arguments, Unset):
            message_arguments = []
            for message_arguments_item_data in self.message_arguments:
                message_arguments_item = message_arguments_item_data.to_dict()
                message_arguments.append(message_arguments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if error_message_identifier is not UNSET:
            field_dict["errorMessageIdentifier"] = error_message_identifier
        if message_arguments is not UNSET:
            field_dict["messageArguments"] = message_arguments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_value_and_use_4696 import BTValueAndUse4696

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _error_message_identifier = d.pop("errorMessageIdentifier", UNSET)
        error_message_identifier: GBTErrorStringEnum | Unset
        if isinstance(_error_message_identifier, Unset):
            error_message_identifier = UNSET
        else:
            error_message_identifier = GBTErrorStringEnum(_error_message_identifier)

        _message_arguments = d.pop("messageArguments", UNSET)
        message_arguments: list[BTValueAndUse4696] | Unset = UNSET
        if _message_arguments is not UNSET:
            message_arguments = []
            for message_arguments_item_data in _message_arguments:
                message_arguments_item = BTValueAndUse4696.from_dict(message_arguments_item_data)

                message_arguments.append(message_arguments_item)

        bt_parameter_expression_error_info_2037 = cls(
            bt_type=bt_type,
            error_message_identifier=error_message_identifier,
            message_arguments=message_arguments,
        )

        bt_parameter_expression_error_info_2037.additional_properties = d
        return bt_parameter_expression_error_info_2037

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
