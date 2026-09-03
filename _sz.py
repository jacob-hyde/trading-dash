import sqlite3
c=sqlite3.connect('trading.db'); c.row_factory=sqlite3.Row; cur=c.cursor()
q={r['symbol']:r['last'] for r in cur.execute('select symbol,last from quotes')}
acct=2501.62; riskcap=acct*0.015
print('risk cap 1.5%% = %.2f; poscap 20%% = %.2f' % (riskcap, acct*0.20))
ready=['MS','MEDP','DNTH','GEO','HOG','NHC','RCUS','BRKR','INGM','PK','GH','CRK']
for s in ready:
    r=cur.execute('select symbol,lane,entry_high,stop,t1,rank from watchlist where symbol=?',(s,)).fetchone()
    last=q.get(s); stop=r['stop']; t1=r['t1']
    if last and stop and last>stop:
        rps=last-stop; sh=min(int(riskcap/rps), int(acct*0.20/last))
        rr=(t1-last)/rps if t1 else 0
        print('%-6s rk%2s lane%s last %g stop %g t1 %s | R/sh %.2f -> ~%dsh (risk $%.0f) RR@last %.1f' % (s,r['rank'],r['lane'],last,stop,t1,rps,sh,sh*rps,rr))
