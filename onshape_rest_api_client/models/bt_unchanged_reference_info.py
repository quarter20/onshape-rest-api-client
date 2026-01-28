from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_revision_info import BTRevisionInfo


T = TypeVar("T", bound="BTUnchangedReferenceInfo")


@_attrs_define
class BTUnchangedReferenceInfo:
    """
    Attributes:
        metadata_unchanged (bool | Unset):
        node_ids (list[str] | Unset):
        to_revision (BTRevisionInfo | Unset): Revision details.
    """

    metadata_unchanged: bool | Unset = UNSET
    node_ids: list[str] | Unset = UNSET
    to_revision: BTRevisionInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata_unchanged = self.metadata_unchanged

        node_ids: list[str] | Unset = UNSET
        if not isinstance(self.node_ids, Unset):
            node_ids = self.node_ids

        to_revision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_revision, Unset):
            to_revision = self.to_revision.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata_unchanged is not UNSET:
            field_dict["metadataUnchanged"] = metadata_unchanged
        if node_ids is not UNSET:
            field_dict["nodeIds"] = node_ids
        if to_revision is not UNSET:
            field_dict["toRevision"] = to_revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_revision_info import BTRevisionInfo

        d = dict(src_dict)
        metadata_unchanged = d.pop("metadataUnchanged", UNSET)

        node_ids = cast(list[str], d.pop("nodeIds", UNSET))

        _to_revision = d.pop("toRevision", UNSET)
        to_revision: BTRevisionInfo | Unset
        if isinstance(_to_revision, Unset):
            to_revision = UNSET
        else:
            to_revision = BTRevisionInfo.from_dict(_to_revision)

        bt_unchanged_reference_info = cls(
            metadata_unchanged=metadata_unchanged,
            node_ids=node_ids,
            to_revision=to_revision,
        )

        bt_unchanged_reference_info.additional_properties = d
        return bt_unchanged_reference_info

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
