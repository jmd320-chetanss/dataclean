from dataclasses import dataclass

from dataclean.cleaners.none_cleaner import NoneCleaner


@dataclass(frozen=True)
class DropCleaner(NoneCleaner):
    pass
