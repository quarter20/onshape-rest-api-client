from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btj_edit_3734 import BTJEdit3734


T = TypeVar("T", bound="BTJEditList2707")


@_attrs_define
class BTJEditList2707:
    """A list of edits that will be applied in order.

    Attributes:
        bt_type (str): Type of JSON object.
        edits (list[BTJEdit3734] | Unset):
    """

    bt_type: str
    edits: list[BTJEdit3734] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        edits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edits, Unset):
            edits = []
            for edits_item_data in self.edits:
                edits_item = edits_item_data.to_dict()
                edits.append(edits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "btType": bt_type,
            }
        )
        if edits is not UNSET:
            field_dict["edits"] = edits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btj_edit_3734 import BTJEdit3734

        d = dict(src_dict)
        bt_type = d.pop("btType")

        _edits = d.pop("edits", UNSET)
        edits: list[BTJEdit3734] | Unset = UNSET
        if _edits is not UNSET:
            edits = []
            for edits_item_data in _edits:
                edits_item = BTJEdit3734.from_dict(edits_item_data)

                edits.append(edits_item)

        btj_edit_list_2707 = cls(
            bt_type=bt_type,
            edits=edits,
        )

        btj_edit_list_2707.additional_properties = d
        return btj_edit_list_2707

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
