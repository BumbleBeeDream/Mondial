# יומן למידה - שוק וטכנולוגיה

כללי היומן:
- כל רשומה כוללת תאריך בדיקה, ממצא, משמעות לרווה, וכתובות מקור אמיתיות בלבד.
- רשומה בתחום מהיר תנועה (AI, Agentforce, תמחור, מודלים) שגילה מעל 60 יום: לאמת מחדש לפני הסתמכות.
- לא מוחקים רשומות. עדכון נרשם כרשומה חדשה עם "מחליף את רשומת X".

---

## 2026-07-07 | מצב Agentforce - אימוץ, דיוק ותמחור

- נתונים מדווחים: כ-29,000 עסקאות וכ-800 מיליון דולר הכנסה שנתית חוזרת. הערכות חיצוניות: רק כ-5-12% מבסיס הלקוחות של סיילספורס בכלל חתמו על עסקה, וכמחצית מזה בתשלום. דיוק ללא כיוונון מוערך בכ-35%, וזמן ממוצע לעלייה לפרודקשן 5-11 חודשים.
- התמחור המקורי של 2 דולר לשיחה תואר כחסם שהוציא מהמשחק עמותות ועסקים קטנים-בינוניים; הוחלף במודלים גמישים יותר.
- משמעות לרווה: פלח ה-SMB, שהוא בסיס הלקוחות שלנו, הוא בדיוק הפלח שנשאר בלי פתרון סוכנים נגיש; ופער ההטמעה (חודשים לפרודקשן) הוא הזדמנות שירותים בפני עצמה.
- מקורות:
  - https://www.salesforceben.com/where-are-we-really-at-with-agentforce-adoption/
  - https://myaskai.com/blog/salesforce-agentforce-complete-guide-2026
  - https://www.salesforceben.com/agentforce-customers-are-doubling-down-60-of-q4-bookings-came-from-expansions/

## 2026-07-07 | MCP בסיילספורס - זמינות ומגבלות

- שרתי MCP מנוהלים של סיילספורס בזמינות כללית מאפריל 2026, ממהדורת Enterprise ומעלה. חושפים דאטה, Flows ופעולות Apex ללקוחות MCP חיצוניים, עם אכיפת הרשאות בצד סיילספורס.
- Agentforce עצמו קיבל תמיכת MCP בבטא: רישום שרתים, רשימת אישורים ברמת מנהל מערכת, וניהול כלי MCP כפעולות סוכן.
- מגבלה מעשית: לקוחות במהדורת Professional ידרשו פתרון מותאם מול ה-REST API.
- מקורות:
  - https://www.salesforcetutorial.com/salesforce-mcp/
  - https://www.salesforce.com/blog/agentforce-mcp/
  - https://developer.salesforce.com/blogs/2025/06/introducing-mcp-support-across-salesforce

## 2026-07-07 | שותפות אנתרופיק-סיילספורס

- קלוד הוא מודל יסוד בפלטפורמת Agentforce 360, וספק המודלים הראשון שמשולב במלואו בתוך גבול האמון של סיילספורס (תעבורה בתוך הענן הפרטי של סיילספורס). דגש על תעשיות מפוקחות.
- הרחבות דו-כיווניות מביאות הקשר ופעולות של סיילספורס לתוך קלוד (התחיל בסלאק, מתרחב ל-Agentforce 360). סיילספורס פתחה את Agentforce 360 לספקי תוכנה עצמאיים.
- משמעות לרווה: לבנות מתחרה ישיר ל-Agentforce על הפלטפורמה = סיכון פלטפורמה גבוה. להיות שכבת ההטמעה, הממשל והליווי של הגשר הזה = הזדמנות שירות.
- מקורות:
  - https://www.anthropic.com/news/salesforce-anthropic-expanded-partnership
  - https://www.salesforce.com/news/stories/salesforce-anthropic-trusted-context-ai-actions-on-claude/
  - https://www.salesforceben.com/anthropics-new-claude-cowork-partnerships-boost-salesforce-stock-4/

## 2026-07-07 | קריסת מודל השעות בשירותים מקצועיים

- מק'קינזי מדווחת שכרבע עד כשליש מההכנסות הגלובליות כבר בתמחור מבוסס תוצאה; וול סטריט ג'ורנל והפייננשל טיימס מדווחים על מעבר ענפי רחב כשבינה מלאכותית דוחסת שבועות עבודה לשעות.
- 67% מרוכשי שירותי ייעוץ מעדיפים הסדר מחיר קבוע, לעומת 41% שלוש שנים קודם (מחקר דלויט 2024, כפי שצוטט).
- משמעות לרווה: תמחור תוצרים במחיר סגור אינו אופציה אלא חלון זמן. מי שנשאר בתעריף שעתי יעביר בסוף את כל ההתייעלות ללקוח.
- מקורות:
  - https://aiweekly.co/alerts/mckinsey-ties-25-of-fees-to-outcomes-as-ai-erodes-billable-hours
  - https://www.theneuron.ai/newsletter/ai-is-breaking-the-billable-hour/
  - https://www.consultingsuccess.com/how-ai-exposed-the-fatal-flaw-in-billable-hour-consulting
  - https://www.newsweek.com/ai-forcing-it-services-to-rethink-pricing-11865023

## 2026-07-07 | שוק בדיקות אוטומטיות לסיילספורס - צפוף

- בצד המתמחים הוותיקים (Provar, Copado, ACCELQ) פועל גל שחקני בינה מלאכותית ייעודיים (Functionize, TestZeus, Sennu.AI, ContextQA). Copado כבר משווקת עוזר שיוצר, מתחזק ומתקן בדיקות.
- הרשומה שימשה בסיס להריגת הרעיון "סוכן בדיקות כמוצר עצמאי" (ראה בית קברות בצנרת הרעיונות).
- מקורות:
  - https://salesforcedevops.net/index.php/2025/10/09/salesforce-test-automation-landscape-2025-report/
  - https://www.browserstack.com/guide/salesforce-test-automation-tools
