from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btb_drawing_operation_params import BTBDrawingOperationParams


T = TypeVar("T", bound="BTDrawingModificationParams")


@_attrs_define
class BTDrawingModificationParams:
    """
    Attributes:
        description (str | Unset): The label that will appear in the document's edit history for this operation. If
            blank, a value will be auto-generated.
        json_requests (list[BTBDrawingOperationParams] | Unset): Array of drawing modification operations.
    """

    description: str | Unset = UNSET
    json_requests: list[BTBDrawingOperationParams] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        json_requests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.json_requests, Unset):
            json_requests = []
            for json_requests_item_data in self.json_requests:
                json_requests_item = json_requests_item_data.to_dict()
                json_requests.append(json_requests_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if json_requests is not UNSET:
            field_dict["jsonRequests"] = json_requests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btb_drawing_operation_params import BTBDrawingOperationParams

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _json_requests = d.pop("jsonRequests", UNSET)
        json_requests: list[BTBDrawingOperationParams] | Unset = UNSET
        if _json_requests is not UNSET:
            json_requests = []
            for json_requests_item_data in _json_requests:
                json_requests_item = BTBDrawingOperationParams.from_dict(json_requests_item_data)

                json_requests.append(json_requests_item)

        bt_drawing_modification_params = cls(
            description=description,
            json_requests=json_requests,
        )

        bt_drawing_modification_params.additional_properties = d
        return bt_drawing_modification_params

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
