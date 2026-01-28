from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_extensions import NodeExtensions
    from ..models.node_extras import NodeExtras


T = TypeVar("T", bound="Node")


@_attrs_define
class Node:
    """
    Attributes:
        camera (int | Unset):
        children (list[int] | Unset):
        extensions (NodeExtensions | Unset):
        extras (NodeExtras | Unset):
        matrix (list[float] | Unset):
        mesh (int | Unset):
        name (str | Unset):
        rotation (list[float] | Unset):
        scale (list[float] | Unset):
        skin (int | Unset):
        translation (list[float] | Unset):
        weights (list[float] | Unset):
    """

    camera: int | Unset = UNSET
    children: list[int] | Unset = UNSET
    extensions: NodeExtensions | Unset = UNSET
    extras: NodeExtras | Unset = UNSET
    matrix: list[float] | Unset = UNSET
    mesh: int | Unset = UNSET
    name: str | Unset = UNSET
    rotation: list[float] | Unset = UNSET
    scale: list[float] | Unset = UNSET
    skin: int | Unset = UNSET
    translation: list[float] | Unset = UNSET
    weights: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        camera = self.camera

        children: list[int] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = self.children

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        matrix: list[float] | Unset = UNSET
        if not isinstance(self.matrix, Unset):
            matrix = self.matrix

        mesh = self.mesh

        name = self.name

        rotation: list[float] | Unset = UNSET
        if not isinstance(self.rotation, Unset):
            rotation = self.rotation

        scale: list[float] | Unset = UNSET
        if not isinstance(self.scale, Unset):
            scale = self.scale

        skin = self.skin

        translation: list[float] | Unset = UNSET
        if not isinstance(self.translation, Unset):
            translation = self.translation

        weights: list[float] | Unset = UNSET
        if not isinstance(self.weights, Unset):
            weights = self.weights

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if camera is not UNSET:
            field_dict["camera"] = camera
        if children is not UNSET:
            field_dict["children"] = children
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if matrix is not UNSET:
            field_dict["matrix"] = matrix
        if mesh is not UNSET:
            field_dict["mesh"] = mesh
        if name is not UNSET:
            field_dict["name"] = name
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
        if scale is not UNSET:
            field_dict["scale"] = scale
        if skin is not UNSET:
            field_dict["skin"] = skin
        if translation is not UNSET:
            field_dict["translation"] = translation
        if weights is not UNSET:
            field_dict["weights"] = weights

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_extensions import NodeExtensions
        from ..models.node_extras import NodeExtras

        d = dict(src_dict)
        camera = d.pop("camera", UNSET)

        children = cast(list[int], d.pop("children", UNSET))

        _extensions = d.pop("extensions", UNSET)
        extensions: NodeExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = NodeExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: NodeExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = NodeExtras.from_dict(_extras)

        matrix = cast(list[float], d.pop("matrix", UNSET))

        mesh = d.pop("mesh", UNSET)

        name = d.pop("name", UNSET)

        rotation = cast(list[float], d.pop("rotation", UNSET))

        scale = cast(list[float], d.pop("scale", UNSET))

        skin = d.pop("skin", UNSET)

        translation = cast(list[float], d.pop("translation", UNSET))

        weights = cast(list[float], d.pop("weights", UNSET))

        node = cls(
            camera=camera,
            children=children,
            extensions=extensions,
            extras=extras,
            matrix=matrix,
            mesh=mesh,
            name=name,
            rotation=rotation,
            scale=scale,
            skin=skin,
            translation=translation,
            weights=weights,
        )

        node.additional_properties = d
        return node

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
