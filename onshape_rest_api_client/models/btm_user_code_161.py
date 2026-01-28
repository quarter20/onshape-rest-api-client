from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btp_statement_269 import BTPStatement269


T = TypeVar("T", bound="BTMUserCode161")


@_attrs_define
class BTMUserCode161:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        parsed (BTPStatement269 | Unset):
        statement (str | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    parsed: BTPStatement269 | Unset = UNSET
    statement: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        parsed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parsed, Unset):
            parsed = self.parsed.to_dict()

        statement = self.statement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parsed is not UNSET:
            field_dict["parsed"] = parsed
        if statement is not UNSET:
            field_dict["statement"] = statement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btp_statement_269 import BTPStatement269

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _parsed = d.pop("parsed", UNSET)
        parsed: BTPStatement269 | Unset
        if isinstance(_parsed, Unset):
            parsed = UNSET
        else:
            parsed = BTPStatement269.from_dict(_parsed)

        statement = d.pop("statement", UNSET)

        btm_user_code_161 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            parsed=parsed,
            statement=statement,
        )

        btm_user_code_161.additional_properties = d
        return btm_user_code_161

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
