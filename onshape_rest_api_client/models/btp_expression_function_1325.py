from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_definition_type import GBTPDefinitionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btp_argument_declaration_232 import BTPArgumentDeclaration232
    from ..models.btp_expression_9 import BTPExpression9
    from ..models.btp_space_10 import BTPSpace10
    from ..models.btp_statement_269 import BTPStatement269
    from ..models.btp_statement_block_271 import BTPStatementBlock271
    from ..models.btp_type_name_290 import BTPTypeName290


T = TypeVar("T", bound="BTPExpressionFunction1325")


@_attrs_define
class BTPExpressionFunction1325:
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
        arguments (list[BTPArgumentDeclaration232] | Unset):
        body (BTPStatementBlock271 | Unset):
        expression (BTPExpression9 | Unset):
        is_lambda (bool | Unset):
        is_lambda_with_no_parens (bool | Unset):
        precondition (BTPStatement269 | Unset):
        return_type (BTPTypeName290 | Unset):
        space_after_arglist (BTPSpace10 | Unset):
        space_after_function (BTPSpace10 | Unset):
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
    arguments: list[BTPArgumentDeclaration232] | Unset = UNSET
    body: BTPStatementBlock271 | Unset = UNSET
    expression: BTPExpression9 | Unset = UNSET
    is_lambda: bool | Unset = UNSET
    is_lambda_with_no_parens: bool | Unset = UNSET
    precondition: BTPStatement269 | Unset = UNSET
    return_type: BTPTypeName290 | Unset = UNSET
    space_after_arglist: BTPSpace10 | Unset = UNSET
    space_after_function: BTPSpace10 | Unset = UNSET
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

        arguments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = []
            for arguments_item_data in self.arguments:
                arguments_item = arguments_item_data.to_dict()
                arguments.append(arguments_item)

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        expression: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expression, Unset):
            expression = self.expression.to_dict()

        is_lambda = self.is_lambda

        is_lambda_with_no_parens = self.is_lambda_with_no_parens

        precondition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.precondition, Unset):
            precondition = self.precondition.to_dict()

        return_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.return_type, Unset):
            return_type = self.return_type.to_dict()

        space_after_arglist: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_arglist, Unset):
            space_after_arglist = self.space_after_arglist.to_dict()

        space_after_function: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_function, Unset):
            space_after_function = self.space_after_function.to_dict()

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
        if arguments is not UNSET:
            field_dict["arguments"] = arguments
        if body is not UNSET:
            field_dict["body"] = body
        if expression is not UNSET:
            field_dict["expression"] = expression
        if is_lambda is not UNSET:
            field_dict["isLambda"] = is_lambda
        if is_lambda_with_no_parens is not UNSET:
            field_dict["isLambdaWithNoParens"] = is_lambda_with_no_parens
        if precondition is not UNSET:
            field_dict["precondition"] = precondition
        if return_type is not UNSET:
            field_dict["returnType"] = return_type
        if space_after_arglist is not UNSET:
            field_dict["spaceAfterArglist"] = space_after_arglist
        if space_after_function is not UNSET:
            field_dict["spaceAfterFunction"] = space_after_function
        if space_in_empty_list is not UNSET:
            field_dict["spaceInEmptyList"] = space_in_empty_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btp_argument_declaration_232 import BTPArgumentDeclaration232
        from ..models.btp_expression_9 import BTPExpression9
        from ..models.btp_space_10 import BTPSpace10
        from ..models.btp_statement_269 import BTPStatement269
        from ..models.btp_statement_block_271 import BTPStatementBlock271
        from ..models.btp_type_name_290 import BTPTypeName290

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

        _arguments = d.pop("arguments", UNSET)
        arguments: list[BTPArgumentDeclaration232] | Unset = UNSET
        if _arguments is not UNSET:
            arguments = []
            for arguments_item_data in _arguments:
                arguments_item = BTPArgumentDeclaration232.from_dict(arguments_item_data)

                arguments.append(arguments_item)

        _body = d.pop("body", UNSET)
        body: BTPStatementBlock271 | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = BTPStatementBlock271.from_dict(_body)

        _expression = d.pop("expression", UNSET)
        expression: BTPExpression9 | Unset
        if isinstance(_expression, Unset):
            expression = UNSET
        else:
            expression = BTPExpression9.from_dict(_expression)

        is_lambda = d.pop("isLambda", UNSET)

        is_lambda_with_no_parens = d.pop("isLambdaWithNoParens", UNSET)

        _precondition = d.pop("precondition", UNSET)
        precondition: BTPStatement269 | Unset
        if isinstance(_precondition, Unset):
            precondition = UNSET
        else:
            precondition = BTPStatement269.from_dict(_precondition)

        _return_type = d.pop("returnType", UNSET)
        return_type: BTPTypeName290 | Unset
        if isinstance(_return_type, Unset):
            return_type = UNSET
        else:
            return_type = BTPTypeName290.from_dict(_return_type)

        _space_after_arglist = d.pop("spaceAfterArglist", UNSET)
        space_after_arglist: BTPSpace10 | Unset
        if isinstance(_space_after_arglist, Unset):
            space_after_arglist = UNSET
        else:
            space_after_arglist = BTPSpace10.from_dict(_space_after_arglist)

        _space_after_function = d.pop("spaceAfterFunction", UNSET)
        space_after_function: BTPSpace10 | Unset
        if isinstance(_space_after_function, Unset):
            space_after_function = UNSET
        else:
            space_after_function = BTPSpace10.from_dict(_space_after_function)

        _space_in_empty_list = d.pop("spaceInEmptyList", UNSET)
        space_in_empty_list: BTPSpace10 | Unset
        if isinstance(_space_in_empty_list, Unset):
            space_in_empty_list = UNSET
        else:
            space_in_empty_list = BTPSpace10.from_dict(_space_in_empty_list)

        btp_expression_function_1325 = cls(
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
            arguments=arguments,
            body=body,
            expression=expression,
            is_lambda=is_lambda,
            is_lambda_with_no_parens=is_lambda_with_no_parens,
            precondition=precondition,
            return_type=return_type,
            space_after_arglist=space_after_arglist,
            space_after_function=space_after_function,
            space_in_empty_list=space_in_empty_list,
        )

        btp_expression_function_1325.additional_properties = d
        return btp_expression_function_1325

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
