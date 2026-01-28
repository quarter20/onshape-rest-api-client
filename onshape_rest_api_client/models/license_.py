from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_extensions import LicenseExtensions


T = TypeVar("T", bound="License")


@_attrs_define
class License:
    """
    Attributes:
        extensions (LicenseExtensions | Unset):
        identifier (str | Unset):
        name (str | Unset):
        url (str | Unset):
    """

    extensions: LicenseExtensions | Unset = UNSET
    identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        identifier = self.identifier

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_extensions import LicenseExtensions

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: LicenseExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = LicenseExtensions.from_dict(_extensions)

        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        license_ = cls(
            extensions=extensions,
            identifier=identifier,
            name=name,
            url=url,
        )

        license_.additional_properties = d
        return license_

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
