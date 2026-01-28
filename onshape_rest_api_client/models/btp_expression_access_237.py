from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_definition_type import GBTPDefinitionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btp_expression_9 import BTPExpression9
    from ..models.btp_property_accessor_23 import BTPPropertyAccessor23
    from ..models.btp_space_10 import BTPSpace10


T = TypeVar("T", bound="BTPExpressionAccess237")


@_attrs_define
class BTPExpressionAccess237:
    """
    Attributes:
        atomic (bool | Unset):
        bt_type (str | Unset): Type of JSON object.
        documentation_type (GBTPDefinitionType | Unset):
        end_source_location (int | Unset):
        node_id (str | Unset):
        short_descriptor (str | Unset):
        space_after (BTPSpace10 | Unset):
        space_before (BTPSpace10 | Unset):
        space_default (bool | Unset):
        start_source_location (int | Unset):
        accessor (BTPPropertyAccessor23 | Unset):
        base (BTPExpression9 | Unset):
        is_safe_navigation (bool | Unset):
        space_in_accessor (BTPSpace10 | Unset):
    """

    atomic: bool | Unset = UNSET
    bt_type: str | Unset = UNSET
    documentation_type: GBTPDefinitionType | Unset = UNSET
    end_source_location: int | Unset = UNSET
    node_id: str | Unset = UNSET
    short_descriptor: str | Unset = UNSET
    space_after: BTPSpace10 | Unset = UNSET
    space_before: BTPSpace10 | Unset = UNSET
    space_default: bool | Unset = UNSET
    start_source_location: int | Unset = UNSET
    accessor: BTPPropertyAccessor23 | Unset = UNSET
    base: BTPExpression9 | Unset = UNSET
    is_safe_navigation: bool | Unset = UNSET
    space_in_accessor: BTPSpace10 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        atomic = self.atomic

        bt_type = self.bt_type

        documentation_type: str | Unset = UNSET
        if not isinstance(self.documentation_type, Unset):
            documentation_type = self.documentation_type.value

        end_source_location = self.end_source_location

        node_id = self.node_id

        short_descriptor = self.short_descriptor

        space_after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after, Unset):
            space_after = self.space_after.to_dict()

        space_before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_before, Unset):
            space_before = self.space_before.to_dict()

        space_default = self.space_default

        start_source_location = self.start_source_location

        accessor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accessor, Unset):
            accessor = self.accessor.to_dict()

        base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base, Unset):
            base = self.base.to_dict()

        is_safe_navigation = self.is_safe_navigation

        space_in_accessor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_in_accessor, Unset):
            space_in_accessor = self.space_in_accessor.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if atomic is not UNSET:
            field_dict["atomic"] = atomic
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if documentation_type is not UNSET:
            field_dict["documentationType"] = documentation_type
        if end_source_location is not UNSET:
            field_dict["endSourceLocation"] = end_source_location
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if short_descriptor is not UNSET:
            field_dict["shortDescriptor"] = short_descriptor
        if space_after is not UNSET:
            field_dict["spaceAfter"] = space_after
        if space_before is not UNSET:
            field_dict["spaceBefore"] = space_before
        if space_default is not UNSET:
            field_dict["spaceDefault"] = space_default
        if start_source_location is not UNSET:
            field_dict["startSourceLocation"] = start_source_location
        if accessor is not UNSET:
            field_dict["accessor"] = accessor
        if base is not UNSET:
            field_dict["base"] = base
        if is_safe_navigation is not UNSET:
            field_dict["isSafeNavigation"] = is_safe_navigation
        if space_in_accessor is not UNSET:
            field_dict["spaceInAccessor"] = space_in_accessor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btp_expression_9 import BTPExpression9
        from ..models.btp_property_accessor_23 import BTPPropertyAccessor23
        from ..models.btp_space_10 import BTPSpace10

        d = dict(src_dict)
        atomic = d.pop("atomic", UNSET)

        bt_type = d.pop("btType", UNSET)

        _documentation_type = d.pop("documentationType", UNSET)
        documentation_type: GBTPDefinitionType | Unset
        if isinstance(_documentation_type, Unset):
            documentation_type = UNSET
        else:
            documentation_type = GBTPDefinitionType(_documentation_type)

        end_source_location = d.pop("endSourceLocation", UNSET)

        node_id = d.pop("nodeId", UNSET)

        short_descriptor = d.pop("shortDescriptor", UNSET)

        _space_after = d.pop("spaceAfter", UNSET)
        space_after: BTPSpace10 | Unset
        if isinstance(_space_after, Unset):
            space_after = UNSET
        else:
            space_after = BTPSpace10.from_dict(_space_after)

        _space_before = d.pop("spaceBefore", UNSET)
        space_before: BTPSpace10 | Unset
        if isinstance(_space_before, Unset):
            space_before = UNSET
        else:
            space_before = BTPSpace10.from_dict(_space_before)

        space_default = d.pop("spaceDefault", UNSET)

        start_source_location = d.pop("startSourceLocation", UNSET)

        _accessor = d.pop("accessor", UNSET)
        accessor: BTPPropertyAccessor23 | Unset
        if isinstance(_accessor, Unset):
            accessor = UNSET
        else:
            accessor = BTPPropertyAccessor23.from_dict(_accessor)

        _base = d.pop("base", UNSET)
        base: BTPExpression9 | Unset
        if isinstance(_base, Unset):
            base = UNSET
        else:
            base = BTPExpression9.from_dict(_base)

        is_safe_navigation = d.pop("isSafeNavigation", UNSET)

        _space_in_accessor = d.pop("spaceInAccessor", UNSET)
        space_in_accessor: BTPSpace10 | Unset
        if isinstance(_space_in_accessor, Unset):
            space_in_accessor = UNSET
        else:
            space_in_accessor = BTPSpace10.from_dict(_space_in_accessor)

        btp_expression_access_237 = cls(
            atomic=atomic,
            bt_type=bt_type,
            documentation_type=documentation_type,
            end_source_location=end_source_location,
            node_id=node_id,
            short_descriptor=short_descriptor,
            space_after=space_after,
            space_before=space_before,
            space_default=space_default,
            start_source_location=start_source_location,
            accessor=accessor,
            base=base,
            is_safe_navigation=is_safe_navigation,
            space_in_accessor=space_in_accessor,
        )

        btp_expression_access_237.additional_properties = d
        return btp_expression_access_237

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
