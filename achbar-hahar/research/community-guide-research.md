# מחקר: הפיכת גיליון Google שיתופי למדריך קהילתי חי, ויזואלי ונגיש

> מחקר רקע עבור דף ההמלצות של מרום גולן (עברית, RTL, קהל מעורב-גילאים, לא-טכני).
> נאסף מחיפוש וסקירת מקורות; קישורי מקור מוטמעים inline.

## 1. גיליון Google כ"שרת" חי

שלוש רמות, בסדר עולה של מורכבות/עלות:

**א. קריאת הגיליון הציבורי בצד-לקוח (gviz / CSV).** גוגל חושפת כל גיליון
"כל מי שיש לו קישור" דרך נקודת קצה מובנית:
- JSON: `…/gviz/tq?tqx=out:json&gid={GID}` — התשובה עטופה ב-callback, צריך
  לקלף ~47 תווים ראשונים ו-2 אחרונים לפני `JSON.parse`
  ([anjanesh.dev](https://anjanesh.dev/retrieving-data-from-a-public-google-spreadsheet-and-display-it-on-a-webpage)).
- CSV: `…/gviz/tq?tqx=out:csv&gid={GID}` — פשוט יותר לפענוח, ונמדד כמהיר/זול
  משמעותית מ-Apps Script
  ([Medium – CSV beats Apps Script](https://medium.com/@abuabdirohman/google-sheets-integration-why-csv-beats-google-apps-script-by-86-9-ae07c0b17f1d)).

*יתרונות:* חינם, ללא שרת, ללא מפתח API, "חי". *חסרונות / מתי נשבר:* הגיליון
חייב להיות ציבורי; פסיקים/שורות בתוך תא שוברים פיצול CSV נאיבי (חובה parser
אמיתי כמו PapaParse); אין caching מובנה; עומס קריאות חריג עלול לפגוש מגבלות
רכות של גוגל. **מיטיגציה:** cache בדפדפן (localStorage + חותמת זמן) ו/או snapshot.
**זו הגישה המומלצת לפרויקט הזה.**

**ב. Google Apps Script web app.** סקריפט שמחזיר JSON — שליטה מלאה (סינון
שורות, הסתרת עמודת מודרציה, גיליון פרטי), אבל איטי יותר ועם מכסות ריצה
([gviz on private sheets](https://sites.google.com/view/metricrat-ai2/guides/use-gviz-to-get-or-query-private-google-sheet-data)).

**ג. SaaS של Sheet-to-API / Sheet-to-site.** Stein / SheetDB / Sheety הופכים
גיליון ל-REST JSON (freemium, מוגבל-קצב). בוני אתרים no-code — Glide ו-Softr —
מייצרים את כל האתר. *Trade-off:* Glide מהיר לבנייה אך מגביל בתוכנית החינמית
(אפליקציה אחת, ~25k שורות); Softr עם עיצוב/SEO טובים יותר אך ~$50+/חודש בקנה
מידה ([Softr alternatives](https://www.softr.io/blog/glide-alternatives)).
ל-Softr יש אפילו [תבנית קהילתית מ-Google Sheets](https://www.softr.io/templates/google-sheets-community-website-template).
**מסקנה:** SaaS חוסך תחזוקה אך מוסיף עלות חודשית ו-lock-in; מסלול ה-HTML-יחיד +
gviz הוא בעצם חינמי ובבעלות מלאה.

## 2. דוגמאות אמיתיות למדריכים קהילתיים/מקומיים

- **מדריכים מקומיים no-code מתוך גיליון** הם דפוס מוכר: לבחור נישה, לבנות סכמה
  לגיליון, למפות עמודות (כותרת, תיאור, תמונה, קטגוריה) לכרטיסים, להוסיף פילטרים
  ([Silicon Review](https://thesiliconreview.com/2026/04/how-to-create-a-local-directory-website-without-coding),
  [GeoDirectory](https://wpgeodirectory.com/how-to-build-neighborhood-directory-website/)).
- **"Link-in-bio" hubs** ([Linktree community templates](https://linktr.ee/s/templates/community-organization))
  הם המתחרה הפשוט ביותר: עסק/עמותה מפנים URL אחד לתפריט, מפה, אנשי קשר.
  *עובד* כי אפס הקמה ונייד-תחילה. *מתאים פחות כאן* כי רשימת לינקים שטוחה לא
  מאפשרת סינון/חיפוש של עשרות מקומות לפי קטגוריה, ושליטת ה-RTL מוגבלת.

**מסקנה:** מה שמצליח — סכמת עמודות נקייה, קטגוריות אמיתיות, URL אחד זכיר.
נכשל — כשהסכמה מבולגנת או שאף אחד לא אחראי על תחזוקה.

## 3. UX למדריך מקומות עם סינון

- **כרטיסים + צ'יפים + חיפוש** הוא הדפוס הקנוני. Google Maps עצמה משתמשת בשורת
  חיפוש + פס צ'יפים אופקי (מסעדות, מלונות…) שמסנן תוצאות חי — מודל אידאלי
  ([UXPin filter UX](https://www.uxpin.com/studio/blog/filter-ui-and-ux/)).
- **תמיד להציג פילטרים פעילים** כצ'יפים הניתנים להסרה, במיוחד בנייד.
- **לקבץ פילטרים לקטגוריות משמעותיות** ולהציג **ספירת תוצאות** כדי שאף אחד לא
  ינחת על רשימה ריקה ([NN/g](https://www.nngroup.com/articles/filter-categories-values/)).
- **נייד-תחילה:** עדיף sheet מסך-מלא על פאנל צד צפוף
  ([Pencil & Paper](https://www.pencilandpaper.io/articles/ux-pattern-analysis-mobile-filters)).
- **מפות:** לקהל לא-טכני, **לינקי חיפוש** של Google Maps
  (`…/maps/search/?api=1&query=<שם>`) קלים יותר, לא דורשים מפתח API, ונפתחים
  באפליקציית המפות של המשתמש — עדיף על iframe מוטמע שמוסיף משקל ותלות billing.

## 4. נגישות לקהל עברי מעורב-גילאים

- **RTL:** `<html lang="he" dir="rtl">`; לשקף פריסה/אייקונים; לשמור מספרי טלפון
  ו-URL ב-LTR בתוך זרימת RTL (בידוד Unicode) כדי שלא יתהפכו.
- **ניגודיות:** WCAG 1.4.3 — לפחות **4.5:1** לטקסט רגיל, **3:1** לטקסט גדול
  ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html),
  [WebAIM](https://webaim.org/articles/contrast/)).
- **גודל גופן:** יחידות יחסיות; גוף ~18px לאור הקהל המבוגר; line-height ≥ 1.5
  ([A11Y Collective](https://www.a11y-collective.com/blog/wcag-minimum-font-size/)).
- **יעדי-מגע:** WCAG 2.5.5 — ~44px עם רווח נדיב בין צ'יפים וכפתורי פעולה.
- **רוחב-פס נמוך / אופליין:** קישוריות בגולן משתנה — lazy-load לתמונות, cache
  של הקריאה האחרונה ב-localStorage כדי שהדף ירונדר גם כשהרשת/גוגל איטיים;
  service worker זעיר יכול לאפשר אופליין.
- **קוראי מסך:** HTML סמנטי (`<button>`, `<a>`, כותרות), alt, ו-aria על צ'יפים.

## 5. ממשל ותחזוקת הגיליון

- **לנעול סכמה עם Data Validation** — רשימות נפתחות לקטגוריה, אזור, ועמודת
  **Status** ("Approved/Pending/Rejected")
  ([OWOX](https://www.owox.com/blog/articles/data-validation-google-sheets)).
- **מודרציה ע"י עמודת Status + טווחים מוגנים** — שיתוף כעורך אך הגנה על עמודת
  ה-Status כך שרק מנהלים מאשרים; הדף מסנן ל-`Status = Approved`
  ([Google – protect ranges](https://support.google.com/docs/answer/1218656)).
- **מניעת נתונים שבורים:** ולידציית URL/טלפון, עמודת "עודכן לאחרונה".
- **לעודד תרומות:** **Google Form** שמוסיף שורות ידידותי יותר מעריכת שורות גולמיות
  ומנתב פריטים חדשים ל-Pending.

## המלצות לפרויקט הזה

- **להשתמש בגישת ה-HTML-יחיד + gviz/CSV החינמית.** דף סטטי אחד (GitHub Pages /
  Netlify) שקורא את הגיליון בצד-לקוח — בלי שרת, בלי תשלום, בבעלות מלאה. **✓ מיושם.**
- **לפענח חזק ולשמור cache.** PapaParse ל-CSV; שמירת הקריאה האחרונה ב-localStorage.
  **✓ מיושם.**
- **עיצוב סביב כרטיסים + צ'יפי-קטגוריה + חיפוש**, במודל Google Maps; ספירות
  תוצאות; נייד-תחילה. **✓ מיושם.**
- **לינקי חיפוש של Google Maps, לא הטמעה** — בלי מפתחות/billing, נפתח באפליקציה
  של המשתמש. **✓ מיושם.**
- **בנייה RTL-תחילה וגדולה כברירת-מחדל:** `dir="rtl"`, גוף ≥16–18px, ניגודיות
  4.5:1, יעדי-מגע ~44px, בידוד LTR לטלפונים. **✓ מיושם.**
- **ממשל בעמודת Status + טווחים מוגנים**, הצגת מאושרים בלבד; קליטת פריטים חדשים
  דרך Google Form ל-Pending. **↗ צעד הבא מומלץ.**
- **לנעול סכמה עם Data Validation** (קטגוריה, אזור, Status). **↗ צעד הבא מומלץ.**
- **מנהל-תוכן אחד-שניים + URL קצר וזכיר** — הבעלות האנושית והלינק היחיד הם מה
  שמשמר מדריכים קהילתיים לאורך זמן. **↗ צעד הבא מומלץ.**
