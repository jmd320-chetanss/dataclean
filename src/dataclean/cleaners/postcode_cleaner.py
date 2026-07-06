from dataclasses import dataclass

from dataclean.cleaners.string_cleaner import StringCleaner


@dataclass(frozen=True)
class PostcodeCleaner(StringCleaner):
    pass
