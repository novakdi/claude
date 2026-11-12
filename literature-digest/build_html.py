#!/usr/bin/env python3
"""Build the designed HTML view of a digest: python3 build_html.py YYYY-MM-DD
Reads digest-data.json (papers by PMID + digests by date), fills template.html, writes digest-YYYY-MM-DD.html."""
import json, sys
date = sys.argv[1]
d = json.load(open("digest-data.json"))
dg = d["digests"][date]
papers = []
for it in dg["items"]:
    p = dict(d["papers"][it["pmid"]]); p["pmid"] = it["pmid"]; p["g"] = it["g"]; papers.append(p)
groups = {k: v for k, v in d["groups"].items() if any(p["g"] == k for p in papers)}
esc = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
import datetime
dt = datetime.date.fromisoformat(date)
nice = f"{dt.day} {dt.strftime('%b %Y')}"
h = open("template.html").read()
for k, v in {"TITLE": f"Marrow Digest {dt.day} {dt.strftime('%b')}", "KICKER": f"Digest · {nice}", "LEDE": dg["lede"],
             "FOOTER": dg["footer"], "G": esc(groups), "P": esc(papers)}.items():
    h = h.replace("{{" + k + "}}", v)
open(f"digest-{date}.html", "w").write(h)
print("wrote", f"digest-{date}.html", len(papers), "papers")
