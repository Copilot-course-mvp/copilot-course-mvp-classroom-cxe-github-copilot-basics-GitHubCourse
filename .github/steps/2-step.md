## Step 2: Chat — /explain, /fix, /generate

Great work on Step 1! 🎉 Now let's explore Copilot Chat's three most powerful slash commands.

### 📖 Theory: Copilot Chat Slash Commands

Copilot Chat (opened with `Ctrl+Shift+I` or from the sidebar) understands special slash commands:

| Command | What it does |
|---------|-------------|
| `/explain` | Explains selected code in plain English |
| `/fix` | Suggests a corrected version of buggy code |
| `/generate` | Creates new code from a natural-language description |

### ⌨️ Activity: Fix and Extend the Scoreboard Parser

1. Open `step-02-chat-explain-fix-generate/exercise.py`. It contains two functions with intentional bugs.

2. Select `parse_scoreboard` and run:

   > **Prompt to try:**
   > ```text
   > /explain this function and list all failure cases
   > ```

   Record the explanation in `copilot-evidence.md`.

3. With `parse_scoreboard` still selected, run:

   > **Prompt to try:**
   > ```text
   > /fix this function — handle spaces around separators, ignore malformed segments, and keep the maximum score for repeated players
   > ```

   Apply the suggested fix.

4. Now generate the missing `top_player` helper:

   > **Prompt to try:**
   > ```text
   > /generate a helper function called top_player that accepts a dict of player scores and returns a (name, score) tuple for the highest score, or None if the dict is empty. When scores are tied, return the player that comes first alphabetically.
   > ```

5. Save and validate:

   ```bash
   python3 scripts/evaluate.py --step step-02
   ```

6. Fill in `step-02-chat-explain-fix-generate/copilot-evidence.md` with the prompts and responses for `/explain`, `/fix`, and `/generate`.

7. Open a pull request targeting `main` with your changes to `step-02-chat-explain-fix-generate/`.

<details>
<summary>Having trouble? 🤷</summary>

- Make sure you have selected the function before using `/explain` or `/fix`.
- If `/generate` produces a different signature, edit it to match `top_player(scores: dict) -> tuple | None`.
- Use `python3 scripts/evaluate.py --step step-02` locally to see exactly which assertions are failing.

</details>
