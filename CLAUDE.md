# Literature digest tracking

This repo backs a recurring literature-search task for a PhD project on the bone marrow microenvironment in pediatric AML/MDS, using CODEX imaging (see `literature-digest/sent-papers.json` for full project scope context inferred from past runs: spatial/cellular composition of bone marrow in pediatric AML/MDS patients, correlation with clinical outcome and therapy response, and functional validation in murine AML/MDS models).

`literature-digest/sent-papers.json` is the standing record of every paper already sent to the user across all past digests.

**Before compiling a new digest:** read this file and exclude any paper whose `pmid` or `doi` already appears in it, even if it would otherwise match the search criteria. Do not resend or re-summarize a paper already listed.

**After sending a new digest:** append every paper included in that digest to the `papers` array in `literature-digest/sent-papers.json` (same shape: `pmid`, `doi`, `title`, `sent_date`), and commit/push the update so the next run sees it.

**Digest presentation (mandatory, every run):** after compiling a digest, ALWAYS create its designed HTML view and publish it as an Artifact so the user gets a link. Do this before finishing the run, never skip it.
1. Add each paper to `literature-digest/digest-data.json` under `papers` (keyed by PMID: journal, title, relevance 1-5, tag, summary, findings, why, doi) and add the digest under `digests` (date, lede, footer, items with group keys s/p/n/o).
2. Run `cd literature-digest && python3 build_html.py YYYY-MM-DD` to write `digest-YYYY-MM-DD.html` (uses `template.html`; do not hand-write the HTML).
3. Publish that HTML with the Artifact tool and include the link in the notification.
4. Commit the md/json/html files and the updated `sent-papers.json` on the session branch and push. Earlier runs each used their own branch, so check that `sent-papers.json` and digest files on the branch contain everything already sent before relying on them.

**Persistent state branch (mandatory, fixes repeated papers):** each scheduled run starts on its own fresh `claude/*` branch that is never merged, so the log on that branch is stale. The single source of truth is the branch `digest-state` (the user explicitly authorized runs to push to it).
- At the START of every run, before searching: `git fetch origin digest-state` and `git checkout origin/digest-state -- literature-digest/` so you have the full `sent-papers.json` and `digest-data.json`. Exclude every PMID/DOI listed there.
- At the END of every run, after committing on the session branch, also publish the updated `literature-digest/` files to `digest-state`: `git push origin HEAD:digest-state` (fast-forward only; if rejected, fetch, re-apply your additions on top of `origin/digest-state`, and push again; never force-push).
- If `digest-state` does not exist, fall back to the union of `sent-papers.json` across all `origin/claude/bold-mccarthy-*` branches and create `digest-state` from it.
