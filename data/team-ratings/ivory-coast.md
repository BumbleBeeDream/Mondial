# חוף השנהב — דוסייה מלא (bottom-up)

אינדקסים: התקפה 58 · הגנה 53 · מאמן cq1.02 cs0.0 · עדכון: 16.6.26

> אלופת אפריקה 2024 (AFCON) · חזרה למונדיאל אחרי 12 שנה · הסגל היקר ביותר באפריקה (~€515M) · Group E
> מסומן ★ = הרכב פותח צפוי (4-3-3 / 4-2-3-1). שווי = Transfermarkt; OVR = EA FC26; כושר = פורם אחרון.
> *הערה: cq/cs לא הופיעו בבסיס הקודם — נגזרו כעת באופן עקבי (מאמן מאוזן, אלוף אפריקה) ומסומנים כתוספת.*

## סגל מלא (26)

### שוערים
| # | שחקן | עמדה | מועדון | גיל | EA FC OVR | שווי TM | כושר אחרון | PlayerScore |
|---|------|------|--------|-----|-----------|---------|------------|-------------|
| ★ | Yahia Fofana | GK | Angers | 25 | 76 | €10M | 6.9 (#1, clean sheet MD1) | 65 |
|  | Mohamed Koné | GK | (ליגה צרפתית) | 26 | 70 | €2M | 6.6 | 52 |
|  | Alban Lafont | GK | Nantes | 27 | 77 | €8M | 6.8 | 64 |

### הגנה
| # | שחקן | עמדה | מועדון | גיל | EA FC OVR | שווי TM | כושר אחרון | PlayerScore |
|---|------|------|--------|-----|-----------|---------|------------|-------------|
| ★ | Wilfried Singo | RB/CB | Galatasaray | 25 | 81 | €40M | 7.4 (ביש' שער הניצחון MD1) | 78 |
| ★ | Odilon Kossounou | CB | Atalanta | 25 | 80 | €30M | 7.1 | 75 |
| ★ | Evan Ndicka | CB | AS Roma | 26 | 81 | €35M | 7.2 | 77 |
| ★ | Ghislain Konan | LB | (ליגה צרפתית/ערב) | 30 | 75 | €4M | 6.9 | 62 |
|  | Ousmane Diomandé | CB | Sporting CP | 22 | 80 | €45M | 7.1 | 76 |
|  | Emmanuel Agbadou | CB | Wolverhampton | 28 | 78 | €22M | 7.0 | 71 |
|  | Guéla Doué | RB | Strasbourg | 23 | 76 | €18M | 7.0 | 68 |
|  | Christopher Operi | LB | (ליגה צרפתית) | 28 | 73 | €5M | 6.7 | 58 |

### קישור
| # | שחקן | עמדה | מועדון | גיל | EA FC OVR | שווי TM | כושר אחרון | PlayerScore |
|---|------|------|--------|-----|-----------|---------|------------|-------------|
| ★ | Franck Kessié (c) | CM/DM | Al-Ahli (KSA) | 29 | 82 | €25M | 7.2 (קפטן, 100+ קאפים) | 76 |
| ★ | Ibrahim Sangaré | DM | Nottingham Forest | 28 | 80 | €30M | 7.1 | 74 |
| ★ | Seko Fofana | CM | Rennes | 30 | 79 | €18M | 7.0 | 70 |
|  | Jean-Michaël Seri | CM | (ותיק) | 34 | 75 | €3M | 6.8 | 58 |
|  | Christ Inao Oulaï | DM | (צעיר) | 19 | 72 | €12M | 6.8 | 62 |
|  | Parfait Guiagon | CM/W | (צעיר) | 21 | 71 | €6M | 6.7 | 57 |

### התקפה
| # | שחקן | עמדה | מועדון | גיל | EA FC OVR | שווי TM | כושר אחרון | PlayerScore |
|---|------|------|--------|-----|-----------|---------|------------|-------------|
| ★ | Simon Adingra | LW/RW | Monaco | 24 | 79 | €35M | 7.1 | 74 |
| ★ | Evann Guessand | ST/W | Crystal Palace | 24 | 78 | €30M | 7.1 | 72 |
| ★ | Amad Diallo | RW | Manchester United | 23 | 80 | €45M | 7.6 (שער ניצחון 90' MD1) | 79 |
|  | Nicolas Pépé | RW | Villarreal | 30 | 77 | €12M | 6.9 | 66 |
|  | Ange-Yoan Bonny | ST | Inter Milan | 22 | 77 | €28M | 7.0 (זימון ראשון, אישור FIFA) | 70 |
|  | Elye Wahi | ST | (ליגה צרפתית) | 23 | 77 | €25M | 6.9 (פגע במשקוף MD1) | 69 |
|  | Yan Diomande | W | RB Leipzig | 20 | 74 | €18M | 6.9 | 65 |
|  | Oumar Diakité | ST | Reims | 22 | 73 | €10M | 6.7 | 61 |
|  | Bazoumana Touré | W | Hoffenheim | 21 | 73 | €12M | 6.8 | 62 |

> **תיקון לבסיס הקודם: Sébastien Haller לא נכלל בסגל הסופי** (הודח, הפתעה). Amad Diallo (Man Utd) הנכס ההתקפי המרכזי; Bonny (Inter) זימון ראשון. *גיל/OVR/שווי לשחקני-עומק = הערכה מצולבת.*

## קווים וחישוב אינדקסים
- **GK 50** (Fofana/Lafont — רמת ליגה צרפתית סבירה, לא עילית)
- **DEF 54** (Ndicka/Kossounou/Diomandé/Singo — איתנה, פיזית, איכות אטלנטה/רומא)
- **MID 58** (Kessié+Sangaré+S.Fofana — חזק, מנוסה, פיזי)
- **ATT 58** (Amad+Adingra+Guessand+Pépé/Wahi/Bonny — מגוון, מהיר, עומק טוב)

**אינדקס התקפה** = 0.6×58 + 0.4×58 = 34.8 + 23.2 = **58.0 → 58** ✓
**אינדקס הגנה** = 0.55×54 + 0.30×50 + 0.15×58 = 29.7 + 15.0 + 8.7 = **53.4 → 53** ✓
(תואם לבסיס הקיים — ללא שינוי.)

## מאמן — Emerse Faé
- **cq 1.02** — צעיר אך מנצח: הוביל את חוף השנהב לזכייה ב-AFCON 2024 בנסיבות דרמטיות. כריזמה, ניהול קבוצה.
- **cs 0.0** — מאוזן (לא הגנתי ולא לחיצה קיצונית); גמיש בין 4-3-3 ל-4-2-3-1, פרגמטי. ב-MD1 נצחון 1-0 מאופק עם clean sheet.

## קבועות / פנדלים / קרנות
- **פנדלים:** Kessié (בעיטות-עומק ותיק), Amad/Pépé אופציות.
- **קרנות / חופשיות:** Seri/Kessié מבצעים; איום ראש: Ndicka, Kossounou, Guessand, Wahi.

## פציעות + קנס-מחליף
- **אין פציעות/השעיות ידועות** לקראת MD2.
- Haller מחוץ לסגל (החלטת מאמן, לא פציעה) — עומק חוד עדיין טוב (Guessand/Wahi/Bonny) → קנס-מחליף קטן.
- Amad Diallo עלה מהספסל וכבש ב-90' ב-MD1 — סימן עומק התקפי איכותי.

## כושר + MD1
- **MD1: חוף השנהב 1-0 אקוודור (Philadelphia, 15.6).** שער: **Amad Diallo 90'** (סייד-פוט אחרי ריצה+בישול של Singo).
- ניצחון זה **סיים רצף של 19-20 משחקים ללא הפסד של אקוודור.** Yeboah/Minda/Wahi פגעו במשקוף. clean sheet יקר.
- מצב Group E אחרי MD1: גרמניה 3 נק' (+6), **חוף השנהב 3 נק' (+1)**, אקוודור 0, קוראסאו 0. פתיחה אידיאלית.
- הרכב צפוי MD2 (נגד גרמניה, 20.6 טורונטו): Y.Fofana; Singo, Kossounou, Ndicka, Konan; Kessié, Sangaré, S.Fofana; Adingra, Guessand, Amad. צפוי בלוק קומפקטי + קאונטר מול גרמניה.

## מקורות (16.6.26)
1. Outlook India / Opta Analyst — Ivory Coast 1-0 Ecuador match report & stats
2. Sky Sports — Amad Diallo 90' winner ends Ecuador unbeaten run (skysports.com)
3. Goal.com — Ivory Coast WC2026 squad (who's in / who's out, Haller)
4. FIFA — Côte d'Ivoire squad announcement (Faé) (fifa.com)
5. EA SPORTS FC 26 + Transfermarkt — OVR & values (ea.com, transfermarkt)
> מקורות מפורטים (FourFourTwo, squawka, soccergraph) החזירו 403. גיל/OVR/שווי לשחקני-עומק הם **הערכה** מצולבת; ליבת ה-XI ושער ה-MD1 מאומתים.
