from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.animation_sampler_extensions import AnimationSamplerExtensions
    from ..models.animation_sampler_extras import AnimationSamplerExtras


T = TypeVar("T", bound="AnimationSampler")


@_attrs_define
class AnimationSampler:
    """
    Attributes:
        extensions (AnimationSamplerExtensions | Unset):
        extras (AnimationSamplerExtras | Unset):
        input_ (int | Unset):
        interpolation (str | Unset):
        output (int | Unset):
    """

    extensions: AnimationSamplerExtensions | Unset = UNSET
    extras: AnimationSamplerExtras | Unset = UNSET
    input_: int | Unset = UNSET
    interpolation: str | Unset = UNSET
    output: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        input_ = self.input_

        interpolation = self.interpolation

        output = self.output

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if input_ is not UNSET:
            field_dict["input"] = input_
        if interpolation is not UNSET:
            field_dict["interpolation"] = interpolation
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.animation_sampler_extensions import AnimationSamplerExtensions
        from ..models.animation_sampler_extras import AnimationSamplerExtras

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: AnimationSamplerExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = AnimationSamplerExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: AnimationSamplerExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = AnimationSamplerExtras.from_dict(_extras)

        input_ = d.pop("input", UNSET)

        interpolation = d.pop("interpolation", UNSET)

        output = d.pop("output", UNSET)

        animation_sampler = cls(
            extensions=extensions,
            extras=extras,
            input_=input_,
            interpolation=interpolation,
            output=output,
        )

        animation_sampler.additional_properties = d
        return animation_sampler

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
