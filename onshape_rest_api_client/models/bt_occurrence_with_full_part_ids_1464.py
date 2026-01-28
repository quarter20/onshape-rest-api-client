from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_full_element_id_with_document_1729 import BTFullElementIdWithDocument1729
    from ..models.bt_occurrence_74 import BTOccurrence74
    from ..models.btbs_matrix_386 import BTBSMatrix386


T = TypeVar("T", bound="BTOccurrenceWithFullPartIds1464")


@_attrs_define
class BTOccurrenceWithFullPartIds1464:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        full_path_as_string (str | Unset):
        head_instance_id (str | Unset):
        internal_occurrence (bool | Unset):
        occurrence_without_head (BTOccurrence74 | Unset):
        occurrence_without_tail (BTOccurrence74 | Unset):
        parent (BTOccurrence74 | Unset):
        path (list[str] | Unset):
        root_occurrence (bool | Unset):
        tail_instance_id (str | Unset):
        full_element_id (BTFullElementIdWithDocument1729 | Unset):
        part_ids (list[str] | Unset):
        transform (BTBSMatrix386 | Unset):
    """

    bt_type: str | Unset = UNSET
    full_path_as_string: str | Unset = UNSET
    head_instance_id: str | Unset = UNSET
    internal_occurrence: bool | Unset = UNSET
    occurrence_without_head: BTOccurrence74 | Unset = UNSET
    occurrence_without_tail: BTOccurrence74 | Unset = UNSET
    parent: BTOccurrence74 | Unset = UNSET
    path: list[str] | Unset = UNSET
    root_occurrence: bool | Unset = UNSET
    tail_instance_id: str | Unset = UNSET
    full_element_id: BTFullElementIdWithDocument1729 | Unset = UNSET
    part_ids: list[str] | Unset = UNSET
    transform: BTBSMatrix386 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        full_path_as_string = self.full_path_as_string

        head_instance_id = self.head_instance_id

        internal_occurrence = self.internal_occurrence

        occurrence_without_head: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence_without_head, Unset):
            occurrence_without_head = self.occurrence_without_head.to_dict()

        occurrence_without_tail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence_without_tail, Unset):
            occurrence_without_tail = self.occurrence_without_tail.to_dict()

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        path: list[str] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path

        root_occurrence = self.root_occurrence

        tail_instance_id = self.tail_instance_id

        full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id, Unset):
            full_element_id = self.full_element_id.to_dict()

        part_ids: list[str] | Unset = UNSET
        if not isinstance(self.part_ids, Unset):
            part_ids = self.part_ids

        transform: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transform, Unset):
            transform = self.transform.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if full_path_as_string is not UNSET:
            field_dict["fullPathAsString"] = full_path_as_string
        if head_instance_id is not UNSET:
            field_dict["headInstanceId"] = head_instance_id
        if internal_occurrence is not UNSET:
            field_dict["internalOccurrence"] = internal_occurrence
        if occurrence_without_head is not UNSET:
            field_dict["occurrenceWithoutHead"] = occurrence_without_head
        if occurrence_without_tail is not UNSET:
            field_dict["occurrenceWithoutTail"] = occurrence_without_tail
        if parent is not UNSET:
            field_dict["parent"] = parent
        if path is not UNSET:
            field_dict["path"] = path
        if root_occurrence is not UNSET:
            field_dict["rootOccurrence"] = root_occurrence
        if tail_instance_id is not UNSET:
            field_dict["tailInstanceId"] = tail_instance_id
        if full_element_id is not UNSET:
            field_dict["fullElementId"] = full_element_id
        if part_ids is not UNSET:
            field_dict["partIds"] = part_ids
        if transform is not UNSET:
            field_dict["transform"] = transform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_full_element_id_with_document_1729 import BTFullElementIdWithDocument1729
        from ..models.bt_occurrence_74 import BTOccurrence74
        from ..models.btbs_matrix_386 import BTBSMatrix386

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        full_path_as_string = d.pop("fullPathAsString", UNSET)

        head_instance_id = d.pop("headInstanceId", UNSET)

        internal_occurrence = d.pop("internalOccurrence", UNSET)

        _occurrence_without_head = d.pop("occurrenceWithoutHead", UNSET)
        occurrence_without_head: BTOccurrence74 | Unset
        if isinstance(_occurrence_without_head, Unset):
            occurrence_without_head = UNSET
        else:
            occurrence_without_head = BTOccurrence74.from_dict(_occurrence_without_head)

        _occurrence_without_tail = d.pop("occurrenceWithoutTail", UNSET)
        occurrence_without_tail: BTOccurrence74 | Unset
        if isinstance(_occurrence_without_tail, Unset):
            occurrence_without_tail = UNSET
        else:
            occurrence_without_tail = BTOccurrence74.from_dict(_occurrence_without_tail)

        _parent = d.pop("parent", UNSET)
        parent: BTOccurrence74 | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = BTOccurrence74.from_dict(_parent)

        path = cast(list[str], d.pop("path", UNSET))

        root_occurrence = d.pop("rootOccurrence", UNSET)

        tail_instance_id = d.pop("tailInstanceId", UNSET)

        _full_element_id = d.pop("fullElementId", UNSET)
        full_element_id: BTFullElementIdWithDocument1729 | Unset
        if isinstance(_full_element_id, Unset):
            full_element_id = UNSET
        else:
            full_element_id = BTFullElementIdWithDocument1729.from_dict(_full_element_id)

        part_ids = cast(list[str], d.pop("partIds", UNSET))

        _transform = d.pop("transform", UNSET)
        transform: BTBSMatrix386 | Unset
        if isinstance(_transform, Unset):
            transform = UNSET
        else:
            transform = BTBSMatrix386.from_dict(_transform)

        bt_occurrence_with_full_part_ids_1464 = cls(
            bt_type=bt_type,
            full_path_as_string=full_path_as_string,
            head_instance_id=head_instance_id,
            internal_occurrence=internal_occurrence,
            occurrence_without_head=occurrence_without_head,
            occurrence_without_tail=occurrence_without_tail,
            parent=parent,
            path=path,
            root_occurrence=root_occurrence,
            tail_instance_id=tail_instance_id,
            full_element_id=full_element_id,
            part_ids=part_ids,
            transform=transform,
        )

        bt_occurrence_with_full_part_ids_1464.additional_properties = d
        return bt_occurrence_with_full_part_ids_1464

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
