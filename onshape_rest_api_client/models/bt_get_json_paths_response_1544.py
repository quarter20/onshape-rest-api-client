from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_json_match_2290 import BTJsonMatch2290


T = TypeVar("T", bound="BTGetJsonPathsResponse1544")


@_attrs_define
class BTGetJsonPathsResponse1544:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        change_id (str | Unset):
        results (list[list[BTJsonMatch2290]] | Unset):
    """

    bt_type: str | Unset = UNSET
    change_id: str | Unset = UNSET
    results: list[list[BTJsonMatch2290]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        change_id = self.change_id

        results: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = []
                for results_item_item_data in results_item_data:
                    results_item_item = results_item_item_data.to_dict()
                    results_item.append(results_item_item)

                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if change_id is not UNSET:
            field_dict["changeId"] = change_id
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_json_match_2290 import BTJsonMatch2290

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        change_id = d.pop("changeId", UNSET)

        _results = d.pop("results", UNSET)
        results: list[list[BTJsonMatch2290]] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = []
                _results_item = results_item_data
                for results_item_item_data in _results_item:
                    results_item_item = BTJsonMatch2290.from_dict(results_item_item_data)

                    results_item.append(results_item_item)

                results.append(results_item)

        bt_get_json_paths_response_1544 = cls(
            bt_type=bt_type,
            change_id=change_id,
            results=results,
        )

        bt_get_json_paths_response_1544.additional_properties = d
        return bt_get_json_paths_response_1544

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
