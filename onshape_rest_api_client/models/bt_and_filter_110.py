from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_query_filter_183 import BTQueryFilter183


T = TypeVar("T", bound="BTAndFilter110")


@_attrs_define
class BTAndFilter110:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        operand1 (BTQueryFilter183 | Unset):
        operand2 (BTQueryFilter183 | Unset):
    """

    bt_type: str | Unset = UNSET
    operand1: BTQueryFilter183 | Unset = UNSET
    operand2: BTQueryFilter183 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        operand1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operand1, Unset):
            operand1 = self.operand1.to_dict()

        operand2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operand2, Unset):
            operand2 = self.operand2.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if operand1 is not UNSET:
            field_dict["operand1"] = operand1
        if operand2 is not UNSET:
            field_dict["operand2"] = operand2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_query_filter_183 import BTQueryFilter183

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _operand1 = d.pop("operand1", UNSET)
        operand1: BTQueryFilter183 | Unset
        if isinstance(_operand1, Unset):
            operand1 = UNSET
        else:
            operand1 = BTQueryFilter183.from_dict(_operand1)

        _operand2 = d.pop("operand2", UNSET)
        operand2: BTQueryFilter183 | Unset
        if isinstance(_operand2, Unset):
            operand2 = UNSET
        else:
            operand2 = BTQueryFilter183.from_dict(_operand2)

        bt_and_filter_110 = cls(
            bt_type=bt_type,
            operand1=operand1,
            operand2=operand2,
        )

        bt_and_filter_110.additional_properties = d
        return bt_and_filter_110

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
