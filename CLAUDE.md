# Literature digest tracking

This repo backs a recurring literature-search task for a PhD project on the bone marrow microenvironment in pediatric AML/MDS, using CODEX imaging (see `literature-digest/sent-papers.json` for full project scope context inferred from past runs: spatial/cellular composition of bone marrow in pediatric AML/MDS patients, correlation with clinical outcome and therapy response, and functional validation in murine AML/MDS models).

`literature-digest/sent-papers.json` is the standing record of every paper already sent to the user across all past digests.

**Before compiling a new digest:** read this file and exclude any paper whose `pmid` or `doi` already appears in it, even if it would otherwise match the search criteria. Do not resend or re-summarize a paper already listed.

**After sending a new digest:** append every paper included in that digest to the `papers` array in `literature-digest/sent-papers.json` (same shape: `pmid`, `doi`, `title`, `sent_date`), and commit/push the update so the next run sees it.

**Digest presentation:** always also produce a nicely designed HTML view of each new digest (`literature-digest/digest-YYYY-MM-DD.html`, same content as the markdown digest, with topic filter, relevance dots, PubMed/DOI links, light/dark themes) and publish it as an Artifact so the user gets a link.
