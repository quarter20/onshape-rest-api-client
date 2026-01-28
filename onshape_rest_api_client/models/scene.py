from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scene_extensions import SceneExtensions
    from ..models.scene_extras import SceneExtras


T = TypeVar("T", bound="Scene")


@_attrs_define
class Scene:
    """
    Attributes:
        extensions (SceneExtensions | Unset):
        extras (SceneExtras | Unset):
        name (str | Unset):
        nodes (list[int] | Unset):
    """

    extensions: SceneExtensions | Unset = UNSET
    extras: SceneExtras | Unset = UNSET
    name: str | Unset = UNSET
    nodes: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        name = self.name

        nodes: list[int] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if name is not UNSET:
            field_dict["name"] = name
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scene_extensions import SceneExtensions
        from ..models.scene_extras import SceneExtras

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: SceneExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = SceneExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: SceneExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = SceneExtras.from_dict(_extras)

        name = d.pop("name", UNSET)

        nodes = cast(list[int], d.pop("nodes", UNSET))

        scene = cls(
            extensions=extensions,
            extras=extras,
            name=name,
            nodes=nodes,
        )

        scene.additional_properties = d
        return scene

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
