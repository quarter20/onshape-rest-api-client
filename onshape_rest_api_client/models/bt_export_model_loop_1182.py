from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_export_model_coedge_1342 import BTExportModelCoedge1342


T = TypeVar("T", bound="BTExportModelLoop1182")


@_attrs_define
class BTExportModelLoop1182:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        coedges (list[BTExportModelCoedge1342] | Unset):
        is_inner (bool | Unset):
        is_outer (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    coedges: list[BTExportModelCoedge1342] | Unset = UNSET
    is_inner: bool | Unset = UNSET
    is_outer: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        coedges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.coedges, Unset):
            coedges = []
            for coedges_item_data in self.coedges:
                coedges_item = coedges_item_data.to_dict()
                coedges.append(coedges_item)

        is_inner = self.is_inner

        is_outer = self.is_outer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if coedges is not UNSET:
            field_dict["coedges"] = coedges
        if is_inner is not UNSET:
            field_dict["isInner"] = is_inner
        if is_outer is not UNSET:
            field_dict["isOuter"] = is_outer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_export_model_coedge_1342 import BTExportModelCoedge1342

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _coedges = d.pop("coedges", UNSET)
        coedges: list[BTExportModelCoedge1342] | Unset = UNSET
        if _coedges is not UNSET:
            coedges = []
            for coedges_item_data in _coedges:
                coedges_item = BTExportModelCoedge1342.from_dict(coedges_item_data)

                coedges.append(coedges_item)

        is_inner = d.pop("isInner", UNSET)

        is_outer = d.pop("isOuter", UNSET)

        bt_export_model_loop_1182 = cls(
            bt_type=bt_type,
            coedges=coedges,
            is_inner=is_inner,
            is_outer=is_outer,
        )

        bt_export_model_loop_1182.additional_properties = d
        return bt_export_model_loop_1182

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
