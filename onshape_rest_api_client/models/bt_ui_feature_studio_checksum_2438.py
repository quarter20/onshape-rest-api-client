from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_microversion_id_366 import BTMicroversionId366


T = TypeVar("T", bound="BTUiFeatureStudioChecksum2438")


@_attrs_define
class BTUiFeatureStudioChecksum2438:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        crc32 (int | Unset):
        microversion (BTMicroversionId366 | Unset):
    """

    bt_type: str | Unset = UNSET
    crc32: int | Unset = UNSET
    microversion: BTMicroversionId366 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        crc32 = self.crc32

        microversion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion, Unset):
            microversion = self.microversion.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if crc32 is not UNSET:
            field_dict["crc32"] = crc32
        if microversion is not UNSET:
            field_dict["microversion"] = microversion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_microversion_id_366 import BTMicroversionId366

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        crc32 = d.pop("crc32", UNSET)

        _microversion = d.pop("microversion", UNSET)
        microversion: BTMicroversionId366 | Unset
        if isinstance(_microversion, Unset):
            microversion = UNSET
        else:
            microversion = BTMicroversionId366.from_dict(_microversion)

        bt_ui_feature_studio_checksum_2438 = cls(
            bt_type=bt_type,
            crc32=crc32,
            microversion=microversion,
        )

        bt_ui_feature_studio_checksum_2438.additional_properties = d
        return bt_ui_feature_studio_checksum_2438

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
