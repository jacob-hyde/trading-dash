# Trading run — 2026-08-25 12:07 ET (Tue)

**Regime:** SPY 765.54 — **risk-on** (200d 707.99, +8.1% above) · **Entry throttle OPEN** (50d 752.26, +1.8% above) — new entries and promotions permitted.
**Account:** $2,463.62 · cash/BP $1,129.92 · equity $1,333.70 · day +$2.45 (+0.10%) · cum +23.41%.
**Portfolio heat:** $60.10 open risk = **2.44%** of the 8% budget. Room for new risk **$136.99**. 3 open — not crowded.

---

## 1. Reconcile — CLEAN
Broker matches the db exactly (HUM 1 · DYN 18 · WSFS 6). **No new fills** since the 8/24 WSFS buy and IRDM sell, both already journaled. No closes, no trims, no auto-adds, no unexplained agentic orders. Realized P&L unchanged at **-$93.25**.

## 2. Positions — all three healthy, none near T1, no thesis breaks

| Sym | Qty @ cost | Px | Unreal. | R | Stop (dist) | T1 (dist) | Held | ER |
|---|---|---|---|---|---|---|---|---|
| HUM | 1 @ 382.00 | 387.98 (+0.35%) | **+$5.98** (+1.57%) | +0.35R | 364.90 (6.3%) | 428.90 (10.5%) | 6d | 11/06 ✓ |
| DYN | 18 @ 25.97 | 26.21 (+0.85%) | **+$4.32** (+0.92%) | +0.21R | 24.85 (5.5%) | 29.20 (11.4%) | 3d | 11/04 ✓ |
| WSFS | 6 @ 79.65 | 78.99 (-0.60%) | **-$3.96** (-0.83%) | -0.24R | 76.90 (**2.7%**) | 89.00 (12.7%) | 1d | 10/22 ✓ |

- All three improved on the 11:07 marks. **HUM** turned green (+$5.98 from +$2.35) and **DYN** added to its gain.
- **WSFS is still the one to watch** — its 76.90 stop sits 2.7% below price, the tightest in the book, and it remains just under its 79.00–80.50 entry zone on day 2. Nothing broken; no cushion.
- No binaries inside any hold window. No held name showed a news-shaped move; **no pending-deal signal on any position**. Today's tape is not a financials selloff (MS +0.8%, STT +0.8%, BPOP +0.2%), so WSFS's drift is idiosyncratic drift, not sector stress.

## 3. Actionable entries — 7 READY (was 8 at 11:07)

**★ = midcap-leader habitat. Rank = tt_util rank (score6 + ★habitat) + 1 if chart A.**

**Theme-clean (no conflict with an open position):**

| # | Sym | Rank | Setup | Zone | Stop | T1 | R:R@top | Size | Notional / risk |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **SOBO** | 6 | Pullback to the 10/20/50d confluence — chart B | 36.60–37.10 (px 36.94) | 35.40 | 40.50 | **2.00** | **13 sh** | $482 / $22.10 |
| 2 | **MMM** | 5 | *(back in zone this run)* Flat base at highs, 4wk 176–185 digestion of the 7/21 gap — **chart A** | 177.50–180.00 (px 179.93) | 173.50 | 197.50 | **2.69** | **2 sh** | $360 / $13.00 |
| 3 | **IEX** | 5 | Pullback-to-20/50d in a stair-step leader — chart B | 228.00–231.50 (px 230.71) | 222.50 | 250.00 | 2.06 | **2 sh** | $463 / $18.00 |
| 4 | **WST** | 5 | Flat base under highs — chart B | 346.00–351.00 (px 350.26) | 342.90 | 375.00 | **2.96** | **1 sh** | $351 / $8.10 |

**Theme-adjacent to an open position — your call:**

| # | Sym | Rank | Conflict | Zone | Stop | T1 | R:R | Size |
|---|---|---|---|---|---|---|---|---|
| 5 | **★TRVI** | 7 | ⚠ DYN (biotech) | 17.90–18.25 (px 18.04) | 17.45 | 19.90 | 2.06 | 26 sh / $475 / $20.80 |
| 6 | CNO | 5 | ⚠ HUM (health/insurance) | 52.90–54.40 (px 53.95) | 52.10 | 59.00 | 2.00 | 9 sh / $490 / $20.70 |
| 7 | MS | 4 | ⚠ WSFS (financials) | 214.00–218.35 (px 215.81) | 200.91 | 253.24 | 2.00 | 2 sh / $437 / $34.88 |

**What changed since 11:07:**
- **MMM re-entered its zone** (180.49 → 179.93) and is the **only chart-A grade in the READY set** — the best-graded structure on the list, though on the weakest numeric score (4/6 Lane B, RS 8).
- **★CXW lost READY by 5 cents** — 33.095 vs a 33.04 zone top. It was the #1 pick an hour ago and the only other chart A. A pullback of 0.2% puts it straight back on the list.
- **VOYA lost READY by 10 cents** — 98.90 vs a 99.00 zone floor.

**Caveats you should weigh before any of these:**
- **Buying power ($1,129.92) still caps you at ~2 of these**, not 7. All seven at their zone tops would be $3,057 of notional. Heat room ($136.99) is not the binding constraint — cash is. Six of the seven are capped by the 20% position limit, not by risk.
- **Six of seven carry a chart-B grade; only MMM graded A.** The recurring flaw across the B's is unchanged: price is arriving at the zone on a slide that broke the 10/20d rather than holding the zone as support ("right side not turning").
- **SOBO, CNO and MS sit at R:R exactly 2.00** — they clear the bar by rounding, nothing more.
- READY is **mechanical only** — the 0.4 review-and-confirm protocol still gates every order.

## 4. Promotes / drops — ZERO promotes, ZERO drops
Full STEP 1C gate re-check ran on **all 136 'new' candidates** (14 weekly-bar pulls, ~14mo each, rescored through `tt_util`):
- **Zero came back lane='skip'** → no structure-broke auto-drops. 113 Lane A / 23 Lane B.
- **Zero age-outs** — the oldest surviving 'new' candidates are the 8/12–8/13 cohort at 8–9 trading days, still inside the ~10-day window. (The 10:09 run already cleared the ≤8/11 cohort.)
- **37 names** passed the 6/6 Lane-A + RS≥70 gate; **4** cleared the base/extension filter and went to the graded chart check. **None promoted:**

| Sym | Rank | Chart grade | Why not promoted |
|---|---|---|---|
| **★NHC** | **7** | **B** — pullback to the rising 10/20d at new highs; ATR expanding +23%, a 209.33 flush inside the 5-week base | Highest-ranked name in the whole pool, but **fails R:R**. With a structure-sound stop 215.00 (5.7% / 1.38 ATR, below the 213–219 shelf) the nearest *real* level — the 239.29 high — is only **0.87R** from the 228 zone top. 2R needs a blue-sky T1 of 254 (6% above the high). |
| **RCUS** | 6 | **A** — 9-week ascending base 27.3–31.7 on higher lows, ATR contracting -16%, volume drying, riding the rising 10/20d | **Best structure in the pool.** But the sound stop 27.20 (below the 27.29 base low) gives only **1.89** at the 29.90 zone top vs the 35.00 measured move. 2.55 only appears with a 27.90 stop that sits *inside* the 27.3–28.0 shelf — a routine wick ends it. Also biotech (⚠DYN). |
| **ECPG** | 6 | **B** — stair-step leader pressing new highs (-1.7% off), ATR expanding +34%, wide 2-week ranges 94.81–104.98 | Price 103.07 is **above** its 98–101 zone. At the zone top with a sound 93.50 stop, the real level (104.98 high) is **0.53R**; 2.00 only with a blue-sky T1 116 (10.5% above the high). |
| **ENVA** | 6 | **F** — extension unwind | Vertical 145→267 in four months, then a 262→237 break through **both** the 10/20d on the heaviest volume in a month. Px 245 still under the 10d/20d (255). Not entry-eligible regardless of a perfect 6/6. |

All four verdicts are written to the candidate notes with a `gate_recheck 2026-08-25` stamp; all 136 carry the stamp.

## 5. Lane C — ZERO events
40 names gapped ≥6% on the gainers scan; after pace-adjusting volume for the 12:07 clock (×2.48) and testing the **open** rather than the last price, none is an EP:
- **NYAX** +13.2% gap on a genuinely neglected base, closing in the upper half — but the whole day is **10,488 shares**, 1.5× pace-adjusted. A 13% gap with no participation is not an event.
- **MAIR** +12.2% gap, neglected — but has deteriorated since 11:07: now closing in the **bottom 3%** of the day's range on 1.3× volume. Textbook gap-and-fade, confirmed.
- **KURA** +9.6% gap, upper 73% of range, 2.5× — but **CHASED** (fails the neglect test). Hard reject per Rules A2, backtested negative.
- **CDLR** +8.6% gap, neglected, upper half — 0.7× volume (23k shares). No participation.
- **GENB** was the only name with real volume (**3.9×**) — but it opened +0.2% and ramped intraday. An intraday ramp is not a gap; correctly rejected on `gap<6%`.
- STDN and APMD are recent listings (29 and 18 daily bars) — below the 66-bar minimum, cannot be scored.

## 6. Flags
- **BLOCKED — floor (lane skip):** BNTX, EL, MEDP — unchanged, fail both lanes.
- **BLOCKED — pending deal:** GSAT (Amazon) — in its zone with a chart A, but the A1.5 block holds.
- **WAIT — binary:** CASY (ER 9/8, inside the ~2-week window).
- **WAIT — chart F:** GD, PRMB, VAC, DXPE, MOH, BNL, TRV, PVLA — all on knife/spike-unwind/broken structure. Not entry-eligible.
- Discovery Lanes A/B skipped — already ran today at 10:09 (once-daily gate). STEP 1D structure refresh likewise (last_wl_score = today).
- EOD prune not due (runs at/after 4:00pm ET).
- No Alpha Vantage calls needed — the binary check was satisfied off the Robinhood earnings calendar (none of the 7 READY names report inside the window).

---
**Dashboard published OK** → https://jacob-hyde.github.io/trading-dash/
Recommendations only — no orders were placed, modified, or cancelled. Not financial advice.
