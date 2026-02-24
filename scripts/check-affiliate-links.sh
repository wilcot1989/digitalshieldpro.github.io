#!/bin/bash
# Affiliate Link Validator for Digital Shield Pro
# Checks all affiliate links across the site for validity
# Usage: ./scripts/check-affiliate-links.sh

CONTENT_DIR="content/posts"
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "========================================="
echo " Digital Shield Pro - Link Validator"
echo "========================================="
echo ""

# Load AWIN API key if available
AWIN_API_KEY=""
if [ -f "partners/partners.xlsx" ]; then
    echo "[INFO] Partners file found"
fi

TOTAL=0
OK=0
FAIL=0
WARN=0

check_url() {
    local url="$1"
    local file="$2"
    local label="$3"
    TOTAL=$((TOTAL + 1))

    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 10 "$url" 2>/dev/null)

    if [ "$HTTP_CODE" -ge 200 ] && [ "$HTTP_CODE" -lt 400 ]; then
        echo -e "  ${GREEN}[OK]${NC} $label ($HTTP_CODE)"
        OK=$((OK + 1))
    elif [ "$HTTP_CODE" -eq 0 ]; then
        echo -e "  ${YELLOW}[TIMEOUT]${NC} $label"
        WARN=$((WARN + 1))
    else
        echo -e "  ${RED}[FAIL]${NC} $label ($HTTP_CODE) - $url"
        FAIL=$((FAIL + 1))
    fi
}

echo "Scanning affiliate links..."
echo ""

# NordVPN links
echo "--- NordVPN ---"
NORDVPN_LINKS=$(grep -r "go.nordvpn.net" $CONTENT_DIR --include="*.md" -l 2>/dev/null)
NORDVPN_COUNT=$(echo "$NORDVPN_LINKS" | grep -c . 2>/dev/null)
echo "  Found in $NORDVPN_COUNT files"
check_url "https://go.nordvpn.net/aff_c?offer_id=612&aff_id=141337&url_id=14830" "" "NordVPN affiliate link"
echo ""

# NordPass links
echo "--- NordPass ---"
NORDPASS_LINKS=$(grep -r "go.nordpass.io" $CONTENT_DIR --include="*.md" -l 2>/dev/null)
NORDPASS_COUNT=$(echo "$NORDPASS_LINKS" | grep -c . 2>/dev/null)
echo "  Found in $NORDPASS_COUNT files"
check_url "https://go.nordpass.io/aff_c?offer_id=488&aff_id=141337&url_id=9356" "" "NordPass affiliate link"
echo ""

# AWIN links
echo "--- AWIN (Bitdefender) ---"
BD_COUNT=$(grep -r "mid=11660" $CONTENT_DIR --include="*.md" -c 2>/dev/null | awk -F: '{s+=$2}END{print s}')
echo "  Found $BD_COUNT links"
check_url "https://www.awin1.com/awclick.php?mid=11660&id=2776410" "" "Bitdefender AWIN link"
echo ""

echo "--- AWIN (Kaspersky) ---"
KS_COUNT=$(grep -r "mid=19487" $CONTENT_DIR --include="*.md" -c 2>/dev/null | awk -F: '{s+=$2}END{print s}')
echo "  Found $KS_COUNT links"
check_url "https://www.awin1.com/awclick.php?mid=19487&id=2776410" "" "Kaspersky AWIN link"
echo ""

echo "--- AWIN (ESET) ---"
ESET_COUNT=$(grep -r "mid=18785" $CONTENT_DIR --include="*.md" -c 2>/dev/null | awk -F: '{s+=$2}END{print s}')
echo "  Found $ESET_COUNT links"
check_url "https://www.awin1.com/awclick.php?mid=18785&id=2776410" "" "ESET AWIN link"
echo ""

echo "--- AWIN (Surfshark) ---"
SS_COUNT=$(grep -r "mid=36608" $CONTENT_DIR --include="*.md" -c 2>/dev/null | awk -F: '{s+=$2}END{print s}')
echo "  Found $SS_COUNT links"
check_url "https://www.awin1.com/awclick.php?mid=36608&id=2776410" "" "Surfshark AWIN link"
echo ""

# Check for untracked bare domain links (potential revenue loss)
echo "--- Revenue Loss Check ---"
echo "  Scanning for bare domain links without affiliate tracking..."
BARE_LINKS=0

for domain in "norton.com" "expressvpn.com" "1password.com" "dashlane.com" "malwarebytes.com" "trendmicro.com"; do
    COUNT=$(grep -r "href=\"https://$domain\"" $CONTENT_DIR --include="*.md" -c 2>/dev/null | awk -F: '{s+=$2}END{print s}')
    COUNT=${COUNT:-0}
    if [ "$COUNT" -gt 0 ]; then
        echo -e "  ${YELLOW}[WARN]${NC} $domain: $COUNT bare links (no affiliate tracking)"
        BARE_LINKS=$((BARE_LINKS + COUNT))
    fi
done

for domain in "www.norton.com" "www.malwarebytes.com" "www.trendmicro.com"; do
    COUNT=$(grep -r "href=\"https://$domain\"" $CONTENT_DIR --include="*.md" -c 2>/dev/null | awk -F: '{s+=$2}END{print s}')
    COUNT=${COUNT:-0}
    if [ "$COUNT" -gt 0 ]; then
        echo -e "  ${YELLOW}[WARN]${NC} $domain: $COUNT bare links (no affiliate tracking)"
        BARE_LINKS=$((BARE_LINKS + COUNT))
    fi
done

if [ "$BARE_LINKS" -eq 0 ]; then
    echo -e "  ${GREEN}[OK]${NC} No bare domain links found for major affiliate programs"
fi

echo ""
echo "========================================="
echo " Results: $OK OK / $FAIL Failed / $WARN Warnings"
echo " Untracked bare links: $BARE_LINKS"
echo "========================================="
