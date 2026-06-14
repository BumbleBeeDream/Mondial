#!/usr/bin/env python3
"""
מנוע Poisson + Dixon-Coles לתחזיות מונדיאל (Mondial).
קלט: xG ביתית, xG אורחת (מתוך מודיפיקטורי METHOD), ו-rho אופציונלי.
פלט: P(נצחון בית/תיקו/נצחון חוץ), התוצאות הסבירות, וה-ניחוש שממקסם EV
לפי טבלת הניקוד של הליגה: תוצאה מדויקת=3, מנצח+הפרש=2, מנצח בלבד=1, מנצח שגוי=0.

שימוש:  python3 engine/poisson.py <xg_home> <xg_away> [rho]
דוגמה:  python3 engine/poisson.py 1.2 0.8
"""
import sys, math


def pois(k, lam):
    return math.exp(-lam) * lam ** k / math.factorial(k)


def dc_tau(i, j, lh, la, rho):
    # תיקון Dixon-Coles לתאים נמוכים (כדורגל אמיתי: יותר 0-0/1-1, פחות 1-0/0-1)
    if i == 0 and j == 0:
        return 1 - lh * la * rho
    if i == 0 and j == 1:
        return 1 + lh * rho
    if i == 1 and j == 0:
        return 1 + la * rho
    if i == 1 and j == 1:
        return 1 - rho
    return 1.0


def matrix(lh, la, rho=-0.12, maxg=8):
    M, tot = {}, 0.0
    for i in range(maxg + 1):
        for j in range(maxg + 1):
            p = max(pois(i, lh) * pois(j, la) * dc_tau(i, j, lh, la, rho), 0.0)
            M[(i, j)] = p
            tot += p
    return {k: v / tot for k, v in M.items()}


def wdl(M):
    h = sum(p for (i, j), p in M.items() if i > j)
    d = sum(p for (i, j), p in M.items() if i == j)
    a = sum(p for (i, j), p in M.items() if i < j)
    return h, d, a


def points(pred, act):
    pi, pj = pred
    ai, aj = act
    if pi == ai and pj == aj:
        return 3
    ro = (pi > pj) - (pi < pj)
    ra = (ai > aj) - (ai < aj)
    if ro != ra:
        return 0                      # מנצח שגוי (כולל תיקו מול הכרעה)
    if (pi - pj) == (ai - aj):
        return 2                      # מנצח + הפרש נכון
    return 1                          # מנצח בלבד


def ev(pred, M):
    return sum(p * points(pred, act) for act, p in M.items())


def report(lh, la, rho=-0.12, home="בית", away="חוץ"):
    M = matrix(lh, la, rho)
    h, d, a = wdl(M)
    cands = [(i, j) for i in range(6) for j in range(6)]
    best = sorted(((ev(c, M), c) for c in cands), reverse=True)
    bi, bj = best[0][1]
    btext = "תיקו" if bi == bj else (home if bi > bj else away)
    out = [f"xG: בית {lh} / חוץ {la}  (rho={rho})",
           "",
           "🎲 הסתברות לתרחיש (3 הדרכים):",
           f"   נצחון {home}: {h:.0%}  ·  תיקו: {d:.0%}  ·  נצחון {away}: {a:.0%}",
           "📊 התוצאות הסבירות (אחוז):"]
    for (i, j), p in sorted(M.items(), key=lambda x: -x[1])[:6]:
        out.append(f"   {i}-{j}: {p:.0%}")
    out.append("🎯 EV לפי ניקוד הליגה (3/2/1/0):")
    for e, (i, j) in best[:5]:
        out.append(f"   {i}-{j}: EV={e:.2f}")
    out.append(f"➡️ ניחוש אופטימלי: {bi}-{bj} ({btext}, EV={best[0][0]:.2f}, סיכוי-מדויק {M[(bi,bj)]:.0%})")
    return "\n".join(out)


if __name__ == "__main__":
    lh, la = float(sys.argv[1]), float(sys.argv[2])
    rho = float(sys.argv[3]) if len(sys.argv) > 3 else -0.12
    print(report(lh, la, rho))
