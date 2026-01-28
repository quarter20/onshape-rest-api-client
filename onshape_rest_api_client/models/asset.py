from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_extensions import AssetExtensions
    from ..models.asset_extras import AssetExtras


T = TypeVar("T", bound="Asset")


@_attrs_define
class Asset:
    """
    Attributes:
        copyright_ (str | Unset):
        extensions (AssetExtensions | Unset):
        extras (AssetExtras | Unset):
        generator (str | Unset):
        min_version (str | Unset):
        version (str | Unset):
    """

    copyright_: str | Unset = UNSET
    extensions: AssetExtensions | Unset = UNSET
    extras: AssetExtras | Unset = UNSET
    generator: str | Unset = UNSET
    min_version: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        copyright_ = self.copyright_

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        generator = self.generator

        min_version = self.min_version

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if generator is not UNSET:
            field_dict["generator"] = generator
        if min_version is not UNSET:
            field_dict["minVersion"] = min_version
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_extensions import AssetExtensions
        from ..models.asset_extras import AssetExtras

        d = dict(src_dict)
        copyright_ = d.pop("copyright", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: AssetExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = AssetExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: AssetExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = AssetExtras.from_dict(_extras)

        generator = d.pop("generator", UNSET)

        min_version = d.pop("minVersion", UNSET)

        version = d.pop("version", UNSET)

        asset = cls(
            copyright_=copyright_,
            extensions=extensions,
            extras=extras,
            generator=generator,
            min_version=min_version,
            version=version,
        )

        asset.additional_properties = d
        return asset

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
