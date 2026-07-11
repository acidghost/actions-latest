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
actions/add-to-project@v2
actions/ai-inference@v2
actions/attest@v4
actions/attest-build-provenance@v4
actions/attest-sbom@v4
actions/cache@v6
actions/checkout@v7
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
actions/upload-code-coverage@v1
actions/upload-pages-artifact@v5
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
ruby/setup-ruby@v1.316.0
taiki-e/install-action@v2
```
<!-- VERSIONS_END -->

<!-- VERSIONS_SHA_START -->
## Latest versions (SHA-pinned)

```
actions/add-to-project@5afcf98fcd03f1c2f92c3c83f58ae24323cc57fd # v2.0.0
actions/ai-inference@a7805884c80886efc241e94a5351df715968a0ad # v2.1.1
actions/attest@a1948c3f048ba23858d222213b7c278aabede763 # v4.1.1
actions/attest-build-provenance@0f67c3f4856b2e3261c31976d6725780e5e4c373 # v4.1.1
actions/attest-sbom@c604332985a26aa8cf1bdc465b92731239ec6b9e # v4.1.0
actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
actions/configure-pages@45bfe0192ca1faeb007ade9deae92b16b8254a0d # v6.0.0
actions/create-github-app-token@bcd2ba49218906704ab6c1aa796996da409d3eb1 # v3.2.0
actions/create-release@0cb9c9b65d5d1901c1f53e5e66eaf4afd303e70e # v1.1.4
actions/delete-package-versions@e5bc658cc4c965c472efe991f8beea3981499c55 # v5.0.0
actions/dependency-review-action@a1d282b36b6f3519aa1f3fc636f609c47dddb294 # v5.0.0
actions/deploy-pages@cd2ce8fcbc39b97be8ca5fce6e763baed58fa128 # v5.0.0
actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
actions/first-interaction@1c4688942c71f71d4f5502a26ea67c331730fa4d # v3.1.0
actions/github-script@3a2844b7e9c422d3c10d287c895573f7108da1b3 # v9.0.0
actions/go-dependency-submission@f35d5c9af13ce9cc32f7930b171e315e878f6921 # v2.0.3
actions/hello-world-docker-action@0b406c0e14ed4b1853113f84b89aa6cdf762e340 # v2
actions/hello-world-javascript-action@ae53f59fd519c0006ceb494ecbfed5f05d4151cf # v1
actions/javascript-action@4be183afbd08ddadedcf09f17e8e112326894107 # v1.0.1
actions/jekyll-build-pages@44a6e6beabd48582f863aeeb6cb2151cc1716697 # v1.0.13
actions/labeler@b8dd2d9be0f68b860e7dae5dae7d772984eacd6d # v6.2.0
actions/setup-dotnet@26b0ec14cb23fa6904739307f278c14f94c95bf1 # v5.4.0
actions/setup-elixir@3c118cec41f6c3bfc2c7f2aef9bec886ab0b2324 # v1.5.0
actions/setup-go@924ae3a1cded613372ab5595356fb5720e22ba16 # v6.5.0
actions/setup-haskell@048c29979717135f04282c42c2186bb5945b2d8f # v1.1.4
actions/setup-java@0f481fcb613427c0f801b606911222b5b6f3083a # v5.5.0
actions/setup-node@48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e # v6.4.0
actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1 # v6.3.0
actions/setup-ruby@e932e7af67fc4a8fc77bd86b744acd4e42fe3543 # v1.1.3
actions/stale@1e223db275d687790206a7acac4d1a11bd6fe629 # v10.4.0
actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
actions/upload-code-coverage@abb5995db9e0199b0e2bb9dbd136fce4cb1ec4d3 # v1.3.0
actions/upload-pages-artifact@fc324d3547104276b827a68afc52ff2a11cc49c9 # v5.0.0
actions/upload-release-asset@e8f9f06c4b078e705bd2ea027f0926603fc9b4d5 # v1.0.2
astral-sh/setup-uv@11f9893b081a58869d3b5fccaea48c9e9e46f990 # v8.3.2
dependabot/fetch-metadata@25dd0e34f4fe68f24cc83900b1fe3fe149efef98 # v3.1.0
docker/build-push-action@53b7df96c91f9c12dcc8a07bcb9ccacbed38856a # v7.3.0
docker/login-action@af1e73f918a031802d376d3c8bbc3fe56130a9b0 # v4.4.0
docker/metadata-action@dc802804100637a589fabce1cb79ff13a1411302 # v6.2.0
docker/setup-buildx-action@bb05f3f5519dd87d3ba754cc423b652a5edd6d2c # v4.2.0
docker/setup-qemu-action@96fe6ef7f33517b61c61be40b68a1882f3264fb8 # v4.2.0
dorny/paths-filter@7b450fff21473bca461d4b92ce414b9d0420d706 # v4.0.2
golangci/golangci-lint-action@ba0d7d2ec06a0ea1cb5fa41b2e4a3ab91d21278a # v9.3.0
goreleaser/goreleaser-action@f06c13b6b1a9625abc9e6e439d9c05a8f2190e94 # v7.2.3
jdx/mise-action@e6a8b3978addb5a52f2b4cd9d91eafa7f0ab959d # v4.2.0
ruby/setup-ruby@d45b1a4e94b71acab930e56e79c6aa188764e7f9 # v1.316.0
taiki-e/install-action@2ca9b94c269419b7b0c711c09d0b21c4e1d51145 # v2.83.1
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
aws-actions/aws-elasticbeanstalk-deploy@v1
aws-actions/aws-lambda-deploy@v1
aws-actions/aws-secretsmanager-get-secrets@v3
aws-actions/closed-issue-message@v2
aws-actions/cloudformation-aws-iam-policy-validator@v1.0.4
aws-actions/codeguru-security@v1
aws-actions/configure-aws-credentials@v6
aws-actions/devops-agent-qa@v1
aws-actions/handle-non-labeled-issues@v1
aws-actions/setup-sam@v3
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
aws-actions/amazon-ecr-login@d539f0932e70871a027e9d5a9d8fc38589180a64 # v2.1.6
aws-actions/amazon-ecs-deploy-express-service@7c48a2de16441d528a3c89829831968dc1455010 # v1.2.2
aws-actions/amazon-ecs-deploy-task-definition@c465972ecbd160473f22e683363b422a5412a3de # v2.6.3
aws-actions/amazon-ecs-render-task-definition@138c24f321fdbdf7edee4a685519d253cae2cdea # v1.9.0
aws-actions/amazon-eks-fargate@fa91b1ce6e342eb17a1d57df976506d02f074640 # v0.1.1
aws-actions/application-observability-for-aws@95bb59e4538ba9ef746805d8a2bbbe531ba2a728 # v1.1.1
aws-actions/aws-cloudformation-github-deploy@81e3b03d2266bcb76c4bcc37a7d71d9cb67838bb # v2.2.0
aws-actions/aws-codebuild-run-build@7e46c3fa1c1f217e26a73712796b1f78938b534b # v1.0.19
aws-actions/aws-devicefarm-browser-testing@08307129ceef7ad2999ce39e54fa9334df61bfb1 # v3
aws-actions/aws-devicefarm-mobile-device-testing@5a6c9fbb66ca99cb92ce07381c8be038f654eff6 # v3
aws-actions/aws-elasticbeanstalk-deploy@cfad3e5e4452cd9c8923cbee2f862e96ba4b52c4 # v1.0.6
aws-actions/aws-lambda-deploy@d496277188b89f0be02d7a2216fc912c0427702a # v1.1.2
aws-actions/aws-secretsmanager-get-secrets@2cb1a461cbd4865ac4299648312e4704c646cd53 # v3.0.1
aws-actions/closed-issue-message@10aaf6366131b673a7c8b7742f8b3849f1d44f18 # v2
aws-actions/cloudformation-aws-iam-policy-validator@aa5ca59693ba89d200db1d2b3af4b60989627bdc # v1.0.4
aws-actions/codeguru-security@44877802cfee29abce47f8ba12b8417d70d01a9b # v1.2.2
aws-actions/configure-aws-credentials@517a711dbcd0e402f90c77e7e2f81e849156e31d # v6.2.2
aws-actions/devops-agent-qa@612e51ffad87aa5c7a6dd62444721882c841957f # v1
aws-actions/handle-non-labeled-issues@d6b11a820a09b58180471df5be076df19f05b9dd # v1.0.1
aws-actions/setup-sam@89ddb14d60e682855e3fea4be85b3c56485de310 # v3
aws-actions/stale-issue-cleanup@0604f2edf84a3a66bc0dfb4a30eb07814cbdf440 # v7.1.1
aws-actions/sustainability-scanner@d6067411fc5290a836e3ebcf388c746d83cf0e9f # v1.3.1
aws-actions/terraform-aws-iam-policy-validator@1cd3c484b95b6c3d9e42ca1797d89ae74eb29ede # v1.0.3
aws-actions/vulnerability-scan-github-action-for-amazon-inspector@f5a63f71de9d790c7c42da74d59efb2c017bdcac # v1.5.0
```

</details>
<!-- AWS-ACTIONS_VERSIONS_SHA_END -->
