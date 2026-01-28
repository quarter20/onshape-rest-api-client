from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_ui_selection_type import GBTUiSelectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_occurrence_74 import BTOccurrence74


T = TypeVar("T", bound="BTUiSelection1185")


@_attrs_define
class BTUiSelection1185:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        deterministic_id_list (list[str] | Unset):
        id (str | Unset):
        occurrence (BTOccurrence74 | Unset):
        table_row_id (str | Unset):
        type_ (GBTUiSelectionType | Unset):
    """

    bt_type: str | Unset = UNSET
    deterministic_id_list: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    occurrence: BTOccurrence74 | Unset = UNSET
    table_row_id: str | Unset = UNSET
    type_: GBTUiSelectionType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        deterministic_id_list: list[str] | Unset = UNSET
        if not isinstance(self.deterministic_id_list, Unset):
            deterministic_id_list = self.deterministic_id_list

        id = self.id

        occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence, Unset):
            occurrence = self.occurrence.to_dict()

        table_row_id = self.table_row_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if deterministic_id_list is not UNSET:
            field_dict["deterministicIdList"] = deterministic_id_list
        if id is not UNSET:
            field_dict["id"] = id
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence
        if table_row_id is not UNSET:
            field_dict["tableRowId"] = table_row_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_occurrence_74 import BTOccurrence74

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        deterministic_id_list = cast(list[str], d.pop("deterministicIdList", UNSET))

        id = d.pop("id", UNSET)

        _occurrence = d.pop("occurrence", UNSET)
        occurrence: BTOccurrence74 | Unset
        if isinstance(_occurrence, Unset):
            occurrence = UNSET
        else:
            occurrence = BTOccurrence74.from_dict(_occurrence)

        table_row_id = d.pop("tableRowId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GBTUiSelectionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GBTUiSelectionType(_type_)

        bt_ui_selection_1185 = cls(
            bt_type=bt_type,
            deterministic_id_list=deterministic_id_list,
            id=id,
            occurrence=occurrence,
            table_row_id=table_row_id,
            type_=type_,
        )

        bt_ui_selection_1185.additional_properties = d
        return bt_ui_selection_1185

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
