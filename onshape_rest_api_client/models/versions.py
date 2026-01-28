from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_api_version import BTApiVersion
from ..types import UNSET, Unset

T = TypeVar("T", bound="Versions")


@_attrs_define
class Versions:
    """
    Attributes:
        available_versions (list[BTApiVersion] | Unset):
        specified_version (BTApiVersion | Unset):
    """

    available_versions: list[BTApiVersion] | Unset = UNSET
    specified_version: BTApiVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_versions: list[str] | Unset = UNSET
        if not isinstance(self.available_versions, Unset):
            available_versions = []
            for available_versions_item_data in self.available_versions:
                available_versions_item = available_versions_item_data.value
                available_versions.append(available_versions_item)

        specified_version: str | Unset = UNSET
        if not isinstance(self.specified_version, Unset):
            specified_version = self.specified_version.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_versions is not UNSET:
            field_dict["availableVersions"] = available_versions
        if specified_version is not UNSET:
            field_dict["specifiedVersion"] = specified_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _available_versions = d.pop("availableVersions", UNSET)
        available_versions: list[BTApiVersion] | Unset = UNSET
        if _available_versions is not UNSET:
            available_versions = []
            for available_versions_item_data in _available_versions:
                available_versions_item = BTApiVersion(available_versions_item_data)

                available_versions.append(available_versions_item)

        _specified_version = d.pop("specifiedVersion", UNSET)
        specified_version: BTApiVersion | Unset
        if isinstance(_specified_version, Unset):
            specified_version = UNSET
        else:
            specified_version = BTApiVersion(_specified_version)

        versions = cls(
            available_versions=available_versions,
            specified_version=specified_version,
        )

        versions.additional_properties = d
        return versions

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
