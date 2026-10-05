# Confirm a company-sourced date + cache the IR URL + close today's dispute row, in one call.
# Usage (bash, from E:/options_scanner):  source agents/earnings_researcher/analysis/helpers/conf.sh
#                                          conf SYM YYYY-MM-DD bmo|amc 'URL'
# Only for a date read off a company source (see memory/feedback_earnings_confirm_bare_symbol.md).
# Prints the calendar row and the dispute row afterwards; direct_db_query writes print nothing.
# Promoted from inbox/fetch/conf.sh (10-01 session) at the 2026-10-04 maintenance. That copy
# hard-coded trade_date='2026-10-01', so reused on another day it would have updated nothing.
conf() {
  local S=$1 D=$2 T=$3 U=$4
  local TODAY; TODAY=$(date +%F)
  local NOW; NOW=$(date +"%Y-%m-%d %H:%M:%S")
  python tools/earnings_confirm.py --symbol "$S" --date "$D" --time "$T" --by agent
  python tools/direct_db_query.py --db E:/options_scanner/data/datalake.db --write \
    --sql "UPDATE symbol_metadata SET ir_earnings_url='$U', ir_url_last_verified='$TODAY' WHERE symbol='$S'" >/dev/null
  python tools/direct_db_query.py --db E:/options_scanner/data/performance.db --write \
    --sql "UPDATE earnings_date_disputes SET resolution='confirmed_agent', resolved_date='$D', resolved_time='$T', resolved_at='$NOW', research_url='$U' WHERE trade_date='$TODAY' AND symbol='$S'" >/dev/null
  python tools/direct_db_query.py --db E:/options_scanner/data/datalake.db \
    --sql "SELECT symbol, earnings_date, earnings_time, date_confirmed, date_confirmed_by FROM earnings_upcoming WHERE symbol='$S'"
  python tools/direct_db_query.py --db E:/options_scanner/data/performance.db \
    --sql "SELECT trade_date, symbol, resolution, resolved_date FROM earnings_date_disputes WHERE trade_date='$TODAY' AND symbol='$S'"
}
