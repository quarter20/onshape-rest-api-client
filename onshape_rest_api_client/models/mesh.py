from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mesh_extensions import MeshExtensions
    from ..models.mesh_extras import MeshExtras
    from ..models.mesh_primitive import MeshPrimitive


T = TypeVar("T", bound="Mesh")


@_attrs_define
class Mesh:
    """
    Attributes:
        extensions (MeshExtensions | Unset):
        extras (MeshExtras | Unset):
        name (str | Unset):
        primitives (list[MeshPrimitive] | Unset):
        weights (list[float] | Unset):
    """

    extensions: MeshExtensions | Unset = UNSET
    extras: MeshExtras | Unset = UNSET
    name: str | Unset = UNSET
    primitives: list[MeshPrimitive] | Unset = UNSET
    weights: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        name = self.name

        primitives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.primitives, Unset):
            primitives = []
            for primitives_item_data in self.primitives:
                primitives_item = primitives_item_data.to_dict()
                primitives.append(primitives_item)

        weights: list[float] | Unset = UNSET
        if not isinstance(self.weights, Unset):
            weights = self.weights

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if name is not UNSET:
            field_dict["name"] = name
        if primitives is not UNSET:
            field_dict["primitives"] = primitives
        if weights is not UNSET:
            field_dict["weights"] = weights

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mesh_extensions import MeshExtensions
        from ..models.mesh_extras import MeshExtras
        from ..models.mesh_primitive import MeshPrimitive

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: MeshExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = MeshExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: MeshExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = MeshExtras.from_dict(_extras)

        name = d.pop("name", UNSET)

        _primitives = d.pop("primitives", UNSET)
        primitives: list[MeshPrimitive] | Unset = UNSET
        if _primitives is not UNSET:
            primitives = []
            for primitives_item_data in _primitives:
                primitives_item = MeshPrimitive.from_dict(primitives_item_data)

                primitives.append(primitives_item)

        weights = cast(list[float], d.pop("weights", UNSET))

        mesh = cls(
            extensions=extensions,
            extras=extras,
            name=name,
            primitives=primitives,
            weights=weights,
        )

        mesh.additional_properties = d
        return mesh

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
