from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_mate_connector_cs_info import BTMateConnectorCSInfo


T = TypeVar("T", bound="BTAssemblyMateConnectorInfo")


@_attrs_define
class BTAssemblyMateConnectorInfo:
    """
    Attributes:
        feature_id (str | Unset):
        mate_connector_cs (BTMateConnectorCSInfo | Unset):
    """

    feature_id: str | Unset = UNSET
    mate_connector_cs: BTMateConnectorCSInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_id = self.feature_id

        mate_connector_cs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mate_connector_cs, Unset):
            mate_connector_cs = self.mate_connector_cs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if mate_connector_cs is not UNSET:
            field_dict["mateConnectorCS"] = mate_connector_cs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_mate_connector_cs_info import BTMateConnectorCSInfo

        d = dict(src_dict)
        feature_id = d.pop("featureId", UNSET)

        _mate_connector_cs = d.pop("mateConnectorCS", UNSET)
        mate_connector_cs: BTMateConnectorCSInfo | Unset
        if isinstance(_mate_connector_cs, Unset):
            mate_connector_cs = UNSET
        else:
            mate_connector_cs = BTMateConnectorCSInfo.from_dict(_mate_connector_cs)

        bt_assembly_mate_connector_info = cls(
            feature_id=feature_id,
            mate_connector_cs=mate_connector_cs,
        )

        bt_assembly_mate_connector_info.additional_properties = d
        return bt_assembly_mate_connector_info

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
