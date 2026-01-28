from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_microversion_id_366 import BTMicroversionId366
    from ..models.bt_microversion_id_and_configuration_2338_configuration_parameter_id_to_value import (
        BTMicroversionIdAndConfiguration2338ConfigurationParameterIdToValue,
    )


T = TypeVar("T", bound="BTMicroversionIdAndConfiguration2338")


@_attrs_define
class BTMicroversionIdAndConfiguration2338:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        cache_key (str | Unset):
        configuration_parameter_id_to_value (BTMicroversionIdAndConfiguration2338ConfigurationParameterIdToValue |
            Unset):
        deleted (bool | Unset):
        description (str | Unset):
        microversion (BTMicroversionId366 | Unset):
    """

    bt_type: str | Unset = UNSET
    cache_key: str | Unset = UNSET
    configuration_parameter_id_to_value: BTMicroversionIdAndConfiguration2338ConfigurationParameterIdToValue | Unset = (
        UNSET
    )
    deleted: bool | Unset = UNSET
    description: str | Unset = UNSET
    microversion: BTMicroversionId366 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        cache_key = self.cache_key

        configuration_parameter_id_to_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration_parameter_id_to_value, Unset):
            configuration_parameter_id_to_value = self.configuration_parameter_id_to_value.to_dict()

        deleted = self.deleted

        description = self.description

        microversion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion, Unset):
            microversion = self.microversion.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if cache_key is not UNSET:
            field_dict["cacheKey"] = cache_key
        if configuration_parameter_id_to_value is not UNSET:
            field_dict["configurationParameterIdToValue"] = configuration_parameter_id_to_value
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if description is not UNSET:
            field_dict["description"] = description
        if microversion is not UNSET:
            field_dict["microversion"] = microversion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_microversion_id_366 import BTMicroversionId366
        from ..models.bt_microversion_id_and_configuration_2338_configuration_parameter_id_to_value import (
            BTMicroversionIdAndConfiguration2338ConfigurationParameterIdToValue,
        )

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        cache_key = d.pop("cacheKey", UNSET)

        _configuration_parameter_id_to_value = d.pop("configurationParameterIdToValue", UNSET)
        configuration_parameter_id_to_value: BTMicroversionIdAndConfiguration2338ConfigurationParameterIdToValue | Unset
        if isinstance(_configuration_parameter_id_to_value, Unset):
            configuration_parameter_id_to_value = UNSET
        else:
            configuration_parameter_id_to_value = (
                BTMicroversionIdAndConfiguration2338ConfigurationParameterIdToValue.from_dict(
                    _configuration_parameter_id_to_value
                )
            )

        deleted = d.pop("deleted", UNSET)

        description = d.pop("description", UNSET)

        _microversion = d.pop("microversion", UNSET)
        microversion: BTMicroversionId366 | Unset
        if isinstance(_microversion, Unset):
            microversion = UNSET
        else:
            microversion = BTMicroversionId366.from_dict(_microversion)

        bt_microversion_id_and_configuration_2338 = cls(
            bt_type=bt_type,
            cache_key=cache_key,
            configuration_parameter_id_to_value=configuration_parameter_id_to_value,
            deleted=deleted,
            description=description,
            microversion=microversion,
        )

        bt_microversion_id_and_configuration_2338.additional_properties = d
        return bt_microversion_id_and_configuration_2338

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
