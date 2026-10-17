# exec'd from build.py
REPO="https://github.com/tapelog-journal/tapelog-mcp"
AIQ=[("What is the TapeLog AI Coach?","A free, open-source (MIT) MCP server and prompt pack that lets Claude, ChatGPT, Cursor and other AI assistants analyze your own DAS Trader Pro or Robinhood CSV exports: win rate, profit factor, expectancy, drawdown, PDT day-trade count, and descriptive breakdowns of where your results were weakest."),
("Is my trading data uploaded anywhere?","The MCP server runs on your own computer and stores fills in ~/.tapelog/fills.json. There is no broker login and no TapeLog cloud. Your AI client sees the tool results you ask for, under that client's own privacy terms."),
("Does it tell me what to trade?","No. TapeLog only describes your own past trades and process, such as timing, sizing, hold times and discipline. It never recommends buying, selling or holding any security and gives no price targets, signals, picks or market predictions. It is educational and record-keeping software, not investment advice, and TapeLog is not a registered investment adviser."),
("Which AI apps does it work with?","Any MCP client: Claude Desktop, Claude Code, Cursor, Windsurf, VS Code, Cline and others. With no MCP client, paste the TapeLog Coach instructions into a ChatGPT Custom GPT or a Claude Project and upload your CSV."),
("Which brokers are supported?","DAS Trader Pro (Trades window CSV), Robinhood (Account activity report CSV), and any broker whose fills you can save as date, time, symbol, side, qty, price, fees."),
("How much does it cost?","The AI Coach is free and open source. The TapeLog spreadsheet journal is still available, with a free Lite version.")]
SOFT={"@context":"https://schema.org","@type":"SoftwareApplication","name":"TapeLog AI Coach (tapelog-mcp)","applicationCategory":"FinanceApplication","operatingSystem":"Windows, macOS, Linux",
 "description":"Open-source MCP server that lets AI assistants analyze your own DAS Trader Pro and Robinhood trade exports: stats, behavioral patterns and period comparisons. Educational; not investment advice.",
 "url":BASE+"/ai-coach/","downloadUrl":REPO,"license":"https://opensource.org/licenses/MIT","isAccessibleForFree":True,
 "offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"publisher":{"@type":"Organization","name":"TapeLog"}}
CODE={"@context":"https://schema.org","@type":"SoftwareSourceCode","name":"tapelog-mcp","codeRepository":REPO,"programmingLanguage":"Python","license":"https://opensource.org/licenses/MIT"}
cfg='''{
  "mcpServers": {
    "tapelog": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/tapelog-journal/tapelog-mcp", "tapelog-mcp"]
    }
  }
}'''
body=f"""<h1>TapeLog AI Coach: a free AI trade-journal coach for Claude, ChatGPT &amp; Cursor</h1>
<p>Point your AI assistant at your <strong>DAS Trader Pro</strong> or <strong>Robinhood</strong> export and ask how you actually traded. TapeLog is an open-source <a href="https://modelcontextprotocol.io">MCP</a> server. It rebuilds your round trips locally, calculates your stats, and describes the patterns in your own behavior.</p>
<p><a class="btn" href="{REPO}">Get it on GitHub (free, MIT)</a><a class="btn alt" href="{REPO}/tree/main/coach">No-install GPT / Claude Project pack</a><a class="btn alt" href="https://thetapelog.beehiiv.com/subscribe">Join the Pro waitlist</a></p>
<p class="note"><strong>Process, not picks.</strong> TapeLog analyzes only your own past trades: timing, sizing, hold times and discipline. It never recommends buying, selling or holding any security, never gives price targets, signals or market predictions, and never places trades. It is educational and record-keeping software, <strong>not investment advice</strong>, and TapeLog is <strong>not a registered investment adviser</strong>.</p>
<h2>What you can ask</h2><ul><li>"Import today's DAS trades and show my stats."</li><li>"Where were my results weakest this month?"</li><li>"Compare last week to this week."</li><li>"How did my position size change after a losing trade?"</li><li>"Give me my <a href="/tapelog/habit-report/">weekly habit report</a>."</li></ul>
<h2>Example output (sample data)</h2><pre>Your 18 trades entered 11:00-12:00 netted -$2,039 (avg -$113, win rate 11%).
On trades taken right after a same-day loss, your average position was
$20,443 vs $9,544 otherwise (2.1x); those 18 trades averaged -$37.61.
Your losing trades were held 26.1 min on average vs 10.4 min for winners.</pre>
<p class="small">Findings are descriptive. Small samples can be noise, so treat them as prompts to reflect on your process.</p>
<h2>Tools</h2><table><tr><th>Tool</th><th>Returns</th></tr><tr><td>import_fills</td><td>Parses DAS Trader, Robinhood or generic CSV and skips duplicates</td></tr><tr><td>get_stats</td><td>Net P&amp;L, win rate, profit factor, expectancy, average win and loss, max drawdown, losing streak, hold time, PDT day-trade count</td></tr><tr><td>find_leaks</td><td>Breakdowns by time of day, weekday, hold time, symbol, direction and after-loss sizing</td></tr><tr><td>compare_periods</td><td>Period A vs B with changes</td></tr><tr><td>weekly_habit_report</td><td>This week vs your prior weeks: habits that appeared or faded, with counts. <a href="/tapelog/habit-report/">See a sample report</a></td></tr><tr><td>list_trades</td><td>Reconstructed round trips</td></tr></table>
<h2>Install (Claude Desktop, Cursor, other MCP clients)</h2><p>Install <a href="https://docs.astral.sh/uv/">uv</a>, then add this to <code>claude_desktop_config.json</code> or <code>~/.cursor/mcp.json</code>:</p><pre>{html.escape(cfg)}</pre>
<p>Claude Code: <code>claude mcp add tapelog -- uvx --from git+https://github.com/tapelog-journal/tapelog-mcp tapelog-mcp</code></p>
<h2>No MCP? Use the Coach prompt</h2><p>Paste <a href="{REPO}/blob/main/coach/instructions.md">the TapeLog Coach instructions</a> into a ChatGPT Custom GPT or a Claude Project, or paste the <a href="{REPO}/blob/main/coach/leak-analysis-prompt.md">one-shot leak-analysis prompt</a> into any chat with your CSV attached.</p>
<h2>How to export your trades</h2><ul><li><a href="/tapelog/guides/how-to-export-trades-from-das-trader/">Export trades from DAS Trader</a></li><li><a href="/tapelog/guides/robinhood-trade-history-export-csv/">Export Robinhood trade history CSV</a></li></ul>
<h2 id="pro">TapeLog Pro (coming soon)</h2><p>A hosted version for people who don't want to install anything: it works directly in ChatGPT and claude.ai, keeps your trade history in the cloud, lets you upload a CSV by email, and sends a weekly AI review of your process. It also alerts you when you break rules you set yourself, like "more than 6 trades before 10:00." The open-source core stays free.</p>
<p><a class="btn" href="https://thetapelog.beehiiv.com/subscribe">Join the Pro waitlist</a></p><p class="small">Joining subscribes you to the free weekly TapeLog newsletter, which is where we'll announce Pro. Unsubscribe anytime.</p>
{AGENT_API_HTML}
<h2>FAQ</h2>{faq_html(AIQ)}
<p>Want a weekly breakdown of your process? Join the free <a href="https://thetapelog.beehiiv.com/subscribe">TapeLog newsletter</a>. Prefer a spreadsheet? The journal below still works.</p>"""
page("/ai-coach/","TapeLog AI Coach: Free AI Trading Journal for Claude, ChatGPT & Cursor (MCP, open source)",
 "Free open-source MCP server and GPT/Claude prompt pack that analyzes your own DAS Trader Pro and Robinhood CSVs: win rate, profit factor, drawdown and behavioral patterns. Process, not picks.",
 body,[SOFT,CODE,faq_ld(AIQ)])
