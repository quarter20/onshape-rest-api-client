from enum import Enum


class BTSearchEntityType(str, Enum):
    APP_STORE_ENTRY = "app_store_entry"
    ASSIGNMENT = "assignment"
    CAPABILITY = "capability"
    CLASSROOM = "classroom"
    CLASSROOM_ITEM = "classroom_item"
    COMMENT_TASK = "comment_task"
    COMPANY = "company"
    DOCUMENT = "document"
    ELEMENT = "element"
    FOLDER = "folder"
    FRIEND = "friend"
    GENERIC_TASK = "generic_task"
    ITEM = "item"
    PART = "part"
    PROJECT = "project"
    PUBLICATION = "publication"
    RELEASE_TASK = "release_task"
    SUBMISSION = "submission"
    TEAM = "team"
    UNKNOWN = "unknown"
    USER = "user"
    VERSION = "version"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
