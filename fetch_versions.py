#!/usr/bin/env python3
"""
Fetch all repos from the GitHub actions organization and their tags via the API,
and generate a versions.txt file with the latest vINTEGER tags.

No git cloning required - uses GitHub REST API only.

Repos known to have no vINTEGER tags are cached in unversioned.txt to skip
API calls on future runs.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent.resolve()
VERSIONS_FILE = SCRIPT_DIR / "versions.txt"
VERSIONS_SHA_FILE = SCRIPT_DIR / "versions-sha.txt"
UNVERSIONED_FILE = SCRIPT_DIR / "unversioned.txt"
README_FILE = SCRIPT_DIR / "README.md"

# Markers for the README section
README_START_MARKER = "<!-- VERSIONS_START -->"
README_END_MARKER = "<!-- VERSIONS_END -->"
README_SHA_START_MARKER = "<!-- VERSIONS_SHA_START -->"
README_SHA_END_MARKER = "<!-- VERSIONS_SHA_END -->"
ORG_NAME = "actions"
ADDITIONAL_REPOS: list[str] = [
    "astral-sh/setup-uv",
    "dependabot/fetch-metadata",
    "docker/build-push-action",
    "docker/login-action",
    "docker/metadata-action",
    "docker/setup-buildx-action",
    "docker/setup-qemu-action",
    "golangci/golangci-lint-action",
    "goreleaser/goreleaser-action",
    "ruby/setup-ruby",
    "taiki-e/install-action",
]
SKIP_REPOS: list[str] = [
    "action-versions",
    "actions-runner-controller",
    "actions-sync",
    "alpine_nodejs",
    "container-prebuilt-action",
    "gh-actions-cache",
    "github",
    "publish-action",
    "publish-immutable-action",
    "runner",
    "runner-container-hooks",
]
GITHUB_API_URL = "https://api.github.com"


def parse_repo(repo_ref: str) -> tuple[str, str]:
    """Parse 'org/repo' format into (org, repo_name) tuple."""
    parts = repo_ref.split("/")
    if len(parts) != 2:
        raise ValueError(f"Invalid repo format: {repo_ref}, expected 'org/repo'")
    return (parts[0], parts[1])


def load_unversioned() -> set[str]:
    """Load the set of repos known to have no vINTEGER tags."""
    if not UNVERSIONED_FILE.exists():
        return set()
    return set(
        line.strip()
        for line in UNVERSIONED_FILE.read_text().splitlines()
        if line.strip()
    )


def save_unversioned(repos: set[str]) -> None:
    """Save the set of repos known to have no vINTEGER tags."""
    with open(UNVERSIONED_FILE, "w") as f:
        for repo_name in sorted(repos):
            f.write(f"{repo_name}\n")


def update_readme(versions_content: str) -> None:
    """Update the README.md with the latest versions in a fenced code block."""
    if not README_FILE.exists():
        print(f"Warning: {README_FILE} not found, skipping README update")
        return

    readme_text = README_FILE.read_text()

    # Build the new section content
    new_section = f"""{README_START_MARKER}
## Latest versions

```
{versions_content}```
{README_END_MARKER}"""

    # Check if markers already exist
    if README_START_MARKER in readme_text and README_END_MARKER in readme_text:
        # Replace existing section
        pattern = re.compile(
            re.escape(README_START_MARKER) + r".*?" + re.escape(README_END_MARKER),
            re.DOTALL,
        )
        new_readme = pattern.sub(new_section, readme_text)
    else:
        # Append to end of file
        new_readme = readme_text.rstrip() + "\n\n" + new_section + "\n"

    README_FILE.write_text(new_readme)
    print(f"Updated {README_FILE} with latest versions")


def update_readme_sha(versions_sha_content: str) -> None:
    """Update the README.md with the latest SHA-pinned versions in a fenced code block."""
    if not README_FILE.exists():
        print(f"Warning: {README_FILE} not found, skipping README SHA update")
        return

    readme_text = README_FILE.read_text()

    # Build the new section content
    new_section = f"""{README_SHA_START_MARKER}
## Latest versions (SHA-pinned)

```
{versions_sha_content}```
{README_SHA_END_MARKER}"""

    # Check if markers already exist
    if README_SHA_START_MARKER in readme_text and README_SHA_END_MARKER in readme_text:
        # Replace existing section
        pattern = re.compile(
            re.escape(README_SHA_START_MARKER)
            + r".*?"
            + re.escape(README_SHA_END_MARKER),
            re.DOTALL,
        )
        new_readme = pattern.sub(new_section, readme_text)
    else:
        # Append to end of file
        new_readme = readme_text.rstrip() + "\n\n" + new_section + "\n"

    README_FILE.write_text(new_readme)
    print(f"Updated {README_FILE} with SHA-pinned versions")


def fetch_repos(org: str) -> list[dict]:
    """Fetch all repos for an organization using curl."""
    repos = []
    page = 1
    per_page = 100

    while True:
        url = f"{GITHUB_API_URL}/orgs/{org}/repos?per_page={per_page}&page={page}"
        headers = ["-H", "Accept: application/vnd.github+json"]

        token = os.environ.get("GITHUB_TOKEN")
        if token:
            headers.extend(["-H", f"Authorization: token {token}"])

        result = subprocess.run(
            ["curl", "-s"] + headers + [url],
            capture_output=True,
            text=True,
            check=True,
        )

        page_repos = json.loads(result.stdout)

        # Handle error responses (e.g., rate limiting)
        if isinstance(page_repos, dict) and "message" in page_repos:
            print(
                f"API error: {page_repos.get('message', 'Unknown error')}",
                file=sys.stderr,
            )
            break

        if not page_repos:
            break

        repos.extend(page_repos)

        if len(page_repos) < per_page:
            break

        page += 1

    return repos


def fetch_tags(org: str, repo_name: str) -> list[tuple[str, str]]:
    """Fetch all tags for a repository using the GitHub API.

    Returns a list of (tag_name, commit_sha) tuples.
    """
    tags = []
    page = 1
    per_page = 100

    while True:
        url = f"{GITHUB_API_URL}/repos/{org}/{repo_name}/tags?per_page={per_page}&page={page}"
        headers = ["-H", "Accept: application/vnd.github+json"]

        token = os.environ.get("GITHUB_TOKEN")
        if token:
            headers.extend(["-H", f"Authorization: token {token}"])

        result = subprocess.run(
            ["curl", "-s"] + headers + [url],
            capture_output=True,
            text=True,
            check=True,
        )

        page_tags = json.loads(result.stdout)

        # Handle error responses (e.g., rate limiting)
        if isinstance(page_tags, dict) and "message" in page_tags:
            print(
                f"  API error for {repo_name}: {page_tags['message']}", file=sys.stderr
            )
            break

        if not page_tags:
            break

        tags.extend((tag["name"], tag["commit"]["sha"]) for tag in page_tags)

        if len(page_tags) < per_page:
            break

        page += 1

    return tags


def get_latest_version_tag(tags: list[tuple[str, str]]) -> str | None:
    """Get the latest vINTEGER tag from a list of (tag_name, commit_sha) tuples.

    Returns only the tag name.
    """
    # Filter to vINTEGER tags (e.g., v1, v2, v10)
    version_pattern = re.compile(r"^v(\d+)$")
    version_tags = []

    for tag_name, _ in tags:
        match = version_pattern.match(tag_name.strip())
        if match:
            version_tags.append((int(match.group(1)), tag_name.strip()))

    if not version_tags:
        return None

    # Sort by version number descending and return the latest tag name
    version_tags.sort(reverse=True, key=lambda x: x[0])
    return version_tags[0][1]


def get_latest_semver_tag(tags: list[tuple[str, str]]) -> tuple[str, str] | None:
    """Get the latest semantic version tag from a list of (tag_name, commit_sha) tuples.

    Returns a tuple of (tag_name, commit_sha) or None if no semver tag found.

    Supports semver format: vX.Y.Z where X, Y, Z are integers.
    """
    # Filter to semver tags (e.g., v1.2.3, v2.0.0)
    version_pattern = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
    version_tags = []

    for tag_name, commit_sha in tags:
        match = version_pattern.match(tag_name.strip())
        if match:
            major = int(match.group(1))
            minor = int(match.group(2))
            patch = int(match.group(3))
            version_tags.append(((major, minor, patch), tag_name.strip(), commit_sha))

    if not version_tags:
        return None

    # Sort by version number descending (major, minor, patch)
    version_tags.sort(reverse=True, key=lambda x: x[0])
    return (version_tags[0][1], version_tags[0][2])


def main():
    """Main function to fetch repos, get tags via API, and generate versions.txt."""
    # Load cached unversioned repos
    unversioned = load_unversioned()
    if unversioned:
        print(f"Loaded {len(unversioned)} known unversioned repos from cache")

    # Fetch repos from the main organization
    print(f"Fetching repos for {ORG_NAME}...")
    org_repos = fetch_repos(ORG_NAME)
    print(f"Found {len(org_repos)} repos")

    # Build list of repos to process: combine org repos with additional repos
    repos_to_process = []

    # Add repos from main organization, excluding skipped ones
    skipped_count = 0
    for repo in org_repos:
        repo_name = repo["name"]
        if repo_name in SKIP_REPOS:
            skipped_count += 1
            continue
        repos_to_process.append((f"{ORG_NAME}/{repo_name}", ORG_NAME, repo_name))

    if skipped_count > 0:
        print(f"Skipped {skipped_count} repos from {ORG_NAME}")

    # Add additional repos
    for additional_repo in ADDITIONAL_REPOS:
        org, repo_name = parse_repo(additional_repo)
        repos_to_process.append((additional_repo, org, repo_name))

    print(
        f"Processing {len(repos_to_process)} repos total (including {len(ADDITIONAL_REPOS)} additional)"
    )

    versions = []
    versions_sha = []
    new_unversioned = set()

    for repo_ref, org, repo_name in repos_to_process:
        # Skip repos known to have no vINTEGER tags
        if repo_ref in unversioned:
            print(f"Skipping {repo_ref} (cached as unversioned)")
            new_unversioned.add(repo_ref)
            continue

        print(f"Fetching tags for {repo_ref}...", end=" ")
        tags = fetch_tags(org, repo_name)
        latest_tag = get_latest_version_tag(tags)
        latest_semver = get_latest_semver_tag(tags)

        if latest_tag:
            # Use vINTEGER tag (preferred)
            versions.append((repo_ref, latest_tag))
            print(f"{latest_tag}")

            # Also add semver info if available
            if latest_semver:
                semver_tag, commit_sha = latest_semver
                versions_sha.append((repo_ref, commit_sha, semver_tag))
        elif latest_semver:
            # Fallback to semver tag when no vINTEGER tag exists
            semver_tag, commit_sha = latest_semver
            versions.append((repo_ref, semver_tag))
            versions_sha.append((repo_ref, commit_sha, semver_tag))
            print(f"{semver_tag} (semver fallback)")
        else:
            # No version tags at all
            print("no version tag")
            new_unversioned.add(repo_ref)

    # Sort alphabetically by repo reference
    versions.sort(key=lambda x: x[0].lower())
    versions_sha.sort(key=lambda x: x[0].lower())

    # Build versions content
    versions_content = (
        "\n".join(f"{repo_ref}@{tag}" for repo_ref, tag in versions) + "\n"
    )

    # Write versions.txt
    with open(VERSIONS_FILE, "w") as f:
        f.write(versions_content)

    # Build versions-sha.txt content
    versions_sha_content = (
        "\n".join(
            f"{repo_ref}@{commit_sha} # {tag}"
            for repo_ref, commit_sha, tag in versions_sha
        )
        + "\n"
    )

    # Write versions-sha.txt
    with open(VERSIONS_SHA_FILE, "w") as f:
        f.write(versions_sha_content)

    # Update README.md with the versions
    update_readme(versions_content)

    # Update README.md with the SHA-pinned versions
    update_readme_sha(versions_sha_content)

    # Update unversioned.txt
    save_unversioned(new_unversioned)

    print(f"\nWrote {len(versions)} versions to {VERSIONS_FILE}")
    print(f"Wrote {len(versions_sha)} versions with SHAs to {VERSIONS_SHA_FILE}")
    print(f"Cached {len(new_unversioned)} unversioned repos to {UNVERSIONED_FILE}")


if __name__ == "__main__":
    main()
