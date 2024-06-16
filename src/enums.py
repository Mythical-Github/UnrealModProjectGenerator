import enum as Enum


class UnrealWindowsDirType(Enum):
    WINDOWS = 'windows'
    WINDOWS_NO_EDITOR = 'windows_no_editor'


def get_enum_from_val(enum: Enum, value: str) -> Enum:
    for member in enum:
        if member.value == value:
            return member
    return None
