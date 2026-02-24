#!/bin/bash
# AWIN Affiliate Reporting for Digital Shield Pro
# Fetches commission data from AWIN API
# Usage: ./scripts/awin-report.sh [days_back]
#
# Requires: AWIN API key in partners/partners.xlsx or set AWIN_API_KEY env var

PUBLISHER_ID="2776410"
DAYS_BACK="${1:-30}"

# Try to load API key from environment or prompt
if [ -z "$AWIN_API_KEY" ]; then
    echo "Set AWIN_API_KEY environment variable first:"
    echo "  export AWIN_API_KEY='your-api-key-here'"
    echo ""
    echo "Your API key is in partners/partners.xlsx"
    exit 1
fi

START_DATE=$(date -d "-${DAYS_BACK} days" +%Y-%m-%dT00:00:00 2>/dev/null || date -v-${DAYS_BACK}d +%Y-%m-%dT00:00:00)
END_DATE=$(date +%Y-%m-%dT23:59:59)

echo "========================================="
echo " AWIN Report: Last $DAYS_BACK days"
echo " Period: $START_DATE to $END_DATE"
echo "========================================="
echo ""

# Fetch transactions
echo "--- Transactions ---"
curl -s -H "Authorization: Bearer $AWIN_API_KEY" \
    "https://api.awin.com/publishers/$PUBLISHER_ID/transactions/?startDate=$START_DATE&endDate=$END_DATE&timezone=Europe/Amsterdam" \
    | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    if isinstance(data, list):
        if len(data) == 0:
            print('  No transactions in this period')
        else:
            total_commission = 0
            by_merchant = {}
            for t in data:
                merchant = t.get('advertiserId', 'Unknown')
                commission = float(t.get('commissionAmount', {}).get('amount', 0))
                status = t.get('commissionStatus', 'unknown')
                total_commission += commission
                if merchant not in by_merchant:
                    by_merchant[merchant] = {'count': 0, 'commission': 0}
                by_merchant[merchant]['count'] += 1
                by_merchant[merchant]['commission'] += commission

            merchant_names = {
                '11660': 'Bitdefender',
                '19487': 'Kaspersky',
                '18785': 'ESET',
                '36608': 'Surfshark'
            }

            print(f'  Total transactions: {len(data)}')
            print(f'  Total commission: EUR {total_commission:.2f}')
            print()
            print('  By merchant:')
            for mid, info in by_merchant.items():
                name = merchant_names.get(str(mid), f'Merchant {mid}')
                print(f'    {name}: {info[\"count\"]} transactions, EUR {info[\"commission\"]:.2f}')
    else:
        print(f'  API Response: {json.dumps(data, indent=2)[:500]}')
except Exception as e:
    print(f'  Error parsing response: {e}')
" 2>/dev/null

echo ""

# Fetch account summary
echo "--- Active Programs ---"
curl -s -H "Authorization: Bearer $AWIN_API_KEY" \
    "https://api.awin.com/publishers/$PUBLISHER_ID/programmes/?relationship=joined" \
    | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    if isinstance(data, list):
        for p in data[:20]:
            name = p.get('name', 'Unknown')
            mid = p.get('id', '?')
            status = p.get('status', '?')
            print(f'  [{mid}] {name} - {status}')
    else:
        print(f'  Response: {json.dumps(data, indent=2)[:500]}')
except Exception as e:
    print(f'  Error: {e}')
" 2>/dev/null

echo ""
echo "========================================="
