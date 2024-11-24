# Project Title: PR Refactor Workflow

## Overview
The PR Refactor Workflow automates processes around pull requests in a GitHub repository. Triggered by pull request events or manual initiation, it fetches pull request data and communicates the information to a specified API endpoint. This aids in seamless integration and updates across platforms.

## File Descriptions

### File Name: `pr-refactor.yml`
- **Purpose**: Automates tasks upon pull request actions and manual triggers in a repository.
- **Functions and Features**:
  - **job_for_pull_request**: 
    - Triggers on `pull_request` events like opened or synchronized.
    - **Input**: Accepts GitHub event parameters.
    - **Output**: Sends pull request data to an external API.
  - **job_for_manual_trigger**:
    - Executes on `workflow_dispatch`.
    - **Input**: Manually triggered, fetches open pull request data.
    - **Output**: Similar to the pull request job, sends data to an API.
- **Dependencies**: 
  - Requires `ubuntu-latest` runner.
  - External tools: `curl`, GitHub `actions/checkout`.

## Setup Instructions
1. Ensure you have a GitHub repository set up with the necessary secrets (`TOKEN`) and variables (`URL`).
2. Configure GitHub Actions in your repository and include the `pr-refactor.yml` file.

## Usage Guide
- **Trigger by Pull Request**: Automatically runs when any pull request is opened, reopened, or synchronized on the main branch.
- **Manual Trigger**: Activate through the GitHub Actions interface.

## Examples

### Pull Request Automation
```yaml
on:
  pull_request:
    branches: [main]
```
- **Expected Result**: Fetches pull request data and sends it to the configured API.

### Manual Dispatch
- Run via GitHub Actions > Workflows > `Dispatch Workflow`
- **Command Example**: `curl -H ... -d "$PR_JSON" ${{ vars.URL }}`

## How the Files Relate
All configurations and jobs are contained within `pr-refactor.yml`, interacting with GitHub and external APIs.

## Contributing
Interested contributors can open pull requests with enhancements or additional jobs, ensuring adherence to workflow standards.

## License
This project is distributed under the MIT License.

## Contact
For questions or contributions, reach out to the project maintainers through GitHub Issues in the repository.