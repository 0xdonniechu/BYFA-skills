#!/usr/bin/env python3
"""Render the winning-product CSV as one clean HTML table.

Usage: python3 render-table.py <input.csv> <output.html> ["Tiêu đề"] ["Dòng mô tả"]
Empty cells stay empty. Columns are the ones listed in SKILL.md (Đầu ra).
"""
import csv
import html
import re
import sys
from urllib.parse import urlparse

TIERS = [
    ("trustmrr.com", "TrustMRR", "verify"),
    ("speedrun.a16z.com", "a16z Speedrun", "fund"),
    ("news.ycombinator.com", "Show HN", "new"),
    ("ycombinator.com", "Y Combinator", "fund"),
    ("producthunt.com", "Product Hunt", "new"),
]
TIER_LABEL = {"verify": "Doanh thu verify", "fund": "Được quỹ đầu tư", "new": "Mới ra mắt, chưa verify"}


def e(v):
    return html.escape(v or "")


def tier(src):
    host = urlparse(src).netloc.lower()
    for dom, name, kind in TIERS:
        if host == dom or host.endswith("." + dom):
            return name, kind
    return (host or ""), "new"


def split_main(v):
    """'$29/tháng (Standard, 5 kênh)' -> ('$29/tháng', 'Standard, 5 kênh')."""
    m = re.match(r"^(.*?)\s*\((.*)\)\s*$", v or "")
    return (m.group(1), m.group(2)) if m else (v or "", "")


def link(url, text):
    if not re.match(r"^https?://", url or ""):
        return e(text)
    return f'<a href="{e(url)}">{e(text)}</a>'


def handle(url):
    m = re.search(r"x\.com/([^/?#]+)", url or "")
    return "@" + m.group(1) if m else ""


def cell_x(v):
    if not v:
        return ""
    m = re.match(r"^X công ty:\s*(\S+)$", v)
    if m:
        return f'<span class="sub">công ty</span> {link(m.group(1), handle(m.group(1)))}'
    return link(v, handle(v)) if v.startswith("http") else e(v)


def wrap(v):
    """Let long tokens like $990/brand/tháng break after a slash, never mid-word."""
    return e(v).replace("/", "/<wbr>")


def row_html(r):
    name, kind = tier(r.get("Nguồn", ""))
    site = r.get("Website", "")
    dom = re.sub(r"^www\.", "", urlparse(site).netloc) if site else ""
    mrr, mrr_sub = split_main(r.get("Doanh thu verify (MRR)", ""))
    price, price_sub = split_main(r.get("Giá thấp nhất", ""))
    fund, fund_sub = split_main(r.get("Vốn", ""))
    traffic = r.get("Traffic", "")
    signal = ""
    if kind == "new" and traffic:
        signal, traffic = traffic, ""
    m = re.match(r"^([\d.,]+)\s+(.*)$", traffic)
    traffic, traffic_sub = (m.group(1), m.group(2)) if m else (traffic, "")
    fit = r.get("Hợp với tôi", "")
    return f"""<tr class="t-{kind}">
<td class="num rank">{e(r.get("Hạng"))}</td>
<td><div class="pname">{link(site, r.get("Sản phẩm")) or e(r.get("Sản phẩm"))}</div><div class="sub">{e(dom)}</div><div class="chip">{e(r.get("Ngách"))}</div></td>
<td class="desc">{e(r.get("Làm gì"))}</td>
<td class="num"><div class="{"sub" if mrr == "chưa verify" else "big"}">{e(mrr)}</div><div class="sub">{e(mrr_sub)}</div></td>
<td><div>{e(fund)}</div><div class="sub">{e(fund_sub)}</div></td>
<td class="num"><div class="big">{e(traffic)}</div><div class="sub">{e(traffic_sub)}</div></td>
<td><div>{wrap(price)}</div><div class="sub">{wrap(price_sub)}</div></td>
<td class="small">{e(r.get("Dùng thử"))}</td>
<td><div>{e(r.get("Founder"))}</div><div class="sub">{cell_x(r.get("X founder", ""))}</div></td>
{f'<td class="small">{e(fit)}<div class="sub">{e(r.get("Vì sao", ""))}</div></td>' if "Hợp với tôi" in r else ""}
<td><span class="badge b-{kind}">{link(r.get("Nguồn"), name)}</span><div class="sub">{e(signal)}</div></td>
</tr>"""


def main():
    if len(sys.argv) < 3:
        sys.exit('Usage: python3 render-table.py <input.csv> <output.html> ["Tiêu đề"] ["Dòng mô tả"]')
    src, out = sys.argv[1], sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else "Winning products"
    lede = sys.argv[4] if len(sys.argv) > 4 else ""
    rows = list(csv.DictReader(open(src, encoding="utf-8"), restval=""))
    counts = {k: sum(1 for r in rows if tier(r.get("Nguồn", ""))[1] == k) for k in TIER_LABEL}
    has_fit = rows and "Hợp với tôi" in rows[0]
    legend = "".join(f'<span class="badge b-{k}">{TIER_LABEL[k]} · {counts[k]}</span>' for k in TIER_LABEL)
    fit_head = "<th>Hợp với tôi</th>" if has_fit else ""
    fit_col = '<col style="width:9%">' if has_fit else ""
    body = "\n".join(row_html(r) for r in rows)
    page = f"""<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--ink:#111827;--muted:#6b7280;--line:#e5e7eb;--bg:#ffffff;--soft:#f9fafb;
--verify:#047857;--verify-bg:#ecfdf5;--fund:#b45309;--fund-bg:#fffbeb;--new:#4b5563;--new-bg:#f3f4f6}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 "Be Vietnam Pro",system-ui,sans-serif}}
.wrap{{max-width:1440px;margin:0 auto;padding:40px 40px 56px}}
h1{{font-size:26px;line-height:1.25;font-weight:700;margin:0 0 6px;letter-spacing:-.01em}}
.lede{{color:var(--muted);margin:0 0 18px}}
.legend{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px}}
table{{width:100%;border-collapse:collapse;table-layout:fixed}}
th{{position:sticky;top:0;background:var(--soft);text-align:left;font-size:12px;font-weight:600;color:var(--muted);
text-transform:uppercase;letter-spacing:.04em;padding:10px 12px;border-bottom:1px solid var(--line)}}
td{{padding:14px 12px;border-bottom:1px solid var(--line);vertical-align:top;overflow-wrap:normal}}
tr td:first-child{{border-left:3px solid transparent}}
tr.t-verify td:first-child{{border-left-color:var(--verify)}}
tr.t-fund td:first-child{{border-left-color:var(--fund)}}
tr.t-new td:first-child{{border-left-color:#d1d5db}}
.num{{text-align:right;font-variant-numeric:tabular-nums}}
th.num{{text-align:right}}
.rank{{color:var(--muted);font-weight:600}}
.pname{{font-weight:600;font-size:15px}}
.big{{font-weight:700;font-size:15px}}
.sub{{color:var(--muted);font-size:12px;line-height:1.45;margin-top:2px}}
.small{{font-size:13px}}
.desc{{font-size:13px;color:#374151}}
.chip{{display:inline-block;margin-top:6px;padding:2px 8px;border-radius:6px;line-height:1.35;background:var(--soft);
border:1px solid var(--line);font-size:11px;color:var(--muted)}}
.badge{{display:inline-block;padding:2px 10px;border-radius:999px;font-size:12px;font-weight:600;white-space:nowrap}}
.b-verify{{color:var(--verify);background:var(--verify-bg)}}
.b-fund{{color:var(--fund);background:var(--fund-bg)}}
.b-new{{color:var(--new);background:var(--new-bg)}}
a{{color:inherit;text-decoration:none;border-bottom:1px solid #d1d5db}}
a:hover{{border-bottom-color:currentColor}}
.badge a{{border:0}}
</style></head><body><div class="wrap">
<h1>{e(title)}</h1><p class="lede">{e(lede)}</p>
<div class="legend">{legend}</div>
<table><colgroup><col style="width:3.5%"><col style="width:13%"><col style="width:18%"><col style="width:10%">
<col style="width:9%"><col style="width:8%"><col style="width:10%"><col style="width:10%"><col style="width:11%">{fit_col}<col style="width:9%"></colgroup>
<thead><tr><th class="num">#</th><th>Sản phẩm</th><th>Làm gì</th><th class="num">MRR verify</th><th>Vốn</th>
<th class="num">Traffic</th><th>Giá thấp nhất</th><th>Dùng thử</th><th>Founder</th>{fit_head}<th>Nguồn</th></tr></thead>
<tbody>
{body}
</tbody></table></div></body></html>
"""
    open(out, "w", encoding="utf-8").write(page)


if __name__ == "__main__":
    main()
