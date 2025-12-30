# Perseus-Lookup

Command-line tools for searching the Perseus Word Study Tool for Greek and Latin words using Python and Beautiful Soup. See the docstrings in each script for more details and usage examples.

## Requirements

- Python 3.8+
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](https://docs.python-requests.org/en/latest/)


Install dependencies (recommended):

```sh
# Using uv (fastest):
uv pip install -r pyproject.toml
# Or with pip (PEP 621 support required):
pip install .
```
## Modern Python Project Notes

- This project now uses [pyproject.toml](https://peps.python.org/pep-0621/) for dependencies and metadata, following modern Python standards.

## Usage

Make the scripts executable:

```sh
chmod +x greek_lookup.py latin_lookup.py
```

Run from the command line:

```sh
python greek_lookup.py logos
python latin_lookup.py verbum
```

Or add aliases to your shell profile (e.g., .zshrc or .bash_profile):

```sh
alias greek='python /path/to/greek_lookup.py'
alias latin='python /path/to/latin_lookup.py'
```

Example output:

```sh
> greek logos
logos > λόγος: computation, reckoning

> latin verbum
verbum > verbum: a word
```

## Testing

Tests are located in the `tests/` folder and use [pytest](https://docs.pytest.org/). To run the tests:

```sh
pytest
# or, if using a virtual environment:
.venv/bin/python -m pytest
```

These tests use real HTTP requests to the Perseus website. For true unit tests, consider mocking network calls.

## Change log
- 2025-12-30: v0.2.0 — Modernized scripts, improved typing and code quality, switched to pyproject.toml for dependency management, and updated documentation.
- 2016-10-03: v0.1.0Updated to Python3
