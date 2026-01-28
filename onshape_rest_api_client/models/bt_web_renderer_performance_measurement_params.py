from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTWebRendererPerformanceMeasurementParams")


@_attrs_define
class BTWebRendererPerformanceMeasurementParams:
    """
    Attributes:
        lines_per_second (float | Unset):
        renderer (str | Unset):
        triangles_per_second (float | Unset):
        vendor (str | Unset):
    """

    lines_per_second: float | Unset = UNSET
    renderer: str | Unset = UNSET
    triangles_per_second: float | Unset = UNSET
    vendor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lines_per_second = self.lines_per_second

        renderer = self.renderer

        triangles_per_second = self.triangles_per_second

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lines_per_second is not UNSET:
            field_dict["linesPerSecond"] = lines_per_second
        if renderer is not UNSET:
            field_dict["renderer"] = renderer
        if triangles_per_second is not UNSET:
            field_dict["trianglesPerSecond"] = triangles_per_second
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lines_per_second = d.pop("linesPerSecond", UNSET)

        renderer = d.pop("renderer", UNSET)

        triangles_per_second = d.pop("trianglesPerSecond", UNSET)

        vendor = d.pop("vendor", UNSET)

        bt_web_renderer_performance_measurement_params = cls(
            lines_per_second=lines_per_second,
            renderer=renderer,
            triangles_per_second=triangles_per_second,
            vendor=vendor,
        )

        bt_web_renderer_performance_measurement_params.additional_properties = d
        return bt_web_renderer_performance_measurement_params

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
