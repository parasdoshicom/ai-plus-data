# Repo Publish Workflow

This repo is public, so publication safety has to be enforced by default rather than remembered ad hoc.

## Intended Path

1. Make changes on a branch, not directly on `main`.
2. Open a pull request.
3. Let `Repo QA` run the public-safety scan and Markdown QA checks.
4. Review the PR against [`publication-safety-checklist.md`](./publication-safety-checklist.md).
5. Merge only after the checks pass.

## Local Guard On This Machine

This clone also uses a local `pre-push` hook in [`.githooks/pre-push`](../.githooks/pre-push) to make the safe path the default even before GitHub settings catch up.

- every push runs the public-safety scan and Markdown link checks
- any push to `main` creates a local backup branch first
- direct pushes to `main` are blocked unless you explicitly override with `ALLOW_MAIN_PUSH=1`

## What The Automated Gate Catches

- credential patterns and private key material
- Telegram bot tokens and operational IDs
- Slack workspace links and likely private dashboard links
- missing local Markdown targets

## What Still Needs GitHub Settings

The workflow is now in the repo, but GitHub branch protection should require the `Public-Safe QA` check before `main` can move.

That last step lives in GitHub settings, not in this public repository.
