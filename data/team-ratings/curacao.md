# קוראסאו — דוסייה מלא (bottom-up)

אינדקסים: התקפה 37 · הגנה 38 · מאמן cq0.95 cs−0.5 · עדכון: 16.6.26

> S5 (החלשה בטורניר) · **האומה הקטנה ביותר אי-פעם שהעפילה** (~156K תושבים) · סגל ~€25.8M (הזול בטורניר) · בכורה היסטורית · Group E
> סגל קומפקטי — רוב השחקנים מליגות הולנדיות/נמוכות-בינוניות. מסומן ★ = הרכב פותח צפוי (4-2-3-1 / בלוק נמוך).

## סגל מלא (26)

### שוערים
| # | שחקן | עמדה | מועדון | גיל | EA FC OVR | שווי TM | כושר אחרון | PlayerScore |
|---|------|------|--------|-----|-----------|---------|------------|-------------|
| ★ | Eloy Room | GK | Miami FC | 36 | 68 | €0.3M | 6.7 (ותיק, #1) | 48 |
|  | Tyrick Bodak | GK | Telstar | 24 | 62 | €0.2M | 6.4 | 42 |
|  | Trevor Doornbusch | GK | VVV-Venlo | 27 | 62 | €0.2M | 6.4 | 42 |

### הגנה
| # | שחקן | עמדה | מועדון | גיל | EA FC OVR | שווי TM | כושר אחרון | PlayerScore |
|---|------|------|--------|-----|-----------|---------|------------|-------------|
| ★ | Sherel Floranus | RB | PEC Zwolle | 27 | 67 | €1.5M | 6.6 | 47 |
| ★ | Juriën Gaari | CB | Abha (KSA) | 28 | 66 | €0.8M | 6.5 | 45 |
| ★ | Armando Obispo | CB | PSV Eindhoven | 26 | 72 | €6M | 6.9 (האיכותי בהגנה) | 56 |
| ★ | Deveron Fonville | LB | NEC Nijmegen | 25 | 66 | €1M | 6.5 | 45 |
|  | Riechedly Bazoer | CB/DM | Konyaspor | 29 | 71 | €2M | 6.7 (רב-תכליתי) | 52 |
|  | Shurandy Sambo | RB | Sparta Rotterdam | 24 | 67 | €1.5M | 6.6 | 47 |
|  | Roshon van Eijma | CB | RKC Waalwijk | 26 | 65 | €0.8M | 6.5 | 44 |
|  | Joshua Brenet | RB/LB | Kayserispor | 31 | 68 | €1M | 6.6 | 46 |

### קישור
| # | שחקן | עמדה | מועדון | גיל | EA FC OVR | שווי TM | כושר אחרון | PlayerScore |
|---|------|------|--------|-----|-----------|---------|------------|-------------|
| ★ | Leandro Bacuna (c) | DM/CM | Iğdır FK (TUR) | 34 | 69 | €0.4M | 6.6 (קפטן) | 46 |
| ★ | Livano Comenencia | CM/AM | FC Zürich | 22 | 68 | €0.7M | 7.0 (שער היסטורי MD1) | 51 |
|  | Juninho Bacuna | CM | FC Volendam | 28 | 70 | €1.5M | 6.8 (3 שערים בהעפלה) | 51 |
|  | Godfried Roemeratoe | CM | RKC Waalwijk | 30 | 64 | €0.5M | 6.4 | 42 |
|  | Tyrese Noslin | CM/W | Telstar | 24 | 63 | €0.4M | 6.4 | 41 |
|  | Kevin Felida | CM | FC Den Bosch | 25 | 62 | €0.3M | 6.3 | 40 |

### התקפה
| # | שחקן | עמדה | מועדון | גיל | EA FC OVR | שווי TM | כושר אחרון | PlayerScore |
|---|------|------|--------|-----|-----------|---------|------------|-------------|
| ★ | Tahith Chong | RW/LW | Sheffield United | 26 | 72 | €4.4M | 6.9 (הנשק ההתקפי הראשי) | 57 |
| ★ | Jurgen Locadia | ST | (חוד מנוסה) | 32 | 69 | €1M | 6.6 | 47 |
|  | Jearl Margaritha | W/ST | (כנף מנוסה) | 28 | 65 | €0.6M | 6.5 | 44 |
|  | Gervane Kastaneer | W/ST | — | 29 | 64 | €0.5M | 6.4 | 42 |
|  | Kenji Gorre | AM/W | — | 31 | 65 | €0.5M | 6.4 | 43 |
|  | Leandro Kappel | ST/W | — | 26 | 63 | €0.4M | 6.3 | 41 |

> סגל קומפקטי: Kastaneer+Gorre צירפו 8 שערים בהעפלה; J.Bacuna 3. אין שחקני-על; הנכסים: Chong (כנף, Sheffield Utd) + Obispo (בלם, PSV). *גיל/OVR/שווי לרוב שחקני העומק = הערכה (מקורות חסומים).*

## קווים וחישוב אינדקסים
- **GK 40** (Room ותיק MLS-תחתון; רמה נמוכה)
- **DEF 38** (Obispo היחיד ברמת ליגה גבוהה; שאר ההגנה הולנדית-בינונית/נמוכה — נפרצה 7× ב-MD1)
- **MID 36** (האחים Bacuna + Comenencia; חרוצים, ללא איכות עילית)
- **ATT 37** (Chong מנהיג; Locadia חוד; מעט איום)

**אינדקס התקפה** = 0.6×37 + 0.4×36 = 22.2 + 14.4 = **36.6 → 37** ✓
**אינדקס הגנה** = 0.55×38 + 0.30×40 + 0.15×36 = 20.9 + 12.0 + 5.4 = **38.3 → 38** ✓
(תואם לבסיס הקיים — ללא שינוי.)

## מאמן — Dick Advocaat
- **cq 0.95** — מאמן ותיק מאוד ומנוסה (בן 78, **המאמן המבוגר אי-פעם במונדיאל**), אך החומר מוגבל מאוד.
- **cs −0.5** — הגנתי-פרגמטי; בלוק נמוך, צמצום נזק, ניסיון לקאונטר.
- הערה: עזב בפברואר 2026 (הוחלף ע"י Fred Rutten) וחזר לתפקיד שבועות לפני הטורניר — יציבות ספסל מסוימת אך ידע מצטבר.

## קבועות / פנדלים / קרנות
- **פנדלים / חופשיות:** Juninho Bacuna (בעיטות עומק, 3 שערים בהעפלה), Chong.
- **קרנות:** Comenencia/J.Bacuna מבצעים; איום ראש: Obispo, Bazoer, Locadia.

## פציעות + קנס-מחליף
- **אין פציעות חדשות ידועות** לקראת MD2.
- אין כוכבי-על שהיעדרם יגרור קנס מהותי; עומק הסגל דליל אך אחיד באיכות → קנסי-מחליף קטנים (~0).

## כושר + MD1
- **MD1: קוראסאו 1-7 גרמניה (Houston, 14.6).** ספגו 7, אך **כבשו את שער המונדיאל ההיסטורי הראשון** (Comenencia 21' — השוותה זמנית 1-1!).
- חשפו פער-איכות תהומי מול עילית; ההגנה נפרצה שוב ושוב. היתרון היחיד: "אין מה להפסיד", משוחררים.
- מצב Group E: קוראסאו 0 נק' (−6), אחרונה.
- הרכב צפוי MD2 (נגד אקוודור): Room; Floranus, Gaari, Obispo, Fonville; Bazoer/L.Bacuna, Comenencia; Chong, J.Bacuna, Margaritha; Locadia. בלוק נמוך, קאונטר, צמצום נזק.

## מקורות (16.6.26)
1. FIFA — Curaçao squad announcement (Advocaat) + Germany 7-1 Curaçao report (fifa.com)
2. Sky Sports — "smallest ever nation" feature + 7-1 report (skysports.com)
3. World Soccer Talk — Curaçao 2026 preview (squad/key player/tactics)
4. beIN Sports — Advocaat official squad / predicted XI vs Germany
5. ESPN — Curaçao 2026 squad & match data (espn.com)
> מקורות מפורטים (FourFourTwo, worldcuppass, olympics, Wikipedia) החזירו 403. ערכי OVR/שווי/גיל ל-Kastaneer/Gorre/Kappel/Margaritha ושוערי-עומק הם **הערכה** מצולבת; ליבת ה-XI ושערי ה-MD1 מאומתים.
