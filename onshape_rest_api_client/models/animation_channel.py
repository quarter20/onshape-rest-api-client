from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.animation_channel_extensions import AnimationChannelExtensions
    from ..models.animation_channel_extras import AnimationChannelExtras
    from ..models.animation_channel_target import AnimationChannelTarget


T = TypeVar("T", bound="AnimationChannel")


@_attrs_define
class AnimationChannel:
    """
    Attributes:
        extensions (AnimationChannelExtensions | Unset):
        extras (AnimationChannelExtras | Unset):
        sampler (int | Unset):
        target (AnimationChannelTarget | Unset):
    """

    extensions: AnimationChannelExtensions | Unset = UNSET
    extras: AnimationChannelExtras | Unset = UNSET
    sampler: int | Unset = UNSET
    target: AnimationChannelTarget | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        sampler = self.sampler

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if sampler is not UNSET:
            field_dict["sampler"] = sampler
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.animation_channel_extensions import AnimationChannelExtensions
        from ..models.animation_channel_extras import AnimationChannelExtras
        from ..models.animation_channel_target import AnimationChannelTarget

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: AnimationChannelExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = AnimationChannelExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: AnimationChannelExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = AnimationChannelExtras.from_dict(_extras)

        sampler = d.pop("sampler", UNSET)

        _target = d.pop("target", UNSET)
        target: AnimationChannelTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = AnimationChannelTarget.from_dict(_target)

        animation_channel = cls(
            extensions=extensions,
            extras=extras,
            sampler=sampler,
            target=target,
        )

        animation_channel.additional_properties = d
        return animation_channel

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
