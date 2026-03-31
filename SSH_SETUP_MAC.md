# GitHub SSH Credentials Setup on macOS

This guide walks you through creating and configuring SSH credentials on macOS so you can clone, pull, push, and create pull requests for this repository using the SSH URL.

---

## Prerequisites

- macOS 10.15 (Catalina) or later
- Terminal app (or iTerm2, Warp, etc.)
- A GitHub account

---

## Step 1 — Check for Existing SSH Keys

Open **Terminal** and run:

```bash
ls -al ~/.ssh
```

Look for files named `id_ed25519` / `id_ed25519.pub` (or `id_rsa` / `id_rsa.pub`).

- **If you see a key pair you want to reuse**, skip to [Step 3](#step-3--add-your-ssh-key-to-the-ssh-agent). In later commands, replace `~/.ssh/id_ed25519` with the path to your existing key file (for example, `~/.ssh/id_rsa`) wherever it appears.
- **If the directory is empty or does not exist**, continue to Step 2.

---

## Step 2 — Generate a New SSH Key

Use the modern Ed25519 algorithm (recommended by GitHub):

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Replace `your_email@example.com` with the email address associated with your GitHub account.

When prompted:

| Prompt | Recommendation |
|---|---|
| `Enter file in which to save the key` | Press **Enter** to accept the default (`~/.ssh/id_ed25519`) |
| `Enter passphrase` | Enter a strong passphrase (optional but recommended) |
| `Enter same passphrase again` | Re-enter the passphrase |

You should see output similar to:

```
Your identification has been saved in /Users/you/.ssh/id_ed25519
Your public key has been saved in /Users/you/.ssh/id_ed25519.pub
```

---

## Step 3 — Add Your SSH Key to the SSH Agent

Start the ssh-agent in the background:

```bash
eval "$(ssh-agent -s)"
```

### Configure `~/.ssh/config` (macOS 10.15 (Catalina) or later)

Check whether the config file exists:

```bash
if [ -f ~/.ssh/config ]; then
  cat ~/.ssh/config
else
  echo "~/.ssh/config does not exist yet; you'll create it in the next step."
fi
```

If the file does not exist or does not contain a `github.com` entry, create/update it:

```bash
if ! grep -q "Host github.com" ~/.ssh/config 2>/dev/null; then
  cat >> ~/.ssh/config << 'EOF'
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
EOF
fi
```

> **Note:** `UseKeychain yes` stores the passphrase in the macOS Keychain so you only need to enter it once per login session.

### Add the key to the agent (and Keychain)

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

> On macOS Monterey 12.0 and earlier, use `-K` instead of `--apple-use-keychain`.

---

## Step 4 — Add the Public Key to Your GitHub Account

1. Copy the public key to your clipboard:

   ```bash
   pbcopy < ~/.ssh/id_ed25519.pub
   ```

2. Open GitHub in your browser and go to **Settings → SSH and GPG keys**:

   ```
   https://github.com/settings/ssh/new
   ```

3. Fill in the form:
   - **Title**: a descriptive name (e.g., `MacBook Pro 2024`)
   - **Key type**: `Authentication Key`
   - **Key**: paste the key you copied with `pbcopy`

4. Click **Add SSH key** and confirm with your GitHub password if prompted.

---

## Step 5 — Test the SSH Connection

```bash
ssh -T git@github.com
```

Expected output (the username will be your own):

```
Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.
```

If you see a warning about an unrecognized host, type `yes` to add GitHub to your known hosts.

---

## Step 6 — Clone This Repository Using SSH

```bash
git clone git@github.com:josevicenteayala/GitHubCourse.git
cd GitHubCourse
```

---

## Step 7 — Configure Your Git Identity (First-Time Setup)

If you have not set your Git name and email globally yet:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Use the same email address as your GitHub account.

---

## Step 8 — Day-to-Day Workflow

### Pull the latest changes

```bash
git pull origin main
```

### Create a feature branch

```bash
git checkout -b feature/my-new-feature
```

### Stage and commit changes

```bash
git add .
git commit -m "feat: describe your change"
```

### Push the branch to GitHub

```bash
git push -u origin feature/my-new-feature
```

### Open a Pull Request

After pushing, GitHub will display a link in the terminal output. Click it, or:

1. Go to the repository on GitHub.
2. Click the **Compare & pull request** button that appears for your branch.
3. Fill in the title and description, then click **Create pull request**.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `Permission denied (publickey)` | Verify the key was added to GitHub and to the agent (`ssh-add -l`) |
| `ssh-add: illegal option -- -apple-use-keychain` | Use `-K` flag (older macOS) |
| Passphrase asked every session | Ensure `UseKeychain yes` is in `~/.ssh/config` |
| Wrong SSH key used | Add `IdentityFile ~/.ssh/id_ed25519` to `~/.ssh/config` for the `github.com` host |
| `Host key verification failed` | Run `ssh-keygen -R github.com` then reconnect |

---

## References

- [GitHub Docs — Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [GitHub Docs — Adding a new SSH key to your account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
- [GitHub Docs — Testing your SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)
