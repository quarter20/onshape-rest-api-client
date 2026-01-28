from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.skin_extensions import SkinExtensions
    from ..models.skin_extras import SkinExtras


T = TypeVar("T", bound="Skin")


@_attrs_define
class Skin:
    """
    Attributes:
        extensions (SkinExtensions | Unset):
        extras (SkinExtras | Unset):
        inverse_bind_matrices (int | Unset):
        joints (list[int] | Unset):
        name (str | Unset):
        skeleton (int | Unset):
    """

    extensions: SkinExtensions | Unset = UNSET
    extras: SkinExtras | Unset = UNSET
    inverse_bind_matrices: int | Unset = UNSET
    joints: list[int] | Unset = UNSET
    name: str | Unset = UNSET
    skeleton: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        inverse_bind_matrices = self.inverse_bind_matrices

        joints: list[int] | Unset = UNSET
        if not isinstance(self.joints, Unset):
            joints = self.joints

        name = self.name

        skeleton = self.skeleton

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if inverse_bind_matrices is not UNSET:
            field_dict["inverseBindMatrices"] = inverse_bind_matrices
        if joints is not UNSET:
            field_dict["joints"] = joints
        if name is not UNSET:
            field_dict["name"] = name
        if skeleton is not UNSET:
            field_dict["skeleton"] = skeleton

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.skin_extensions import SkinExtensions
        from ..models.skin_extras import SkinExtras

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: SkinExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = SkinExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: SkinExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = SkinExtras.from_dict(_extras)

        inverse_bind_matrices = d.pop("inverseBindMatrices", UNSET)

        joints = cast(list[int], d.pop("joints", UNSET))

        name = d.pop("name", UNSET)

        skeleton = d.pop("skeleton", UNSET)

        skin = cls(
            extensions=extensions,
            extras=extras,
            inverse_bind_matrices=inverse_bind_matrices,
            joints=joints,
            name=name,
            skeleton=skeleton,
        )

        skin.additional_properties = d
        return skin

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
