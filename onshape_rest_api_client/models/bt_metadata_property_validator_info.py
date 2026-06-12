from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMetadataPropertyValidatorInfo")


@_attrs_define
class BTMetadataPropertyValidatorInfo:
    """
    Attributes:
        max_ (float | Unset):
        max_count (int | Unset):
        max_date (datetime.datetime | None | Unset):
        max_length (int | Unset):
        min_ (float | Unset):
        min_count (int | Unset):
        min_date (datetime.datetime | None | Unset):
        min_length (int | Unset):
        pattern (str | Unset):
        quantity_type (int | Unset):
    """

    max_: float | Unset = UNSET
    max_count: int | Unset = UNSET
    max_date: datetime.datetime | None | Unset = UNSET
    max_length: int | Unset = UNSET
    min_: float | Unset = UNSET
    min_count: int | Unset = UNSET
    min_date: datetime.datetime | None | Unset = UNSET
    min_length: int | Unset = UNSET
    pattern: str | Unset = UNSET
    quantity_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_ = self.max_

        max_count = self.max_count

        max_date: None | str | Unset
        if isinstance(self.max_date, Unset):
            max_date = UNSET
        elif isinstance(self.max_date, datetime.datetime):
            max_date = self.max_date.isoformat()
        else:
            max_date = self.max_date

        max_length = self.max_length

        min_ = self.min_

        min_count = self.min_count

        min_date: None | str | Unset
        if isinstance(self.min_date, Unset):
            min_date = UNSET
        elif isinstance(self.min_date, datetime.datetime):
            min_date = self.min_date.isoformat()
        else:
            min_date = self.min_date

        min_length = self.min_length

        pattern = self.pattern

        quantity_type = self.quantity_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if max_count is not UNSET:
            field_dict["maxCount"] = max_count
        if max_date is not UNSET:
            field_dict["maxDate"] = max_date
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if min_ is not UNSET:
            field_dict["min"] = min_
        if min_count is not UNSET:
            field_dict["minCount"] = min_count
        if min_date is not UNSET:
            field_dict["minDate"] = min_date
        if min_length is not UNSET:
            field_dict["minLength"] = min_length
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if quantity_type is not UNSET:
            field_dict["quantityType"] = quantity_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_ = d.pop("max", UNSET)

        max_count = d.pop("maxCount", UNSET)

        def _parse_max_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                max_date_type_0 = datetime.datetime.fromisoformat(data)

                return max_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        max_date = _parse_max_date(d.pop("maxDate", UNSET))

        max_length = d.pop("maxLength", UNSET)

        min_ = d.pop("min", UNSET)

        min_count = d.pop("minCount", UNSET)

        def _parse_min_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                min_date_type_0 = datetime.datetime.fromisoformat(data)

                return min_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        min_date = _parse_min_date(d.pop("minDate", UNSET))

        min_length = d.pop("minLength", UNSET)

        pattern = d.pop("pattern", UNSET)

        quantity_type = d.pop("quantityType", UNSET)

        bt_metadata_property_validator_info = cls(
            max_=max_,
            max_count=max_count,
            max_date=max_date,
            max_length=max_length,
            min_=min_,
            min_count=min_count,
            min_date=min_date,
            min_length=min_length,
            pattern=pattern,
            quantity_type=quantity_type,
        )

        bt_metadata_property_validator_info.additional_properties = d
        return bt_metadata_property_validator_info

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
