from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_definition_type import GBTPDefinitionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btp_expression_9 import BTPExpression9
    from ..models.btp_name_261 import BTPName261
    from ..models.btp_space_10 import BTPSpace10


T = TypeVar("T", bound="BTPExpressionCall240")


@_attrs_define
class BTPExpressionCall240:
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
        function_expression (BTPExpression9 | Unset):
        function_name (BTPName261 | Unset):
        function_name_string (str | Unset):
        is_arrow_call (bool | Unset):
        space_in_empty_list (BTPSpace10 | Unset):
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
    function_expression: BTPExpression9 | Unset = UNSET
    function_name: BTPName261 | Unset = UNSET
    function_name_string: str | Unset = UNSET
    is_arrow_call: bool | Unset = UNSET
    space_in_empty_list: BTPSpace10 | Unset = UNSET
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

        function_expression: dict[str, Any] | Unset = UNSET
        if not isinstance(self.function_expression, Unset):
            function_expression = self.function_expression.to_dict()

        function_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.function_name, Unset):
            function_name = self.function_name.to_dict()

        function_name_string = self.function_name_string

        is_arrow_call = self.is_arrow_call

        space_in_empty_list: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_in_empty_list, Unset):
            space_in_empty_list = self.space_in_empty_list.to_dict()

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
        if function_expression is not UNSET:
            field_dict["functionExpression"] = function_expression
        if function_name is not UNSET:
            field_dict["functionName"] = function_name
        if function_name_string is not UNSET:
            field_dict["functionNameString"] = function_name_string
        if is_arrow_call is not UNSET:
            field_dict["isArrowCall"] = is_arrow_call
        if space_in_empty_list is not UNSET:
            field_dict["spaceInEmptyList"] = space_in_empty_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btp_expression_9 import BTPExpression9
        from ..models.btp_name_261 import BTPName261
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

        _function_expression = d.pop("functionExpression", UNSET)
        function_expression: BTPExpression9 | Unset
        if isinstance(_function_expression, Unset):
            function_expression = UNSET
        else:
            function_expression = BTPExpression9.from_dict(_function_expression)

        _function_name = d.pop("functionName", UNSET)
        function_name: BTPName261 | Unset
        if isinstance(_function_name, Unset):
            function_name = UNSET
        else:
            function_name = BTPName261.from_dict(_function_name)

        function_name_string = d.pop("functionNameString", UNSET)

        is_arrow_call = d.pop("isArrowCall", UNSET)

        _space_in_empty_list = d.pop("spaceInEmptyList", UNSET)
        space_in_empty_list: BTPSpace10 | Unset
        if isinstance(_space_in_empty_list, Unset):
            space_in_empty_list = UNSET
        else:
            space_in_empty_list = BTPSpace10.from_dict(_space_in_empty_list)

        btp_expression_call_240 = cls(
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
            function_expression=function_expression,
            function_name=function_name,
            function_name_string=function_name_string,
            is_arrow_call=is_arrow_call,
            space_in_empty_list=space_in_empty_list,
        )

        btp_expression_call_240.additional_properties = d
        return btp_expression_call_240

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
