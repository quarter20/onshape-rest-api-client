from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_surface_type import GBTSurfaceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_bounding_box_1052 import BTBoundingBox1052
    from ..models.bt_entity_geometry_35 import BTEntityGeometry35
    from ..models.bt_immutable_byte_array import BTImmutableByteArray
    from ..models.bt_immutable_double_array import BTImmutableDoubleArray
    from ..models.bt_immutable_float_array import BTImmutableFloatArray
    from ..models.bt_immutable_int_array import BTImmutableIntArray


T = TypeVar("T", bound="BTSimulationFace2147")


@_attrs_define
class BTSimulationFace2147:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        compressed (bool | Unset):
        decompressed (BTEntityGeometry35 | Unset):
        error_code (int | Unset):
        estimated_memory_usage_in_bytes (int | Unset):
        has_tessellation_error (bool | Unset):
        setting_index (int | Unset):
        compressed_uvs (BTImmutableByteArray | Unset):
        flip_computed_normals (bool | Unset):
        indices (BTImmutableIntArray | Unset):
        indices_stored_as_differences (bool | Unset):
        is_planar (bool | Unset):
        max_principle_curvature_magnitudes (BTImmutableFloatArray | Unset):
        min_principle_curvature_magnitudes (BTImmutableFloatArray | Unset):
        normals (BTImmutableFloatArray | Unset):
        points (BTImmutableFloatArray | Unset):
        surface_parameters (BTImmutableDoubleArray | Unset):
        surface_type (GBTSurfaceType | Unset):
        texture_coordinates (BTImmutableFloatArray | Unset):
        triangle_count (int | Unset):
        bounds (BTBoundingBox1052 | Unset): An axis-aligned bounding box indicated by two opposite corners.
        sample_triangle_point_indices (BTImmutableIntArray | Unset):
        triangle_normal_indices (BTImmutableIntArray | Unset):
        triangle_point_indices (BTImmutableIntArray | Unset):
    """

    bt_type: str | Unset = UNSET
    compressed: bool | Unset = UNSET
    decompressed: BTEntityGeometry35 | Unset = UNSET
    error_code: int | Unset = UNSET
    estimated_memory_usage_in_bytes: int | Unset = UNSET
    has_tessellation_error: bool | Unset = UNSET
    setting_index: int | Unset = UNSET
    compressed_uvs: BTImmutableByteArray | Unset = UNSET
    flip_computed_normals: bool | Unset = UNSET
    indices: BTImmutableIntArray | Unset = UNSET
    indices_stored_as_differences: bool | Unset = UNSET
    is_planar: bool | Unset = UNSET
    max_principle_curvature_magnitudes: BTImmutableFloatArray | Unset = UNSET
    min_principle_curvature_magnitudes: BTImmutableFloatArray | Unset = UNSET
    normals: BTImmutableFloatArray | Unset = UNSET
    points: BTImmutableFloatArray | Unset = UNSET
    surface_parameters: BTImmutableDoubleArray | Unset = UNSET
    surface_type: GBTSurfaceType | Unset = UNSET
    texture_coordinates: BTImmutableFloatArray | Unset = UNSET
    triangle_count: int | Unset = UNSET
    bounds: BTBoundingBox1052 | Unset = UNSET
    sample_triangle_point_indices: BTImmutableIntArray | Unset = UNSET
    triangle_normal_indices: BTImmutableIntArray | Unset = UNSET
    triangle_point_indices: BTImmutableIntArray | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        compressed = self.compressed

        decompressed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.decompressed, Unset):
            decompressed = self.decompressed.to_dict()

        error_code = self.error_code

        estimated_memory_usage_in_bytes = self.estimated_memory_usage_in_bytes

        has_tessellation_error = self.has_tessellation_error

        setting_index = self.setting_index

        compressed_uvs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compressed_uvs, Unset):
            compressed_uvs = self.compressed_uvs.to_dict()

        flip_computed_normals = self.flip_computed_normals

        indices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indices, Unset):
            indices = self.indices.to_dict()

        indices_stored_as_differences = self.indices_stored_as_differences

        is_planar = self.is_planar

        max_principle_curvature_magnitudes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_principle_curvature_magnitudes, Unset):
            max_principle_curvature_magnitudes = self.max_principle_curvature_magnitudes.to_dict()

        min_principle_curvature_magnitudes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_principle_curvature_magnitudes, Unset):
            min_principle_curvature_magnitudes = self.min_principle_curvature_magnitudes.to_dict()

        normals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.normals, Unset):
            normals = self.normals.to_dict()

        points: dict[str, Any] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = self.points.to_dict()

        surface_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.surface_parameters, Unset):
            surface_parameters = self.surface_parameters.to_dict()

        surface_type: str | Unset = UNSET
        if not isinstance(self.surface_type, Unset):
            surface_type = self.surface_type.value

        texture_coordinates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.texture_coordinates, Unset):
            texture_coordinates = self.texture_coordinates.to_dict()

        triangle_count = self.triangle_count

        bounds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bounds, Unset):
            bounds = self.bounds.to_dict()

        sample_triangle_point_indices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sample_triangle_point_indices, Unset):
            sample_triangle_point_indices = self.sample_triangle_point_indices.to_dict()

        triangle_normal_indices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.triangle_normal_indices, Unset):
            triangle_normal_indices = self.triangle_normal_indices.to_dict()

        triangle_point_indices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.triangle_point_indices, Unset):
            triangle_point_indices = self.triangle_point_indices.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if compressed is not UNSET:
            field_dict["compressed"] = compressed
        if decompressed is not UNSET:
            field_dict["decompressed"] = decompressed
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if estimated_memory_usage_in_bytes is not UNSET:
            field_dict["estimatedMemoryUsageInBytes"] = estimated_memory_usage_in_bytes
        if has_tessellation_error is not UNSET:
            field_dict["hasTessellationError"] = has_tessellation_error
        if setting_index is not UNSET:
            field_dict["settingIndex"] = setting_index
        if compressed_uvs is not UNSET:
            field_dict["compressedUvs"] = compressed_uvs
        if flip_computed_normals is not UNSET:
            field_dict["flipComputedNormals"] = flip_computed_normals
        if indices is not UNSET:
            field_dict["indices"] = indices
        if indices_stored_as_differences is not UNSET:
            field_dict["indicesStoredAsDifferences"] = indices_stored_as_differences
        if is_planar is not UNSET:
            field_dict["isPlanar"] = is_planar
        if max_principle_curvature_magnitudes is not UNSET:
            field_dict["maxPrincipleCurvatureMagnitudes"] = max_principle_curvature_magnitudes
        if min_principle_curvature_magnitudes is not UNSET:
            field_dict["minPrincipleCurvatureMagnitudes"] = min_principle_curvature_magnitudes
        if normals is not UNSET:
            field_dict["normals"] = normals
        if points is not UNSET:
            field_dict["points"] = points
        if surface_parameters is not UNSET:
            field_dict["surfaceParameters"] = surface_parameters
        if surface_type is not UNSET:
            field_dict["surfaceType"] = surface_type
        if texture_coordinates is not UNSET:
            field_dict["textureCoordinates"] = texture_coordinates
        if triangle_count is not UNSET:
            field_dict["triangleCount"] = triangle_count
        if bounds is not UNSET:
            field_dict["bounds"] = bounds
        if sample_triangle_point_indices is not UNSET:
            field_dict["sampleTrianglePointIndices"] = sample_triangle_point_indices
        if triangle_normal_indices is not UNSET:
            field_dict["triangleNormalIndices"] = triangle_normal_indices
        if triangle_point_indices is not UNSET:
            field_dict["trianglePointIndices"] = triangle_point_indices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_bounding_box_1052 import BTBoundingBox1052
        from ..models.bt_entity_geometry_35 import BTEntityGeometry35
        from ..models.bt_immutable_byte_array import BTImmutableByteArray
        from ..models.bt_immutable_double_array import BTImmutableDoubleArray
        from ..models.bt_immutable_float_array import BTImmutableFloatArray
        from ..models.bt_immutable_int_array import BTImmutableIntArray

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        compressed = d.pop("compressed", UNSET)

        _decompressed = d.pop("decompressed", UNSET)
        decompressed: BTEntityGeometry35 | Unset
        if isinstance(_decompressed, Unset):
            decompressed = UNSET
        else:
            decompressed = BTEntityGeometry35.from_dict(_decompressed)

        error_code = d.pop("errorCode", UNSET)

        estimated_memory_usage_in_bytes = d.pop("estimatedMemoryUsageInBytes", UNSET)

        has_tessellation_error = d.pop("hasTessellationError", UNSET)

        setting_index = d.pop("settingIndex", UNSET)

        _compressed_uvs = d.pop("compressedUvs", UNSET)
        compressed_uvs: BTImmutableByteArray | Unset
        if isinstance(_compressed_uvs, Unset):
            compressed_uvs = UNSET
        else:
            compressed_uvs = BTImmutableByteArray.from_dict(_compressed_uvs)

        flip_computed_normals = d.pop("flipComputedNormals", UNSET)

        _indices = d.pop("indices", UNSET)
        indices: BTImmutableIntArray | Unset
        if isinstance(_indices, Unset):
            indices = UNSET
        else:
            indices = BTImmutableIntArray.from_dict(_indices)

        indices_stored_as_differences = d.pop("indicesStoredAsDifferences", UNSET)

        is_planar = d.pop("isPlanar", UNSET)

        _max_principle_curvature_magnitudes = d.pop("maxPrincipleCurvatureMagnitudes", UNSET)
        max_principle_curvature_magnitudes: BTImmutableFloatArray | Unset
        if isinstance(_max_principle_curvature_magnitudes, Unset):
            max_principle_curvature_magnitudes = UNSET
        else:
            max_principle_curvature_magnitudes = BTImmutableFloatArray.from_dict(_max_principle_curvature_magnitudes)

        _min_principle_curvature_magnitudes = d.pop("minPrincipleCurvatureMagnitudes", UNSET)
        min_principle_curvature_magnitudes: BTImmutableFloatArray | Unset
        if isinstance(_min_principle_curvature_magnitudes, Unset):
            min_principle_curvature_magnitudes = UNSET
        else:
            min_principle_curvature_magnitudes = BTImmutableFloatArray.from_dict(_min_principle_curvature_magnitudes)

        _normals = d.pop("normals", UNSET)
        normals: BTImmutableFloatArray | Unset
        if isinstance(_normals, Unset):
            normals = UNSET
        else:
            normals = BTImmutableFloatArray.from_dict(_normals)

        _points = d.pop("points", UNSET)
        points: BTImmutableFloatArray | Unset
        if isinstance(_points, Unset):
            points = UNSET
        else:
            points = BTImmutableFloatArray.from_dict(_points)

        _surface_parameters = d.pop("surfaceParameters", UNSET)
        surface_parameters: BTImmutableDoubleArray | Unset
        if isinstance(_surface_parameters, Unset):
            surface_parameters = UNSET
        else:
            surface_parameters = BTImmutableDoubleArray.from_dict(_surface_parameters)

        _surface_type = d.pop("surfaceType", UNSET)
        surface_type: GBTSurfaceType | Unset
        if isinstance(_surface_type, Unset):
            surface_type = UNSET
        else:
            surface_type = GBTSurfaceType(_surface_type)

        _texture_coordinates = d.pop("textureCoordinates", UNSET)
        texture_coordinates: BTImmutableFloatArray | Unset
        if isinstance(_texture_coordinates, Unset):
            texture_coordinates = UNSET
        else:
            texture_coordinates = BTImmutableFloatArray.from_dict(_texture_coordinates)

        triangle_count = d.pop("triangleCount", UNSET)

        _bounds = d.pop("bounds", UNSET)
        bounds: BTBoundingBox1052 | Unset
        if isinstance(_bounds, Unset):
            bounds = UNSET
        else:
            bounds = BTBoundingBox1052.from_dict(_bounds)

        _sample_triangle_point_indices = d.pop("sampleTrianglePointIndices", UNSET)
        sample_triangle_point_indices: BTImmutableIntArray | Unset
        if isinstance(_sample_triangle_point_indices, Unset):
            sample_triangle_point_indices = UNSET
        else:
            sample_triangle_point_indices = BTImmutableIntArray.from_dict(_sample_triangle_point_indices)

        _triangle_normal_indices = d.pop("triangleNormalIndices", UNSET)
        triangle_normal_indices: BTImmutableIntArray | Unset
        if isinstance(_triangle_normal_indices, Unset):
            triangle_normal_indices = UNSET
        else:
            triangle_normal_indices = BTImmutableIntArray.from_dict(_triangle_normal_indices)

        _triangle_point_indices = d.pop("trianglePointIndices", UNSET)
        triangle_point_indices: BTImmutableIntArray | Unset
        if isinstance(_triangle_point_indices, Unset):
            triangle_point_indices = UNSET
        else:
            triangle_point_indices = BTImmutableIntArray.from_dict(_triangle_point_indices)

        bt_simulation_face_2147 = cls(
            bt_type=bt_type,
            compressed=compressed,
            decompressed=decompressed,
            error_code=error_code,
            estimated_memory_usage_in_bytes=estimated_memory_usage_in_bytes,
            has_tessellation_error=has_tessellation_error,
            setting_index=setting_index,
            compressed_uvs=compressed_uvs,
            flip_computed_normals=flip_computed_normals,
            indices=indices,
            indices_stored_as_differences=indices_stored_as_differences,
            is_planar=is_planar,
            max_principle_curvature_magnitudes=max_principle_curvature_magnitudes,
            min_principle_curvature_magnitudes=min_principle_curvature_magnitudes,
            normals=normals,
            points=points,
            surface_parameters=surface_parameters,
            surface_type=surface_type,
            texture_coordinates=texture_coordinates,
            triangle_count=triangle_count,
            bounds=bounds,
            sample_triangle_point_indices=sample_triangle_point_indices,
            triangle_normal_indices=triangle_normal_indices,
            triangle_point_indices=triangle_point_indices,
        )

        bt_simulation_face_2147.additional_properties = d
        return bt_simulation_face_2147

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
