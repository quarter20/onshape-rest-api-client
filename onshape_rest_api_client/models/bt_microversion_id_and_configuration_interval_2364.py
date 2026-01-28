from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_microversion_id_and_configuration_2338 import BTMicroversionIdAndConfiguration2338
    from ..models.bt_microversion_id_interval_367 import BTMicroversionIdInterval367


T = TypeVar("T", bound="BTMicroversionIdAndConfigurationInterval2364")


@_attrs_define
class BTMicroversionIdAndConfigurationInterval2364:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        from_ (BTMicroversionIdAndConfiguration2338 | Unset):
        microversion_id_interval (BTMicroversionIdInterval367 | Unset):
        to (BTMicroversionIdAndConfiguration2338 | Unset):
    """

    bt_type: str | Unset = UNSET
    from_: BTMicroversionIdAndConfiguration2338 | Unset = UNSET
    microversion_id_interval: BTMicroversionIdInterval367 | Unset = UNSET
    to: BTMicroversionIdAndConfiguration2338 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        microversion_id_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id_interval, Unset):
            microversion_id_interval = self.microversion_id_interval.to_dict()

        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if from_ is not UNSET:
            field_dict["from"] = from_
        if microversion_id_interval is not UNSET:
            field_dict["microversionIdInterval"] = microversion_id_interval
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_microversion_id_and_configuration_2338 import BTMicroversionIdAndConfiguration2338
        from ..models.bt_microversion_id_interval_367 import BTMicroversionIdInterval367

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: BTMicroversionIdAndConfiguration2338 | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = BTMicroversionIdAndConfiguration2338.from_dict(_from_)

        _microversion_id_interval = d.pop("microversionIdInterval", UNSET)
        microversion_id_interval: BTMicroversionIdInterval367 | Unset
        if isinstance(_microversion_id_interval, Unset):
            microversion_id_interval = UNSET
        else:
            microversion_id_interval = BTMicroversionIdInterval367.from_dict(_microversion_id_interval)

        _to = d.pop("to", UNSET)
        to: BTMicroversionIdAndConfiguration2338 | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = BTMicroversionIdAndConfiguration2338.from_dict(_to)

        bt_microversion_id_and_configuration_interval_2364 = cls(
            bt_type=bt_type,
            from_=from_,
            microversion_id_interval=microversion_id_interval,
            to=to,
        )

        bt_microversion_id_and_configuration_interval_2364.additional_properties = d
        return bt_microversion_id_and_configuration_interval_2364

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
