# Contributing Guidelines


## 1. Branch Strategy

We use a simplified Feature Branch workflow:

* **`main`**: Always stable and production-ready. Protected from direct pushes.
* **`feature/<short-name>`**: New features (e.g., `feature/user-login`).
* **`fix/<short-name>`**: Bug fixes (e.g., `fix/header-overflow`).
* **`chore/<short-name>`**: Refactoring, dependencies, or maintenance (e.g., `chore/update-deps`).

---

## 2. Local Setup & Development

1. Pull the latest `main` branch before starting work:
 ```bash
 git checkout main
 git pull origin main
```

2. Create your working branch:
```bash
git checkout -b feature/your-feature-name

```


3. Test your changes locally before opening a Pull Request.

---

## 3. Commit Message Format

Write concise, imperative commit messages that explain **what** changed:

```text
<type>: <short summary in present tense>

```

| Type | When to Use | Example |
| --- | --- | --- |
| **`feat`** | Adding new functionality | `feat: add password reset flow` |
| **`fix`** | Resolving a bug or error | `fix: resolve crash on null API response` |
| **`docs`** | Updating documentation or comments | `docs: update setup steps in README` |
| **`style`** | Code formatting, missing semicolons, etc. | `style: run linter on auth module` |
| **`refactor`** | Restructuring code without changing behavior | `refactor: simplify database query helper` |
| **`chore`** | Updating build scripts, dependencies, or tools | `chore: upgrade react to v19` |

---

## 4. Submitting a Pull Request (PR)

1. Open a PR targeting the **`main`** branch.
2. Provide a clear title and brief description covering:
* **What** was changed.
* **Why** it was changed.
* How to test it locally.


3. Keep PRs focused on a single responsibility—smaller PRs are reviewed much faster.
4. Request review from at least **1 team member**.
5. Once approved, use **Squash and Merge** to keep the `main` branch history clean, then delete your feature branch.

---

## 5. Code Quality & Security

* **Never commit secrets**: Check `.env` files, API keys, or access tokens before staging files.
* **Format & Lint**: Run the project's linter/formatter (`npm run lint`, `pytest`, etc.) prior to committing.
* **Keep dependencies clean**: Avoid adding heavy external libraries for trivial utility functions.
* **Responsible for AI-generated code by yourself**: AI codes is accepted but any code committed must have the committer be responsible.
