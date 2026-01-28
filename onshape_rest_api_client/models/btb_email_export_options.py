from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTBEmailExportOptions")


@_attrs_define
class BTBEmailExportOptions:
    """Options for exporting elements as a link in an email.

    Attributes:
        email_link (bool): Use `true` if a link in an email should be sent. Default: False.
        email_to (list[str]): List of email addresses to send the email to.
        from_user_id (str): Id of the user who does the export.
        email_message (str | Unset): Message to send in the email body along with the download link.
        email_subject (str | Unset): Subject to send the email with. Default: 'User sent you a file exported from
            Onshape'.
        password (str | Unset): A password to protect the email with. Default: 'false'.
        password_required (bool | Unset): Use `true` if the email should be protected with a password. Default: False.
        send_copy_to_me (bool | Unset): Use `true` if email copy should be sent to the user who does the export.
            Default: False.
        valid_for_days (int | Unset): Number of days to keep the link valid for. Default: 3.
    """

    email_to: list[str]
    from_user_id: str
    email_link: bool = False
    email_message: str | Unset = UNSET
    email_subject: str | Unset = "User sent you a file exported from Onshape"
    password: str | Unset = "false"
    password_required: bool | Unset = False
    send_copy_to_me: bool | Unset = False
    valid_for_days: int | Unset = 3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_link = self.email_link

        email_to = self.email_to

        from_user_id = self.from_user_id

        email_message = self.email_message

        email_subject = self.email_subject

        password = self.password

        password_required = self.password_required

        send_copy_to_me = self.send_copy_to_me

        valid_for_days = self.valid_for_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emailLink": email_link,
                "emailTo": email_to,
                "fromUserId": from_user_id,
            }
        )
        if email_message is not UNSET:
            field_dict["emailMessage"] = email_message
        if email_subject is not UNSET:
            field_dict["emailSubject"] = email_subject
        if password is not UNSET:
            field_dict["password"] = password
        if password_required is not UNSET:
            field_dict["passwordRequired"] = password_required
        if send_copy_to_me is not UNSET:
            field_dict["sendCopyToMe"] = send_copy_to_me
        if valid_for_days is not UNSET:
            field_dict["validForDays"] = valid_for_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_link = d.pop("emailLink")

        email_to = cast(list[str], d.pop("emailTo"))

        from_user_id = d.pop("fromUserId")

        email_message = d.pop("emailMessage", UNSET)

        email_subject = d.pop("emailSubject", UNSET)

        password = d.pop("password", UNSET)

        password_required = d.pop("passwordRequired", UNSET)

        send_copy_to_me = d.pop("sendCopyToMe", UNSET)

        valid_for_days = d.pop("validForDays", UNSET)

        btb_email_export_options = cls(
            email_link=email_link,
            email_to=email_to,
            from_user_id=from_user_id,
            email_message=email_message,
            email_subject=email_subject,
            password=password,
            password_required=password_required,
            send_copy_to_me=send_copy_to_me,
            valid_for_days=valid_for_days,
        )

        btb_email_export_options.additional_properties = d
        return btb_email_export_options

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
