from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_matrix_3x3340 import BTMatrix3X3340


T = TypeVar("T", bound="BTImageMapping3821")


@_attrs_define
class BTImageMapping3821:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        deterministic_ids (list[str] | Unset):
        uv_transform (BTMatrix3X3340 | Unset):
    """

    bt_type: str | Unset = UNSET
    deterministic_ids: list[str] | Unset = UNSET
    uv_transform: BTMatrix3X3340 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        deterministic_ids: list[str] | Unset = UNSET
        if not isinstance(self.deterministic_ids, Unset):
            deterministic_ids = self.deterministic_ids

        uv_transform: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uv_transform, Unset):
            uv_transform = self.uv_transform.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if deterministic_ids is not UNSET:
            field_dict["deterministicIds"] = deterministic_ids
        if uv_transform is not UNSET:
            field_dict["uvTransform"] = uv_transform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_matrix_3x3340 import BTMatrix3X3340

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        deterministic_ids = cast(list[str], d.pop("deterministicIds", UNSET))

        _uv_transform = d.pop("uvTransform", UNSET)
        uv_transform: BTMatrix3X3340 | Unset
        if isinstance(_uv_transform, Unset):
            uv_transform = UNSET
        else:
            uv_transform = BTMatrix3X3340.from_dict(_uv_transform)

        bt_image_mapping_3821 = cls(
            bt_type=bt_type,
            deterministic_ids=deterministic_ids,
            uv_transform=uv_transform,
        )

        bt_image_mapping_3821.additional_properties = d
        return bt_image_mapping_3821

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
