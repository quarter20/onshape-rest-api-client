from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.animation_channel import AnimationChannel
    from ..models.animation_extensions import AnimationExtensions
    from ..models.animation_extras import AnimationExtras
    from ..models.animation_sampler import AnimationSampler


T = TypeVar("T", bound="Animation")


@_attrs_define
class Animation:
    """
    Attributes:
        channels (list[AnimationChannel] | Unset):
        extensions (AnimationExtensions | Unset):
        extras (AnimationExtras | Unset):
        name (str | Unset):
        samplers (list[AnimationSampler] | Unset):
    """

    channels: list[AnimationChannel] | Unset = UNSET
    extensions: AnimationExtensions | Unset = UNSET
    extras: AnimationExtras | Unset = UNSET
    name: str | Unset = UNSET
    samplers: list[AnimationSampler] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        name = self.name

        samplers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.samplers, Unset):
            samplers = []
            for samplers_item_data in self.samplers:
                samplers_item = samplers_item_data.to_dict()
                samplers.append(samplers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if name is not UNSET:
            field_dict["name"] = name
        if samplers is not UNSET:
            field_dict["samplers"] = samplers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.animation_channel import AnimationChannel
        from ..models.animation_extensions import AnimationExtensions
        from ..models.animation_extras import AnimationExtras
        from ..models.animation_sampler import AnimationSampler

        d = dict(src_dict)
        _channels = d.pop("channels", UNSET)
        channels: list[AnimationChannel] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = AnimationChannel.from_dict(channels_item_data)

                channels.append(channels_item)

        _extensions = d.pop("extensions", UNSET)
        extensions: AnimationExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = AnimationExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: AnimationExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = AnimationExtras.from_dict(_extras)

        name = d.pop("name", UNSET)

        _samplers = d.pop("samplers", UNSET)
        samplers: list[AnimationSampler] | Unset = UNSET
        if _samplers is not UNSET:
            samplers = []
            for samplers_item_data in _samplers:
                samplers_item = AnimationSampler.from_dict(samplers_item_data)

                samplers.append(samplers_item)

        animation = cls(
            channels=channels,
            extensions=extensions,
            extras=extras,
            name=name,
            samplers=samplers,
        )

        animation.additional_properties = d
        return animation

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
