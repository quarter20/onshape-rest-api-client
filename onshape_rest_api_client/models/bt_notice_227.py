from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_notice_level import GBTNoticeLevel
from ..models.gbt_notice_type import GBTNoticeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_location_info_226 import BTLocationInfo226
    from ..models.bt_node_reference_21 import BTNodeReference21
    from ..models.bt_parameter_expression_error_info_2037 import BTParameterExpressionErrorInfo2037


T = TypeVar("T", bound="BTNotice227")


@_attrs_define
class BTNotice227:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        expression_error_info (BTParameterExpressionErrorInfo2037 | Unset):
        level (GBTNoticeLevel | Unset):
        location_infos (list[BTLocationInfo226] | Unset):
        message (str | Unset):
        node_id (str | Unset):
        parameter_id (str | Unset):
        stack_trace (list[BTLocationInfo226] | Unset):
        try_node (BTNodeReference21 | Unset):
        type_ (GBTNoticeType | Unset):
    """

    bt_type: str | Unset = UNSET
    expression_error_info: BTParameterExpressionErrorInfo2037 | Unset = UNSET
    level: GBTNoticeLevel | Unset = UNSET
    location_infos: list[BTLocationInfo226] | Unset = UNSET
    message: str | Unset = UNSET
    node_id: str | Unset = UNSET
    parameter_id: str | Unset = UNSET
    stack_trace: list[BTLocationInfo226] | Unset = UNSET
    try_node: BTNodeReference21 | Unset = UNSET
    type_: GBTNoticeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        expression_error_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expression_error_info, Unset):
            expression_error_info = self.expression_error_info.to_dict()

        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        location_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.location_infos, Unset):
            location_infos = []
            for location_infos_item_data in self.location_infos:
                location_infos_item = location_infos_item_data.to_dict()
                location_infos.append(location_infos_item)

        message = self.message

        node_id = self.node_id

        parameter_id = self.parameter_id

        stack_trace: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_trace, Unset):
            stack_trace = []
            for stack_trace_item_data in self.stack_trace:
                stack_trace_item = stack_trace_item_data.to_dict()
                stack_trace.append(stack_trace_item)

        try_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.try_node, Unset):
            try_node = self.try_node.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if expression_error_info is not UNSET:
            field_dict["expressionErrorInfo"] = expression_error_info
        if level is not UNSET:
            field_dict["level"] = level
        if location_infos is not UNSET:
            field_dict["locationInfos"] = location_infos
        if message is not UNSET:
            field_dict["message"] = message
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if stack_trace is not UNSET:
            field_dict["stackTrace"] = stack_trace
        if try_node is not UNSET:
            field_dict["tryNode"] = try_node
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_location_info_226 import BTLocationInfo226
        from ..models.bt_node_reference_21 import BTNodeReference21
        from ..models.bt_parameter_expression_error_info_2037 import BTParameterExpressionErrorInfo2037

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _expression_error_info = d.pop("expressionErrorInfo", UNSET)
        expression_error_info: BTParameterExpressionErrorInfo2037 | Unset
        if isinstance(_expression_error_info, Unset):
            expression_error_info = UNSET
        else:
            expression_error_info = BTParameterExpressionErrorInfo2037.from_dict(_expression_error_info)

        _level = d.pop("level", UNSET)
        level: GBTNoticeLevel | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = GBTNoticeLevel(_level)

        _location_infos = d.pop("locationInfos", UNSET)
        location_infos: list[BTLocationInfo226] | Unset = UNSET
        if _location_infos is not UNSET:
            location_infos = []
            for location_infos_item_data in _location_infos:
                location_infos_item = BTLocationInfo226.from_dict(location_infos_item_data)

                location_infos.append(location_infos_item)

        message = d.pop("message", UNSET)

        node_id = d.pop("nodeId", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        _stack_trace = d.pop("stackTrace", UNSET)
        stack_trace: list[BTLocationInfo226] | Unset = UNSET
        if _stack_trace is not UNSET:
            stack_trace = []
            for stack_trace_item_data in _stack_trace:
                stack_trace_item = BTLocationInfo226.from_dict(stack_trace_item_data)

                stack_trace.append(stack_trace_item)

        _try_node = d.pop("tryNode", UNSET)
        try_node: BTNodeReference21 | Unset
        if isinstance(_try_node, Unset):
            try_node = UNSET
        else:
            try_node = BTNodeReference21.from_dict(_try_node)

        _type_ = d.pop("type", UNSET)
        type_: GBTNoticeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GBTNoticeType(_type_)

        bt_notice_227 = cls(
            bt_type=bt_type,
            expression_error_info=expression_error_info,
            level=level,
            location_infos=location_infos,
            message=message,
            node_id=node_id,
            parameter_id=parameter_id,
            stack_trace=stack_trace,
            try_node=try_node,
            type_=type_,
        )

        bt_notice_227.additional_properties = d
        return bt_notice_227

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
