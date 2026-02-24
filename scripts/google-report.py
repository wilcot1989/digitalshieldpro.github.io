#!/usr/bin/env python3
"""
Digital Shield Pro — Google Analytics & Search Console Report
Usage:
  python3 scripts/google-report.py              # Last 7 days
  python3 scripts/google-report.py --days 30    # Last 30 days
  python3 scripts/google-report.py --days 7 --save   # Save to reports/
"""

import os
import sys
import argparse
from datetime import datetime, timedelta

# --- Config ---
CREDENTIALS = os.path.join(os.path.dirname(__file__), "..", "google", "digital-shield-pro-efc885dda41f.json")
GA4_PROPERTY_ID = "525730353"
SC_SITE_URL = "sc-domain:digitalshieldpro.com"
SITE_BASE = "https://digitalshieldpro.com"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath(CREDENTIALS)

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric, OrderBy
from google.oauth2 import service_account
from googleapiclient.discovery import build


def ga4_client():
    return BetaAnalyticsDataClient()


def sc_client():
    creds = service_account.Credentials.from_service_account_file(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"],
        scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
    )
    return build("searchconsole", "v1", credentials=creds)


def ga4_report(client, start, end):
    prop = f"properties/{GA4_PROPERTY_ID}"
    lines = []

    # --- Overview ---
    req = RunReportRequest(
        property=prop,
        date_ranges=[DateRange(start_date=start, end_date=end)],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="sessions"),
            Metric(name="screenPageViews"),
            Metric(name="averageSessionDuration"),
            Metric(name="bounceRate"),
        ],
    )
    resp = client.run_report(req)
    if resp.totals:
        t = resp.totals[0].metric_values
        users, sessions, views = t[0].value, t[1].value, t[2].value
        avg_dur = float(t[3].value) if t[3].value else 0
        bounce = float(t[4].value) * 100 if t[4].value else 0
        lines.append("## GA4 Overview")
        lines.append(f"  Users:            {users}")
        lines.append(f"  Sessions:         {sessions}")
        lines.append(f"  Pageviews:        {views}")
        lines.append(f"  Avg duration:     {avg_dur:.0f}s")
        lines.append(f"  Bounce rate:      {bounce:.1f}%")
    else:
        lines.append("## GA4 Overview\n  No data yet")

    # --- Top Pages ---
    req = RunReportRequest(
        property=prop,
        date_ranges=[DateRange(start_date=start, end_date=end)],
        dimensions=[Dimension(name="pagePath")],
        metrics=[Metric(name="screenPageViews"), Metric(name="activeUsers")],
        order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="screenPageViews"), desc=True)],
        limit=20,
    )
    resp = client.run_report(req)
    lines.append("\n## Top Pages (GA4)")
    lines.append(f"  {'Page':<55} {'Views':>6} {'Users':>6}")
    lines.append(f"  {'-'*69}")
    for row in resp.rows:
        page = row.dimension_values[0].value
        views = row.metric_values[0].value
        users = row.metric_values[1].value
        lines.append(f"  {page:<55} {views:>6} {users:>6}")
    if not resp.rows:
        lines.append("  No data yet")

    # --- Traffic Sources ---
    req = RunReportRequest(
        property=prop,
        date_ranges=[DateRange(start_date=start, end_date=end)],
        dimensions=[Dimension(name="sessionSource"), Dimension(name="sessionMedium")],
        metrics=[Metric(name="sessions"), Metric(name="activeUsers")],
        order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
        limit=15,
    )
    resp = client.run_report(req)
    lines.append("\n## Traffic Sources")
    lines.append(f"  {'Source':<30} {'Medium':<15} {'Sessions':>8} {'Users':>6}")
    lines.append(f"  {'-'*63}")
    for row in resp.rows:
        src = row.dimension_values[0].value
        med = row.dimension_values[1].value
        sess = row.metric_values[0].value
        users = row.metric_values[1].value
        lines.append(f"  {src:<30} {med:<15} {sess:>8} {users:>6}")
    if not resp.rows:
        lines.append("  No data yet")

    # --- Devices ---
    req = RunReportRequest(
        property=prop,
        date_ranges=[DateRange(start_date=start, end_date=end)],
        dimensions=[Dimension(name="deviceCategory")],
        metrics=[Metric(name="sessions"), Metric(name="activeUsers")],
        order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
    )
    resp = client.run_report(req)
    lines.append("\n## Devices")
    for row in resp.rows:
        dev = row.dimension_values[0].value
        sess = row.metric_values[0].value
        users = row.metric_values[1].value
        lines.append(f"  {dev:<20} {sess:>6} sessions, {users:>4} users")

    # --- Countries ---
    req = RunReportRequest(
        property=prop,
        date_ranges=[DateRange(start_date=start, end_date=end)],
        dimensions=[Dimension(name="country")],
        metrics=[Metric(name="sessions"), Metric(name="activeUsers")],
        order_bys=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name="sessions"), desc=True)],
        limit=10,
    )
    resp = client.run_report(req)
    lines.append("\n## Countries")
    for row in resp.rows:
        country = row.dimension_values[0].value or "(not set)"
        sess = row.metric_values[0].value
        users = row.metric_values[1].value
        lines.append(f"  {country:<25} {sess:>6} sessions, {users:>4} users")

    return "\n".join(lines)


def sc_report(service, start, end):
    lines = []

    # --- Top Queries ---
    resp = service.searchanalytics().query(
        siteUrl=SC_SITE_URL,
        body={"startDate": start, "endDate": end, "dimensions": ["query"], "rowLimit": 25},
    ).execute()

    lines.append("## Top Search Queries")
    lines.append(f"  {'Query':<45} {'Clicks':>7} {'Impr':>7} {'CTR':>7} {'Pos':>6}")
    lines.append(f"  {'-'*74}")
    for row in resp.get("rows", []):
        q = row["keys"][0]
        c = row.get("clicks", 0)
        i = row.get("impressions", 0)
        ctr = row.get("ctr", 0) * 100
        pos = row.get("position", 0)
        lines.append(f"  {q:<45} {c:>7} {i:>7} {ctr:>6.1f}% {pos:>5.1f}")
    if not resp.get("rows"):
        lines.append("  No search data yet")

    # --- Top Pages ---
    resp = service.searchanalytics().query(
        siteUrl=SC_SITE_URL,
        body={"startDate": start, "endDate": end, "dimensions": ["page"], "rowLimit": 25},
    ).execute()

    lines.append("\n## Top Pages in Google Search")
    lines.append(f"  {'Page':<55} {'Clicks':>7} {'Impr':>7} {'Pos':>6}")
    lines.append(f"  {'-'*77}")
    for row in resp.get("rows", []):
        p = row["keys"][0].replace(SITE_BASE, "") or "/"
        c = row.get("clicks", 0)
        i = row.get("impressions", 0)
        pos = row.get("position", 0)
        lines.append(f"  {p:<55} {c:>7} {i:>7} {pos:>5.1f}")
    if not resp.get("rows"):
        lines.append("  No page data yet")

    # --- Devices ---
    resp = service.searchanalytics().query(
        siteUrl=SC_SITE_URL,
        body={"startDate": start, "endDate": end, "dimensions": ["device"], "rowLimit": 10},
    ).execute()

    lines.append("\n## Search by Device")
    for row in resp.get("rows", []):
        dev = row["keys"][0]
        c = row.get("clicks", 0)
        i = row.get("impressions", 0)
        pos = row.get("position", 0)
        lines.append(f"  {dev:<15} {c:>5} clicks, {i:>6} impressions, pos {pos:.1f}")

    # --- Countries ---
    resp = service.searchanalytics().query(
        siteUrl=SC_SITE_URL,
        body={"startDate": start, "endDate": end, "dimensions": ["country"], "rowLimit": 10},
    ).execute()

    lines.append("\n## Search by Country")
    for row in resp.get("rows", []):
        country = row["keys"][0]
        c = row.get("clicks", 0)
        i = row.get("impressions", 0)
        pos = row.get("position", 0)
        lines.append(f"  {country:<15} {c:>5} clicks, {i:>6} impressions, pos {pos:.1f}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Digital Shield Pro Report")
    parser.add_argument("--days", type=int, default=7, help="Number of days to report (default: 7)")
    parser.add_argument("--save", action="store_true", help="Save report to reports/ directory")
    args = parser.parse_args()

    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=args.days)).strftime("%Y-%m-%d")

    header = []
    header.append("=" * 70)
    header.append(f"  DIGITAL SHIELD PRO — Performance Report")
    header.append(f"  Period: {start_date} to {end_date} ({args.days} days)")
    header.append(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    header.append("=" * 70)

    report_parts = ["\n".join(header)]

    # GA4
    print("Fetching GA4 data...")
    try:
        ga4 = ga4_client()
        report_parts.append("\n" + ga4_report(ga4, start_date, end_date))
    except Exception as e:
        report_parts.append(f"\n## GA4 Error: {e}")

    # Search Console
    print("Fetching Search Console data...")
    try:
        sc = sc_client()
        report_parts.append("\n" + sc_report(sc, start_date, end_date))
    except Exception as e:
        report_parts.append(f"\n## Search Console Error: {e}")

    report = "\n".join(report_parts)
    print("\n" + report)

    if args.save:
        reports_dir = os.path.join(os.path.dirname(__file__), "..", "reports")
        os.makedirs(reports_dir, exist_ok=True)
        filename = f"report-{end_date}.txt"
        filepath = os.path.join(reports_dir, filename)
        with open(filepath, "w") as f:
            f.write(report)
        print(f"\nSaved to {filepath}")


if __name__ == "__main__":
    main()
