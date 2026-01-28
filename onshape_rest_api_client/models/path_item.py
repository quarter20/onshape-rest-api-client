from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation import Operation
    from ..models.parameter import Parameter
    from ..models.path_item_extensions import PathItemExtensions
    from ..models.server import Server


T = TypeVar("T", bound="PathItem")


@_attrs_define
class PathItem:
    """
    Attributes:
        delete (Operation | Unset):
        description (str | Unset):
        extensions (PathItemExtensions | Unset):
        get (Operation | Unset):
        getref (str | Unset):
        head (Operation | Unset):
        options (Operation | Unset):
        parameters (list[Parameter] | Unset):
        patch (Operation | Unset):
        post (Operation | Unset):
        put (Operation | Unset):
        servers (list[Server] | Unset):
        summary (str | Unset):
        trace (Operation | Unset):
    """

    delete: Operation | Unset = UNSET
    description: str | Unset = UNSET
    extensions: PathItemExtensions | Unset = UNSET
    get: Operation | Unset = UNSET
    getref: str | Unset = UNSET
    head: Operation | Unset = UNSET
    options: Operation | Unset = UNSET
    parameters: list[Parameter] | Unset = UNSET
    patch: Operation | Unset = UNSET
    post: Operation | Unset = UNSET
    put: Operation | Unset = UNSET
    servers: list[Server] | Unset = UNSET
    summary: str | Unset = UNSET
    trace: Operation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete.to_dict()

        description = self.description

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        get: dict[str, Any] | Unset = UNSET
        if not isinstance(self.get, Unset):
            get = self.get.to_dict()

        getref = self.getref

        head: dict[str, Any] | Unset = UNSET
        if not isinstance(self.head, Unset):
            head = self.head.to_dict()

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        patch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.patch, Unset):
            patch = self.patch.to_dict()

        post: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post, Unset):
            post = self.post.to_dict()

        put: dict[str, Any] | Unset = UNSET
        if not isinstance(self.put, Unset):
            put = self.put.to_dict()

        servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        summary = self.summary

        trace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trace, Unset):
            trace = self.trace.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete is not UNSET:
            field_dict["delete"] = delete
        if description is not UNSET:
            field_dict["description"] = description
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if get is not UNSET:
            field_dict["get"] = get
        if getref is not UNSET:
            field_dict["get$ref"] = getref
        if head is not UNSET:
            field_dict["head"] = head
        if options is not UNSET:
            field_dict["options"] = options
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if patch is not UNSET:
            field_dict["patch"] = patch
        if post is not UNSET:
            field_dict["post"] = post
        if put is not UNSET:
            field_dict["put"] = put
        if servers is not UNSET:
            field_dict["servers"] = servers
        if summary is not UNSET:
            field_dict["summary"] = summary
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.operation import Operation
        from ..models.parameter import Parameter
        from ..models.path_item_extensions import PathItemExtensions
        from ..models.server import Server

        d = dict(src_dict)
        _delete = d.pop("delete", UNSET)
        delete: Operation | Unset
        if isinstance(_delete, Unset):
            delete = UNSET
        else:
            delete = Operation.from_dict(_delete)

        description = d.pop("description", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: PathItemExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = PathItemExtensions.from_dict(_extensions)

        _get = d.pop("get", UNSET)
        get: Operation | Unset
        if isinstance(_get, Unset):
            get = UNSET
        else:
            get = Operation.from_dict(_get)

        getref = d.pop("get$ref", UNSET)

        _head = d.pop("head", UNSET)
        head: Operation | Unset
        if isinstance(_head, Unset):
            head = UNSET
        else:
            head = Operation.from_dict(_head)

        _options = d.pop("options", UNSET)
        options: Operation | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = Operation.from_dict(_options)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[Parameter] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = Parameter.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        _patch = d.pop("patch", UNSET)
        patch: Operation | Unset
        if isinstance(_patch, Unset):
            patch = UNSET
        else:
            patch = Operation.from_dict(_patch)

        _post = d.pop("post", UNSET)
        post: Operation | Unset
        if isinstance(_post, Unset):
            post = UNSET
        else:
            post = Operation.from_dict(_post)

        _put = d.pop("put", UNSET)
        put: Operation | Unset
        if isinstance(_put, Unset):
            put = UNSET
        else:
            put = Operation.from_dict(_put)

        _servers = d.pop("servers", UNSET)
        servers: list[Server] | Unset = UNSET
        if _servers is not UNSET:
            servers = []
            for servers_item_data in _servers:
                servers_item = Server.from_dict(servers_item_data)

                servers.append(servers_item)

        summary = d.pop("summary", UNSET)

        _trace = d.pop("trace", UNSET)
        trace: Operation | Unset
        if isinstance(_trace, Unset):
            trace = UNSET
        else:
            trace = Operation.from_dict(_trace)

        path_item = cls(
            delete=delete,
            description=description,
            extensions=extensions,
            get=get,
            getref=getref,
            head=head,
            options=options,
            parameters=parameters,
            patch=patch,
            post=post,
            put=put,
            servers=servers,
            summary=summary,
            trace=trace,
        )

        path_item.additional_properties = d
        return path_item

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
