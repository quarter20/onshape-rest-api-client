from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTStdVersionReplaceParams")


@_attrs_define
class BTStdVersionReplaceParams:
    """Parameters for replacing the standard library version of `onshape/std` imports in the Feature Studios of a
    workspace.

        Attributes:
            replace_with (str): The standard library version to write into the matched imports. A bare major version is
                normalized to `major.0` (the form used by std imports). Example: 2830.0.
            commit (bool | Unset): `true` to commit the modified Feature Studios to the workspace. When `false`, the
                replacements are left as uncommitted edits that a user can review and commit in the Onshape UI. Default: True.
            exclude_versions (list[str] | Unset): Standard library versions to leave alone, in the same syntax as
                `includeVersions`. Subtracted from the versions selected by `includeVersions`. Example: ['2650'].
            feature_studio_name_wildcard_filter (str | Unset): Wildcard filter on Feature Studio tab name, where `*` matches
                any sequence of characters and `?` matches a single character. Matching is case insensitive. If blank, all
                Feature Studios in the workspace are considered. Example: Library*.
            include_versions (list[str] | Unset): Standard library versions to replace. Each entry is a version (`2830`), a
                specific point release (`2830.1`), or a range with either end optionally omitted (`2600-2700`, `2900-`,
                `-1800`). An entry may itself be a comma separated list. If empty, every version matches. Example: ['2600-2700',
                '2900-'].
    """

    replace_with: str
    commit: bool | Unset = True
    exclude_versions: list[str] | Unset = UNSET
    feature_studio_name_wildcard_filter: str | Unset = UNSET
    include_versions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replace_with = self.replace_with

        commit = self.commit

        exclude_versions: list[str] | Unset = UNSET
        if not isinstance(self.exclude_versions, Unset):
            exclude_versions = self.exclude_versions

        feature_studio_name_wildcard_filter = self.feature_studio_name_wildcard_filter

        include_versions: list[str] | Unset = UNSET
        if not isinstance(self.include_versions, Unset):
            include_versions = self.include_versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "replaceWith": replace_with,
            }
        )
        if commit is not UNSET:
            field_dict["commit"] = commit
        if exclude_versions is not UNSET:
            field_dict["excludeVersions"] = exclude_versions
        if feature_studio_name_wildcard_filter is not UNSET:
            field_dict["featureStudioNameWildcardFilter"] = feature_studio_name_wildcard_filter
        if include_versions is not UNSET:
            field_dict["includeVersions"] = include_versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        replace_with = d.pop("replaceWith")

        commit = d.pop("commit", UNSET)

        exclude_versions = cast(list[str], d.pop("excludeVersions", UNSET))

        feature_studio_name_wildcard_filter = d.pop("featureStudioNameWildcardFilter", UNSET)

        include_versions = cast(list[str], d.pop("includeVersions", UNSET))

        bt_std_version_replace_params = cls(
            replace_with=replace_with,
            commit=commit,
            exclude_versions=exclude_versions,
            feature_studio_name_wildcard_filter=feature_studio_name_wildcard_filter,
            include_versions=include_versions,
        )

        bt_std_version_replace_params.additional_properties = d
        return bt_std_version_replace_params

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
