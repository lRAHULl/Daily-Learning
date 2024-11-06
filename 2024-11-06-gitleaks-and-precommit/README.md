# GitLeaks and Pre-commit

[GitLeaks](https://github.com/gitleaks/gitleaks?tab=readme-ov-file#gitleaks)

[Pre-Commit](https://pre-commit.com/)

GitLeaks is an open-source secret scanner which can be used to proactively scan for secrets in code repositories and prevent any secret leaks from happening.

Pre-commit is a hook manager (specifically pre-commit hooks) in git repository. It can be used to check and apply rules to code before the code gets commited.

GitLeaks can be paired with pre-commit to enforce our developement environment to reject the commits which have Secrets in them!

GitLeaks scans for a defined set of commonly known secret patterns. Furthermore, GitLeaks can be customised to apply our own rules for secrets scanning -- this gives us a lot of control on what we define as a secret.

Pre-commit can be used to manage packages for helping with our pre-commit hooks. Common use-cases of such pre-commit hooks include linters, code-formatters, static-scanners and secret-scanners. Pre-commit is a powerful tool -- it can increase your code quality, code security and productivity.

## *Learn Something new Everyday* - Rahul
