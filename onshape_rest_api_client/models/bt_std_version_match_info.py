from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTStdVersionMatchInfo")


@_attrs_define
class BTStdVersionMatchInfo:
    """One `onshape/std` import version string matched inside a Feature Studio.

    Attributes:
        end_column (int | Unset): One-based column one past the last character of the version string. Example: 55.
        end_index (int | Unset): Zero-based character index one past the last character of the version string. Example:
            54.
        end_line (int | Unset): One-based line one past the last character of the version string. Example: 2.
        matching_lines (str | Unset): The full text of the lines the match falls on, for display. Example: export
            import(path : "onshape/std/geometry.fs", version : "2650.0");.
        start_column (int | Unset): One-based column of the first character of the version string. Example: 49.
        start_index (int | Unset): Zero-based character index of the first character of the version string. Example: 48.
        start_line (int | Unset): One-based line of the version string. Example: 2.
        version (str | Unset): The matched standard library version, as written in the import. Example: 2650.0.
    """

    end_column: int | Unset = UNSET
    end_index: int | Unset = UNSET
    end_line: int | Unset = UNSET
    matching_lines: str | Unset = UNSET
    start_column: int | Unset = UNSET
    start_index: int | Unset = UNSET
    start_line: int | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_column = self.end_column

        end_index = self.end_index

        end_line = self.end_line

        matching_lines = self.matching_lines

        start_column = self.start_column

        start_index = self.start_index

        start_line = self.start_line

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_column is not UNSET:
            field_dict["endColumn"] = end_column
        if end_index is not UNSET:
            field_dict["endIndex"] = end_index
        if end_line is not UNSET:
            field_dict["endLine"] = end_line
        if matching_lines is not UNSET:
            field_dict["matchingLines"] = matching_lines
        if start_column is not UNSET:
            field_dict["startColumn"] = start_column
        if start_index is not UNSET:
            field_dict["startIndex"] = start_index
        if start_line is not UNSET:
            field_dict["startLine"] = start_line
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_column = d.pop("endColumn", UNSET)

        end_index = d.pop("endIndex", UNSET)

        end_line = d.pop("endLine", UNSET)

        matching_lines = d.pop("matchingLines", UNSET)

        start_column = d.pop("startColumn", UNSET)

        start_index = d.pop("startIndex", UNSET)

        start_line = d.pop("startLine", UNSET)

        version = d.pop("version", UNSET)

        bt_std_version_match_info = cls(
            end_column=end_column,
            end_index=end_index,
            end_line=end_line,
            matching_lines=matching_lines,
            start_column=start_column,
            start_index=start_index,
            start_line=start_line,
            version=version,
        )

        bt_std_version_match_info.additional_properties = d
        return bt_std_version_match_info

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
