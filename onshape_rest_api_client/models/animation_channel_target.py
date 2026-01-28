from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.animation_channel_target_extensions import AnimationChannelTargetExtensions
    from ..models.animation_channel_target_extras import AnimationChannelTargetExtras


T = TypeVar("T", bound="AnimationChannelTarget")


@_attrs_define
class AnimationChannelTarget:
    """
    Attributes:
        extensions (AnimationChannelTargetExtensions | Unset):
        extras (AnimationChannelTargetExtras | Unset):
        node (int | Unset):
        path (str | Unset):
    """

    extensions: AnimationChannelTargetExtensions | Unset = UNSET
    extras: AnimationChannelTargetExtras | Unset = UNSET
    node: int | Unset = UNSET
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        node = self.node

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if node is not UNSET:
            field_dict["node"] = node
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.animation_channel_target_extensions import AnimationChannelTargetExtensions
        from ..models.animation_channel_target_extras import AnimationChannelTargetExtras

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: AnimationChannelTargetExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = AnimationChannelTargetExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: AnimationChannelTargetExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = AnimationChannelTargetExtras.from_dict(_extras)

        node = d.pop("node", UNSET)

        path = d.pop("path", UNSET)

        animation_channel_target = cls(
            extensions=extensions,
            extras=extras,
            node=node,
            path=path,
        )

        animation_channel_target.additional_properties = d
        return animation_channel_target

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
