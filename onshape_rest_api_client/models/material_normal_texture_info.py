from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.material_normal_texture_info_extensions import MaterialNormalTextureInfoExtensions
    from ..models.material_normal_texture_info_extras import MaterialNormalTextureInfoExtras


T = TypeVar("T", bound="MaterialNormalTextureInfo")


@_attrs_define
class MaterialNormalTextureInfo:
    """
    Attributes:
        extensions (MaterialNormalTextureInfoExtensions | Unset):
        extras (MaterialNormalTextureInfoExtras | Unset):
        index (int | Unset):
        scale (float | Unset):
        tex_coord (int | Unset):
    """

    extensions: MaterialNormalTextureInfoExtensions | Unset = UNSET
    extras: MaterialNormalTextureInfoExtras | Unset = UNSET
    index: int | Unset = UNSET
    scale: float | Unset = UNSET
    tex_coord: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        index = self.index

        scale = self.scale

        tex_coord = self.tex_coord

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if index is not UNSET:
            field_dict["index"] = index
        if scale is not UNSET:
            field_dict["scale"] = scale
        if tex_coord is not UNSET:
            field_dict["texCoord"] = tex_coord

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.material_normal_texture_info_extensions import MaterialNormalTextureInfoExtensions
        from ..models.material_normal_texture_info_extras import MaterialNormalTextureInfoExtras

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: MaterialNormalTextureInfoExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = MaterialNormalTextureInfoExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: MaterialNormalTextureInfoExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = MaterialNormalTextureInfoExtras.from_dict(_extras)

        index = d.pop("index", UNSET)

        scale = d.pop("scale", UNSET)

        tex_coord = d.pop("texCoord", UNSET)

        material_normal_texture_info = cls(
            extensions=extensions,
            extras=extras,
            index=index,
            scale=scale,
            tex_coord=tex_coord,
        )

        material_normal_texture_info.additional_properties = d
        return material_normal_texture_info

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
