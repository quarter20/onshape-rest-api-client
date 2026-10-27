from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_std_version_match_info import BTStdVersionMatchInfo


T = TypeVar("T", bound="BTFeatureStudioStdVersionMatchInfo")


@_attrs_define
class BTFeatureStudioStdVersionMatchInfo:
    """The `onshape/std` import versions matched in one Feature Studio.

    Attributes:
        element_id (str | Unset): The element ID of the Feature Studio. Example: a1b2c3d4e5f60718293a4b5c.
        matches (list[BTStdVersionMatchInfo] | Unset): The matches in this Feature Studio in the order they appear in
            the source.
        name (str | Unset): The tab name of the Feature Studio. Example: Library Utilities.
    """

    element_id: str | Unset = UNSET
    matches: list[BTStdVersionMatchInfo] | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_id = self.element_id

        matches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.matches, Unset):
            matches = []
            for matches_item_data in self.matches:
                matches_item = matches_item_data.to_dict()
                matches.append(matches_item)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if matches is not UNSET:
            field_dict["matches"] = matches
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_std_version_match_info import BTStdVersionMatchInfo  # noqa: PLC0415

        d = dict(src_dict)
        element_id = d.pop("elementId", UNSET)

        _matches = d.pop("matches", UNSET)
        matches: list[BTStdVersionMatchInfo] | Unset = UNSET
        if _matches is not UNSET:
            matches = []
            for matches_item_data in _matches:
                matches_item = BTStdVersionMatchInfo.from_dict(matches_item_data)

                matches.append(matches_item)

        name = d.pop("name", UNSET)

        bt_feature_studio_std_version_match_info = cls(
            element_id=element_id,
            matches=matches,
            name=name,
        )

        bt_feature_studio_std_version_match_info.additional_properties = d
        return bt_feature_studio_std_version_match_info

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
