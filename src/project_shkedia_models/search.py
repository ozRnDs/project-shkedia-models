from pydantic import BaseModel
from typing import List,Any
from math import ceil

class SearchResult(BaseModel):
    total_results_number: int
    page_number: int = 0
    page_size: int | None = None
    results: List[Any]

    @property
    def number_of_pages(self):
        return ceil(self.total_results_number/self.page_size)