from dataclasses import dataclass

from dataclean.cleaners.string_cleaner import StringCleaner


@dataclass(frozen=True)
class EnumCleaner(StringCleaner):
    pass
