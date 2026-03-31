# How to Create a GitHub Classroom for This Template

This guide walks instructors through creating a GitHub Classroom assignment that uses this repository as a template so that every student gets their own copy of the GitHub Copilot Hands-On Course.

---

## Prerequisites

- A GitHub account with the **Owner** or **Admin** role in a GitHub organization
- A GitHub organization to use for your classroom (or permission to create one)
- This repository configured as a **template repository** (see [Step 1](#step-1--make-this-repository-a-template))

---

## Step 1 — Make This Repository a Template

If the repository is not already marked as a template:

1. Go to the repository on GitHub.
2. Click **Settings** (top navigation bar).
3. In the **General** section, check the box **Template repository**.
4. Click **Save** (the page saves automatically).

> **Why?** GitHub Classroom creates a copy of the template repository for each student. The repository must be flagged as a template for this to work.

---

## Step 2 — Create a GitHub Organization (If Needed)

GitHub Classroom requires an organization. If you do not already have one:

1. Go to [https://github.com/organizations/plan](https://github.com/organizations/plan).
2. Choose the **Free** plan (sufficient for Classroom).
3. Fill in the organization name and contact email.
4. Click **Create organization**.

> **Tip:** Use a name that reflects your course, for example `copilot-workshop-2025`.

---

## Step 3 — Create a New Classroom

1. Go to [https://classroom.github.com](https://classroom.github.com) and sign in with your GitHub account.
2. Click **New classroom**.
3. Select the organization you created (or an existing one).
4. Enter a classroom name (e.g., `GitHub Copilot Hands-On`).
5. Optionally invite TAs or co-instructors by entering their GitHub usernames.
6. Click **Create classroom**.

---

## Step 4 — Create an Assignment

1. Inside your classroom, click **New assignment**.
2. Configure the assignment basics:

   | Setting | Recommended Value |
   |---|---|
   | **Assignment title** | `GitHub Copilot Hands-On Course` |
   | **Deadline** | Set according to your schedule (optional) |
   | **Individual or group** | **Individual assignment** |
   | **Repository visibility** | **Private** (recommended) or **Public** |

3. Click **Continue**.

### Select the Template Repository

4. In the **Add a template repository** search box, search for your fork or copy of this repository (e.g., `your-org/GitHubCourse`).
5. Select it from the results.
6. Click **Continue**.

### Configure Feedback (Optional)

7. Enable **Autograding** if you want automated feedback:
   - Click **Add test** → **Run Command**.
   - Set the test name to `Evaluate exercises`.
   - Set the run command to:

     ```bash
     python3 scripts/evaluate.py --auto
     ```

   - Set points as desired (e.g., `100`).
   - Click **Save test**.

8. Click **Create assignment**.

---

## Step 5 — Share the Assignment Link with Students

After creating the assignment, GitHub Classroom generates a unique **invitation link**.

1. Copy the invitation link from the assignment page.
2. Share it with your students via your LMS, email, or course website.

When a student clicks the link:

1. They are prompted to sign in to GitHub (if not already signed in).
2. They accept the assignment.
3. GitHub Classroom automatically creates a **private copy** of this template repository in the organization, named `<assignment-name>-<github-username>`.
4. The `0-start-exercise.yml` workflow triggers automatically and sets up the interactive exercise issue for the student.

---

## Step 6 — Monitor Student Progress

GitHub Classroom provides several ways to track progress:

- **Assignment dashboard** — shows each student's repository, last commit time, and autograding results.
- **Autograding results** — if configured, you can see pass/fail status per student.
- **Student repositories** — visit individual repositories to review pull requests, issues, and workflow runs.

### Reviewing Submissions

Each student's copy will contain:

| Artifact | Location |
|---|---|
| Exercise solutions | `step-01-code-completion/exercise.py` through `step-07-debugging-assistance/exercise.py` |
| Evidence of Copilot usage | `step-*/copilot-evidence.md` files |
| Automated evaluation logs | **Actions** tab → step workflow runs |
| Interactive progress | **Issues** tab → exercise issue with step-by-step comments |

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Template repository not found in search | Ensure the repository is marked as a **Template repository** in Settings → General |
| Workflows do not trigger for students | Check that GitHub Actions is enabled for the organization: Settings → Actions → General → Allow all actions |
| Students see permission errors | Verify repository visibility and that students accepted the assignment invitation |
| Autograding fails with `ModuleNotFoundError` | The `evaluate.py` script uses only the Python standard library — ensure the runner has Python 3.8+ |
| Exercise issue is not created | The `0-start-exercise.yml` workflow must run successfully — check the Actions tab for errors |

---

## Tips for Instructors

- **Set a deadline** in the assignment to encourage timely completion.
- **Use private repositories** so students cannot copy each other's work.
- **Pin the exercise issue** in each student's repository so it is easy to find.
- **Review `copilot-evidence.md`** files to verify students are genuinely using Copilot rather than writing code manually.
- **Run the evaluator locally** against a student's submission to see detailed results:

  ```bash
  git clone <student-repo-url>
  cd <student-repo>
  python3 scripts/evaluate.py --auto
  ```

---

## References

- [GitHub Classroom Documentation](https://docs.github.com/en/education/manage-coursework-with-github-classroom)
- [Creating an Assignment](https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/create-an-individual-assignment)
- [Setting Up Autograding](https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/create-an-individual-assignment#testing-assignments-with-autograding)
- [GitHub Classroom — Getting Started](https://classroom.github.com)
- [Template Repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)
