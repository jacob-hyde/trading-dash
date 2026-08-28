# Trading run — Friday 2026-08-28 16:06 ET (EOD CLOSE)

**SPY 769.39 — risk-on** (200d 709.41) · **throttle OPEN** (50d 753.39).
Account $2,428.32 · cash/BP $1,085.64 · open risk $83.11 = **3.42%** of the 8% heat
budget, **$111.16 of room**. Open P&L **+$5.01**. Day −$15.95 (−0.65%).

## 1. Positions — 3 open, all GTC stop-protected, no action

| Sym | Qty | Avg | Close | P&L | R | Stop | Cushion | Day |
|---|---|---|---|---|---|---|---|---|
| CLMT | 10 | 47.00 | 47.76 | +7.60 (+1.62%) | +0.29R | 44.40 | 7.03% | 2 |
| ★HUM | 1 | 382.00 | 385.71 | +3.71 (+0.97%) | +0.22R | 364.90 | 5.70% | 11 |
| CON | 14 | 34.70 | 34.25 | −6.30 (−1.30%) | −0.18R | 32.20 | 5.99% | 3 |

Broker matches the db exactly — all shares `held_for_sells`, i.e. every stop is live
into the weekend. **Zero new fills since the 12:35 DYN stop.** Nothing near T1, nothing
to trail, **zero earnings inside the 16-day window** for any position or any active
watchlist name.

## 2. Reconcile — CLEAN

No closes, no trims, no adds, no unexplained agentic activity. The only fill on the
wire this week beyond DYN was the user-placed WSFS market sell (8/27), already journaled.

## 3. Lane C — all four pending EPs KILLED at the day-0 confirm

Every one of the four intraday EPs staged this morning opened as a valid event and
**closed in the bottom of its own day-0 range**, failing the upper-half-close test:

| Sym | Gap | Day-0 range | Close | Where it closed |
|---|---|---|---|---|
| AFRM | +11.1% | 77.59 – 90.44 | 77.75 | **lower 1%** — gave back the entire gap |
| KLAR | +6.4% | 14.18 – 15.06 | 14.18 | **exactly on the low** |
| GAP | +19.0% | 23.36 – 25.80 | 23.51 | lower 6% |
| SOLS | +15.4% | 63.13 – 67.50 | 63.61 | lower 11% |

All four **dropped**. The 15:25 run called this exactly. Fresh gap scan found **zero new
events**: FRNM's +6.1% is an intraday ramp (opened 14.03 vs a 13.94 close = +0.6% gap),
SPB's +15.4% is a bad late print (regular-session last 88.63 vs 88.50), PD 2.1× and
FLUT 1.7× both fail the 3× volume gate, and ESTC's +23.9% remains a hard chased reject
(A2). **Lane C ends the week 0 events taken, 4 staged, 4 correctly killed.**

## 4. EOD prune — 9 archived, all price-trigger

Stops hit: **PACS, BNTX, TRVI, DFTX, WST, PTGX**. Ran >5% past the zone top:
**CHEF, RHI, XMTR**. Active watchlist **103 → 94**. The stop/missed split flipped from
last week's 3:11 to 6:3 — zones are no longer set too low; this week the market came
down to them.

## 5. Promotes / drops

- **Promotes: none.** 1C re-checked the 28-name 8/22–8/23 cohort — **zero `lane==skip`,
  zero gate drops, zero age-outs** (oldest open candidate is 8/19 = 7 trading days).
  Nine cleared the numeric gate (HPQ RS 100, SLG 96, INSW 93, PK 89, CVSA 86, KFY 82,
  APLE 79, SLDE 75, CF 71) but promotions were **deliberately deferred**: 18 names are
  already READY against buying power for two, so more promotions cannot change Monday.
  KFY additionally carries a tentative 9/8 binary. These go to the front of Monday's
  chart-check queue.
- **Drops: 4** — AFRM, GAP, SOLS, KLAR (Lane C day-0 confirm, above).
- **SKIP / floor flags: none.** No active watchlist row failed the Lane floor this run.

## 6. Actionable entries — 18 READY in zone, capital funds TWO

Sizing is rules-based (1.5% = $36.42 risk cap, 20% = $485.66 notional cap). ★ = habitat.
R:R is measured at the **zone top**.

| Sym | R:R | Zone | Stop | T1 | Shares | Notional | Risk | Chart |
|---|---|---|---|---|---|---|---|---|
| **★ADPT** | **2.18** | 24.85–25.40 | 23.75 | 29.00 | 19 | $482.60 | $31.35 | **A** high-tight flag |
| **★EWTX** | **2.17** | 42.60–43.95 | 41.90 | 48.40 | 11 | $483.45 | $22.55 | B post-catalyst flat base |
| **★ELVN** | **2.16** | 57.60–59.10 | 55.90 | 66.00 | 8 | $472.80 | $25.60 | **A** flat shelf at highs |
| **★NRIX** | **2.11** | 25.95–27.20 | 25.40 | 31.00 | 17 | $462.40 | $30.60 | **A** flat base at highs |
| **★FLYW** | **2.07** | 18.19–18.87 | 17.55 | 21.60 | 25 | $471.75 | $33.00 | **A** ascending base |
| ★MGNI | 2.04 | 22.90–23.75 | 22.40 | 26.50 | 20 | $475.00 | $27.00 | B post-gap shelf |
| ★OSCR | 2.02 | 30.30–30.75 | 27.60 | 37.10 | 11 | $338.25 | $34.65 | B flat base |
| ★FA | 2.00 | 20.90–21.30 | 19.95 | 24.00 | 22 | $468.60 | $29.70 | B flat base at highs |

Then, non-habitat: BFH 2.07 (B), IEX 2.06 (B), HALO 2.05 (B, **⚠theme — HUM**),
NDSN 2.04 (B), CLH 2.00 (B), MS 2.00 (B), VCTR 2.00 (A, **⚠acquirer** — the 8/26
"breakout" IS the $7B First Eagle deal pop; verify dilution/financing before sizing),
YPF 2.00 (B, **⚠theme — CLMT**), NHC 2.00 (B), FTDR 2.00 (B).

**The five ★-habitat chart-A names lead: ADPT, ELVN, NRIX, FLYW** (and EWTX on R:R).
Zone moves at the bell: **CLH, OSCR, MGNI, BFH, NHC came back INTO** their zones;
BPOP, CLDX and NEU left. READY is mechanical only — the 0.4 review-and-confirm
protocol still gates any actual order.

## 7. Friday weekly review + live-vs-sim scorecard

Three closed this week, all losers, **realized −$43.27**:

| Sym | live R | sim R | delta | cause |
|---|---|---|---|---|
| ★IRDM | −0.75 | −1.00 | **+0.25** | better exit — the 47.90 limit beat the stop |
| WSFS | −0.82 | −0.49 (leg still open) | **−0.33** | worse exit — hand-sold a plan the machine still holds |
| ★DYN | −1.01 | −1.00 | −0.01 | one cent of stop slippage |

**Week 3: live −2.58R vs sim −2.49R → delta −0.09R (−0.03 avgR). Inside the ±0.3 band,
no divergence flag.** The loss is shaped correctly — nothing exceeded its planned 1R,
worst outcome −1.01R.

**RUNNING TALLY since 2026-08-10: live −2.43R vs sim −2.82R, delta +0.39R over 12
trades. Rule breaks: 3 cumulative, none in weeks 2 or 3.** 12 of the 50 closed trades
needed for the mid-September sizing checkpoint are on the board — sizing stays fixed.

⚠️ **The week's real flag: 18 names closed READY, capital was available for two, and the
book went to the weekend with 3 positions and 3.4% heat.** Weeks 1–3 have all ended
under-deployed against the heat budget. Not a rule break — but if the September
checkpoint shows positive expectancy, under-deployment, not sizing, becomes the binding
limit on this account.

---
**Dashboard published OK** → https://jacob-hyde.github.io/trading-dash/
No orders were placed, modified or cancelled. Not financial advice.
