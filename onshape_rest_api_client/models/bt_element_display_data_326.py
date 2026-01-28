from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_annotation_element_display_data_894 import BTAnnotationElementDisplayData894
    from ..models.bt_full_element_id_756 import BTFullElementId756
    from ..models.bt_microversion_id_366 import BTMicroversionId366
    from ..models.bt_microversion_id_and_configuration_interval_2364 import BTMicroversionIdAndConfigurationInterval2364
    from ..models.bt_microversion_id_interval_367 import BTMicroversionIdInterval367


T = TypeVar("T", bound="BTElementDisplayData326")


@_attrs_define
class BTElementDisplayData326:
    """
    Attributes:
        annotations_for_element (BTAnnotationElementDisplayData894 | Unset):
        bt_type (str | Unset): Type of JSON object.
        element_id (str | Unset):
        from_full_element_id (BTFullElementId756 | Unset):
        full_element_id (BTFullElementId756 | Unset):
        incremental (bool | Unset):
        instance_count (int | Unset):
        keep_from_microversion (bool | Unset):
        microversion_id (BTMicroversionId366 | Unset):
        microversion_id_and_configuration_interval (BTMicroversionIdAndConfigurationInterval2364 | Unset):
        microversion_interval (BTMicroversionIdInterval367 | Unset):
        version_for_rasterization (BTElementDisplayData326 | Unset):
    """

    annotations_for_element: BTAnnotationElementDisplayData894 | Unset = UNSET
    bt_type: str | Unset = UNSET
    element_id: str | Unset = UNSET
    from_full_element_id: BTFullElementId756 | Unset = UNSET
    full_element_id: BTFullElementId756 | Unset = UNSET
    incremental: bool | Unset = UNSET
    instance_count: int | Unset = UNSET
    keep_from_microversion: bool | Unset = UNSET
    microversion_id: BTMicroversionId366 | Unset = UNSET
    microversion_id_and_configuration_interval: BTMicroversionIdAndConfigurationInterval2364 | Unset = UNSET
    microversion_interval: BTMicroversionIdInterval367 | Unset = UNSET
    version_for_rasterization: BTElementDisplayData326 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations_for_element: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations_for_element, Unset):
            annotations_for_element = self.annotations_for_element.to_dict()

        bt_type = self.bt_type

        element_id = self.element_id

        from_full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_full_element_id, Unset):
            from_full_element_id = self.from_full_element_id.to_dict()

        full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id, Unset):
            full_element_id = self.full_element_id.to_dict()

        incremental = self.incremental

        instance_count = self.instance_count

        keep_from_microversion = self.keep_from_microversion

        microversion_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id, Unset):
            microversion_id = self.microversion_id.to_dict()

        microversion_id_and_configuration_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id_and_configuration_interval, Unset):
            microversion_id_and_configuration_interval = self.microversion_id_and_configuration_interval.to_dict()

        microversion_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_interval, Unset):
            microversion_interval = self.microversion_interval.to_dict()

        version_for_rasterization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version_for_rasterization, Unset):
            version_for_rasterization = self.version_for_rasterization.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations_for_element is not UNSET:
            field_dict["annotationsForElement"] = annotations_for_element
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if from_full_element_id is not UNSET:
            field_dict["fromFullElementId"] = from_full_element_id
        if full_element_id is not UNSET:
            field_dict["fullElementId"] = full_element_id
        if incremental is not UNSET:
            field_dict["incremental"] = incremental
        if instance_count is not UNSET:
            field_dict["instanceCount"] = instance_count
        if keep_from_microversion is not UNSET:
            field_dict["keepFromMicroversion"] = keep_from_microversion
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if microversion_id_and_configuration_interval is not UNSET:
            field_dict["microversionIdAndConfigurationInterval"] = microversion_id_and_configuration_interval
        if microversion_interval is not UNSET:
            field_dict["microversionInterval"] = microversion_interval
        if version_for_rasterization is not UNSET:
            field_dict["versionForRasterization"] = version_for_rasterization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_annotation_element_display_data_894 import BTAnnotationElementDisplayData894
        from ..models.bt_full_element_id_756 import BTFullElementId756
        from ..models.bt_microversion_id_366 import BTMicroversionId366
        from ..models.bt_microversion_id_and_configuration_interval_2364 import (
            BTMicroversionIdAndConfigurationInterval2364,
        )
        from ..models.bt_microversion_id_interval_367 import BTMicroversionIdInterval367

        d = dict(src_dict)
        _annotations_for_element = d.pop("annotationsForElement", UNSET)
        annotations_for_element: BTAnnotationElementDisplayData894 | Unset
        if isinstance(_annotations_for_element, Unset):
            annotations_for_element = UNSET
        else:
            annotations_for_element = BTAnnotationElementDisplayData894.from_dict(_annotations_for_element)

        bt_type = d.pop("btType", UNSET)

        element_id = d.pop("elementId", UNSET)

        _from_full_element_id = d.pop("fromFullElementId", UNSET)
        from_full_element_id: BTFullElementId756 | Unset
        if isinstance(_from_full_element_id, Unset):
            from_full_element_id = UNSET
        else:
            from_full_element_id = BTFullElementId756.from_dict(_from_full_element_id)

        _full_element_id = d.pop("fullElementId", UNSET)
        full_element_id: BTFullElementId756 | Unset
        if isinstance(_full_element_id, Unset):
            full_element_id = UNSET
        else:
            full_element_id = BTFullElementId756.from_dict(_full_element_id)

        incremental = d.pop("incremental", UNSET)

        instance_count = d.pop("instanceCount", UNSET)

        keep_from_microversion = d.pop("keepFromMicroversion", UNSET)

        _microversion_id = d.pop("microversionId", UNSET)
        microversion_id: BTMicroversionId366 | Unset
        if isinstance(_microversion_id, Unset):
            microversion_id = UNSET
        else:
            microversion_id = BTMicroversionId366.from_dict(_microversion_id)

        _microversion_id_and_configuration_interval = d.pop("microversionIdAndConfigurationInterval", UNSET)
        microversion_id_and_configuration_interval: BTMicroversionIdAndConfigurationInterval2364 | Unset
        if isinstance(_microversion_id_and_configuration_interval, Unset):
            microversion_id_and_configuration_interval = UNSET
        else:
            microversion_id_and_configuration_interval = BTMicroversionIdAndConfigurationInterval2364.from_dict(
                _microversion_id_and_configuration_interval
            )

        _microversion_interval = d.pop("microversionInterval", UNSET)
        microversion_interval: BTMicroversionIdInterval367 | Unset
        if isinstance(_microversion_interval, Unset):
            microversion_interval = UNSET
        else:
            microversion_interval = BTMicroversionIdInterval367.from_dict(_microversion_interval)

        _version_for_rasterization = d.pop("versionForRasterization", UNSET)
        version_for_rasterization: BTElementDisplayData326 | Unset
        if isinstance(_version_for_rasterization, Unset):
            version_for_rasterization = UNSET
        else:
            version_for_rasterization = BTElementDisplayData326.from_dict(_version_for_rasterization)

        bt_element_display_data_326 = cls(
            annotations_for_element=annotations_for_element,
            bt_type=bt_type,
            element_id=element_id,
            from_full_element_id=from_full_element_id,
            full_element_id=full_element_id,
            incremental=incremental,
            instance_count=instance_count,
            keep_from_microversion=keep_from_microversion,
            microversion_id=microversion_id,
            microversion_id_and_configuration_interval=microversion_id_and_configuration_interval,
            microversion_interval=microversion_interval,
            version_for_rasterization=version_for_rasterization,
        )

        bt_element_display_data_326.additional_properties = d
        return bt_element_display_data_326

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
