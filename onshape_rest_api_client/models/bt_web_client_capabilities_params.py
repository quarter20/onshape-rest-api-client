from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTWebClientCapabilitiesParams")


@_attrs_define
class BTWebClientCapabilitiesParams:
    """
    Attributes:
        angle_instanced_arrays (bool | Unset):
        client_browser_storage_quota (float | Unset):
        client_browser_storage_used (float | Unset):
        compressed_texture_s3_tc (bool | Unset):
        depth_texture (bool | Unset):
        device_pixel_ratio (float | Unset):
        draw_buffers (bool | Unset):
        ext_texture_filter_anisotropic (bool | Unset):
        has_3_d_mouse (bool | Unset):
        oes_element_index_uint (bool | Unset):
        oes_standard_derivatives (bool | Unset):
        oes_texture_float (bool | Unset):
        oes_texture_float_linear (bool | Unset):
        oes_texture_half_float (bool | Unset):
        oes_texture_half_float_linear (bool | Unset):
        oes_vertex_array_object (bool | Unset):
        renderer (str | Unset):
        screen_height (int | Unset):
        screen_width (int | Unset):
        supports_web_gl2 (bool | Unset):
        supports_web_gpu (bool | Unset):
        vendor (str | Unset):
    """

    angle_instanced_arrays: bool | Unset = UNSET
    client_browser_storage_quota: float | Unset = UNSET
    client_browser_storage_used: float | Unset = UNSET
    compressed_texture_s3_tc: bool | Unset = UNSET
    depth_texture: bool | Unset = UNSET
    device_pixel_ratio: float | Unset = UNSET
    draw_buffers: bool | Unset = UNSET
    ext_texture_filter_anisotropic: bool | Unset = UNSET
    has_3_d_mouse: bool | Unset = UNSET
    oes_element_index_uint: bool | Unset = UNSET
    oes_standard_derivatives: bool | Unset = UNSET
    oes_texture_float: bool | Unset = UNSET
    oes_texture_float_linear: bool | Unset = UNSET
    oes_texture_half_float: bool | Unset = UNSET
    oes_texture_half_float_linear: bool | Unset = UNSET
    oes_vertex_array_object: bool | Unset = UNSET
    renderer: str | Unset = UNSET
    screen_height: int | Unset = UNSET
    screen_width: int | Unset = UNSET
    supports_web_gl2: bool | Unset = UNSET
    supports_web_gpu: bool | Unset = UNSET
    vendor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        angle_instanced_arrays = self.angle_instanced_arrays

        client_browser_storage_quota = self.client_browser_storage_quota

        client_browser_storage_used = self.client_browser_storage_used

        compressed_texture_s3_tc = self.compressed_texture_s3_tc

        depth_texture = self.depth_texture

        device_pixel_ratio = self.device_pixel_ratio

        draw_buffers = self.draw_buffers

        ext_texture_filter_anisotropic = self.ext_texture_filter_anisotropic

        has_3_d_mouse = self.has_3_d_mouse

        oes_element_index_uint = self.oes_element_index_uint

        oes_standard_derivatives = self.oes_standard_derivatives

        oes_texture_float = self.oes_texture_float

        oes_texture_float_linear = self.oes_texture_float_linear

        oes_texture_half_float = self.oes_texture_half_float

        oes_texture_half_float_linear = self.oes_texture_half_float_linear

        oes_vertex_array_object = self.oes_vertex_array_object

        renderer = self.renderer

        screen_height = self.screen_height

        screen_width = self.screen_width

        supports_web_gl2 = self.supports_web_gl2

        supports_web_gpu = self.supports_web_gpu

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if angle_instanced_arrays is not UNSET:
            field_dict["angleInstancedArrays"] = angle_instanced_arrays
        if client_browser_storage_quota is not UNSET:
            field_dict["clientBrowserStorageQuota"] = client_browser_storage_quota
        if client_browser_storage_used is not UNSET:
            field_dict["clientBrowserStorageUsed"] = client_browser_storage_used
        if compressed_texture_s3_tc is not UNSET:
            field_dict["compressedTextureS3tc"] = compressed_texture_s3_tc
        if depth_texture is not UNSET:
            field_dict["depthTexture"] = depth_texture
        if device_pixel_ratio is not UNSET:
            field_dict["devicePixelRatio"] = device_pixel_ratio
        if draw_buffers is not UNSET:
            field_dict["drawBuffers"] = draw_buffers
        if ext_texture_filter_anisotropic is not UNSET:
            field_dict["extTextureFilterAnisotropic"] = ext_texture_filter_anisotropic
        if has_3_d_mouse is not UNSET:
            field_dict["has3dMouse"] = has_3_d_mouse
        if oes_element_index_uint is not UNSET:
            field_dict["oesElementIndexUint"] = oes_element_index_uint
        if oes_standard_derivatives is not UNSET:
            field_dict["oesStandardDerivatives"] = oes_standard_derivatives
        if oes_texture_float is not UNSET:
            field_dict["oesTextureFloat"] = oes_texture_float
        if oes_texture_float_linear is not UNSET:
            field_dict["oesTextureFloatLinear"] = oes_texture_float_linear
        if oes_texture_half_float is not UNSET:
            field_dict["oesTextureHalfFloat"] = oes_texture_half_float
        if oes_texture_half_float_linear is not UNSET:
            field_dict["oesTextureHalfFloatLinear"] = oes_texture_half_float_linear
        if oes_vertex_array_object is not UNSET:
            field_dict["oesVertexArrayObject"] = oes_vertex_array_object
        if renderer is not UNSET:
            field_dict["renderer"] = renderer
        if screen_height is not UNSET:
            field_dict["screenHeight"] = screen_height
        if screen_width is not UNSET:
            field_dict["screenWidth"] = screen_width
        if supports_web_gl2 is not UNSET:
            field_dict["supportsWebGL2"] = supports_web_gl2
        if supports_web_gpu is not UNSET:
            field_dict["supportsWebGPU"] = supports_web_gpu
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        angle_instanced_arrays = d.pop("angleInstancedArrays", UNSET)

        client_browser_storage_quota = d.pop("clientBrowserStorageQuota", UNSET)

        client_browser_storage_used = d.pop("clientBrowserStorageUsed", UNSET)

        compressed_texture_s3_tc = d.pop("compressedTextureS3tc", UNSET)

        depth_texture = d.pop("depthTexture", UNSET)

        device_pixel_ratio = d.pop("devicePixelRatio", UNSET)

        draw_buffers = d.pop("drawBuffers", UNSET)

        ext_texture_filter_anisotropic = d.pop("extTextureFilterAnisotropic", UNSET)

        has_3_d_mouse = d.pop("has3dMouse", UNSET)

        oes_element_index_uint = d.pop("oesElementIndexUint", UNSET)

        oes_standard_derivatives = d.pop("oesStandardDerivatives", UNSET)

        oes_texture_float = d.pop("oesTextureFloat", UNSET)

        oes_texture_float_linear = d.pop("oesTextureFloatLinear", UNSET)

        oes_texture_half_float = d.pop("oesTextureHalfFloat", UNSET)

        oes_texture_half_float_linear = d.pop("oesTextureHalfFloatLinear", UNSET)

        oes_vertex_array_object = d.pop("oesVertexArrayObject", UNSET)

        renderer = d.pop("renderer", UNSET)

        screen_height = d.pop("screenHeight", UNSET)

        screen_width = d.pop("screenWidth", UNSET)

        supports_web_gl2 = d.pop("supportsWebGL2", UNSET)

        supports_web_gpu = d.pop("supportsWebGPU", UNSET)

        vendor = d.pop("vendor", UNSET)

        bt_web_client_capabilities_params = cls(
            angle_instanced_arrays=angle_instanced_arrays,
            client_browser_storage_quota=client_browser_storage_quota,
            client_browser_storage_used=client_browser_storage_used,
            compressed_texture_s3_tc=compressed_texture_s3_tc,
            depth_texture=depth_texture,
            device_pixel_ratio=device_pixel_ratio,
            draw_buffers=draw_buffers,
            ext_texture_filter_anisotropic=ext_texture_filter_anisotropic,
            has_3_d_mouse=has_3_d_mouse,
            oes_element_index_uint=oes_element_index_uint,
            oes_standard_derivatives=oes_standard_derivatives,
            oes_texture_float=oes_texture_float,
            oes_texture_float_linear=oes_texture_float_linear,
            oes_texture_half_float=oes_texture_half_float,
            oes_texture_half_float_linear=oes_texture_half_float_linear,
            oes_vertex_array_object=oes_vertex_array_object,
            renderer=renderer,
            screen_height=screen_height,
            screen_width=screen_width,
            supports_web_gl2=supports_web_gl2,
            supports_web_gpu=supports_web_gpu,
            vendor=vendor,
        )

        bt_web_client_capabilities_params.additional_properties = d
        return bt_web_client_capabilities_params

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
