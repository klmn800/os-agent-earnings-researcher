"""Scratch-DB tests for the patched earnings_confirm.py (2026-09-14 safety change).

Loads the PATCHED copy next to this file by path (not tools/earnings_confirm.py)
and never touches production: functions get db_path=SCR, and CLI runs patch
DB_PATH to SCR before calling main(). Run:
    python analysis/earnings_confirm_patch/test_earnings_confirm.py
"""
import importlib.util
import os
import sqlite3
import subprocess
import sys

sys.path.insert(0, r'E:\options_scanner')  # so the module's `tools.*` imports resolve

HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.join(HERE, 'earnings_confirm.py')
SCR = os.path.join(HERE, 'test_confirm.db')
CSV = os.path.join(HERE, 'test_bulk.csv')

spec = importlib.util.spec_from_file_location('ec_patched', MOD)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.DB_PATH = SCR  # belt and braces: any call that forgets db_path hits scratch

results = []


def check(name, cond, detail=''):
    results.append(cond)
    print('{}  {}{}'.format('PASS' if cond else 'FAIL', name, '' if cond else '   -> ' + str(detail)))


def fresh():
    for p in (SCR, SCR + '-wal', SCR + '-shm'):
        if os.path.exists(p):
            os.remove(p)
    c = sqlite3.connect(SCR)
    c.execute("CREATE TABLE earnings_upcoming (symbol TEXT PRIMARY KEY, earnings_date DATE NOT NULL, "
              "earnings_time TEXT, date_confirmed INTEGER DEFAULT 0, date_confirmed_by TEXT, "
              "date_confirmed_at TEXT)")
    c.executemany("INSERT INTO earnings_upcoming VALUES (?,?,?,?,?,?)", [
        ('AAA', '2026-09-28', 'Unknown', 0, None, None),
        ('BEN', '2026-09-30', 'bmo', 1, 'ben', '2026-09-01T10:00:00'),
        ('AGT', '2026-09-29', 'bmo', 1, 'agent', '2026-09-08T07:21:07'),
    ])
    c.commit()
    c.close()


def row(sym):
    c = sqlite3.connect(SCR)
    r = c.execute("SELECT earnings_date, earnings_time, date_confirmed, date_confirmed_by "
                  "FROM earnings_upcoming WHERE symbol=?", (sym,)).fetchone()
    c.close()
    return r


RUN = ("import sys, importlib.util; sys.path.insert(0, r'E:\\options_scanner'); "
       "s = importlib.util.spec_from_file_location('ec', r'{mod}'); m = importlib.util.module_from_spec(s); "
       "s.loader.exec_module(m); m.DB_PATH = r'{db}'; "
       "sys.argv = ['earnings_confirm.py'] + {argv!r}; m.main()")


def cli(argv):
    p = subprocess.run([sys.executable, '-c', RUN.format(mod=MOD, db=SCR, argv=argv)],
                       capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


# ---------------------------------------------------------------- functions
fresh()
r = m.set_time('aaa', 'AMC', set_by='agent', db_path=SCR)
check('set_time writes time only, date stays unconfirmed',
      r['success'] and row('AAA') == ('2026-09-28', 'amc', 0, None), (r, row('AAA')))
check('set_time message says date NOT confirmed', 'date NOT confirmed' in r['message'], r)

r = m.confirm_symbol('AAA', None, 'bmo', confirmed_by='agent', db_path=SCR)
check('confirm without date refused, row unchanged',
      not r['success'] and row('AAA') == ('2026-09-28', 'amc', 0, None), (r, row('AAA')))

r = m.confirm_symbol('AAA', '2026-09-28', confirmed_by='Ben', db_path=SCR)
check('confirmed_by outside {ben,agent} refused', not r['success'] and row('AAA')[2] == 0, r)

try:
    m.confirm_symbol('AAA', '2026-09-28', db_path=SCR)
    check('confirm_symbol with no confirmed_by raises TypeError', False, 'no exception')
except TypeError:
    check('confirm_symbol with no confirmed_by raises TypeError', row('AAA')[2] == 0)

r = m.confirm_symbol('AAA', '2026-09-3O', confirmed_by='agent', db_path=SCR)
check('bad date format refused', not r['success'] and row('AAA')[2] == 0, r)

r = m.confirm_symbol('AAA', '2026-09-28', 'noon', confirmed_by='agent', db_path=SCR)
check('bad time refused before any write', not r['success'] and row('AAA')[2] == 0, r)

r = m.confirm_symbol('AAA', '2026-09-30', 'bmo', confirmed_by='agent', db_path=SCR)
check('normal agent confirm works (date -> 09-30, bmo, agent)',
      r['success'] and row('AAA') == ('2026-09-30', 'bmo', 1, 'agent'), (r, row('AAA')))
check('confirm message reports +2d', 'date changed +2d' in r['message'], r)

r = m.confirm_symbol('AAA', '2026-09-30', 'unknown', confirmed_by='agent', db_path=SCR)
check("time 'unknown' stored as 'Unknown'", row('AAA')[1] == 'Unknown', row('AAA'))

r = m.confirm_symbol('BEN', '2026-09-30', 'bmo', confirmed_by='agent', db_path=SCR)
check('agent re-confirm of ben row (same values) refused, stamp stays ben',
      not r['success'] and row('BEN') == ('2026-09-30', 'bmo', 1, 'ben'), (r, row('BEN')))

r = m.set_time('BEN', 'amc', set_by='agent', db_path=SCR)
check('agent set_time on ben row refused',
      not r['success'] and row('BEN') == ('2026-09-30', 'bmo', 1, 'ben'), (r, row('BEN')))

r = m.set_time('BEN', 'amc', set_by='ben', db_path=SCR)
check('ben set_time on ben row allowed, confirmation kept',
      r['success'] and row('BEN') == ('2026-09-30', 'amc', 1, 'ben'), (r, row('BEN')))

r = m.confirm_symbol('BEN', '2026-10-01', confirmed_by='ben', db_path=SCR)
check('ben re-confirm of ben row with new date allowed',
      r['success'] and row('BEN') == ('2026-10-01', 'amc', 1, 'ben'), (r, row('BEN')))

r = m.confirm_symbol('AGT', '2026-09-23', 'bmo', confirmed_by='agent', db_path=SCR)
check('agent can correct its own confirmed row (the PAYX case)',
      r['success'] and row('AGT') == ('2026-09-23', 'bmo', 1, 'agent'), (r, row('AGT')))

r = m.set_time('AGT', 'amc', set_by='agent', db_path=SCR)
check('set_time on agent-confirmed row keeps its confirmation',
      r['success'] and row('AGT') == ('2026-09-23', 'amc', 1, 'agent'), (r, row('AGT')))

r = m.set_time('ZZZ', 'bmo', set_by='agent', db_path=SCR)
check('set_time unknown symbol refused', not r['success'], r)

# bulk: one good row, one dateless row
fresh()
with open(CSV, 'w', encoding='utf-8') as f:
    f.write('# comment\nsymbol,date,time\nAAA,2026-09-29,amc\nAGT,,amc\n')
m.bulk_import(CSV, confirmed_by='agent', db_path=SCR)
check('bulk: dated row confirmed', row('AAA') == ('2026-09-29', 'amc', 1, 'agent'), row('AAA'))
check('bulk: dateless row rejected, untouched',
      row('AGT') == ('2026-09-29', 'bmo', 1, 'agent'), row('AGT'))

# ---------------------------------------------------------------- CLI
fresh()
before = [row(s) for s in ('AAA', 'BEN', 'AGT')]
bad = [
    (['--symbol', 'AAA', '--by', 'agent'], 'bare --symbol'),
    (['--symbol', 'AAA'], 'bare --symbol, no --by'),
    (['--symbol', 'AAA', '--date', '2026-09-30', '--time', 'bmo'], 'confirm without --by'),
    (['--symbol', 'AAA', '--time', 'amc', '--by', 'agent'], 'time without --date or --time-only'),
    (['--symbol', 'AAA', '--time-only', '--by', 'agent'], '--time-only without --time'),
    (['--symbol', 'AAA', '--time-only', '--time', 'amc', '--date', '2026-09-30', '--by', 'agent'],
     '--time-only with --date'),
    (['--list', '--time-only'], '--time-only without --symbol'),
    (['--symbol', 'AAA', '--date', '2026-09-30', '--by', 'claude'], '--by outside choices'),
    (['--bulk-file', CSV], '--bulk-file without --by'),
]
for argv, name in bad:
    code, out = cli(argv)
    check('CLI rejects: ' + name + ' (exit 2)', code == 2, (code, out[-200:]))
check('CLI rejections wrote nothing', [row(s) for s in ('AAA', 'BEN', 'AGT')] == before)

code, out = cli(['--symbol', 'AAA', '--time', 'amc', '--time-only', '--by', 'agent'])
check('CLI --time-only works', code == 0 and row('AAA') == ('2026-09-28', 'amc', 0, None), (code, out))

code, out = cli(['--symbol', 'BEN', '--date', '2026-09-30', '--by', 'agent'])
check('CLI agent over ben row exits 1, row intact',
      code == 1 and row('BEN') == ('2026-09-30', 'bmo', 1, 'ben'), (code, out))

code, out = cli(['--symbol', 'AAA', '--date', '2026-09-30', '--time', 'bmo', '--by', 'agent'])
check('CLI full agent confirm works', code == 0 and row('AAA') == ('2026-09-30', 'bmo', 1, 'agent'), (code, out))

code, out = cli(['--list'])
check('CLI --list still works (no --by needed)', code == 0 and 'AAA' in out, (code, out))

code, out = cli(['--list-unconfirmed', '--days', '400'])
check('CLI --list-unconfirmed still works', code == 0, (code, out))

for p in (SCR, SCR + '-wal', SCR + '-shm', CSV):
    if os.path.exists(p):
        os.remove(p)

print('\n{}/{} passed'.format(sum(results), len(results)))
sys.exit(0 if all(results) else 1)
