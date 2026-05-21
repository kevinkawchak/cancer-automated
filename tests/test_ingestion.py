"""Tests for robust web search and PDF processing.

LICENSE: MIT
"""

from __future__ import annotations

from conftest import load_module


def test_web_search_returns_results_without_network():
    web = load_module("web_search", "ingestion/web_search.py")
    client = web.WebSearchClient(max_attempts=4, base_delay_s=0.0)
    response = client.search("oncology trial automation", max_results=3)
    assert len(response.results) >= 1
    assert response.query == "oncology trial automation"


def test_web_search_rejects_zero_attempts():
    web = load_module("web_search", "ingestion/web_search.py")
    try:
        web.WebSearchClient(max_attempts=0)
    except ValueError:
        return
    raise AssertionError("expected ValueError for max_attempts=0")


def test_pdf_processor_reports_missing_file():
    pdf = load_module("pdf_processor", "ingestion/pdf_processor.py")
    extract = pdf.PDFProcessor().extract("does_not_exist.pdf")
    assert not extract.ok
    assert "not found" in extract.status


def test_pdf_processor_chunk_estimate():
    pdf = load_module("pdf_processor", "ingestion/pdf_processor.py")
    processor = pdf.PDFProcessor(chunk_cap_bytes=200_000)
    assert processor.chunks_needed("") == 1
    assert processor.chunks_needed("x" * 450_000) == 3
