from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAppElementChangeParams")


@_attrs_define
class BTAppElementChangeParams:
    """
    Attributes:
        subelement_id (str): The id of the subelement to edit. The value is determined by the application.
        base_content (str | Unset): This base64-encoded data is treated as a full representation of the sub-element's
            data and all deltas previously added will no longer be returned.
        delta (str | Unset): This base64-encoded data is a delta which the application can apply to the last added
            baseContent data.
    """

    subelement_id: str
    base_content: str | Unset = UNSET
    delta: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subelement_id = self.subelement_id

        base_content = self.base_content

        delta = self.delta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subelementId": subelement_id,
            }
        )
        if base_content is not UNSET:
            field_dict["baseContent"] = base_content
        if delta is not UNSET:
            field_dict["delta"] = delta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subelement_id = d.pop("subelementId")

        base_content = d.pop("baseContent", UNSET)

        delta = d.pop("delta", UNSET)

        bt_app_element_change_params = cls(
            subelement_id=subelement_id,
            base_content=base_content,
            delta=delta,
        )

        bt_app_element_change_params.additional_properties = d
        return bt_app_element_change_params

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
