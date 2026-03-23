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
actions/configure-pages@v5
actions/create-github-app-token@v3
actions/create-release@v1
actions/delete-package-versions@v5
actions/dependency-review-action@v3
actions/deploy-pages@v4
actions/download-artifact@v8
actions/first-interaction@v3
actions/github-script@v8
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
dependabot/fetch-metadata@v2
docker/build-push-action@v7
docker/login-action@v4
docker/metadata-action@v6
docker/setup-buildx-action@v4
docker/setup-qemu-action@v4
golangci/golangci-lint-action@v9
goreleaser/goreleaser-action@v7
jdx/mise-action@v4
ruby/setup-ruby@v1.295.0
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
actions/configure-pages@983d7736d9b0ae728b81ab479565c72886d7745b # v5.0.0
actions/create-github-app-token@f8d387b68d61c58ab83c6c016672934102569859 # v3.0.0
actions/create-release@0cb9c9b65d5d1901c1f53e5e66eaf4afd303e70e # v1.1.4
actions/delete-package-versions@e5bc658cc4c965c472efe991f8beea3981499c55 # v5.0.0
actions/dependency-review-action@2031cfc080254a8a887f58cffee85186f0e49e48 # v4.9.0
actions/deploy-pages@d6db90164ac5ed86f2b6aed7e0febac5b3c0c03e # v4.0.5
actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
actions/first-interaction@1c4688942c71f71d4f5502a26ea67c331730fa4d # v3.1.0
actions/github-script@ed597411d8f924073f98dfc5c65a23a2325f34cd # v8.0.0
actions/go-dependency-submission@f35d5c9af13ce9cc32f7930b171e315e878f6921 # v2.0.3
actions/hello-world-docker-action@0b406c0e14ed4b1853113f84b89aa6cdf762e340 # v2
actions/hello-world-javascript-action@ae53f59fd519c0006ceb494ecbfed5f05d4151cf # v1
actions/javascript-action@4be183afbd08ddadedcf09f17e8e112326894107 # v1.0.1
actions/jekyll-build-pages@44a6e6beabd48582f863aeeb6cb2151cc1716697 # v1.0.13
actions/labeler@634933edcd8ababfe52f92936142cc22ac488b1b # v6.0.1
actions/setup-copilot@01f2415f3de9e622b1cc969773f108741021a606 # v0.0.5
actions/setup-dotnet@c2fa09f4bde5ebb9d1777cf28262a3eb3db3ced7 # v5.2.0
actions/setup-elixir@3c118cec41f6c3bfc2c7f2aef9bec886ab0b2324 # v1.5.0
actions/setup-go@4b73464bb391d4059bd26b0524d20df3927bd417 # v6.3.0
actions/setup-haskell@048c29979717135f04282c42c2186bb5945b2d8f # v1.1.4
actions/setup-java@be666c2fcd27ec809703dec50e508c2fdc7f6654 # v5.2.0
actions/setup-node@53b83947a5a98c8d113130e565377fae1a50d02f # v6.3.0
actions/setup-python@a309ff8b426b58ec0e2a45f0f869d46889d02405 # v6.2.0
actions/setup-ruby@e932e7af67fc4a8fc77bd86b744acd4e42fe3543 # v1.1.3
actions/stale@b5d41d4e1d5dceea10e7104786b73624c18a190f # v10.2.0
actions/upload-artifact@bbbca2ddaa5d8feaa63e36b76fdaad77386f024f # v7.0.0
actions/upload-pages-artifact@7b1f4a764d45c48632c6b24a0339c27f5614fb0b # v4.0.0
actions/upload-release-asset@e8f9f06c4b078e705bd2ea027f0926603fc9b4d5 # v1.0.2
astral-sh/setup-uv@37802adc94f370d6bfd71619e3f0bf239e1f3b78 # v7.6.0
dependabot/fetch-metadata@21025c705c08248db411dc16f3619e6b5f9ea21a # v2.5.0
docker/build-push-action@d08e5c354a6adb9ed34480a06d141179aa583294 # v7.0.0
docker/login-action@b45d80f862d83dbcd57f89517bcf500b2ab88fb2 # v4.0.0
docker/metadata-action@030e881283bb7a6894de51c315a6bfe6a94e05cf # v6.0.0
docker/setup-buildx-action@4d04d5d9486b7bd6fa91e7baf45bbb4f8b9deedd # v4.0.0
docker/setup-qemu-action@ce360397dd3f832beb865e1373c09c0e9f86d70a # v4.0.0
golangci/golangci-lint-action@1e7e51e771db61008b38414a730f564565cf7c20 # v9.2.0
goreleaser/goreleaser-action@ec59f474b9834571250b370d4735c50f8e2d1e29 # v7.0.0
jdx/mise-action@1648a7812b9aeae629881980618f079932869151 # v4.0.1
ruby/setup-ruby@319994f95fa847cf3fb3cd3dbe89f6dcde9f178f # v1.295.0
taiki-e/install-action@06203676c62f0d3c765be3f2fcfbebbcb02d09f5 # v2.69.6
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
aws-actions/aws-elasticbeanstalk-deploy@v1.0.2
aws-actions/aws-lambda-deploy@v1
aws-actions/aws-secretsmanager-get-secrets@v2
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
aws-actions/amazon-ecr-login@261fc3d4806db1fa66a15cc11113c456db8870a7 # v2.1.0
aws-actions/amazon-ecs-deploy-express-service@1cd950681bc125e2c0d50696c5d53fc2c0bacfd4 # v1.2.0
aws-actions/amazon-ecs-deploy-task-definition@cbf54ec46642b86ff78c2f5793da6746954cf8ff # v2.6.0
aws-actions/amazon-ecs-render-task-definition@77954e213ba1f9f9cb016b86a1d4f6fcdea0d57e # v1.8.4
aws-actions/amazon-eks-fargate@fa91b1ce6e342eb17a1d57df976506d02f074640 # v0.1.1
aws-actions/application-observability-for-aws@95bb59e4538ba9ef746805d8a2bbbe531ba2a728 # v1.1.1
aws-actions/aws-cloudformation-github-deploy@c6cd26bb03f19ebe84c84e9cdbedfb307bf44fb4 # v2.0.0
aws-actions/aws-codebuild-run-build@4d15a47425739ac2296ba5e7eee3bdd4bfbdd767 # v1.0.18
aws-actions/aws-elasticbeanstalk-deploy@c4fb70705562024f8cdc83f001e9b08695ac4164 # v1.0.2
aws-actions/aws-lambda-deploy@29ea35c124579506cf0475e20df36198eb670d89 # v1.1.0
aws-actions/aws-secretsmanager-get-secrets@a9a7eb4e2f2871d30dc5b892576fde60a2ecc802 # v2.0.10
aws-actions/closed-issue-message@10aaf6366131b673a7c8b7742f8b3849f1d44f18 # v2
aws-actions/cloudformation-aws-iam-policy-validator@aa5ca59693ba89d200db1d2b3af4b60989627bdc # v1.0.4
aws-actions/codeguru-security@44877802cfee29abce47f8ba12b8417d70d01a9b # v1.2.2
aws-actions/configure-aws-credentials@8df5847569e6427dd6c4fb1cf565c83acfa8afa7 # v6.0.0
aws-actions/setup-sam@d78e1a4a9656d3b223e59b80676a797f20093133 # v2
aws-actions/stale-issue-cleanup@0604f2edf84a3a66bc0dfb4a30eb07814cbdf440 # v7.1.1
aws-actions/sustainability-scanner@d6067411fc5290a836e3ebcf388c746d83cf0e9f # v1.3.1
aws-actions/terraform-aws-iam-policy-validator@1cd3c484b95b6c3d9e42ca1797d89ae74eb29ede # v1.0.3
aws-actions/vulnerability-scan-github-action-for-amazon-inspector@47e8686a3b2158018648eab3851ac6d06894db7c # v1.4.1
```

</details>
<!-- AWS-ACTIONS_VERSIONS_SHA_END -->
