from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.camera_extensions import CameraExtensions
    from ..models.camera_extras import CameraExtras
    from ..models.camera_orthographic import CameraOrthographic
    from ..models.camera_perspective import CameraPerspective


T = TypeVar("T", bound="Camera")


@_attrs_define
class Camera:
    """
    Attributes:
        extensions (CameraExtensions | Unset):
        extras (CameraExtras | Unset):
        name (str | Unset):
        orthographic (CameraOrthographic | Unset):
        perspective (CameraPerspective | Unset):
        type_ (str | Unset):
    """

    extensions: CameraExtensions | Unset = UNSET
    extras: CameraExtras | Unset = UNSET
    name: str | Unset = UNSET
    orthographic: CameraOrthographic | Unset = UNSET
    perspective: CameraPerspective | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        name = self.name

        orthographic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.orthographic, Unset):
            orthographic = self.orthographic.to_dict()

        perspective: dict[str, Any] | Unset = UNSET
        if not isinstance(self.perspective, Unset):
            perspective = self.perspective.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if name is not UNSET:
            field_dict["name"] = name
        if orthographic is not UNSET:
            field_dict["orthographic"] = orthographic
        if perspective is not UNSET:
            field_dict["perspective"] = perspective
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.camera_extensions import CameraExtensions
        from ..models.camera_extras import CameraExtras
        from ..models.camera_orthographic import CameraOrthographic
        from ..models.camera_perspective import CameraPerspective

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: CameraExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = CameraExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: CameraExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = CameraExtras.from_dict(_extras)

        name = d.pop("name", UNSET)

        _orthographic = d.pop("orthographic", UNSET)
        orthographic: CameraOrthographic | Unset
        if isinstance(_orthographic, Unset):
            orthographic = UNSET
        else:
            orthographic = CameraOrthographic.from_dict(_orthographic)

        _perspective = d.pop("perspective", UNSET)
        perspective: CameraPerspective | Unset
        if isinstance(_perspective, Unset):
            perspective = UNSET
        else:
            perspective = CameraPerspective.from_dict(_perspective)

        type_ = d.pop("type", UNSET)

        camera = cls(
            extensions=extensions,
            extras=extras,
            name=name,
            orthographic=orthographic,
            perspective=perspective,
            type_=type_,
        )

        camera.additional_properties = d
        return camera

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
