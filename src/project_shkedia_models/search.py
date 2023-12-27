from pydantic import BaseModel
from typing import List,Any

class SearchResult(BaseModel):
    total_results_number: int
    page_number: int = 0
    page_size: int | None = None
    results: List[Any]