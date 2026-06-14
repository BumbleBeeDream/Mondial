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


def coach_mult(quality=1.0, style=0.0):
    """מקדמי מאמן מובנים (במקום הזזה ידנית של אינדקסים):
    quality: 0.90 (חלש/חדש מאוד) .. 1.00 (ממוצע) .. 1.10 (עילית) — כמה מוציא מהסגל.
    style:  -1 הגנתי .. 0 מאוזן .. +1 התקפי — מזיז xG בין התקפה (לי) להגנה (יריב).
    מחזיר (att_mult, def_solidity) — att_mult על ה-xG שלי, def_solidity מוריד xG ליריב.
    """
    att_mult = quality * (1.0 + 0.12 * style)      # התקפי מעלה את ה-xG שלי
    def_solidity = quality * (1.0 - 0.12 * style)  # הגנתי (style<0) מחזק בלימה → יריב כובש פחות
    return att_mult, def_solidity


def lambdas(h_att, h_def, a_att, a_def, hadv=1.10, ctx_h=1.0, ctx_a=1.0,
            h_cq=1.0, h_cs=0.0, a_cq=1.0, a_cs=0.0):
    # מקדמי מאמן לכל צד
    h_am, h_ds = coach_mult(h_cq, h_cs)
    a_am, a_ds = coach_mult(a_cq, a_cs)
    # λ = בסיס × התקפה שלי×מאמן-התקפה × חולשת הגנת היריב×בלימת-מאמן-היריב × בית × הקשר
    lh = BASE * (h_att / 50.0) * h_am * (50.0 / a_def) / a_ds * hadv * ctx_h
    la = BASE * (a_att / 50.0) * a_am * (50.0 / h_def) / h_ds * (1.0 / hadv) ** 0.5 * ctx_a
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
    # מאמנים: cq=איכות (0.9-1.1), cs=סגנון (-1 הגנתי .. +1 התקפי)
    p.add_argument("--hcq", type=float, default=1.0); p.add_argument("--hcs", type=float, default=0.0)
    p.add_argument("--acq", type=float, default=1.0); p.add_argument("--acs", type=float, default=0.0)
    a = p.parse_args()
    lh, la = lambdas(a.hatt, a.hdef, a.aatt, a.adef, a.hadv, a.ctxh, a.ctxa,
                     a.hcq, a.hcs, a.acq, a.acs)
    print(f"{a.home}: התקפה {a.hatt} / הגנה {a.hdef} · מאמן(איכות {a.hcq}, סגנון {a.hcs})")
    print(f"{a.away}: התקפה {a.aatt} / הגנה {a.adef} · מאמן(איכות {a.acq}, סגנון {a.acs})")
    print(f"→ λ: {a.home} {lh} / {a.away} {la}\n")
    print(report(lh, la, home=a.home, away=a.away))
