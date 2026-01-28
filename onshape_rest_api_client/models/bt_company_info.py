from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_address_info import BTAddressInfo
    from ..models.bt_purchase_info import BTPurchaseInfo


T = TypeVar("T", bound="BTCompanyInfo")


@_attrs_define
class BTCompanyInfo:
    """
    Attributes:
        address (BTAddressInfo | Unset):
        admin (bool | Unset):
        description (str | Unset):
        domain_prefix (str | Unset):
        enterprise_base_url (str | Unset):
        enterprise_subtype (int | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        image (str | Unset):
        name (str | Unset): Name of the resource.
        no_public_documents (bool | Unset):
        owner_id (str | Unset):
        purchase (BTPurchaseInfo | Unset):
        secondary_domain_prefixes (list[str] | Unset):
        state (int | Unset):
        type_ (int | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    address: BTAddressInfo | Unset = UNSET
    admin: bool | Unset = UNSET
    description: str | Unset = UNSET
    domain_prefix: str | Unset = UNSET
    enterprise_base_url: str | Unset = UNSET
    enterprise_subtype: int | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    image: str | Unset = UNSET
    name: str | Unset = UNSET
    no_public_documents: bool | Unset = UNSET
    owner_id: str | Unset = UNSET
    purchase: BTPurchaseInfo | Unset = UNSET
    secondary_domain_prefixes: list[str] | Unset = UNSET
    state: int | Unset = UNSET
    type_: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        admin = self.admin

        description = self.description

        domain_prefix = self.domain_prefix

        enterprise_base_url = self.enterprise_base_url

        enterprise_subtype = self.enterprise_subtype

        href = self.href

        id = self.id

        image = self.image

        name = self.name

        no_public_documents = self.no_public_documents

        owner_id = self.owner_id

        purchase: dict[str, Any] | Unset = UNSET
        if not isinstance(self.purchase, Unset):
            purchase = self.purchase.to_dict()

        secondary_domain_prefixes: list[str] | Unset = UNSET
        if not isinstance(self.secondary_domain_prefixes, Unset):
            secondary_domain_prefixes = self.secondary_domain_prefixes

        state = self.state

        type_ = self.type_

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if admin is not UNSET:
            field_dict["admin"] = admin
        if description is not UNSET:
            field_dict["description"] = description
        if domain_prefix is not UNSET:
            field_dict["domainPrefix"] = domain_prefix
        if enterprise_base_url is not UNSET:
            field_dict["enterpriseBaseUrl"] = enterprise_base_url
        if enterprise_subtype is not UNSET:
            field_dict["enterpriseSubtype"] = enterprise_subtype
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if name is not UNSET:
            field_dict["name"] = name
        if no_public_documents is not UNSET:
            field_dict["noPublicDocuments"] = no_public_documents
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if purchase is not UNSET:
            field_dict["purchase"] = purchase
        if secondary_domain_prefixes is not UNSET:
            field_dict["secondaryDomainPrefixes"] = secondary_domain_prefixes
        if state is not UNSET:
            field_dict["state"] = state
        if type_ is not UNSET:
            field_dict["type"] = type_
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_address_info import BTAddressInfo
        from ..models.bt_purchase_info import BTPurchaseInfo

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: BTAddressInfo | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = BTAddressInfo.from_dict(_address)

        admin = d.pop("admin", UNSET)

        description = d.pop("description", UNSET)

        domain_prefix = d.pop("domainPrefix", UNSET)

        enterprise_base_url = d.pop("enterpriseBaseUrl", UNSET)

        enterprise_subtype = d.pop("enterpriseSubtype", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        name = d.pop("name", UNSET)

        no_public_documents = d.pop("noPublicDocuments", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        _purchase = d.pop("purchase", UNSET)
        purchase: BTPurchaseInfo | Unset
        if isinstance(_purchase, Unset):
            purchase = UNSET
        else:
            purchase = BTPurchaseInfo.from_dict(_purchase)

        secondary_domain_prefixes = cast(list[str], d.pop("secondaryDomainPrefixes", UNSET))

        state = d.pop("state", UNSET)

        type_ = d.pop("type", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_company_info = cls(
            address=address,
            admin=admin,
            description=description,
            domain_prefix=domain_prefix,
            enterprise_base_url=enterprise_base_url,
            enterprise_subtype=enterprise_subtype,
            href=href,
            id=id,
            image=image,
            name=name,
            no_public_documents=no_public_documents,
            owner_id=owner_id,
            purchase=purchase,
            secondary_domain_prefixes=secondary_domain_prefixes,
            state=state,
            type_=type_,
            view_ref=view_ref,
        )

        bt_company_info.additional_properties = d
        return bt_company_info

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
