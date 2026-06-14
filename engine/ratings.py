#!/usr/bin/env python3
"""
שכבת דירוג שחקנים→קבוצה→λ, שמזינה את מנוע הפואסון.
מקבלת אינדקסי התקפה/הגנה (0-100) שנגזרו מדירוגי השחקנים (ראה research/player-rating-system.md)
ומחזירה λ לכל צד, ואז מריצה את מנוע הפואסון לבחירת הניחוש לפי EV.

שימוש:
  python3 engine/ratings.py --home "BRA" --hatt 88 --hdef 80 \\
                            --away "MAR" --aatt 70 --adef 78 --hadv 1.10
"""
import argparse, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from poisson import report  # noqa: E402

BASE = 1.35  # שערים ממוצעים לקבוצה במשחק (מכויל למונדיאל ~2.7 סה"כ)


def lambdas(h_att, h_def, a_att, a_def, hadv=1.10, ctx_h=1.0, ctx_a=1.0):
    # λ = בסיס × עוצמת התקפה שלי × חולשת הגנת היריב × יתרון בית × הקשר
    lh = BASE * (h_att / 50.0) * (50.0 / a_def) * hadv * ctx_h
    la = BASE * (a_att / 50.0) * (50.0 / h_def) * (1.0 / hadv) ** 0.5 * ctx_a
    # קאפ ריאלי
    lh = min(max(lh, 0.2), 3.6)
    la = min(max(la, 0.2), 3.6)
    return round(lh, 2), round(la, 2)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--home", default="HOME"); p.add_argument("--away", default="AWAY")
    p.add_argument("--hatt", type=float, required=True); p.add_argument("--hdef", type=float, required=True)
    p.add_argument("--aatt", type=float, required=True); p.add_argument("--adef", type=float, required=True)
    p.add_argument("--hadv", type=float, default=1.10)
    p.add_argument("--ctxh", type=float, default=1.0); p.add_argument("--ctxa", type=float, default=1.0)
    a = p.parse_args()
    lh, la = lambdas(a.hatt, a.hdef, a.aatt, a.adef, a.hadv, a.ctxh, a.ctxa)
    print(f"{a.home}: התקפה {a.hatt} / הגנה {a.hdef}  |  {a.away}: התקפה {a.aatt} / הגנה {a.adef}")
    print(f"→ λ: {a.home} {lh} / {a.away} {la}\n")
    print(report(lh, la))
