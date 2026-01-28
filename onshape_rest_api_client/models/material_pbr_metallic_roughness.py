from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.material_pbr_metallic_roughness_extensions import MaterialPbrMetallicRoughnessExtensions
    from ..models.material_pbr_metallic_roughness_extras import MaterialPbrMetallicRoughnessExtras
    from ..models.texture_info import TextureInfo


T = TypeVar("T", bound="MaterialPbrMetallicRoughness")


@_attrs_define
class MaterialPbrMetallicRoughness:
    """
    Attributes:
        base_color_factor (list[float] | Unset):
        base_color_texture (TextureInfo | Unset):
        extensions (MaterialPbrMetallicRoughnessExtensions | Unset):
        extras (MaterialPbrMetallicRoughnessExtras | Unset):
        metallic_factor (float | Unset):
        metallic_roughness_texture (TextureInfo | Unset):
        roughness_factor (float | Unset):
    """

    base_color_factor: list[float] | Unset = UNSET
    base_color_texture: TextureInfo | Unset = UNSET
    extensions: MaterialPbrMetallicRoughnessExtensions | Unset = UNSET
    extras: MaterialPbrMetallicRoughnessExtras | Unset = UNSET
    metallic_factor: float | Unset = UNSET
    metallic_roughness_texture: TextureInfo | Unset = UNSET
    roughness_factor: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_color_factor: list[float] | Unset = UNSET
        if not isinstance(self.base_color_factor, Unset):
            base_color_factor = self.base_color_factor

        base_color_texture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_color_texture, Unset):
            base_color_texture = self.base_color_texture.to_dict()

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        metallic_factor = self.metallic_factor

        metallic_roughness_texture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metallic_roughness_texture, Unset):
            metallic_roughness_texture = self.metallic_roughness_texture.to_dict()

        roughness_factor = self.roughness_factor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_color_factor is not UNSET:
            field_dict["baseColorFactor"] = base_color_factor
        if base_color_texture is not UNSET:
            field_dict["baseColorTexture"] = base_color_texture
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if metallic_factor is not UNSET:
            field_dict["metallicFactor"] = metallic_factor
        if metallic_roughness_texture is not UNSET:
            field_dict["metallicRoughnessTexture"] = metallic_roughness_texture
        if roughness_factor is not UNSET:
            field_dict["roughnessFactor"] = roughness_factor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.material_pbr_metallic_roughness_extensions import MaterialPbrMetallicRoughnessExtensions
        from ..models.material_pbr_metallic_roughness_extras import MaterialPbrMetallicRoughnessExtras
        from ..models.texture_info import TextureInfo

        d = dict(src_dict)
        base_color_factor = cast(list[float], d.pop("baseColorFactor", UNSET))

        _base_color_texture = d.pop("baseColorTexture", UNSET)
        base_color_texture: TextureInfo | Unset
        if isinstance(_base_color_texture, Unset):
            base_color_texture = UNSET
        else:
            base_color_texture = TextureInfo.from_dict(_base_color_texture)

        _extensions = d.pop("extensions", UNSET)
        extensions: MaterialPbrMetallicRoughnessExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = MaterialPbrMetallicRoughnessExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: MaterialPbrMetallicRoughnessExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = MaterialPbrMetallicRoughnessExtras.from_dict(_extras)

        metallic_factor = d.pop("metallicFactor", UNSET)

        _metallic_roughness_texture = d.pop("metallicRoughnessTexture", UNSET)
        metallic_roughness_texture: TextureInfo | Unset
        if isinstance(_metallic_roughness_texture, Unset):
            metallic_roughness_texture = UNSET
        else:
            metallic_roughness_texture = TextureInfo.from_dict(_metallic_roughness_texture)

        roughness_factor = d.pop("roughnessFactor", UNSET)

        material_pbr_metallic_roughness = cls(
            base_color_factor=base_color_factor,
            base_color_texture=base_color_texture,
            extensions=extensions,
            extras=extras,
            metallic_factor=metallic_factor,
            metallic_roughness_texture=metallic_roughness_texture,
            roughness_factor=roughness_factor,
        )

        material_pbr_metallic_roughness.additional_properties = d
        return material_pbr_metallic_roughness

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
