from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_feature_studio_std_version_match_info import BTFeatureStudioStdVersionMatchInfo


T = TypeVar("T", bound="BTFeatureStudioStdVersionMatchesInfo")


@_attrs_define
class BTFeatureStudioStdVersionMatchesInfo:
    """The `onshape/std` import versions matching a search, across the Feature Studios of a workspace, version or
    microversion.

        Attributes:
            feature_studios (list[BTFeatureStudioStdVersionMatchInfo] | Unset): The Feature Studios with at least one match,
                sorted by tab name.
            matched_element_count (int | Unset): The number of Feature Studios searched after applying the tab name filter.
                Example: 12.
            results_truncated (bool | Unset): `true` if there were too many matches to report and the list was truncated.
    """

    feature_studios: list[BTFeatureStudioStdVersionMatchInfo] | Unset = UNSET
    matched_element_count: int | Unset = UNSET
    results_truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_studios: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feature_studios, Unset):
            feature_studios = []
            for feature_studios_item_data in self.feature_studios:
                feature_studios_item = feature_studios_item_data.to_dict()
                feature_studios.append(feature_studios_item)

        matched_element_count = self.matched_element_count

        results_truncated = self.results_truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feature_studios is not UNSET:
            field_dict["featureStudios"] = feature_studios
        if matched_element_count is not UNSET:
            field_dict["matchedElementCount"] = matched_element_count
        if results_truncated is not UNSET:
            field_dict["resultsTruncated"] = results_truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_feature_studio_std_version_match_info import BTFeatureStudioStdVersionMatchInfo  # noqa: PLC0415

        d = dict(src_dict)
        _feature_studios = d.pop("featureStudios", UNSET)
        feature_studios: list[BTFeatureStudioStdVersionMatchInfo] | Unset = UNSET
        if _feature_studios is not UNSET:
            feature_studios = []
            for feature_studios_item_data in _feature_studios:
                feature_studios_item = BTFeatureStudioStdVersionMatchInfo.from_dict(feature_studios_item_data)

                feature_studios.append(feature_studios_item)

        matched_element_count = d.pop("matchedElementCount", UNSET)

        results_truncated = d.pop("resultsTruncated", UNSET)

        bt_feature_studio_std_version_matches_info = cls(
            feature_studios=feature_studios,
            matched_element_count=matched_element_count,
            results_truncated=results_truncated,
        )

        bt_feature_studio_std_version_matches_info.additional_properties = d
        return bt_feature_studio_std_version_matches_info

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
