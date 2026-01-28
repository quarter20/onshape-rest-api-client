from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.camera_perspective_extensions import CameraPerspectiveExtensions
    from ..models.camera_perspective_extras import CameraPerspectiveExtras


T = TypeVar("T", bound="CameraPerspective")


@_attrs_define
class CameraPerspective:
    """
    Attributes:
        aspect_ratio (float | Unset):
        extensions (CameraPerspectiveExtensions | Unset):
        extras (CameraPerspectiveExtras | Unset):
        yfov (float | Unset):
        zfar (float | Unset):
        znear (float | Unset):
    """

    aspect_ratio: float | Unset = UNSET
    extensions: CameraPerspectiveExtensions | Unset = UNSET
    extras: CameraPerspectiveExtras | Unset = UNSET
    yfov: float | Unset = UNSET
    zfar: float | Unset = UNSET
    znear: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aspect_ratio = self.aspect_ratio

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        yfov = self.yfov

        zfar = self.zfar

        znear = self.znear

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspect_ratio is not UNSET:
            field_dict["aspectRatio"] = aspect_ratio
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if yfov is not UNSET:
            field_dict["yfov"] = yfov
        if zfar is not UNSET:
            field_dict["zfar"] = zfar
        if znear is not UNSET:
            field_dict["znear"] = znear

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.camera_perspective_extensions import CameraPerspectiveExtensions
        from ..models.camera_perspective_extras import CameraPerspectiveExtras

        d = dict(src_dict)
        aspect_ratio = d.pop("aspectRatio", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: CameraPerspectiveExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = CameraPerspectiveExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: CameraPerspectiveExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = CameraPerspectiveExtras.from_dict(_extras)

        yfov = d.pop("yfov", UNSET)

        zfar = d.pop("zfar", UNSET)

        znear = d.pop("znear", UNSET)

        camera_perspective = cls(
            aspect_ratio=aspect_ratio,
            extensions=extensions,
            extras=extras,
            yfov=yfov,
            zfar=zfar,
            znear=znear,
        )

        camera_perspective.additional_properties = d
        return camera_perspective

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
