"""Rebuild the research tables and exportable figures from explicit evidence coding.
Run: /tmp/native-research-venv/bin/python research/native-competitive-2026-10-26/build.py
Dependencies: matplotlib. No network calls; no inferred missing financial values.
"""
from pathlib import Path
import csv, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

ROOT = Path(__file__).resolve().parent
# C = capability explicitly described by vendor; P = partial/approval/external-agent
# dependency; ? = insufficient evidence. These are evidence categories, not scores.
COLS = ['Brand from URL','Generate visuals','Recurring planning','Publish socials','Launch paid ads','Optimize paid ads']
ROWS = [
 ('Native','Full workflow',['C','C','C','C','C','C'],'https://native.no/; https://native.no/ads-on-autopilot'),
 ('Blaze','Full workflow',['C','C','C','C','C','P'],'https://www.blaze.ai/faq; https://www.blaze.ai/pricing; https://www.blaze.ai/'),
 ('Holo','Full workflow',['C','C','C','C','C','P'],'https://tryholo.ai/; https://tech.eu/2026/10/15/vilnius-based-holo-raises-eur5m-to-bring-ai-powered-marketing-to-small-businesses/'),
 ('Plai','Full workflow / ads-led',['C','C','?','C','C','C'],'https://www.plai.io/; https://www.plai.io/pricing'),
 ('Marky','Social-led',['C','C','P','C','?','?'],'https://www.mymarky.ai/; https://www.mymarky.ai/pricing'),
 ('Mizo','Social-led',['C','C','C','C','?','?'],'https://mizo-ai.com/en'),
 ('Predis','Social / creative',['P','C','C','C','?','?'],'https://help.predis.ai/knowledgebase/en/article/get-started-with-auto-posting-using-predis; https://predis.ai/pricing/'),
 ('Marblism / Sonny','AI employee suite',['C','C','C','C','?','?'],'https://www.marblism.com/ai-employees/sonny'),
 ('Sintra / Soshie','AI employee suite',['C','C','C','C','?','?'],'https://www.sintra.com/; https://help.sintra.ai/en/articles/9612920-soshie'),
 ('Zeely','Ads-led',['P','C','?','?','C','P'],'https://zeely.ai/; https://zeely.ai/price/'),
 ('Ocoya','Social workflow',['P','C','P','C','?','?'],'https://www.ocoya.com/'),
 ('SocialBee','Social workflow',['P','C','P','C','?','?'],'https://socialbee.com/pricing/'),
 ('Nuelink','Publishing infrastructure',['P','P','P','C','?','?'],'https://nuelink.com/; https://help.nuelink.com/article/48-whats-an-automation-and-how-does-it-work'),
 ('Postiz','Publishing infrastructure',['P','C','P','C','?','?'],'https://postiz.com/; https://postiz.com/pricing'),
 ('Followr','Watchlist',['?','P','P','P','?','?'],'https://trustmrr.com/startup/followr'),
 ('Sentrive','Watchlist',['?','?','P','P','?','?'],'https://trustmrr.com/startup/sentrive'),
]
MRR = [
 {'company':'Postiz','mrr_usd':314913,'subscriptions':9237,'data_date':'2026-10-25','status':'payment-connected snapshot','source':'https://trustmrr.com/startup/postiz'},
 {'company':'Post Bridge','mrr_usd':49687,'subscriptions':1663,'data_date':'2026-10-25','status':'payment-connected snapshot','source':'https://trustmrr.com/startup/post-bridge'},
 {'company':'Marky','mrr_usd':22032,'subscriptions':480,'data_date':'2026-10-25','status':'payment-connected snapshot','source':'https://trustmrr.com/startup/marky'},
 {'company':'Followr','mrr_usd':5119,'subscriptions':290,'data_date':'2026-10-25','status':'payment-connected snapshot','source':'https://trustmrr.com/startup/followr'},
 {'company':'Sentrive','mrr_usd':147,'subscriptions':3,'data_date':'2026-10-25','status':'payment-connected snapshot','source':'https://trustmrr.com/startup/sentrive'},
 {'company':'Supergrow','mrr_usd':79479,'subscriptions':2315,'data_date':'2026-02-28','status':'STALE: Stripe API key expired; excluded from current chart','source':'https://trustmrr.com/startup/supergrow'},
]
FINANCE = [
 ('Native','Undisclosed; YC F26 confirmed','35000000','NOK','Founder quote reported before launch; no transaction/pre/post-money details','2000000','USD ARR','Founder/vendor claim on YC; not payment-verified','2026 launch post; NOK 35M report 2026-01-28','https://www.ycombinator.com/companies/native; https://www.finansavisen.no/medier/2026/01/28/8323464/oskar-westerlin-med-milliarddrom'),
 ('Blaze','Seed investor confirmed; amount undisclosed','','','No confirmed valuation','','','Do not attribute Almanac legacy funding to standalone Blaze','2025 seed investor record','https://www.array.vc/portfolio/blazeai'),
 ('Holo','EUR 5000000 seed announced 2026-10-15','','','No confirmed valuation','5000000','USD ARR','Reported milestone, not payment-verified','2026-10-15','https://www.cobalt.legal/news-cases/market-one-capital-leads-eur-5-million-seed-round-for-lithuanian-startup-holo/; https://tech.eu/2026/10/15/vilnius-based-holo-raises-eur5m-to-bring-ai-powered-marketing-to-small-businesses/'),
 ('Sintra','USD 17000000 seed announced 2025-06-10','','','No confirmed valuation','12000000','USD ARR','Historical reported milestone; not current ARR','2025-06-10','https://www.cobalt.legal/news-cases/practica-capital-backs-lithuanian-ai-startup-in-record-usd-17-million-seed-round/; https://tech.eu/2025/06/10/lithuanian-ai-startup-sintra-secures-17m-seed-empowering-smbs-with-ai-helpers/'),
 ('Zeely','SEC sold USD 8838942 (2026-09-14), USD 2091993 (2026-10-16)','','','No confirmed valuation','','','Separate offerings; do not add historic announcements without reconciliation','2026-10-16','https://www.sec.gov/Archives/edgar/data/2155182/000215518226000001/xslFormDX01/primary_doc.xml; https://www.sec.gov/Archives/edgar/data/2155182/000215518226000002/xslFormDX01/primary_doc.xml'),
 ('Marblism','USD 500000 total recorded by CB Insights; secondary evidence','','','No confirmed valuation','','','YC profile confirms company; database funding not independently reconciled','Database checked 2026-10-26','https://www.cbinsights.com/company/marblism/financials; https://www.ycombinator.com/companies/marblism'),
 ('Predis','USD 155000 seed in Dealroom; secondary evidence','','','No confirmed valuation','','','Do not use Dealroom modelled enterprise value as transaction valuation','2022-05 round; checked 2026-10-26','https://app.dealroom.co/companies/predis_ai'),
 ('Ocoya','USD 30000 seed in CB Insights; secondary evidence','','','No confirmed valuation','','','Conflicting aggregator claim of USD 67M excluded','2020-11-17 round; checked 2026-10-26','https://www.cbinsights.com/company/ocoya/financials'),
 ('Marky','AppSumo describes bootstrapped','','','No confirmed valuation','22032','USD MRR','TrustMRR connected snapshot; not audited company revenue','2026-10-25','https://appsumo.com/products/marky-v4-0/; https://trustmrr.com/startup/marky'),
 ('Mizo','Not established','','','No confirmed valuation','','','mizo-ai.com is not mizo.tech','Checked 2026-10-26','https://mizo-ai.com/en'),
 ('Plai','Not established','','','No confirmed valuation','','','No public amount verified in this research','Checked 2026-10-26','https://www.plai.io/'),
 ('Nuelink','Founder describes self-funded in interview','','','No confirmed valuation','','','Not independently audited','2026-10 interview','https://assiyaq.com/nuelink-from-moroccan-startup-to-global-social-media-leader/'),
 ('SocialBee','Not established','','','No confirmed valuation','','','No public amount verified in this research','Checked 2026-10-26','https://socialbee.com/'),
 ('Postiz','Not established','','','No confirmed valuation','314913','USD MRR','TrustMRR connected snapshot','2026-10-25','https://trustmrr.com/startup/postiz'),
 ('Followr','Not established','','','No confirmed valuation','5119','USD MRR','TrustMRR connected snapshot','2026-10-25','https://trustmrr.com/startup/followr'),
 ('Sentrive','Founder listing: bootstrapped','','','No confirmed valuation','147','USD MRR','TrustMRR snapshot; founder narrative has different older MRR','2026-10-25','https://trustmrr.com/startup/sentrive'),
]

def write_csv(name, headers, rows):
 with (ROOT/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.writer(f);w.writerow(headers);w.writerows(rows)

write_csv('capability-matrix.csv',['company','category',*COLS,'sources'],[(a,b,*c,d) for a,b,c,d in ROWS])
write_csv('trustmrr-snapshot.csv',list(MRR[0]),[[r[k] for k in MRR[0]] for r in MRR])
write_csv('funding-valuation.csv',['company','funding_evidence','valuation','valuation_currency','valuation_basis','revenue_metric','revenue_unit','caveat','evidence_date','sources'],FINANCE)
(ROOT/'data.json').write_text(json.dumps({'as_of':'2026-10-26','matrix_columns':COLS,'matrix':ROWS,'trustmrr':MRR,'finance':FINANCE},ensure_ascii=False,indent=2))

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
def save(fig,name):
 for ext in ['png','svg','pdf']:fig.savefig(ROOT/f'{name}.{ext}',bbox_inches='tight',dpi=180)
 plt.close(fig)

fig,ax=plt.subplots(figsize=(12,10))
codes={'?':0,'P':1,'C':2}
ax.imshow([[codes[v] for v in r[2]] for r in ROWS],cmap=ListedColormap(['#eceff3','#ffdf9e','#237c77']),vmin=0,vmax=2,aspect='auto')
ax.set_xticks(range(len(COLS)),COLS,rotation=25,ha='right');ax.set_yticks(range(len(ROWS)),[r[0] for r in ROWS])
for i,r in enumerate(ROWS):
 for j,v in enumerate(r[2]):ax.text(j,i,v,ha='center',va='center',color='white' if v=='C' else '#253245',fontweight='bold')
ax.set_title('NATIVE & ALTERNATIVES — CAPABILITY EVIDENCE\nVendor documentation coding, not hands-on quality scores',loc='left',pad=20,fontweight='bold')
fig.text(.1,-.035,'C: explicitly described by vendor   P: partial / conditional / external dependency   ?: insufficient evidence\nUnknown is not absent. Plans and approval requirements differ. Sources and caveats: README.md + capability-matrix.csv.',fontsize=10)
save(fig,'01-capability-matrix')

fig,ax=plt.subplots(figsize=(11,6))
current=MRR[:5][::-1];ys=range(len(current));vals=[r['mrr_usd'] for r in current]
ax.barh(list(ys),vals,color='#237c77',height=.58)
ax.set_yticks(list(ys),[r['company'] for r in current]);ax.set_xscale('log');ax.set_xlim(80,1500000)
for i,v in enumerate(vals):ax.text(v*1.15,i,f'${v:,.0f}',va='center',fontweight='bold')
ax.set_xlabel('USD MRR — logarithmic axis (not revenue in the last 30 days)')
ax.set_title('TRUSTMRR — CONNECTED MRR SNAPSHOTS\nSource data updated 25 Oct 2026; accessed 26 Oct 2026',loc='left',pad=20,fontweight='bold')
fig.text(.04,-.045,'Selection is not a market census. Connected payment accounts are not an audit of total company revenue.\nSupergrow ($79,479; 28 Feb 2026; expired Stripe key) excluded. Sources: trustmrr-snapshot.csv.',fontsize=10)
save(fig,'02-trustmrr-mrr')

# Categorical map: positions within each box are layout only, never numeric scores.
fig,ax=plt.subplots(figsize=(13,7.5));ax.set_xlim(0,3);ax.set_ylim(0,2)
cells={
 (0,1):('SOCIAL-FIRST AUTOPILOT','Marky · Mizo · Predis\nMarblism / Sonny · Sintra / Soshie'),
 (1,1):('SOCIAL + PAID ADS','Native · Blaze · Holo'),
 (2,1):('PAID-ADS-LED','Plai · Zeely'),
 (0,0):('SOCIAL WORKFLOW','Ocoya · SocialBee'),
 (1,0):('PUBLISHING INFRASTRUCTURE','Postiz · Nuelink'),
 (2,0):('LIMITED PUBLIC EVIDENCE','Followr · Sentrive'),
}
for (x,y),(title,names) in cells.items():
 ax.add_patch(plt.Rectangle((x+.035,y+.06),.93,.86,color='#e8f2f0' if y else '#eef0f4',zorder=0))
 ax.text(x+.09,y+.76,title,fontsize=11,fontweight='bold',color='#237c77')
 ax.text(x+.09,y+.55,names,fontsize=12,va='top',linespacing=1.8)
ax.axis('off');ax.set_title('COMPETITIVE POSITIONING — CATEGORICAL MAP\nAnalyst classification of documented workflows; no performance ranking',loc='left',pad=18,fontweight='bold')
fig.text(.13,.015,'Box placement and distance have no numerical meaning. Holo paid optimization is not fully verified.\nCapability matrix and README.md explain scope, evidence and approval constraints.',fontsize=10)
save(fig,'03-positioning-map')
print('Created 3 CSVs, data.json and 3 figures in PNG/SVG/PDF.')
