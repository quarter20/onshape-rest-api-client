from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTElementLocationParams")


@_attrs_define
class BTElementLocationParams:
    """The location at which the new element should be inserted.

    Attributes:
        element_id (str | Unset): The id of an element which provides context for the position value specified.
        position (int | Unset): An indicator for the relative placement of the new element. If elementId is specified, a
            negative number indicates insertion prior to the element and a non-negative number indicates insertion following
            the element. If no elementId is specified, a negative value indicates insertion at the end of the element list
            and a non-negative number indicates insertion at the start of the element list.
    """

    element_id: str | Unset = UNSET
    position: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_id = self.element_id

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        element_id = d.pop("elementId", UNSET)

        position = d.pop("position", UNSET)

        bt_element_location_params = cls(
            element_id=element_id,
            position=position,
        )

        bt_element_location_params.additional_properties = d
        return bt_element_location_params

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
