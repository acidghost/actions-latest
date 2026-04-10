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

The script generates the following files:

- **`versions.txt`** - Default bundle with actions org + additional repos
- **`versions-sha.txt`** - SHA-pinned format for default bundle
- **`{org}-versions.txt`** - Per-org version files (e.g., `aws-actions-versions.txt`)
- **`{org}-versions-sha.txt`** - Per-org SHA-pinned files
- **`index.json`** - Discovery file listing all available bundles

## API

An `index.json` file is available at:

https://acidghost.github.io/actions-latest/index.json

This file lists all available bundles and their download URLs.

### Example Response

```json
{
  "bundles": {
    "default": {
      "versions_url": "https://acidghost.github.io/actions-latest/versions.txt",
      "versions_sha_url": "https://acidghost.github.io/actions-latest/versions-sha.txt"
    }
  },
  "orgs": {
    "aws-actions": {
      "versions_url": "https://acidghost.github.io/actions-latest/aws-actions-versions.txt",
      "versions_sha_url": "https://acidghost.github.io/actions-latest/aws-actions-versions-sha.txt"
    }
  }
}
```

### Usage Examples

```bash
# Fetch index to discover available bundles
curl -s https://acidghost.github.io/actions-latest/index.json | jq '.'

# Get default bundle versions
curl -s https://acidghost.github.io/actions-latest/versions.txt

# Get AWS-specific versions
curl -s https://acidghost.github.io/actions-latest/aws-actions-versions.txt
```

## Fork Note

This is a personal fork of the [actions-latest](https://github.com/simonw/actions-latest) project by [Simon Willison](https://github.com/simonw). Contributions to this fork may not be considered or merged.

<!-- VERSIONS_START -->
## Latest versions

```
actions/add-to-project@v1.0.2
actions/ai-inference@v2
actions/attest@v4
actions/attest-build-provenance@v4
actions/attest-sbom@v4
actions/cache@v5
actions/checkout@v6
actions/configure-pages@v6
actions/create-github-app-token@v3
actions/create-release@v1
actions/delete-package-versions@v5
actions/dependency-review-action@v3
actions/deploy-pages@v5
actions/download-artifact@v8
actions/first-interaction@v3
actions/github-script@v9
actions/go-dependency-submission@v2
actions/hello-world-docker-action@v2
actions/hello-world-javascript-action@v1
actions/javascript-action@v1
actions/jekyll-build-pages@v1
actions/labeler@v6
actions/setup-copilot@v0
actions/setup-dotnet@v5
actions/setup-elixir@v1
actions/setup-go@v6
actions/setup-haskell@v1
actions/setup-java@v5
actions/setup-node@v6
actions/setup-python@v6
actions/setup-ruby@v1
actions/stale@v10
actions/upload-artifact@v7
actions/upload-pages-artifact@v4
actions/upload-release-asset@v1
astral-sh/setup-uv@v7
dependabot/fetch-metadata@v3
docker/build-push-action@v7
docker/login-action@v4
docker/metadata-action@v6
docker/setup-buildx-action@v4
docker/setup-qemu-action@v4
dorny/paths-filter@v4
golangci/golangci-lint-action@v9
goreleaser/goreleaser-action@v7
jdx/mise-action@v4
ruby/setup-ruby@v1.300.0
taiki-e/install-action@v2
```
<!-- VERSIONS_END -->

<!-- VERSIONS_SHA_START -->
## Latest versions (SHA-pinned)

```
actions/add-to-project@244f685bbc3b7adfa8466e08b698b5577571133e # v1.0.2
actions/ai-inference@af6ad2c4ac4edf01884054fc3a6caa6d2567c13a # v2.0.8
actions/attest@59d89421af93a897026c735860bf21b6eb4f7b26 # v4.1.0
actions/attest-build-provenance@a2bbfa25375fe432b6a289bc6b6cd05ecd0c4c32 # v4.1.0
actions/attest-sbom@c604332985a26aa8cf1bdc465b92731239ec6b9e # v4.1.0
actions/cache@668228422ae6a00e4ad889ee87cd7109ec5666a7 # v5.0.4
actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
actions/configure-pages@45bfe0192ca1faeb007ade9deae92b16b8254a0d # v6.0.0
actions/create-github-app-token@f8d387b68d61c58ab83c6c016672934102569859 # v3.0.0
actions/create-release@0cb9c9b65d5d1901c1f53e5e66eaf4afd303e70e # v1.1.4
actions/delete-package-versions@e5bc658cc4c965c472efe991f8beea3981499c55 # v5.0.0
actions/dependency-review-action@2031cfc080254a8a887f58cffee85186f0e49e48 # v4.9.0
actions/deploy-pages@cd2ce8fcbc39b97be8ca5fce6e763baed58fa128 # v5.0.0
actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
actions/first-interaction@1c4688942c71f71d4f5502a26ea67c331730fa4d # v3.1.0
actions/github-script@3a2844b7e9c422d3c10d287c895573f7108da1b3 # v9.0.0
actions/go-dependency-submission@f35d5c9af13ce9cc32f7930b171e315e878f6921 # v2.0.3
actions/hello-world-docker-action@0b406c0e14ed4b1853113f84b89aa6cdf762e340 # v2
actions/hello-world-javascript-action@ae53f59fd519c0006ceb494ecbfed5f05d4151cf # v1
actions/javascript-action@4be183afbd08ddadedcf09f17e8e112326894107 # v1.0.1
actions/jekyll-build-pages@44a6e6beabd48582f863aeeb6cb2151cc1716697 # v1.0.13
actions/labeler@634933edcd8ababfe52f92936142cc22ac488b1b # v6.0.1
actions/setup-copilot@01f2415f3de9e622b1cc969773f108741021a606 # v0.0.5
actions/setup-dotnet@c2fa09f4bde5ebb9d1777cf28262a3eb3db3ced7 # v5.2.0
actions/setup-elixir@3c118cec41f6c3bfc2c7f2aef9bec886ab0b2324 # v1.5.0
actions/setup-go@4a3601121dd01d1626a1e23e37211e3254c1c06c # v6.4.0
actions/setup-haskell@048c29979717135f04282c42c2186bb5945b2d8f # v1.1.4
actions/setup-java@be666c2fcd27ec809703dec50e508c2fdc7f6654 # v5.2.0
actions/setup-node@53b83947a5a98c8d113130e565377fae1a50d02f # v6.3.0
actions/setup-python@a309ff8b426b58ec0e2a45f0f869d46889d02405 # v6.2.0
actions/setup-ruby@e932e7af67fc4a8fc77bd86b744acd4e42fe3543 # v1.1.3
actions/stale@b5d41d4e1d5dceea10e7104786b73624c18a190f # v10.2.0
actions/upload-artifact@bbbca2ddaa5d8feaa63e36b76fdaad77386f024f # v7.0.0
actions/upload-pages-artifact@7b1f4a764d45c48632c6b24a0339c27f5614fb0b # v4.0.0
actions/upload-release-asset@e8f9f06c4b078e705bd2ea027f0926603fc9b4d5 # v1.0.2
astral-sh/setup-uv@cec208311dfd045dd5311c1add060b2062131d57 # v8.0.0
dependabot/fetch-metadata@ffa630c65fa7e0ecfa0625b5ceda64399aea1b36 # v3.0.0
docker/build-push-action@d08e5c354a6adb9ed34480a06d141179aa583294 # v7.0.0
docker/login-action@4907a6ddec9925e35a0a9e82d7399ccc52663121 # v4.1.0
docker/metadata-action@030e881283bb7a6894de51c315a6bfe6a94e05cf # v6.0.0
docker/setup-buildx-action@4d04d5d9486b7bd6fa91e7baf45bbb4f8b9deedd # v4.0.0
docker/setup-qemu-action@ce360397dd3f832beb865e1373c09c0e9f86d70a # v4.0.0
dorny/paths-filter@fbd0ab8f3e69293af611ebaee6363fc25e6d187d # v4.0.1
golangci/golangci-lint-action@1e7e51e771db61008b38414a730f564565cf7c20 # v9.2.0
goreleaser/goreleaser-action@ec59f474b9834571250b370d4735c50f8e2d1e29 # v7.0.0
jdx/mise-action@1648a7812b9aeae629881980618f079932869151 # v4.0.1
ruby/setup-ruby@e65c17d16e57e481586a6a5a0282698790062f92 # v1.300.0
taiki-e/install-action@b8be7f5e140177087325943c4a8e169d01c59b3d # v2.75.3
```
<!-- VERSIONS_SHA_END -->

## Orgs

<!-- AWS-ACTIONS_VERSIONS_START -->
<details>
<summary><h3><code>aws-actions</code></h3></summary>

```
aws-actions/amazon-ecr-login@v2
aws-actions/amazon-ecs-deploy-express-service@v1
aws-actions/amazon-ecs-deploy-task-definition@v2
aws-actions/amazon-ecs-render-task-definition@v1
aws-actions/amazon-eks-fargate@v0
aws-actions/application-observability-for-aws@v1
aws-actions/aws-cloudformation-github-deploy@v2
aws-actions/aws-codebuild-run-build@v1
aws-actions/aws-devicefarm-browser-testing@v3
aws-actions/aws-devicefarm-mobile-device-testing@v3
aws-actions/aws-elasticbeanstalk-deploy@v1.0.4
aws-actions/aws-lambda-deploy@v1
aws-actions/aws-secretsmanager-get-secrets@v3
aws-actions/closed-issue-message@v2
aws-actions/cloudformation-aws-iam-policy-validator@v1.0.4
aws-actions/codeguru-security@v1
aws-actions/configure-aws-credentials@v6
aws-actions/setup-sam@v2
aws-actions/stale-issue-cleanup@v6
aws-actions/sustainability-scanner@v1
aws-actions/terraform-aws-iam-policy-validator@v1.0.3
aws-actions/vulnerability-scan-github-action-for-amazon-inspector@v1
```

</details>
<!-- AWS-ACTIONS_VERSIONS_END -->

<!-- AWS-ACTIONS_VERSIONS_SHA_START -->
<details>
<summary><h3><code>aws-actions</code> (SHA-pinned)</h3></summary>

```
aws-actions/amazon-ecr-login@f2e9fc6c2b355c1890b65e6f6f0e2ac3e6e22f78 # v2.1.2
aws-actions/amazon-ecs-deploy-express-service@1cd950681bc125e2c0d50696c5d53fc2c0bacfd4 # v1.2.0
aws-actions/amazon-ecs-deploy-task-definition@fc8fc60f3a60ffd500fcb13b209c59d221ac8c8c # v2.6.1
aws-actions/amazon-ecs-render-task-definition@77954e213ba1f9f9cb016b86a1d4f6fcdea0d57e # v1.8.4
aws-actions/amazon-eks-fargate@fa91b1ce6e342eb17a1d57df976506d02f074640 # v0.1.1
aws-actions/application-observability-for-aws@95bb59e4538ba9ef746805d8a2bbbe531ba2a728 # v1.1.1
aws-actions/aws-cloudformation-github-deploy@64bde66a4001208fc0917038be8846d99c9d0585 # v2.1.0
aws-actions/aws-codebuild-run-build@7e46c3fa1c1f217e26a73712796b1f78938b534b # v1.0.19
aws-actions/aws-devicefarm-browser-testing@08307129ceef7ad2999ce39e54fa9334df61bfb1 # v3
aws-actions/aws-devicefarm-mobile-device-testing@5a6c9fbb66ca99cb92ce07381c8be038f654eff6 # v3
aws-actions/aws-elasticbeanstalk-deploy@1f56e4e813ae4eb167e69ca324234c336c1df573 # v1.0.4
aws-actions/aws-lambda-deploy@29ea35c124579506cf0475e20df36198eb670d89 # v1.1.0
aws-actions/aws-secretsmanager-get-secrets@2cb1a461cbd4865ac4299648312e4704c646cd53 # v3.0.1
aws-actions/closed-issue-message@10aaf6366131b673a7c8b7742f8b3849f1d44f18 # v2
aws-actions/cloudformation-aws-iam-policy-validator@aa5ca59693ba89d200db1d2b3af4b60989627bdc # v1.0.4
aws-actions/codeguru-security@44877802cfee29abce47f8ba12b8417d70d01a9b # v1.2.2
aws-actions/configure-aws-credentials@ec61189d14ec14c8efccab744f656cffd0e33f37 # v6.1.0
aws-actions/setup-sam@d78e1a4a9656d3b223e59b80676a797f20093133 # v2
aws-actions/stale-issue-cleanup@0604f2edf84a3a66bc0dfb4a30eb07814cbdf440 # v7.1.1
aws-actions/sustainability-scanner@d6067411fc5290a836e3ebcf388c746d83cf0e9f # v1.3.1
aws-actions/terraform-aws-iam-policy-validator@1cd3c484b95b6c3d9e42ca1797d89ae74eb29ede # v1.0.3
aws-actions/vulnerability-scan-github-action-for-amazon-inspector@47e8686a3b2158018648eab3851ac6d06894db7c # v1.4.1
```

</details>
<!-- AWS-ACTIONS_VERSIONS_SHA_END -->
