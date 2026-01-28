from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_diff_json_response_2725_patch import BTDiffJsonResponse2725Patch
    from ..models.btj_edit_3734 import BTJEdit3734


T = TypeVar("T", bound="BTDiffJsonResponse2725")


@_attrs_define
class BTDiffJsonResponse2725:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        change (BTJEdit3734 | Unset): An edit that will be applied to the application element's json data.
        patch (BTDiffJsonResponse2725Patch | Unset):
        source_change_id (str | Unset):
        target_change_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    change: BTJEdit3734 | Unset = UNSET
    patch: BTDiffJsonResponse2725Patch | Unset = UNSET
    source_change_id: str | Unset = UNSET
    target_change_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        change: dict[str, Any] | Unset = UNSET
        if not isinstance(self.change, Unset):
            change = self.change.to_dict()

        patch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.patch, Unset):
            patch = self.patch.to_dict()

        source_change_id = self.source_change_id

        target_change_id = self.target_change_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if change is not UNSET:
            field_dict["change"] = change
        if patch is not UNSET:
            field_dict["patch"] = patch
        if source_change_id is not UNSET:
            field_dict["sourceChangeId"] = source_change_id
        if target_change_id is not UNSET:
            field_dict["targetChangeId"] = target_change_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_diff_json_response_2725_patch import BTDiffJsonResponse2725Patch
        from ..models.btj_edit_3734 import BTJEdit3734

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _change = d.pop("change", UNSET)
        change: BTJEdit3734 | Unset
        if isinstance(_change, Unset):
            change = UNSET
        else:
            change = BTJEdit3734.from_dict(_change)

        _patch = d.pop("patch", UNSET)
        patch: BTDiffJsonResponse2725Patch | Unset
        if isinstance(_patch, Unset):
            patch = UNSET
        else:
            patch = BTDiffJsonResponse2725Patch.from_dict(_patch)

        source_change_id = d.pop("sourceChangeId", UNSET)

        target_change_id = d.pop("targetChangeId", UNSET)

        bt_diff_json_response_2725 = cls(
            bt_type=bt_type,
            change=change,
            patch=patch,
            source_change_id=source_change_id,
            target_change_id=target_change_id,
        )

        bt_diff_json_response_2725.additional_properties = d
        return bt_diff_json_response_2725

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
