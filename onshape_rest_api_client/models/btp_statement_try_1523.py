from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_definition_type import GBTPDefinitionType
from ..models.gbtp_type import GBTPType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btp_annotation_231 import BTPAnnotation231
    from ..models.btp_identifier_8 import BTPIdentifier8
    from ..models.btp_space_10 import BTPSpace10
    from ..models.btp_statement_block_271 import BTPStatementBlock271


T = TypeVar("T", bound="BTPStatementTry1523")


@_attrs_define
class BTPStatementTry1523:
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
        annotation (BTPAnnotation231 | Unset):
        body (BTPStatementBlock271 | Unset):
        catch_block (BTPStatementBlock271 | Unset):
        catch_variable (BTPIdentifier8 | Unset):
        identifier (BTPIdentifier8 | Unset):
        silent (bool | Unset):
        space_after_catch (BTPSpace10 | Unset):
        space_before_silent (BTPSpace10 | Unset):
        standard_type (GBTPType | Unset):
        type_name (str | Unset):
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
    annotation: BTPAnnotation231 | Unset = UNSET
    body: BTPStatementBlock271 | Unset = UNSET
    catch_block: BTPStatementBlock271 | Unset = UNSET
    catch_variable: BTPIdentifier8 | Unset = UNSET
    identifier: BTPIdentifier8 | Unset = UNSET
    silent: bool | Unset = UNSET
    space_after_catch: BTPSpace10 | Unset = UNSET
    space_before_silent: BTPSpace10 | Unset = UNSET
    standard_type: GBTPType | Unset = UNSET
    type_name: str | Unset = UNSET
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

        annotation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotation, Unset):
            annotation = self.annotation.to_dict()

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        catch_block: dict[str, Any] | Unset = UNSET
        if not isinstance(self.catch_block, Unset):
            catch_block = self.catch_block.to_dict()

        catch_variable: dict[str, Any] | Unset = UNSET
        if not isinstance(self.catch_variable, Unset):
            catch_variable = self.catch_variable.to_dict()

        identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        silent = self.silent

        space_after_catch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_catch, Unset):
            space_after_catch = self.space_after_catch.to_dict()

        space_before_silent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_before_silent, Unset):
            space_before_silent = self.space_before_silent.to_dict()

        standard_type: str | Unset = UNSET
        if not isinstance(self.standard_type, Unset):
            standard_type = self.standard_type.value

        type_name = self.type_name

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
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if body is not UNSET:
            field_dict["body"] = body
        if catch_block is not UNSET:
            field_dict["catchBlock"] = catch_block
        if catch_variable is not UNSET:
            field_dict["catchVariable"] = catch_variable
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if silent is not UNSET:
            field_dict["silent"] = silent
        if space_after_catch is not UNSET:
            field_dict["spaceAfterCatch"] = space_after_catch
        if space_before_silent is not UNSET:
            field_dict["spaceBeforeSilent"] = space_before_silent
        if standard_type is not UNSET:
            field_dict["standardType"] = standard_type
        if type_name is not UNSET:
            field_dict["typeName"] = type_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btp_annotation_231 import BTPAnnotation231
        from ..models.btp_identifier_8 import BTPIdentifier8
        from ..models.btp_space_10 import BTPSpace10
        from ..models.btp_statement_block_271 import BTPStatementBlock271

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

        _annotation = d.pop("annotation", UNSET)
        annotation: BTPAnnotation231 | Unset
        if isinstance(_annotation, Unset):
            annotation = UNSET
        else:
            annotation = BTPAnnotation231.from_dict(_annotation)

        _body = d.pop("body", UNSET)
        body: BTPStatementBlock271 | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = BTPStatementBlock271.from_dict(_body)

        _catch_block = d.pop("catchBlock", UNSET)
        catch_block: BTPStatementBlock271 | Unset
        if isinstance(_catch_block, Unset):
            catch_block = UNSET
        else:
            catch_block = BTPStatementBlock271.from_dict(_catch_block)

        _catch_variable = d.pop("catchVariable", UNSET)
        catch_variable: BTPIdentifier8 | Unset
        if isinstance(_catch_variable, Unset):
            catch_variable = UNSET
        else:
            catch_variable = BTPIdentifier8.from_dict(_catch_variable)

        _identifier = d.pop("identifier", UNSET)
        identifier: BTPIdentifier8 | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = BTPIdentifier8.from_dict(_identifier)

        silent = d.pop("silent", UNSET)

        _space_after_catch = d.pop("spaceAfterCatch", UNSET)
        space_after_catch: BTPSpace10 | Unset
        if isinstance(_space_after_catch, Unset):
            space_after_catch = UNSET
        else:
            space_after_catch = BTPSpace10.from_dict(_space_after_catch)

        _space_before_silent = d.pop("spaceBeforeSilent", UNSET)
        space_before_silent: BTPSpace10 | Unset
        if isinstance(_space_before_silent, Unset):
            space_before_silent = UNSET
        else:
            space_before_silent = BTPSpace10.from_dict(_space_before_silent)

        _standard_type = d.pop("standardType", UNSET)
        standard_type: GBTPType | Unset
        if isinstance(_standard_type, Unset):
            standard_type = UNSET
        else:
            standard_type = GBTPType(_standard_type)

        type_name = d.pop("typeName", UNSET)

        btp_statement_try_1523 = cls(
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
            annotation=annotation,
            body=body,
            catch_block=catch_block,
            catch_variable=catch_variable,
            identifier=identifier,
            silent=silent,
            space_after_catch=space_after_catch,
            space_before_silent=space_before_silent,
            standard_type=standard_type,
            type_name=type_name,
        )

        btp_statement_try_1523.additional_properties = d
        return btp_statement_try_1523

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
