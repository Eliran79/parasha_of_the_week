---
title: "פרה אדומה: חוק שימור האינפורמציה ששלמה המלך לא פתר"
parasha: "כי תישא / פרשת פרה"
date: "2026-03-07"
tags: ["פיזיקה", "שימור_אינפורמציה", "קוונטום", "ARC", "לנדאואר", "טומאה_וטהרה"]
emoji: "🔴"
excerpt: "שלמה המלך אמר על כל התורה אחכמה — ודווקא על פרה אדומה: והיא רחוקה ממני. כי הוא חיפש הגיון לוקאלי. ARC מציע שאלה אחרת: לאן הולכת הטומאה?"
author: "אלירן סבג"
year: 2026
---

# פרה אדומה: חוק שימור האינפורמציה ששלמה המלך לא פתר

> "אָמַרְתִּי אֶחְכָּמָה וְהִיא רְחוֹקָה מִמֶּנִּי"
> — קהלת ז:כג, על פרה אדומה (מדרש תנחומא)

שלמה המלך — החכם מכל האדם — עמד בפני מצווה אחת וכשל. לא מחוסר ידע. מחוסר מסגרת.

הוא שאל את השאלה הלא נכונה.

---

## הפרדוקס שפצע את שלמה

פרה אדומה היא טקס הטהרה מטומאת מת. הפרוטוקול מוזר באופן בוטה:

| שלב | פעולה | תוצאה |
|------|--------|--------|
| א | כהן שורף פרה אדומה | הכהן **נטמא** |
| ב | אדם טמא מוזה במי הנדה (אפר + מים) | האדם **נטהר** |
| ג | הכהן המזה | **נטמא** |

הטמא יוצא טהור. המטהר יוצא טמא.

שלמה שאל: **מדוע?** — חיפש לוגיקה פנימית לכל צעד.

ARC שואל שאלה אחרת: **לאן הולכת הטומאה?**

---

## תשובה: היא לא הולכת לשום מקום

$$\text{טמא}(\text{אדם}) + \text{טהור}(\text{כהן}) \xrightarrow{\text{פרה אדומה}} \text{טהור}(\text{אדם}) + \text{טמא}(\text{כהן})$$

סכום הביטים: **שמור**.

זה לא מיסטיקה — זה חוק שימור. בפיזיקה מודרנית קוראים לו **עקרון לנדאואר** (Landauer's Principle, 1961):

> מחיקת ביט אחד של מידע דורשת אנרגיה מינימלית של $k_B T \ln 2$.

מידע לא נמחק. הוא **מועבר**, וההעברה עולה אנרגיה.

השריפה של הפרה — האש — היא האנרגיה ששולמה עבור העברת הביט מהאדם הטמא לכהן המזה.

$$E_{\text{שריפה}} \geq k_B T \ln 2 \quad \text{(מחיר ההעברה)}$$

---

## "תוכו כברו" — בעקבות Hidden Variables של איינשטיין

רש"י מביא: הפרה כשרה רק אם היא **אדומה מבפנים ומבחוץ**. "תוכו כברו."

בפיזיקה: זהו המצב שאיינשטיין חיפש כל חייו.

איינשטיין סרב לקבל את מכניקת הקוונטום כתורה שלמה. הוא טען שחייבים להיות **hidden variables** — מצבים פנימיים נסתרים שהפיזיקה הקוונטית פשוט לא מודדת. "אלוהים לא משחק בקוביות."

בל (Bell, 1964) הוכיח מתמטית: אם hidden variables קיימים — הטבע חייב לעמוד בתנאי מסוים. הניסויים של אספקט (Aspect, 1982) הפריכו את זה.

**הטבע אינו "תוכו כברו".**

פרה אדומה, לעומת זאת, **מוגדרת** כ-"תוכו כברו":

$$\text{state}_{\text{internal}} = \text{state}_{\text{external}} \Rightarrow \text{zero information gap}$$

זוהי מערכת ללא hidden variables — **pure state** — המכשיר היחיד שמסוגל להעביר ביט טומאה בלי לייצר noise. כל מערכת אחרת תוסיף אי-ודאות. הפרה לא.

---

## "שלא עלה עליה עול" — Clean Quantum State

תנאי שני: הפרה **לא עבדה** מעולם.

בלשון מערכות מידע: **אין side-channel. אין היסטוריה. אין residual state.**

$$\rho_{\text{פרה}} = |\psi_0\rangle\langle\psi_0| \quad \text{(pure state, not mixed)}$$

מערכת שעבדה בעבר נושאת **entanglement** עם כל מה שנגעה בו. אי אפשר לבצע בה העברת ביט נקייה — יש "רעש" מהסביבה.

"שלא עלה עליה עול" = הגדרת **clean ancilla** במחשוב קוונטומי — קיוביט עזר שחייב להיות במצב $|0\rangle$ לפני שמשתמשים בו כמדיום.

הפרה היא ה-ancilla של פרוטוקול הטהרה.

---

## מי חיים ואפר — מדיום קוונטי

המזיגה הספציפית: **מים חיים + אפר הפרה**.

$$\underbrace{\text{מים חיים}}_{\text{continuous}} + \underbrace{\text{אפר}}_{\text{discrete}} = \text{מדיום ההעברה}$$

זהו **Nitai Principle** — הרצף מתוקן על ידי הדיסקרטי.

- המים הם הרצף: נוזל, זורם, ב-superposition
- האפר הוא המפתח הדיסקרטי: שרוף, קבוע, מקודד את ה-pure state

יחד הם יוצרים את המדיום שמאפשר העברת ביט בלי אובדן מידע — בדיוק כמו מקוד תיקון שגיאות (error correction) שמשתמש בקיוביטים רציפים ומידע דיסקרטי.

```python
# מודל פשוט של העברת טומאה כהעברת ביט

def ritual_transfer(person_state: int, kohen_state: int) -> tuple[int, int]:
    """
    פרוטוקול פרה אדומה: העברת ביט טומאה
    0 = טהור, 1 = טמא
    שימור: sum(states) = const
    """
    total = person_state + kohen_state  # שמור!

    if person_state == 1:  # אדם טמא
        # ביט עובר לכהן
        return 0, min(kohen_state + 1, 1)
    return person_state, kohen_state

# לפני
person, kohen = 1, 0   # טמא, טהור
print(f"לפני:  אדם={person} כהן={kohen}  סכום={person+kohen}")

# אחרי הזאה
person, kohen = ritual_transfer(person, kohen)
print(f"אחרי:  אדם={person} כהן={kohen}  סכום={person+kohen}")

# הסכום שמור — חוק שימור האינפורמציה
```

```
לפני:  אדם=1 כהן=0  סכום=1
אחרי:  אדם=0 כהן=1  סכום=1
```

---

## למה שלמה לא פתר את זה

שלמה ניסה להבין כל צעד **לוקאלית**:

- "מדוע הכהן נטמא? הוא עשה מצווה!"
- "מדוע האפר מטהר? הוא שריפה!"

אבל שימור אינפורמציה הוא עיקרון **גלובלי**. הוא לא נראה הגיוני בסקאלה של צעד בודד.

זה בדיוק הפרדוקס של $P \neq NP$ — בעיה שנראית קשה לוקאלית (ניתן לאמת תשובה ביעילות, אבל קשה למצוא אחת) ואילו המבנה הגלובלי שלה מוגדר ומובן.

$$\underbrace{\text{הגיוני לוקאלית?}}_{\text{לא}} \quad \neq \quad \underbrace{\text{עקבי גלובלית?}}_{\text{כן}}$$

**"חוקה"** בלשון התורה = עיקרון שנראה שרירותי מבפנים, אבל נחוץ מבחוץ.

---

## השלישייה: פורים ← כי תישא ← פרה אדומה

שלושה שבועות, שלוש גרסאות של אותו חוק:

### פורים — היפוך מצב במערכת סגורה

$$\text{גזרת מוות} \xrightarrow{\text{ונהפוך הוא}} \text{ניצחון}$$

האינפורמציה (גזרת המוות) לא נמחקה — היא **התהפכה**. המערכת סגורה. הסכום שמור.

### כי תישא — ספירה כמגע ישיר

> "כי תשא את ראש בני ישראל... ונתנו איש כֹּפֶר נַפְשׁוֹ"

ספירה ישירה = מגע ישיר עם ה-state הכולל = **unbounded operation** = סכנה.

מחצית השקל = **bounded intermediary** — כל אחד תורם יחידה קבועה, הסכום מחושב בלי לגעת ישירות בהתפלגות.

זה Landauer: אל תמדוד את כל המצב ישירות — מדוד דרך צעדים מוגבלים.

$$\sum_{i=1}^{N} \frac{1}{2} \text{ שקל} = \frac{N}{2} \quad \text{(ספירה עקיפה, בטוחה)}$$

### עגל הזהב — כישלון ה-Bound

משה עלה להר ← המערכת ממתינה ← העם לא יכול להחזיק uncertainty ← יצרו פתרון עצמאי.

$$\text{העגל} = \text{local unbounded move} + \text{no constraint} = \text{information corruption}$$

הלוחות נשברו — לא כי האינפורמציה נהרסה. כי ה**כלי** לא יכול להכיל state כשהמקבל לא מוכן.

### פרה אדומה — שימור שלם

$$\text{מת} \to \text{טומאה} \to \text{מעבר} \to \text{טהרה} \quad : \quad \Delta I_{\text{total}} = 0$$

שלוש פרשות. שלושה ביטויים של:

> **המידע לא נהרס. הוא עובר. הוא מתהפך. הוא שמור.**

---

## עיקרון ניתאי — הפרה כתיקון הרצף

<div class="english" markdown="1">

### The Nitai Principle in Parashat Parah

The **Nitai Principle** states: continuous approximations accumulate error. Reality is discrete. Correction requires a discrete anchor.

$$f_{\text{continuous}}(x) \approx f_{\text{real}}(x) \quad \text{but} \quad \lim_{n \to \infty} \varepsilon_n \neq 0$$

The Red Heifer ritual is the oldest known implementation:

| Component | Type | Role |
|-----------|------|------|
| Living water | Continuous | Carries the transfer medium |
| Ashes of the heifer | Discrete | Encodes the pure-state key |
| Together | Hybrid | Error-correcting medium |

The **tamei state** is a continuous drift — accumulated contact with death, spreading like a wave function. The ritual snaps it back to a defined discrete state (tahor), exactly as a GPS correction snaps a drifting position back to ground truth.

Nitai read this portion at his Bar Mitzvah. The principle that bears his name — correcting the continuous with the discrete — is written explicitly in Bamidbar 19. He didn't just read the law. He embodied it: at 13, the moment a Jewish boy becomes discrete — a full, counted, bounded member of the chain — he read the parasha that defines why that discretization matters.

</div>

---

## סיכום: מה ש-ARC קורא מהפרשה

| עיקרון | פרשה | פיזיקה |
|--------|-------|--------|
| שימור אינפורמציה | פרה אדומה | Landauer's Principle |
| Zero hidden variables | תוכו כברו | Bell's Theorem |
| Clean ancilla | שלא עלה עליה עול | Quantum error correction |
| Bounded measurement | מחצית השקל | Indirect state tomography |
| State flip in closed system | ונהפוך הוא | Unitary evolution |
| Nitai Principle | מים חיים + אפר | Continuous→Discrete correction |

שלמה המלך אמר "אמרתי אחכמה."

הוא חיפש חכמה לוקאלית — למה כל צעד הגיוני בפני עצמו.

אבל פרה אדומה היא לא פרדוקס מקומי. היא **חוק גלובלי**.

והחוקים הגלובליים הגדולים ביותר תמיד נראים כ-"חוקה" — גזירה בלתי מוסברת — עד שמוצאים את המסגרת הנכונה.

איינשטיין לא קיבל שאלוהים משחק בקוביות — עד יום מותו ב-1955 הוא עדיין חיפש hidden variables.

לנו לקח 3,300 שנה לקבל שטומאה היא ביט.

---

*פרשת כי תישא / פרשת פרה — מוצאי שבת, ז' באדר ב' תשפ"ו*

*לניתאי — שקרא את הפרשה ביום שנהפך לדיסקרטי.*
