from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_microversion_id_366 import BTMicroversionId366
    from ..models.bt_microversion_id_and_configuration_2338 import BTMicroversionIdAndConfiguration2338


T = TypeVar("T", bound="BTFullElementIdAndPartId643")


@_attrs_define
class BTFullElementIdAndPartId643:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        configured (bool | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        microversion_id (BTMicroversionId366 | Unset):
        microversion_id_and_configuration (BTMicroversionIdAndConfiguration2338 | Unset):
        target (BTMicroversionIdAndConfiguration2338 | Unset):
        part_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    configured: bool | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    microversion_id: BTMicroversionId366 | Unset = UNSET
    microversion_id_and_configuration: BTMicroversionIdAndConfiguration2338 | Unset = UNSET
    target: BTMicroversionIdAndConfiguration2338 | Unset = UNSET
    part_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        configured = self.configured

        document_id = self.document_id

        element_id = self.element_id

        microversion_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id, Unset):
            microversion_id = self.microversion_id.to_dict()

        microversion_id_and_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id_and_configuration, Unset):
            microversion_id_and_configuration = self.microversion_id_and_configuration.to_dict()

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        part_id = self.part_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if configured is not UNSET:
            field_dict["configured"] = configured
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if microversion_id_and_configuration is not UNSET:
            field_dict["microversionIdAndConfiguration"] = microversion_id_and_configuration
        if target is not UNSET:
            field_dict["target"] = target
        if part_id is not UNSET:
            field_dict["partId"] = part_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_microversion_id_366 import BTMicroversionId366
        from ..models.bt_microversion_id_and_configuration_2338 import BTMicroversionIdAndConfiguration2338

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        configured = d.pop("configured", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        _microversion_id = d.pop("microversionId", UNSET)
        microversion_id: BTMicroversionId366 | Unset
        if isinstance(_microversion_id, Unset):
            microversion_id = UNSET
        else:
            microversion_id = BTMicroversionId366.from_dict(_microversion_id)

        _microversion_id_and_configuration = d.pop("microversionIdAndConfiguration", UNSET)
        microversion_id_and_configuration: BTMicroversionIdAndConfiguration2338 | Unset
        if isinstance(_microversion_id_and_configuration, Unset):
            microversion_id_and_configuration = UNSET
        else:
            microversion_id_and_configuration = BTMicroversionIdAndConfiguration2338.from_dict(
                _microversion_id_and_configuration
            )

        _target = d.pop("target", UNSET)
        target: BTMicroversionIdAndConfiguration2338 | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = BTMicroversionIdAndConfiguration2338.from_dict(_target)

        part_id = d.pop("partId", UNSET)

        bt_full_element_id_and_part_id_643 = cls(
            bt_type=bt_type,
            configured=configured,
            document_id=document_id,
            element_id=element_id,
            microversion_id=microversion_id,
            microversion_id_and_configuration=microversion_id_and_configuration,
            target=target,
            part_id=part_id,
        )

        bt_full_element_id_and_part_id_643.additional_properties = d
        return bt_full_element_id_and_part_id_643

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
