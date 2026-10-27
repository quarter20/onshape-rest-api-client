from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_std_version_replace_info_element_id_to_replacement_count import (
        BTStdVersionReplaceInfoElementIdToReplacementCount,
    )


T = TypeVar("T", bound="BTStdVersionReplaceInfo")


@_attrs_define
class BTStdVersionReplaceInfo:
    """The result of replacing the standard library version of 'onshape/std' imports in the Feature Studios of a workspace.

    Attributes:
        committed (bool | Unset): True if the modified Feature Studios were committed to the workspace. False if
            'commit' was not requested, or if there was nothing to replace.
        element_id_to_replacement_count (BTStdVersionReplaceInfoElementIdToReplacementCount | Unset): Map from the
            element ID of each modified Feature Studio to the number of import versions replaced in it. Feature Studios with
            no replacements are omitted.
        total_replacement_count (int | Unset): The total number of import versions replaced across all Feature Studios.
            Example: 7.
    """

    committed: bool | Unset = UNSET
    element_id_to_replacement_count: BTStdVersionReplaceInfoElementIdToReplacementCount | Unset = UNSET
    total_replacement_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        committed = self.committed

        element_id_to_replacement_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_id_to_replacement_count, Unset):
            element_id_to_replacement_count = self.element_id_to_replacement_count.to_dict()

        total_replacement_count = self.total_replacement_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if committed is not UNSET:
            field_dict["committed"] = committed
        if element_id_to_replacement_count is not UNSET:
            field_dict["elementIdToReplacementCount"] = element_id_to_replacement_count
        if total_replacement_count is not UNSET:
            field_dict["totalReplacementCount"] = total_replacement_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_std_version_replace_info_element_id_to_replacement_count import (
            BTStdVersionReplaceInfoElementIdToReplacementCount,  # noqa: PLC0415
        )

        d = dict(src_dict)
        committed = d.pop("committed", UNSET)

        _element_id_to_replacement_count = d.pop("elementIdToReplacementCount", UNSET)
        element_id_to_replacement_count: BTStdVersionReplaceInfoElementIdToReplacementCount | Unset
        if isinstance(_element_id_to_replacement_count, Unset):
            element_id_to_replacement_count = UNSET
        else:
            element_id_to_replacement_count = BTStdVersionReplaceInfoElementIdToReplacementCount.from_dict(
                _element_id_to_replacement_count
            )

        total_replacement_count = d.pop("totalReplacementCount", UNSET)

        bt_std_version_replace_info = cls(
            committed=committed,
            element_id_to_replacement_count=element_id_to_replacement_count,
            total_replacement_count=total_replacement_count,
        )

        bt_std_version_replace_info.additional_properties = d
        return bt_std_version_replace_info

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
