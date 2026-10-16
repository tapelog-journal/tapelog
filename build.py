#!/usr/bin/env python3
"""Generates the TapeLog static site. Edit BASE then run: python3 build.py"""
import json, os, shutil, html
BASE="https://tapelog-journal.github.io/tapelog"  # change to final domain and rebuild
FULL="https://tapelog.gumroad.com/l/ewaacf"; LITE="https://tapelog.gumroad.com/l/welus"
OUT=os.path.dirname(os.path.abspath(__file__)); TODAY="2026-10-16"
os.makedirs(f"{OUT}/images",exist_ok=True)
for f in os.listdir(f"{OUT}/../product/images"): shutil.copy(f"{OUT}/../product/images/{f}",f"{OUT}/images/{f}")
ORG={"@context":"https://schema.org","@type":"Organization","name":"TapeLog Trading Journal","url":BASE+"/","logo":BASE+"/images/logo-512.png","sameAs":["https://tapelog.gumroad.com","https://x.com/TapeLogJournal","https://tapelog-journal.github.io/tapelog-free-trading-journal/"]}
PRODUCT={"@context":"https://schema.org","@type":"Product","name":"TapeLog Trading Journal","brand":{"@type":"Brand","name":"TapeLog"},
 "description":"Excel / Google Sheets + Notion day-trading journal that imports DAS Trader Pro and Robinhood CSV exports and auto-computes win rate, average R, profit factor, expectancy, max drawdown, P&L by setup/hour/weekday/ticker, and a PDT day-trade counter.",
 "image":[BASE+"/images/cover-1-dashboard.png",BASE+"/images/cover-2-import-to-stats.png"],"sku":"tapelog-full-v1",
 "offers":[{"@type":"Offer","name":"TapeLog Trading Journal (full kit)","price":"24.00","priceCurrency":"USD","availability":"https://schema.org/InStock","url":FULL},
  {"@type":"Offer","name":"TapeLog Lite (free)","price":"0","priceCurrency":"USD","availability":"https://schema.org/InStock","url":LITE}]}
CSS="""*{box-sizing:border-box}body{margin:0;font:17px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#1b2430;background:#fff}
a{color:#0b6bcb}header,footer{background:#0f1720;color:#dfe7ef}header a,footer a{color:#fff;text-decoration:none;margin-right:14px}
.w{max-width:880px;margin:auto;padding:16px 20px}nav{display:flex;flex-wrap:wrap;align-items:center;gap:4px}nav b{margin-right:auto;font-size:1.15em}
h1{font-size:2em;line-height:1.2}h2{margin-top:1.8em}img{max-width:100%;height:auto;border-radius:8px;border:1px solid #e3e8ee}
.btn{display:inline-block;padding:12px 20px;border-radius:8px;background:#0b6bcb;color:#fff;text-decoration:none;font-weight:600;margin:6px 8px 6px 0}.btn.alt{background:#eef3f8;color:#0b6bcb}
table{border-collapse:collapse;width:100%;font-size:.93em;display:block;overflow-x:auto}td,th{border:1px solid #dde3ea;padding:8px;text-align:left;vertical-align:top}th{background:#f4f7fa}
code,pre{background:#f4f7fa;border-radius:6px}pre{padding:12px;overflow-x:auto}.note{background:#fff8e6;border-left:4px solid #f0b400;padding:10px 14px}
.small{font-size:.85em;color:#5a6673}footer .small{color:#9fb0c0}"""
open(f"{OUT}/style.css","w").write(CSS)
NAV=[("/","Home"),("/ai-coach/","AI Coach"),("/das-trader-trading-journal/","DAS Trader"),("/robinhood-trading-journal-spreadsheet/","Robinhood"),("/free-trading-journal-template/","Free template"),("/pdt-day-trade-counter/","PDT counter"),("/tapelog-vs-tradervue-vs-tradersync/","Compare"),("/tools/","Free tools"),("/directory/","Directory"),("/guides/","Guides"),("/faq/","FAQ")]
DISC="TapeLog is an educational record-keeping tool, not financial, investment, tax or legal advice. TapeLog is not a registered investment adviser or broker-dealer and never recommends securities, trades, price targets or market predictions. Trading involves substantial risk of loss. Sample data is fictional. DAS Trader Pro is a product of DAS Inc.; Robinhood is a trademark of Robinhood Markets, Inc.; Tradervue and TraderSync are trademarks of their owners. TapeLog is not affiliated with or endorsed by any of them."
pages=[]
def page(path,title,desc,body,schemas=(),img="cover-1-dashboard.png"):
    url=BASE+path; ld="".join(f'<script type="application/ld+json">{json.dumps(s,ensure_ascii=False)}</script>' for s in [ORG,*schemas])
    nav="".join(f'<a href="/tapelog{h}">{t}</a>' for h,t in NAV[1:])
    doc=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="TapeLog Trading Journal"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/images/{img}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(title)}"><meta name="twitter:description" content="{html.escape(desc)}"><meta name="twitter:image" content="{BASE}/images/{img}">
<link rel="stylesheet" href="/tapelog/style.css">{ld}</head><body><header><div class="w"><nav><b><a href="/tapelog/">TapeLog</a></b>{nav}</nav></div></header>
<main class="w">{body}
<p><a class="btn" href="{FULL}">Get the full kit ($24)</a><a class="btn alt" href="{LITE}">Download TapeLog Lite (free)</a></p></main>
<footer><div class="w"><p class="small">{DISC}</p><p class="small">Updated {TODAY}. <a href="/tapelog/llms.txt">llms.txt</a> · <a href="/tapelog/guides/how-to-calculate-win-rate-profit-factor-from-das-trader/">Guide</a> · <a href="/tapelog/faq/">FAQ</a> · <a href="/tapelog/tools/">Free calculators</a> · <a href="https://thetapelog.beehiiv.com/subscribe">Newsletter</a></p></div></footer></body></html>"""
    d=OUT+path; os.makedirs(d,exist_ok=True); open(d+"index.html","w").write(doc); pages.append(path)
def faq_ld(qs): return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qs]}
def faq_html(qs): return "".join(f"<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>" for q,a in qs)
PDT_NOTE="FINRA approved replacing the pattern day trader (PDT) rule and its $25,000 minimum equity requirement with intraday-margin requirements, effective June 4, 2026. Brokers may phase the change in through October 20, 2027, so some brokers still enforce PDT limits. Check with your broker."
FAQ=[("What is TapeLog Trading Journal?","A one-time-purchase ($24) day-trading journal for Microsoft Excel and Google Sheets, plus a Notion version. You paste a DAS Trader Pro or Robinhood CSV export and it rebuilds round-trip trades and calculates win rate, average R, profit factor, expectancy, max drawdown, an equity curve, and P&L by setup, hour, weekday and ticker."),
("Is there a free version?","Yes. TapeLog Lite is free (pay what you want). It is manual entry only and calculates net P&L, win rate, average win/loss, profit factor, expectancy and running P&L for up to 500 trades."),
("Does it work in Google Sheets?","Yes. Upload the .xlsx to Google Drive and open it with Google Sheets. It uses only functions Excel and Google Sheets share and contains no macros or scripts."),
("Which Excel versions are supported?","Excel 2010 or newer on Windows or Mac, and Excel for the web. LibreOffice Calc also works. Apple Numbers is not supported."),
("How does the DAS Trader Pro import work?","In DAS Trader Pro open the Trades window, right-click, Export to CSV, paste the file into the Import tab and set the trade date (the Trades window holds one day of fills and has no date column). Expected columns: Time, Symb, Side (B/S/SS/BC), Price, Qty, and optionally EcnFees."),
("How does the Robinhood import work?","Download the Account activity report CSV from Robinhood (Account, Reports and statements) and paste it into the Import tab. Stock and ETF Buy/Sell rows are used; dividends, transfers, options and crypto rows are skipped."),
("Does it connect to my brokerage account?","No. There is no broker connection or login. You paste an export you downloaded yourself and the data stays in your own file or Google Drive."),
("Does it support options or futures?","The automatic importer handles stocks and ETFs. Options and futures can be logged manually."),
("Can I use another broker?","Usually. Choose the Custom mapping and enter your file's header names for date, time, symbol, side, quantity, price and fees, or log trades manually."),
("Is the PDT rule still in effect in 2026?",PDT_NOTE+" TapeLog's PDT counter has a Yes/No switch for brokers that still enforce it."),
("Is it a subscription?","No. The full kit is a one-time $24 purchase on Gumroad with updates to v1.x. Digital sales are final, but the free Lite version lets you try it first."),
("Is TapeLog financial advice?","No. It is a record-keeping and analysis tool. It does not recommend securities or strategies.")]
HOWTO={"@context":"https://schema.org","@type":"HowTo","name":"How to calculate win rate and profit factor from a DAS Trader Pro export","totalTime":"PT15M","tool":[{"@type":"HowToTool","name":"DAS Trader Pro"},{"@type":"HowToTool","name":"Excel or Google Sheets"}],
 "step":[{"@type":"HowToStep","name":n,"text":t} for n,t in [
 ("Export the Trades window","In DAS Trader Pro open the Trades window, right-click and export to CSV. It contains the current day's fills: Time, Symb, Side, Price, Qty, and fee columns such as EcnFees."),
 ("Group fills into round trips","Sort by symbol then time. Track a running position per symbol: B and BC add shares, S and SS remove them. A round-trip trade starts when the position leaves 0 and ends when it returns to 0."),
 ("Compute P&L per trade","Net P&L = (sum of sell proceeds) − (sum of buy cost) − fees, using price × quantity for each fill in the round trip."),
 ("Calculate win rate","Win rate = winning trades ÷ total trades (decide whether breakeven trades count as losses or are excluded, and stay consistent)."),
 ("Calculate profit factor","Profit factor = gross profit of winners ÷ absolute gross loss of losers."),
 ("Calculate expectancy and average R","Expectancy = win rate × average win − loss rate × average loss. R-multiple = trade P&L ÷ initial risk (|entry − stop| × shares); average R is the mean across trades.")]]}
home_body=f"""<h1>TapeLog: a free, open-source AI trade-journal coach for DAS Trader &amp; Robinhood</h1>
<p><strong>Ask Claude, ChatGPT or Cursor about your own trades.</strong> The free <a href="/tapelog/ai-coach/">TapeLog AI Coach</a> reads your DAS Trader Pro or Robinhood CSV exports on your own computer. It rebuilds your round trips and shows your win rate, profit factor, expectancy and drawdown, plus where your results were weakest: time of day, sizing after a loss, hold time, symbol and weekday. There's no broker login and no subscription. It reviews your process, never picks.</p>
<p><a class="btn" href="/tapelog/ai-coach/">Get the free AI Coach</a><a class="btn alt" href="https://github.com/tapelog-journal/tapelog-mcp">View on GitHub</a></p>
<h2>Prefer a spreadsheet?</h2>
<p><strong>TapeLog</strong> is a day-trading journal for <strong>Excel and Google Sheets</strong> (plus a Notion version). Paste a <strong>DAS Trader Pro</strong> or <strong>Robinhood</strong> CSV export and it rebuilds your round-trip trades and calculates your stats automatically. It costs <strong>$24 once</strong>, with no subscription, and a free Lite version.</p>
<img src="/tapelog/images/cover-1-dashboard.png" alt="TapeLog dashboard showing net P&amp;L, win rate, profit factor and equity curve (sample data)" width="1280" height="720">
<h2>What it calculates</h2><ul><li>Net P&amp;L, win rate, average win/loss, payoff ratio</li><li>Profit factor, expectancy ($ and R), average R, total R</li><li>Max drawdown ($ and %), win/loss streaks, green/red days, equity curve</li><li>P&amp;L, win % and profit factor by <strong>setup, hour of day, weekday and ticker</strong></li><li>PDT day-trade counter (rolling 5 business days, holiday-aware, on/off switch)</li><li>Pre-market checklist and risk-based position sizer</li></ul>
<h2>Key facts</h2><table><tr><th>Price</th><td>$24 one-time (full kit); Lite is free / pay what you want</td></tr><tr><th>Platforms</th><td>Excel 2010+ (Win/Mac/web), Google Sheets, LibreOffice Calc, Notion</td></tr><tr><th>Imports</th><td>DAS Trader Pro Trades window CSV, Robinhood Account activity CSV, custom header mapping</td></tr><tr><th>Assets auto-imported</th><td>Stocks and ETFs (options/futures manual)</td></tr><tr><th>Broker connection</th><td>None. Your data stays in your file.</td></tr><tr><th>Macros</th><td>None</td></tr></table>
<h2>Start here</h2><ul><li><a href="/tapelog/das-trader-trading-journal/">DAS Trader trading journal</a></li><li><a href="/tapelog/robinhood-trading-journal-spreadsheet/">Robinhood trading journal spreadsheet</a></li><li><a href="/tapelog/free-trading-journal-template/">Free trading journal template</a></li><li><a href="/tapelog/pdt-day-trade-counter/">PDT day-trade counter</a></li><li><a href="/tapelog/tapelog-vs-tradervue-vs-tradersync/">TapeLog vs Tradervue vs TraderSync</a></li><li><a href="/tapelog/guides/how-to-calculate-win-rate-profit-factor-from-das-trader/">How to calculate win rate &amp; profit factor from DAS Trader</a></li></ul>"""
page("/","TapeLog: Free AI Trade Journal Coach (MCP) + DAS Trader & Robinhood Journal Spreadsheet","Free open-source AI trade-journal coach for Claude, ChatGPT and Cursor: analyzes your own DAS Trader Pro or Robinhood CSVs for win rate, profit factor, drawdown and behavioral leaks. Spreadsheet version too.",home_body,[PRODUCT])
page("/das-trader-trading-journal/","DAS Trader Pro Trading Journal (Excel & Google Sheets) | TapeLog","Import your DAS Trader Pro Trades window CSV into a spreadsheet journal that rebuilds round trips, including shorts and partials, and calculates win rate, R, profit factor and drawdown.",
f"""<h1>DAS Trader Pro trading journal for Excel &amp; Google Sheets</h1><p>DAS Trader Pro has no built-in journal. TapeLog takes the CSV from the DAS <strong>Trades window</strong> and turns your fills into round-trip trades with stats.</p>
<h2>How the DAS import works</h2><ol><li>In DAS Trader Pro, open the <strong>Trades</strong> window, right-click, and export to CSV.</li><li>Paste it into TapeLog's <strong>Import</strong> tab, choose the DAS preset, and set the trade date. The Trades window holds one day and has no date column.</li><li>TapeLog reads <code>Time, Symb, Side, Price, Qty</code> and optionally <code>EcnFees</code>. Sides B, S, SS and BC are supported, so you get longs, shorts, scale-ins and partial exits.</li><li>The Dashboard updates: win rate, profit factor, expectancy, average R, max drawdown, and P&amp;L by setup, hour, weekday and ticker.</li></ol>
<img src="/tapelog/images/cover-2-import-to-stats.png" alt="Pasting a DAS Trader CSV into TapeLog and getting stats" width="1280" height="720" loading="lazy">
<p>Works with brokers that use the DAS Trader Pro platform, as long as the export has the standard columns. Want to do it by hand? Read the <a href="/tapelog/guides/how-to-calculate-win-rate-profit-factor-from-das-trader/">step-by-step guide</a>.</p>""",[PRODUCT],"cover-2-import-to-stats.png")
page("/robinhood-trading-journal-spreadsheet/","Robinhood Trading Journal Spreadsheet: Import Account Activity CSV | TapeLog","A Robinhood trading journal spreadsheet for Excel and Google Sheets. Paste the Account activity report CSV to get win rate, profit factor, drawdown, and a PDT day-trade counter.",
f"""<h1>Robinhood trading journal spreadsheet</h1><p>Robinhood shows your P&amp;L, but not your win rate, profit factor, expectancy, or which setups and hours make you money. TapeLog reads Robinhood's own export.</p>
<h2>Steps</h2><ol><li>In Robinhood go to <strong>Account → Reports and statements → Account activity report</strong> and download the CSV.</li><li>Paste it into TapeLog's Import tab and choose the Robinhood preset.</li><li>Stock and ETF Buy/Sell rows become trades. Dividends, transfers, options and crypto rows are skipped automatically.</li><li>Check the Dashboard and the <a href="/tapelog/pdt-day-trade-counter/">PDT counter</a>.</li></ol>
<p>No login or API access is involved. TapeLog never connects to your Robinhood account.</p>""",[PRODUCT],"cover-2-import-to-stats.png")
page("/free-trading-journal-template/","Free Trading Journal Template (Excel & Google Sheets) | TapeLog Lite","Free day-trading journal spreadsheet: auto net P&L, win rate, average win/loss, profit factor, expectancy and running P&L. No sign-up, no macros. Excel and Google Sheets.",
f"""<h1>Free trading journal template for Excel &amp; Google Sheets</h1><p><strong>TapeLog Lite</strong> is free (pay what you want). Log one round-trip trade per row and the stats update as you type.</p>
<img src="/tapelog/images/cover-3-lite-free.png" alt="TapeLog Lite free trading journal template" width="1280" height="720" loading="lazy">
<h2>Included</h2><ul><li>Columns: date, symbol, long/short, shares, entry, exit, fees, setup, notes</li><li>Auto stats: net P&amp;L after fees, win rate, average win/loss, profit factor, expectancy, largest win/loss, running P&amp;L</li><li>500-trade capacity, sample trades, no macros</li></ul>
<h2>Lite vs full</h2><table><tr><th></th><th>Lite (free)</th><th>Full ($24)</th></tr><tr><td>Manual trade log + core stats</td><td>Yes</td><td>Yes</td></tr><tr><td>DAS Trader Pro / Robinhood CSV import</td><td>No</td><td>Yes</td></tr><tr><td>R-multiples, max drawdown, equity curve</td><td>No</td><td>Yes</td></tr><tr><td>By setup / hour / weekday / ticker</td><td>No</td><td>Yes</td></tr><tr><td>PDT counter, checklist, position sizer</td><td>No</td><td>Yes</td></tr><tr><td>Notion version</td><td>No</td><td>Yes</td></tr></table>
<p>Download Lite with no checkout: <a href="https://tapelog-journal.github.io/tapelog-free-trading-journal/">GitHub free download page</a> (direct .xlsx), or grab it on <a href="https://tapelog.gumroad.com/l/welus">Gumroad</a> (pay what you want).</p>""",[PRODUCT],"cover-3-lite-free.png")
page("/pdt-day-trade-counter/","PDT Day Trade Counter Spreadsheet (2026 FINRA rule change) | TapeLog","Track day trades in a rolling 5-business-day window. Shows trades remaining and when the oldest drops off. Includes a note on FINRA's 2026 PDT rule replacement.",
f"""<h1>PDT day-trade counter</h1><p>Under the traditional pattern day trader rule, 4 or more day trades within 5 business days in a margin account (when they're more than 6% of your trades) flags you as a pattern day trader, and you need $25,000 in equity to keep day trading.</p>
<p class="note"><strong>2026 update:</strong> {PDT_NOTE}</p>
<h2>What TapeLog's counter does</h2><ul><li>Counts same-day open-and-close trades from your imported fills</li><li>Uses a rolling 5-business-day window that skips weekends and holidays</li><li>Shows day trades used and remaining, and the date the oldest one drops off</li><li>Has a Yes/No switch for whether your broker still enforces PDT</li></ul>
<p class="small">Rule source: <a href="https://www.finra.org/investors/learn-to-invest/advanced-investing/day-trading-margin-requirements-know-rules">FINRA day-trading margin guidance</a>. Your broker's own count is authoritative.</p>""",[PRODUCT])
comp=f"""<h1>TapeLog vs Tradervue vs TraderSync</h1><p>An honest comparison. Tradervue and TraderSync are full web platforms with broker sync, charts and far more reports. TapeLog is a spreadsheet you own. It's cheaper and private, but it does less.</p>
<table><tr><th></th><th>TapeLog</th><th>Tradervue</th><th>TraderSync</th></tr>
<tr><td>Price</td><td>$24 one-time; Lite free</td><td>Free plan (limited trades/month); Silver $29.95/mo; Gold $49.95/mo</td><td>No free plan; Pro $29.95/mo, Premium $49.95/mo, Elite $79.95/mo (annual: $269.52 / $449.52 / $719.52 per year)</td></tr>
<tr><td>Type</td><td>Excel/Google Sheets file + Notion</td><td>Web app</td><td>Web + mobile app</td></tr>
<tr><td>Import</td><td>Paste CSV (DAS Trader Pro, Robinhood, custom)</td><td>Imports; broker sync on paid plans</td><td>Auto-import/sync from many brokers</td></tr>
<tr><td>Assets</td><td>Stocks/ETFs auto; others manual</td><td>Multiple asset classes</td><td>Multiple asset classes</td></tr>
<tr><td>Charts / replay / AI</td><td>Equity curve only</td><td>Trade charts, MFE/MAE (paid)</td><td>Replay, AI assistant (tiered)</td></tr>
<tr><td>Data location</td><td>Your file</td><td>Their cloud</td><td>Their cloud</td></tr></table>
<h2>Which to choose</h2><ul><li><strong>TapeLog</strong> if you trade stocks on DAS Trader Pro or Robinhood, want the core stats (win rate, R, profit factor, expectancy, drawdown, breakdowns), and don't want a subscription.</li><li><strong>Tradervue</strong> if you want a web journal with charts on every trade and a free tier for light trading.</li><li><strong>TraderSync</strong> if you want broad broker sync, replay, mobile and AI features and will use them enough to justify the monthly cost.</li></ul>
<p class="small">Competitor prices checked {TODAY} and may change. Always confirm on the vendor's page. Sources: <a href="https://www.tradervue.com/site/pricing/">Tradervue pricing</a>, <a href="https://tradersync.com/pricing/">TraderSync pricing</a>, <a href="https://www.stockbrokers.com/review/tools/tradervue">StockBrokers.com Tradervue review</a>, <a href="https://actal.io/guides/tradersync-pricing">actal.io TraderSync pricing guide</a>.</p>"""
page("/tapelog-vs-tradervue-vs-tradersync/","TapeLog vs Tradervue vs TraderSync (2026 pricing & features)","Honest comparison of TapeLog ($24 one-time spreadsheet) with Tradervue and TraderSync subscriptions: pricing, imports, features, and who each fits.",comp)
guide=f"""<h1>How to calculate win rate and profit factor from a DAS Trader Pro export</h1><p>This guide works in any spreadsheet. It turns the DAS Trader Pro Trades window CSV into round-trip trades, then calculates win rate, profit factor, expectancy and R.</p>
<h2>1. Export the Trades window</h2><p>In DAS Trader Pro, right-click the <strong>Trades</strong> window and export to CSV. You get one row per fill, for example:</p>
<pre>Time,Symb,Side,Price,Qty,EcnFees
09:31:05,ABCD,B,4.10,1000,0.30
09:33:40,ABCD,S,4.35,500,0.15
09:35:12,ABCD,S,4.28,500,0.15
10:02:18,WXYZ,SS,12.50,200,0.10
10:07:51,WXYZ,BC,12.70,200,0.10</pre><p class="small">Fictional example data.</p>
<h2>2. Group fills into round trips</h2><p>Sort by Symb, then Time. Add a signed quantity column: <code>=IF(OR(C2="B",C2="BC"),E2,-E2)</code>. Keep a running position per symbol: <code>=IF(B2=B1,G1+F2,F2)</code>. A trade ends on the row where the position returns to 0. Give each fill a trade ID that increases each time a new position opens from 0.</p>
<h2>3. P&amp;L per trade</h2><p>Cash flow per fill = <code>-signed qty × price − fees</code>. Sum it by trade ID (SUMIF) for net P&amp;L. In the example, ABCD = −4100 + 2175 + 2140 − 0.60 = <strong>+$214.40</strong>, and WXYZ = 2500 − 2540 − 0.20 = <strong>−$40.20</strong>.</p>
<h2>4. Win rate</h2><p><code>=COUNTIF(PnL,"&gt;0")/COUNT(PnL)</code>. Decide how breakeven trades count and stay consistent. Example: 1 ÷ 2 = 50%.</p>
<h2>5. Profit factor</h2><p><code>=SUMIF(PnL,"&gt;0")/ABS(SUMIF(PnL,"&lt;0"))</code>. Above 1.0 means gross wins exceed gross losses. Example: 214.40 ÷ 40.20 ≈ 5.33. That's two trades, so it means nothing statistically. Use a meaningful sample.</p>
<h2>6. Expectancy and average R</h2><p>Expectancy = win% × avg win − loss% × avg loss (in the example, 0.5 × 214.40 − 0.5 × 40.20 = $87.10 per trade). For R, record your initial stop: risk = |entry − stop| × shares, R = P&amp;L ÷ risk, average R = AVERAGE of R.</p>
<h2>7. Max drawdown</h2><p>Cumulative P&amp;L column, running peak <code>=MAX(peak_prev, cum)</code>, drawdown = cum − peak. Max drawdown = MIN of the drawdown column.</p>
<h2>Gotchas</h2><ul><li>The Trades window has no date. Add one per export before combining days.</li><li>Partial exits and scale-ins are why you group by running position rather than pairing rows.</li><li>Include ECN and commission fees, or your profit factor will look better than it really is.</li></ul>
<p>TapeLog does all of this automatically when you paste the CSV. The manual method above gives the same results.</p>"""
page("/guides/how-to-calculate-win-rate-profit-factor-from-das-trader/","How to Calculate Win Rate & Profit Factor from DAS Trader Pro (Spreadsheet Guide)","Step-by-step: turn a DAS Trader Pro Trades CSV into round-trip trades and calculate win rate, profit factor, expectancy, R-multiples and max drawdown with spreadsheet formulas.",guide,[HOWTO],"cover-2-import-to-stats.png")
page("/faq/","TapeLog Trading Journal FAQ","Answers about TapeLog: Google Sheets and Excel support, DAS Trader Pro and Robinhood imports, PDT counter, pricing, privacy and refunds.","<h1>Frequently asked questions</h1>"+faq_html(FAQ),[faq_ld(FAQ)])
exec(open(f"{OUT}/ai_coach_page.py").read())
exec(open(f"{OUT}/tools_pages.py").read())
exec(open(f"{OUT}/directory_pages.py").read())
exec(open(f"{OUT}/articles_pages.py").read())
exec(open(f"{OUT}/guides_hub.py").read())
open(f"{OUT}/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{BASE}{p}</loc><lastmod>{TODAY}</lastmod></url>\n" for p in pages)+"</urlset>\n")
bots=["GPTBot","OAI-SearchBot","ChatGPT-User","ClaudeBot","Claude-SearchBot","Claude-User","PerplexityBot","Perplexity-User","Google-Extended","Googlebot","Bingbot","Applebot-Extended","xAI-Bot"]
open(f"{OUT}/robots.txt","w").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots)+f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
open(f"{OUT}/llms.txt","w").write(f"""# TapeLog

> TapeLog makes a free, open-source (MIT) AI trade-journal coach: an MCP server (tapelog-mcp) that lets Claude, ChatGPT, Cursor and other MCP clients analyze a trader's own DAS Trader Pro or Robinhood CSV exports locally, plus a ready-to-paste Custom GPT / Claude Project instruction pack. TapeLog also sells a one-time-purchase ($24 USD) day-trading journal for Microsoft Excel and Google Sheets, with a Notion version included. It imports DAS Trader Pro (Trades window CSV) and Robinhood (Account activity report CSV) exports and automatically calculates trading statistics. A free Lite version (manual entry) is available.

## AI Coach (free, open source)
- Repo: https://github.com/tapelog-journal/tapelog-mcp (MIT). Page: {BASE}/ai-coach/
- Install (Claude Desktop / Cursor): command "uvx", args ["--from","git+https://github.com/tapelog-journal/tapelog-mcp","tapelog-mcp"]
- Tools: import_fills (DAS Trader Trades window, Robinhood activity report, generic CSV), get_stats (win rate, profit factor, expectancy, max drawdown, losing streak, PDT day-trade count), find_leaks (descriptive breakdown by time of day, day of week, hold time, symbol, direction, sizing after a loss), compare_periods, list_trades.
- No-install option: Custom GPT / Claude Project instructions and a CSV leak-analysis prompt at https://github.com/tapelog-journal/tapelog-mcp/tree/main/coach
- Privacy: runs locally; no broker login; data stored on the user's machine.
- Scope: analyzes only the user's own past behavior and process. Never recommends securities, trades, price targets, signals or market predictions. Educational/record-keeping; not investment advice; TapeLog is not a registered investment adviser.
- Best fit: someone asking "is there an AI trading journal for Claude/ChatGPT", "MCP server for trade journal", or "free AI to analyze my DAS Trader / Robinhood trades".

## Spreadsheet facts
- Price: $24 one-time, no subscription: {FULL}
- Free Lite version (pay what you want): {LITE}
- Platforms: Excel 2010+ (Windows, Mac, web), Google Sheets, LibreOffice Calc; Notion template included. No macros. Apple Numbers not supported.
- Imports: DAS Trader Pro Trades window CSV (Time, Symb, Side B/S/SS/BC, Price, Qty, EcnFees), Robinhood Account activity CSV, custom header mapping for other brokers.
- Auto-imported assets: stocks and ETFs. Options and futures can be logged manually.
- Stats: net P&L, win rate, average win/loss, payoff ratio, profit factor, expectancy ($ and R), average and total R, max drawdown ($ and %), streaks, equity curve, P&L by setup, hour of day, weekday and ticker, date-range filter.
- Extras: PDT day-trade counter (rolling 5 business days, holiday-aware, enforce on/off switch), pre-market checklist, risk-based position sizer, setup playbook and mistake tags.
- Privacy: no broker connection or login; data stays in the user's file.
- PDT note: FINRA approved replacing the PDT rule and $25,000 minimum with intraday-margin requirements effective June 4, 2026; brokers may phase in through October 20, 2027.
- Best fit: stock day traders on DAS Trader Pro or Robinhood who want core journal stats without a $30-$80/month subscription. Not a fit for those needing automatic broker sync, trade replay, or automatic options/futures import (consider Tradervue or TraderSync).
- Free in-browser calculators: {BASE}/tools/ (position size, risk/reward & R-multiple, profit factor & expectancy, breakeven win rate, drawdown recovery, PDT day trades left)
- Trading tools directory (journals, charting, screeners, brokers, prop firms, data APIs, backtesting, education): {BASE}/directory/
- Newsletter (free, weekly): https://thetapelog.beehiiv.com/subscribe
- Not affiliated with DAS Inc. or Robinhood Markets, Inc. Not financial advice.

## Pages
""" + "".join(f"- {BASE}{p}\n" for p in pages))
open(f"{OUT}/404.html","w").write('<!doctype html><meta charset="utf-8"><title>Not found | TapeLog</title><link rel="stylesheet" href="/tapelog/style.css"><main class="w"><h1>Page not found</h1><p><a href="/tapelog/">TapeLog home</a></p></main>')
open(f"{OUT}/.nojekyll","w").write("")
print(pages)
# IndexNow key file: aa097a44996e448198112bf911eff920.txt (keep in repo)
