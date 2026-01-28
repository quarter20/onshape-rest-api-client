from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_next_part_number_param import BTNextPartNumberParam


T = TypeVar("T", bound="BTNextPartNumbersParam")


@_attrs_define
class BTNextPartNumbersParam:
    """
    Attributes:
        item_part_numbers (list[BTNextPartNumberParam] | Unset):
        skip_part_numbers (list[str] | Unset): Comma-separated list of part numbers to skip creating new part numbers
            for.
    """

    item_part_numbers: list[BTNextPartNumberParam] | Unset = UNSET
    skip_part_numbers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_part_numbers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.item_part_numbers, Unset):
            item_part_numbers = []
            for item_part_numbers_item_data in self.item_part_numbers:
                item_part_numbers_item = item_part_numbers_item_data.to_dict()
                item_part_numbers.append(item_part_numbers_item)

        skip_part_numbers: list[str] | Unset = UNSET
        if not isinstance(self.skip_part_numbers, Unset):
            skip_part_numbers = self.skip_part_numbers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_part_numbers is not UNSET:
            field_dict["itemPartNumbers"] = item_part_numbers
        if skip_part_numbers is not UNSET:
            field_dict["skipPartNumbers"] = skip_part_numbers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_next_part_number_param import BTNextPartNumberParam

        d = dict(src_dict)
        _item_part_numbers = d.pop("itemPartNumbers", UNSET)
        item_part_numbers: list[BTNextPartNumberParam] | Unset = UNSET
        if _item_part_numbers is not UNSET:
            item_part_numbers = []
            for item_part_numbers_item_data in _item_part_numbers:
                item_part_numbers_item = BTNextPartNumberParam.from_dict(item_part_numbers_item_data)

                item_part_numbers.append(item_part_numbers_item)

        skip_part_numbers = cast(list[str], d.pop("skipPartNumbers", UNSET))

        bt_next_part_numbers_param = cls(
            item_part_numbers=item_part_numbers,
            skip_part_numbers=skip_part_numbers,
        )

        bt_next_part_numbers_param.additional_properties = d
        return bt_next_part_numbers_param

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
