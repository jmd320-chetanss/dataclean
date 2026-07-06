from dataclasses import dataclass

from dataclean.cleaners.col_cleaner import ColCleaner


@dataclass(frozen=True)
class NoneCleaner(ColCleaner):
    def clean_value(self, value: str | None) -> str | None:
        return value
