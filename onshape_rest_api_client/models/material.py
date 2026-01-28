from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.material_extensions import MaterialExtensions
    from ..models.material_extras import MaterialExtras
    from ..models.material_normal_texture_info import MaterialNormalTextureInfo
    from ..models.material_occlusion_texture_info import MaterialOcclusionTextureInfo
    from ..models.material_pbr_metallic_roughness import MaterialPbrMetallicRoughness
    from ..models.texture_info import TextureInfo


T = TypeVar("T", bound="Material")


@_attrs_define
class Material:
    """
    Attributes:
        alpha_cutoff (float | Unset):
        alpha_mode (str | Unset):
        double_sided (bool | Unset):
        emissive_factor (list[float] | Unset):
        emissive_texture (TextureInfo | Unset):
        extensions (MaterialExtensions | Unset):
        extras (MaterialExtras | Unset):
        name (str | Unset):
        normal_texture (MaterialNormalTextureInfo | Unset):
        occlusion_texture (MaterialOcclusionTextureInfo | Unset):
        pbr_metallic_roughness (MaterialPbrMetallicRoughness | Unset):
    """

    alpha_cutoff: float | Unset = UNSET
    alpha_mode: str | Unset = UNSET
    double_sided: bool | Unset = UNSET
    emissive_factor: list[float] | Unset = UNSET
    emissive_texture: TextureInfo | Unset = UNSET
    extensions: MaterialExtensions | Unset = UNSET
    extras: MaterialExtras | Unset = UNSET
    name: str | Unset = UNSET
    normal_texture: MaterialNormalTextureInfo | Unset = UNSET
    occlusion_texture: MaterialOcclusionTextureInfo | Unset = UNSET
    pbr_metallic_roughness: MaterialPbrMetallicRoughness | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alpha_cutoff = self.alpha_cutoff

        alpha_mode = self.alpha_mode

        double_sided = self.double_sided

        emissive_factor: list[float] | Unset = UNSET
        if not isinstance(self.emissive_factor, Unset):
            emissive_factor = self.emissive_factor

        emissive_texture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.emissive_texture, Unset):
            emissive_texture = self.emissive_texture.to_dict()

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        name = self.name

        normal_texture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.normal_texture, Unset):
            normal_texture = self.normal_texture.to_dict()

        occlusion_texture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occlusion_texture, Unset):
            occlusion_texture = self.occlusion_texture.to_dict()

        pbr_metallic_roughness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pbr_metallic_roughness, Unset):
            pbr_metallic_roughness = self.pbr_metallic_roughness.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alpha_cutoff is not UNSET:
            field_dict["alphaCutoff"] = alpha_cutoff
        if alpha_mode is not UNSET:
            field_dict["alphaMode"] = alpha_mode
        if double_sided is not UNSET:
            field_dict["doubleSided"] = double_sided
        if emissive_factor is not UNSET:
            field_dict["emissiveFactor"] = emissive_factor
        if emissive_texture is not UNSET:
            field_dict["emissiveTexture"] = emissive_texture
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if name is not UNSET:
            field_dict["name"] = name
        if normal_texture is not UNSET:
            field_dict["normalTexture"] = normal_texture
        if occlusion_texture is not UNSET:
            field_dict["occlusionTexture"] = occlusion_texture
        if pbr_metallic_roughness is not UNSET:
            field_dict["pbrMetallicRoughness"] = pbr_metallic_roughness

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.material_extensions import MaterialExtensions
        from ..models.material_extras import MaterialExtras
        from ..models.material_normal_texture_info import MaterialNormalTextureInfo
        from ..models.material_occlusion_texture_info import MaterialOcclusionTextureInfo
        from ..models.material_pbr_metallic_roughness import MaterialPbrMetallicRoughness
        from ..models.texture_info import TextureInfo

        d = dict(src_dict)
        alpha_cutoff = d.pop("alphaCutoff", UNSET)

        alpha_mode = d.pop("alphaMode", UNSET)

        double_sided = d.pop("doubleSided", UNSET)

        emissive_factor = cast(list[float], d.pop("emissiveFactor", UNSET))

        _emissive_texture = d.pop("emissiveTexture", UNSET)
        emissive_texture: TextureInfo | Unset
        if isinstance(_emissive_texture, Unset):
            emissive_texture = UNSET
        else:
            emissive_texture = TextureInfo.from_dict(_emissive_texture)

        _extensions = d.pop("extensions", UNSET)
        extensions: MaterialExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = MaterialExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: MaterialExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = MaterialExtras.from_dict(_extras)

        name = d.pop("name", UNSET)

        _normal_texture = d.pop("normalTexture", UNSET)
        normal_texture: MaterialNormalTextureInfo | Unset
        if isinstance(_normal_texture, Unset):
            normal_texture = UNSET
        else:
            normal_texture = MaterialNormalTextureInfo.from_dict(_normal_texture)

        _occlusion_texture = d.pop("occlusionTexture", UNSET)
        occlusion_texture: MaterialOcclusionTextureInfo | Unset
        if isinstance(_occlusion_texture, Unset):
            occlusion_texture = UNSET
        else:
            occlusion_texture = MaterialOcclusionTextureInfo.from_dict(_occlusion_texture)

        _pbr_metallic_roughness = d.pop("pbrMetallicRoughness", UNSET)
        pbr_metallic_roughness: MaterialPbrMetallicRoughness | Unset
        if isinstance(_pbr_metallic_roughness, Unset):
            pbr_metallic_roughness = UNSET
        else:
            pbr_metallic_roughness = MaterialPbrMetallicRoughness.from_dict(_pbr_metallic_roughness)

        material = cls(
            alpha_cutoff=alpha_cutoff,
            alpha_mode=alpha_mode,
            double_sided=double_sided,
            emissive_factor=emissive_factor,
            emissive_texture=emissive_texture,
            extensions=extensions,
            extras=extras,
            name=name,
            normal_texture=normal_texture,
            occlusion_texture=occlusion_texture,
            pbr_metallic_roughness=pbr_metallic_roughness,
        )

        material.additional_properties = d
        return material

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
