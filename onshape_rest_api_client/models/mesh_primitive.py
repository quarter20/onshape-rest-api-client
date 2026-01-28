from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mesh_primitive_attributes import MeshPrimitiveAttributes
    from ..models.mesh_primitive_extensions import MeshPrimitiveExtensions
    from ..models.mesh_primitive_extras import MeshPrimitiveExtras
    from ..models.mesh_primitive_targets_item import MeshPrimitiveTargetsItem


T = TypeVar("T", bound="MeshPrimitive")


@_attrs_define
class MeshPrimitive:
    """
    Attributes:
        attributes (MeshPrimitiveAttributes | Unset):
        extensions (MeshPrimitiveExtensions | Unset):
        extras (MeshPrimitiveExtras | Unset):
        indices (int | Unset):
        material (int | Unset):
        mode (int | Unset):
        targets (list[MeshPrimitiveTargetsItem] | Unset):
    """

    attributes: MeshPrimitiveAttributes | Unset = UNSET
    extensions: MeshPrimitiveExtensions | Unset = UNSET
    extras: MeshPrimitiveExtras | Unset = UNSET
    indices: int | Unset = UNSET
    material: int | Unset = UNSET
    mode: int | Unset = UNSET
    targets: list[MeshPrimitiveTargetsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        indices = self.indices

        material = self.material

        mode = self.mode

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if indices is not UNSET:
            field_dict["indices"] = indices
        if material is not UNSET:
            field_dict["material"] = material
        if mode is not UNSET:
            field_dict["mode"] = mode
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mesh_primitive_attributes import MeshPrimitiveAttributes
        from ..models.mesh_primitive_extensions import MeshPrimitiveExtensions
        from ..models.mesh_primitive_extras import MeshPrimitiveExtras
        from ..models.mesh_primitive_targets_item import MeshPrimitiveTargetsItem

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: MeshPrimitiveAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = MeshPrimitiveAttributes.from_dict(_attributes)

        _extensions = d.pop("extensions", UNSET)
        extensions: MeshPrimitiveExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = MeshPrimitiveExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: MeshPrimitiveExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = MeshPrimitiveExtras.from_dict(_extras)

        indices = d.pop("indices", UNSET)

        material = d.pop("material", UNSET)

        mode = d.pop("mode", UNSET)

        _targets = d.pop("targets", UNSET)
        targets: list[MeshPrimitiveTargetsItem] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = MeshPrimitiveTargetsItem.from_dict(targets_item_data)

                targets.append(targets_item)

        mesh_primitive = cls(
            attributes=attributes,
            extensions=extensions,
            extras=extras,
            indices=indices,
            material=material,
            mode=mode,
            targets=targets,
        )

        mesh_primitive.additional_properties = d
        return mesh_primitive

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
