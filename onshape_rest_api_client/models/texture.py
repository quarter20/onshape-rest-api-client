from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.texture_extensions import TextureExtensions
    from ..models.texture_extras import TextureExtras


T = TypeVar("T", bound="Texture")


@_attrs_define
class Texture:
    """
    Attributes:
        extensions (TextureExtensions | Unset):
        extras (TextureExtras | Unset):
        name (str | Unset):
        sampler (int | Unset):
        source (int | Unset):
    """

    extensions: TextureExtensions | Unset = UNSET
    extras: TextureExtras | Unset = UNSET
    name: str | Unset = UNSET
    sampler: int | Unset = UNSET
    source: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        name = self.name

        sampler = self.sampler

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if name is not UNSET:
            field_dict["name"] = name
        if sampler is not UNSET:
            field_dict["sampler"] = sampler
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.texture_extensions import TextureExtensions
        from ..models.texture_extras import TextureExtras

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: TextureExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = TextureExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: TextureExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = TextureExtras.from_dict(_extras)

        name = d.pop("name", UNSET)

        sampler = d.pop("sampler", UNSET)

        source = d.pop("source", UNSET)

        texture = cls(
            extensions=extensions,
            extras=extras,
            name=name,
            sampler=sampler,
            source=source,
        )

        texture.additional_properties = d
        return texture

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
