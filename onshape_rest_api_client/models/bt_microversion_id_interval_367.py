from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_microversion_id_366 import BTMicroversionId366


T = TypeVar("T", bound="BTMicroversionIdInterval367")


@_attrs_define
class BTMicroversionIdInterval367:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        from_ (BTMicroversionId366 | Unset):
        to (BTMicroversionId366 | Unset):
        trivial (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    from_: BTMicroversionId366 | Unset = UNSET
    to: BTMicroversionId366 | Unset = UNSET
    trivial: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        trivial = self.trivial

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if trivial is not UNSET:
            field_dict["trivial"] = trivial

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_microversion_id_366 import BTMicroversionId366

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: BTMicroversionId366 | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = BTMicroversionId366.from_dict(_from_)

        _to = d.pop("to", UNSET)
        to: BTMicroversionId366 | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = BTMicroversionId366.from_dict(_to)

        trivial = d.pop("trivial", UNSET)

        bt_microversion_id_interval_367 = cls(
            bt_type=bt_type,
            from_=from_,
            to=to,
            trivial=trivial,
        )

        bt_microversion_id_interval_367.additional_properties = d
        return bt_microversion_id_interval_367

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
