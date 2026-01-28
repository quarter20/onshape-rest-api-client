from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.interpolation import Interpolation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accessor_model import AccessorModel


T = TypeVar("T", bound="Sampler")


@_attrs_define
class Sampler:
    """
    Attributes:
        input_ (AccessorModel | Unset):
        interpolation (Interpolation | Unset):
        output (AccessorModel | Unset):
    """

    input_: AccessorModel | Unset = UNSET
    interpolation: Interpolation | Unset = UNSET
    output: AccessorModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        interpolation: str | Unset = UNSET
        if not isinstance(self.interpolation, Unset):
            interpolation = self.interpolation.value

        output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_ is not UNSET:
            field_dict["input"] = input_
        if interpolation is not UNSET:
            field_dict["interpolation"] = interpolation
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accessor_model import AccessorModel

        d = dict(src_dict)
        _input_ = d.pop("input", UNSET)
        input_: AccessorModel | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = AccessorModel.from_dict(_input_)

        _interpolation = d.pop("interpolation", UNSET)
        interpolation: Interpolation | Unset
        if isinstance(_interpolation, Unset):
            interpolation = UNSET
        else:
            interpolation = Interpolation(_interpolation)

        _output = d.pop("output", UNSET)
        output: AccessorModel | Unset
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = AccessorModel.from_dict(_output)

        sampler = cls(
            input_=input_,
            interpolation=interpolation,
            output=output,
        )

        sampler.additional_properties = d
        return sampler

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
