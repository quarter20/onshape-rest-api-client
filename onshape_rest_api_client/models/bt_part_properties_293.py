from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_configured_part_properties_2645 import BTConfiguredPartProperties2645
    from ..models.bt_one_part_properties_230 import BTOnePartProperties230
    from ..models.bt_part_properties_293_identity_id_to_query_index import BTPartProperties293IdentityIdToQueryIndex
    from ..models.bt_tessellation_properties_927 import BTTessellationProperties927


T = TypeVar("T", bound="BTPartProperties293")


@_attrs_define
class BTPartProperties293:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        configured_parts (BTConfiguredPartProperties2645 | Unset):
        identity_id_to_query_index (BTPartProperties293IdentityIdToQueryIndex | Unset):
        node_id (str | Unset):
        parts (list[BTOnePartProperties230] | Unset):
        rough_bytes_estimate (int | Unset):
        tessellation_properties (BTTessellationProperties927 | Unset):
    """

    bt_type: str | Unset = UNSET
    configured_parts: BTConfiguredPartProperties2645 | Unset = UNSET
    identity_id_to_query_index: BTPartProperties293IdentityIdToQueryIndex | Unset = UNSET
    node_id: str | Unset = UNSET
    parts: list[BTOnePartProperties230] | Unset = UNSET
    rough_bytes_estimate: int | Unset = UNSET
    tessellation_properties: BTTessellationProperties927 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        configured_parts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configured_parts, Unset):
            configured_parts = self.configured_parts.to_dict()

        identity_id_to_query_index: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identity_id_to_query_index, Unset):
            identity_id_to_query_index = self.identity_id_to_query_index.to_dict()

        node_id = self.node_id

        parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)

        rough_bytes_estimate = self.rough_bytes_estimate

        tessellation_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tessellation_properties, Unset):
            tessellation_properties = self.tessellation_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if configured_parts is not UNSET:
            field_dict["configuredParts"] = configured_parts
        if identity_id_to_query_index is not UNSET:
            field_dict["identityIdToQueryIndex"] = identity_id_to_query_index
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parts is not UNSET:
            field_dict["parts"] = parts
        if rough_bytes_estimate is not UNSET:
            field_dict["roughBytesEstimate"] = rough_bytes_estimate
        if tessellation_properties is not UNSET:
            field_dict["tessellationProperties"] = tessellation_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_configured_part_properties_2645 import BTConfiguredPartProperties2645
        from ..models.bt_one_part_properties_230 import BTOnePartProperties230
        from ..models.bt_part_properties_293_identity_id_to_query_index import BTPartProperties293IdentityIdToQueryIndex
        from ..models.bt_tessellation_properties_927 import BTTessellationProperties927

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _configured_parts = d.pop("configuredParts", UNSET)
        configured_parts: BTConfiguredPartProperties2645 | Unset
        if isinstance(_configured_parts, Unset):
            configured_parts = UNSET
        else:
            configured_parts = BTConfiguredPartProperties2645.from_dict(_configured_parts)

        _identity_id_to_query_index = d.pop("identityIdToQueryIndex", UNSET)
        identity_id_to_query_index: BTPartProperties293IdentityIdToQueryIndex | Unset
        if isinstance(_identity_id_to_query_index, Unset):
            identity_id_to_query_index = UNSET
        else:
            identity_id_to_query_index = BTPartProperties293IdentityIdToQueryIndex.from_dict(
                _identity_id_to_query_index
            )

        node_id = d.pop("nodeId", UNSET)

        _parts = d.pop("parts", UNSET)
        parts: list[BTOnePartProperties230] | Unset = UNSET
        if _parts is not UNSET:
            parts = []
            for parts_item_data in _parts:
                parts_item = BTOnePartProperties230.from_dict(parts_item_data)

                parts.append(parts_item)

        rough_bytes_estimate = d.pop("roughBytesEstimate", UNSET)

        _tessellation_properties = d.pop("tessellationProperties", UNSET)
        tessellation_properties: BTTessellationProperties927 | Unset
        if isinstance(_tessellation_properties, Unset):
            tessellation_properties = UNSET
        else:
            tessellation_properties = BTTessellationProperties927.from_dict(_tessellation_properties)

        bt_part_properties_293 = cls(
            bt_type=bt_type,
            configured_parts=configured_parts,
            identity_id_to_query_index=identity_id_to_query_index,
            node_id=node_id,
            parts=parts,
            rough_bytes_estimate=rough_bytes_estimate,
            tessellation_properties=tessellation_properties,
        )

        bt_part_properties_293.additional_properties = d
        return bt_part_properties_293

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
