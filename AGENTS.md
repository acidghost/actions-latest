# Agent Guide for actions-latest

## Project Overview

This is a personal fork of the [actions-latest](https://github.com/simonw/actions-latest) project by Simon Willison. It's a simple Python 3.12+ script that:

- Fetches all repos from the GitHub `actions` organization via the GitHub REST API
- Extracts the latest `vINTEGER` tag (e.g., `v1`, `v2`, `v10`) from each repo
- Writes results to `versions.txt` (one line per repo: `org/repo@tag`)
- Updates the README.md with the latest versions
- Caches repos known to have no vINTEGER tags to avoid repeated API calls

**Note**: This is a personal fork. Contributions may not be considered or merged.

## Essential Commands

### Running Tests

```bash
python -m unittest test_fetch_versions -v
```

### Running the Main Script

```bash
python fetch_versions.py
```

### CI Workflow

The GitHub Actions workflow runs automatically daily at 4:51 UTC and can be manually triggered via `workflow_dispatch`. It:

1. Runs tests
2. Executes `fetch_versions.py`
3. Commits and pushes changes to `versions.txt` and `unversioned.txt`

## Code Organization

### Key Files

- **`fetch_versions.py`** - Main script (217 lines)
  - `fetch_repos()` - Fetches all repos for an org with pagination
  - `fetch_tags()` - Fetches all tags for a repo with pagination
  - `get_latest_version_tag()` - Extracts latest `^v(\d+)$` pattern tag
  - `update_readme()` - Updates README.md between marker comments
  - `load_unversioned()` / `save_unversioned()` - Cache management
  - `main()` - Orchestrates the entire process

- **`test_fetch_versions.py`** - Unit tests (372 lines)
  - Uses standard Python `unittest` framework
  - Tests each function independently with mocked subprocess calls
  - Integration tests for the full `main()` function

- **`versions.txt`** - Output file (auto-generated)
  - Format: one line per repo: `org/repo@tag`
  - Sorted alphabetically by repo name

- **`unversioned.txt`** - Cache file (auto-generated)
  - List of repos known to have no vINTEGER tags
  - Sorted alphabetically, one per line

- **`README.md`** - Documentation
  - Contains auto-updated versions section between `<!-- VERSIONS_START -->` and `<!-- VERSIONS_END -->` markers

- **`.github/workflows/update.yml`** - CI workflow
  - Runs on cron schedule and manual dispatch
  - Commits changes with message "chore: update versions"

## Code Conventions and Patterns

### Type Hints

- Python 3.12+ style: `set[str]`, `list[dict]`, `str | None`
- All functions have type hints for parameters and return types

### File Operations

- Use `pathlib.Path` for all file operations
- `Path(__file__).parent.resolve()` for script directory
- `Path.read_text()` / `Path.write_text()` for file I/O

### HTTP Requests

- **No external HTTP libraries** (no `requests`, `httpx`, etc.)
- Uses `subprocess.run` with `curl` to call GitHub API
- Accept header: `application/vnd.github+json`
- Base URL: `https://api.github.com`

### Version Tag Pattern

- Only matches `^v(\d+)$` pattern (e.g., `v1`, `v2`, `v10`)
- Does NOT match: `v1.0`, `v1.0.0`, `v1-beta`, `release-1`
- Sorting is numeric, not lexicographic (v10 > v9)

### Pagination

- GitHub API uses `per_page=100` (max limit)
- Loop until empty response or fewer than `per_page` items returned
- Applied to both `fetch_repos()` and `fetch_tags()`

### Caching Strategy

- `unversioned.txt` caches repos without vINTEGER tags
- Reduces API calls on subsequent runs
- Cache is loaded at start and updated at end of run
- Sorted alphabetically before saving

### README Updates

- Uses regex to find and replace content between markers
- Pattern: `re.escape(README_START_MARKER) + r".*?" + re.escape(README_END_MARKER)` with `re.DOTALL`
- If markers don't exist, appends to end of README

### Error Handling

- API errors (e.g., rate limiting) detected by checking for `"message"` key in response
- Errors printed to stderr, processing continues for other repos
- Subprocess calls use `check=True` to raise exceptions on non-zero exit codes

## Testing Patterns

### Test Structure

```python
class TestFunctionName(unittest.TestCase):
    def test_specific_behavior(self):
        # Arrange
        mock_input = [...]

        # Act
        result = function_under_test(mock_input)

        # Assert
        self.assertEqual(result, expected)
```

### Mocking Subprocess Calls

```python
@patch("fetch_versions.subprocess.run")
def test_fetch_repos(self, mock_run):
    mock_run.return_value = MagicMock(
        stdout=json.dumps([...]),
        returncode=0,
    )
    # Call function and assert
```

### Temporary Files in Tests

```python
with tempfile.TemporaryDirectory() as tmpdir:
    tmppath = Path(tmpdir)
    # Create test files and test logic
```

### Integration Testing

- Use `@patch` decorators for all external dependencies
- Test full `main()` function with all components mocked
- Verify file I/O by reading generated files

## Important Gotchas

### Version Tag Matching

- The script only cares about `vINTEGER` tags, not semantic versioning
- Many repos use `v1.0.0` style tags and will be marked as "unversioned"
- This is by design - the script targets GitHub Actions' integer-only version scheme

### API Rate Limiting

- GitHub API has rate limits (60 requests/hour for unauthenticated)
- The script uses caching to minimize API calls on subsequent runs
- If hitting limits, consider authenticating (not currently implemented)

### No Dependencies

- Project has NO external dependencies
- Uses only Python standard library
- No `requirements.txt`, `pyproject.toml`, or `setup.py` files

### CI Commit Behavior

- The workflow commits with message "chore: update versions"
- Uses github-actions[bot] identity
- Only commits if there are actual changes (uses `git diff --staged --quiet`)

### README Marker Placement

- Markers must exist in README for updates to work in-place
- If missing, content is appended to the end of README
- Markers are: `<!-- VERSIONS_START -->` and `<!-- VERSIONS_END -->`

### Output File Format

- `versions.txt` has a trailing newline
- Each line ends with a newline
- Format is strictly: `org/repo@tag` (no variations)

## Modifying the Codebase

### Adding New Features

1. Write tests in `test_fetch_versions.py` following existing patterns
2. Implement in `fetch_versions.py` with type hints
3. Use standard library only (no new dependencies)
4. Run tests locally before committing

### Testing Changes

Always run: `python -m unittest test_fetch_versions -v`
