from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.camera_orthographic_extensions import CameraOrthographicExtensions
    from ..models.camera_orthographic_extras import CameraOrthographicExtras


T = TypeVar("T", bound="CameraOrthographic")


@_attrs_define
class CameraOrthographic:
    """
    Attributes:
        extensions (CameraOrthographicExtensions | Unset):
        extras (CameraOrthographicExtras | Unset):
        xmag (float | Unset):
        ymag (float | Unset):
        zfar (float | Unset):
        znear (float | Unset):
    """

    extensions: CameraOrthographicExtensions | Unset = UNSET
    extras: CameraOrthographicExtras | Unset = UNSET
    xmag: float | Unset = UNSET
    ymag: float | Unset = UNSET
    zfar: float | Unset = UNSET
    znear: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        xmag = self.xmag

        ymag = self.ymag

        zfar = self.zfar

        znear = self.znear

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if xmag is not UNSET:
            field_dict["xmag"] = xmag
        if ymag is not UNSET:
            field_dict["ymag"] = ymag
        if zfar is not UNSET:
            field_dict["zfar"] = zfar
        if znear is not UNSET:
            field_dict["znear"] = znear

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.camera_orthographic_extensions import CameraOrthographicExtensions
        from ..models.camera_orthographic_extras import CameraOrthographicExtras

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: CameraOrthographicExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = CameraOrthographicExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: CameraOrthographicExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = CameraOrthographicExtras.from_dict(_extras)

        xmag = d.pop("xmag", UNSET)

        ymag = d.pop("ymag", UNSET)

        zfar = d.pop("zfar", UNSET)

        znear = d.pop("znear", UNSET)

        camera_orthographic = cls(
            extensions=extensions,
            extras=extras,
            xmag=xmag,
            ymag=ymag,
            zfar=zfar,
            znear=znear,
        )

        camera_orthographic.additional_properties = d
        return camera_orthographic

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
