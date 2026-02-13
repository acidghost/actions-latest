# actions-latest

Keeping track of the latest versions of various GitHub Actions

https://acidghost.github.io/actions-latest/versions.txt

https://acidghost.github.io/actions-latest/versions-sha.txt

Access that URL for a list of all of the official Actions belonging to the [GitHub Actions](https://github.com/actions) organization along with their latest version tags.

You can point coding agents such as Claude Code and Codex CLI at this URL so they know the most recent Actions versions to use in their workflow files.

## Usage

### Running Locally

To run the script locally and avoid GitHub API rate limits, set a `GITHUB_TOKEN` environment variable:

```bash
export GITHUB_TOKEN=ghp_your_token_here
python3 fetch_versions.py
```

The token is optional - without it, the script works with lower API rate limits (60 requests/hour for unauthenticated requests).

### Output Files

The script generates two version files:

- **`versions.txt`** - Simple format with integer version tags: `actions/checkout@v6`
- **`versions-sha.txt`** - SHA-pinned format with semver tags: `actions/checkout@abcdef123 # v6.1.0`

## Fork Note

This is a personal fork of the [actions-latest](https://github.com/simonw/actions-latest) project by [Simon Willison](https://github.com/simonw). Contributions to this fork may not be considered or merged.

<!-- VERSIONS_START -->
## Latest versions

```
actions/add-to-project@v1.0.2
actions/ai-inference@v2
actions/attest@v3
actions/attest-build-provenance@v3
actions/attest-sbom@v3
actions/cache@v5
actions/checkout@v6
actions/configure-pages@v5
actions/create-github-app-token@v2
actions/create-release@v1
actions/delete-package-versions@v5
actions/dependency-review-action@v4
actions/deploy-pages@v4
actions/download-artifact@v7
actions/first-interaction@v3
actions/github-script@v8
actions/go-dependency-submission@v2
actions/hello-world-docker-action@v2
actions/hello-world-javascript-action@v1
actions/javascript-action@v1
actions/jekyll-build-pages@v1
actions/labeler@v6
actions/setup-dotnet@v5
actions/setup-elixir@v1
actions/setup-go@v6
actions/setup-haskell@v1
actions/setup-java@v5
actions/setup-node@v6
actions/setup-python@v6
actions/setup-ruby@v1
actions/stale@v10
actions/upload-artifact@v6
actions/upload-pages-artifact@v4
actions/upload-release-asset@v1
astral-sh/setup-uv@v7
dependabot/fetch-metadata@v2
docker/build-push-action@v6
docker/login-action@v3
docker/setup-buildx-action@v3
golangci/golangci-lint-action@v9
goreleaser/goreleaser-action@v6
ruby/setup-ruby@v1.288.0
taiki-e/install-action@v2
```
<!-- VERSIONS_END -->

<!-- VERSIONS_SHA_START -->
## Latest versions (SHA-pinned)

```
actions/add-to-project@244f685bbc3b7adfa8466e08b698b5577571133e # v1.0.2
actions/ai-inference@a380166897b5408b8fb7dddd148142794cb5624a # v2.0.6
actions/attest@e59cbc1ad1ac2d59339667419eb8cdde6eb61e3d # v3.2.0
actions/attest-build-provenance@96278af6caaf10aea03fd8d33a09a777ca52d62f # v3.2.0
actions/attest-sbom@4651f806c01d8637787e274ac3bdf724ef169f34 # v3.0.0
actions/cache@cdf6c1fa76f9f475f3d7449005a359c84ca0f306 # v5.0.3
actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
actions/configure-pages@983d7736d9b0ae728b81ab479565c72886d7745b # v5.0.0
actions/create-github-app-token@29824e69f54612133e76f7eaac726eef6c875baf # v2.2.1
actions/create-release@0cb9c9b65d5d1901c1f53e5e66eaf4afd303e70e # v1.1.4
actions/delete-package-versions@e5bc658cc4c965c472efe991f8beea3981499c55 # v5.0.0
actions/dependency-review-action@3c4e3dcb1aa7874d2c16be7d79418e9b7efd6261 # v4.8.2
actions/deploy-pages@d6db90164ac5ed86f2b6aed7e0febac5b3c0c03e # v4.0.5
actions/download-artifact@37930b1c2abaa49bbe596cd826c3c89aef350131 # v7.0.0
actions/first-interaction@1c4688942c71f71d4f5502a26ea67c331730fa4d # v3.1.0
actions/github-script@ed597411d8f924073f98dfc5c65a23a2325f34cd # v8.0.0
actions/go-dependency-submission@f35d5c9af13ce9cc32f7930b171e315e878f6921 # v2.0.3
actions/javascript-action@4be183afbd08ddadedcf09f17e8e112326894107 # v1.0.1
actions/jekyll-build-pages@44a6e6beabd48582f863aeeb6cb2151cc1716697 # v1.0.13
actions/labeler@634933edcd8ababfe52f92936142cc22ac488b1b # v6.0.1
actions/setup-dotnet@baa11fbfe1d6520db94683bd5c7a3818018e4309 # v5.1.0
actions/setup-elixir@3c118cec41f6c3bfc2c7f2aef9bec886ab0b2324 # v1.5.0
actions/setup-go@7a3fe6cf4cb3a834922a1244abfce67bcef6a0c5 # v6.2.0
actions/setup-haskell@048c29979717135f04282c42c2186bb5945b2d8f # v1.1.4
actions/setup-java@be666c2fcd27ec809703dec50e508c2fdc7f6654 # v5.2.0
actions/setup-node@6044e13b5dc448c55e2357c09f80417699197238 # v6.2.0
actions/setup-python@a309ff8b426b58ec0e2a45f0f869d46889d02405 # v6.2.0
actions/setup-ruby@e932e7af67fc4a8fc77bd86b744acd4e42fe3543 # v1.1.3
actions/stale@997185467fa4f803885201cee163a9f38240193d # v10.1.1
actions/upload-artifact@b7c566a772e6b6bfb58ed0dc250532a479d7789f # v6.0.0
actions/upload-pages-artifact@7b1f4a764d45c48632c6b24a0339c27f5614fb0b # v4.0.0
actions/upload-release-asset@e8f9f06c4b078e705bd2ea027f0926603fc9b4d5 # v1.0.2
astral-sh/setup-uv@eac588ad8def6316056a12d4907a9d4d84ff7a3b # v7.3.0
dependabot/fetch-metadata@21025c705c08248db411dc16f3619e6b5f9ea21a # v2.5.0
docker/build-push-action@10e90e3645eae34f1e60eeb005ba3a3d33f178e8 # v6.19.2
docker/login-action@c94ce9fb468520275223c153574b00df6fe4bcc9 # v3.7.0
docker/setup-buildx-action@8d2750c68a42422c14e847fe6c8ac0403b4cbd6f # v3.12.0
golangci/golangci-lint-action@1e7e51e771db61008b38414a730f564565cf7c20 # v9.2.0
goreleaser/goreleaser-action@e435ccd777264be153ace6237001ef4d979d3a7a # v6.4.0
ruby/setup-ruby@09a7688d3b55cf0e976497ff046b70949eeaccfd # v1.288.0
taiki-e/install-action@d4422f254e595ee762a758628fe4f16ce050fa2e # v2.67.28
```
<!-- VERSIONS_SHA_END -->
