from __future__ import annotations

from collections import UserList
from typing import Any, Callable, Dict, Iterable


class RecordBatch(UserList):
    def __init__(self, initlist: Iterable[Dict[str, Any]]) -> None:
        self.data = list(initlist)

    def apply(
        self, transform: Callable[[...], Iterable[Dict[str, Any]]], **kwargs
    ) -> RecordBatch:
        """
        Applies a transformation on records
        and returns the transformed records.

        Args:
            self (RecordBatch): The source records.

            transform (
                Callable[
                    [...],
                    Iterable[Dict[str, Any]]
                ]
            ):
                A transformation method that receives a record batch
                and returns the transformed batch.

        Returns:
            RecordBatch: The transformed records.
        """
        return RecordBatch(initlist=transform(self, **kwargs))
