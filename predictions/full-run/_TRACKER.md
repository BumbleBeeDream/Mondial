# ריצה מלאה — כל יתרת המונדיאל (החל 16.6.2026) · bottom-up

> מטרה: לכל משחק שנותר עד הגמר (19.7): (1) **בניית מסד דירוג bottom-up** (שחקן-שחקן, 5 מקורות) →
> `data/team-ratings/`, (2) λ דרך `engine/ratings.py` → `poisson.py`, (3) ראשי + 🃏 ג'וקר, (4) רענון ביום המשחק.
> בועז (כניסה יחידה). ברקט נעול: 🇫🇷 צרפת אלופה.

## סוכני שלב הבתים (10, רצים ברקע)
| סוכן | בתים | מסמכי דירוג לבנות | משחקים | קובץ | סטטוס |
|------|------|------|:--:|------|------|
| A | A | mexico, south-korea, south-africa, czechia | MD2+MD3 (4) | group-A.md | ⏳ |
| B | B | canada, switzerland, qatar, bosnia | MD2+MD3 (4) | group-B.md | ⏳ |
| C | C | brazil, morocco | MD2+MD3 (4) | group-C.md | ⏳ |
| D | D | usa, paraguay | MD2+MD3 (4) | group-D.md | ⏳ |
| E | E | germany, curacao | MD2+MD3 (4) | group-E.md | ⏳ |
| F | F | netherlands, sweden, tunisia, japan | MD2+MD3 (4) | group-F.md | ⏳ |
| GH | G+H | — (קיימים) | MD2+MD3 (8) | group-GH.md | ⏳ |
| IJ | I+J | — (קיימים) | MD2+MD3 (8) | group-IJ.md | ⏳ |
| K | K (בית המוות) | portugal, congo, uzbekistan, colombia | **MD1(17.6)**+MD2+MD3 (6) | group-K.md | ⏳ |
| L | L | england, croatia, ghana, panama | **MD1(17.6)**+MD2+MD3 (6) | group-L.md | ⏳ |

## אחרי הבתים
- **סוכן נוקאאוט (KO):** R32→גמר לפי הברקט הנעול + מנצחי-בתים מוקרנים מהדיגסטים. יושק כשהבתים יסתיימו.

## רענון ביום המשחק (לפי player-rating-system.md)
- **בסיס:** המסמכים שנבנים עכשיו (חד-פעמי).
- **רענון 24ש' (07:00):** כושר אחרון + פציעות → עדכון אינדקסים.
- **רענון 1ש' (לפני בעיטה):** הרכב פותח סופי → אם משנה תוצאה = התראה.
- MD3 = תלוי-טבלה → כל תחזיות MD3 מסומנות "⚠️ רענן אחרי MD2".
