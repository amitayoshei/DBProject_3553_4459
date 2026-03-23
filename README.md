<div align="center">
  <h1>🏋️‍♂️ PowerGym Pro - Database Project</h1>
  <p><b>מערכת מתקדמת לניהול מתאמנים, מדדי גוף ותוכניות אימון</b></p>

  <img src="https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge&logo=supabase" alt="Supabase" />
  <img src="https://img.shields.io/badge/Scripts-Python-3776AB?style=for-the-badge&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/SQL-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql" alt="PostgreSQL" />
</div>

<br />

## 📋 פרטי ההגשה

| שם מגיש | תעודת זהות |
| :--- | :---: |
| **יאיר חיים זיו** | 3553 |
| **אמיתי אברהם יושעי** | 4459 |

* **היחידה הנבחרת מתוך המערכת:** ניהול ומעקב אישי - מתאמנים, מדדי גוף, תוכניות ויומני אימון.

<hr />

## 📑 תוכן עניינים
* [🚀 שלב א': אפיון והקמת מסד הנתונים](#-שלב-א-אפיון-והקמת-מסד-הנתונים)
  * [מבוא למערכת](#-מבוא-למערכת)
  * [מסכי המערכת (Mockups)](#-מסכי-המערכת-mockups)
  * [תרשימי אפיון](#️-תרשימי-אפיון)
  * [החלטות עיצוב וארכיטקטורה](#-החלטות-עיצוב-וארכיטקטורה)
  * [שיטות הכנסת נתונים](#️-שיטות-הכנסת-נתונים)
  * [גיבוי ושחזור נתונים](#️-גיבוי-ושחזור-נתונים)
* [🔍 שלב ב': שאילתות ואילוצים](#-שלב-ב-שאילתות-ואילוצים)
  * [חלק א'1: שאילתות שליפה (SELECT) כפולות](#חלק-א1-שאילתות-שליפה-select-כפולות---השוואת-יעילות)
  * [חלק א'2: שאילתות שליפה (SELECT) מורכבות](#חלק-א2-שאילתות-שליפה-select-מורכבות)
  * [חלק ב': שאילתות עדכון (UPDATE)](#חלק-ג-שאילתות-עדכון-update)
  * [חלק ג': שאילתות מחיקה (DELETE)](#חלק-ד-שאילתות-מחיקה-delete)
  * [חלק ה': אילוצים (ALTER TABLE)](#חלק-ה-אילוצים-alter-table)
  * [חלק ו': ניהול עסקאות (Transactions) - COMMIT / ROLLBACK](#חלק-ו-ניהול-עסקאות-transactions---commit--rollback)

<hr />

# 🚀 שלב א': אפיון והקמת מסד הנתונים

## 🎯 מבוא למערכת
המערכת מיועדת לניהול מקיף של מכון כושר או מאמן אישי, תוך התמקדות במעקב אחר **500 מתאמנים פעילים**. 

**הנתונים הנשמרים במערכת כוללים:**
* 👤 פרופילים אישיים והצהרות בריאות.
* 📏 היסטוריית מדדי גוף (משקל, אחוזי שומן, מסת שריר וחישוב BMI אוטומטי).
* 📝 תוכניות אימון מפורטות המקושרות לתרגילים ולסרטוני הדרכה.
* 📈 מעקב יומי ואנליזה באמצעות יומני אימון (Workout Logs).

**הפונקציונליות העיקרית:** המערכת מאפשרת להקצות תוכניות אימון מותאמות אישית, לעקוב אחר התקדמות ויעדים לאורך זמן על בסיס עשרות אלפי רשומות, ולספק גישה מהירה להוראות וסרטוני ביצוע של התרגילים השונים.

<hr />

## 💻 מסכי המערכת (Mockups)

<p align="center">
  <b>1. דשבורד מתאמן (Trainee Dashboard)</b><br/>
  <i>מסך הבית המציג את תמונת המצב העדכנית והתקדמות המשקל</i><br/>
  <img src="https://github.com/user-attachments/assets/1261cfd8-0f36-48ce-a40d-3353fee654e3" width="700" alt="Trainee Dashboard" />
</p>
<br/>

<p align="center">
  <b>2. היסטוריית מדידות גוף (Measurements History)</b><br/>
  <i>מעקב טבלאי מפורט אחר משקל, אחוזי שומן ומדדי BMI</i><br/>
  <img src="https://github.com/user-attachments/assets/fde4bbc7-9786-4aeb-a1b3-44e712f4b2cb" width="700" alt="Measurements" />
</p>
<br/>

<p align="center">
  <b>3. תוכנית אימון (Workout Program)</b><br/>
  <i>הצגת התרגילים, הסטים, החזרות והוראות הביצוע</i><br/>
  <img src="https://github.com/user-attachments/assets/f71a9f0d-6a92-42eb-8e79-240615bc0415" width="700" alt="Workout Program" />
</p>
<br/>

<p align="center">
  <b>4. יומן אימון (Workout Log Entry)</b><br/>
  <i>טופס דיווח יומי המאפשר למתאמן להזין משך אימון ופידבק</i><br/>
  <img src="https://github.com/user-attachments/assets/ddb79232-1b82-41d2-9846-554a4f93cb30" width="700" alt="Workout Log" />
</p>

<hr />

## 🗺️ תרשימי אפיון

### תרשים ERD (מושגי)
<p align="center">
  <img src="https://github.com/user-attachments/assets/8b04b38b-1800-4935-a9b4-71bf9b871be8" width="800" alt="ERD Diagram" />
</p>

### תרשים DSD (לוגי)
<p align="center">
  <img src="https://github.com/user-attachments/assets/f299b465-cb32-441a-9fa8-d03502066527" width="800" alt="DSD Diagram" />
</p>

<hr />

## 🧠 החלטות עיצוב וארכיטקטורה
1. **קישור ישיר לקבוצות שריר:** החלטנו לפשט את מבנה התרגילים ולוותר על טבלת קשר מיותרת. במקום זאת, ישות ה-`MUSCLE_GROUP` מקושרת ישירות כישות אב לטבלת ה-`EXERCISE`.
2. **ניהול מרובה סרטונים:** אפשרנו קשר של יחיד לרבים (1:N) בין תרגיל לסרטוני הדרכה, מתוך הבנה שלתרגיל מורכב עשויות להיות מספר וריאציות.
3. **אבטחת איכות נתונים (Constraints):** הוגדרו אילוצי `CHECK` קשיחים (כמו ווידוא ציון BMI בטווח הגיוני של 10-60).

<hr />

## ⚙️ שיטות הכנסת נתונים
כדי למלא את מסד הנתונים בכמויות המידע הנדרשות (מעל 40,000 שורות סך הכל), השתמשנו ב-3 שיטות שונות:

### 1. תכנות (Python Scripts)
כתיבת סקריפטים בשפת פייתון כדי לייצר בצורה אוטומטית פקודות SQL (שאילתות `INSERT`) המוניות. שיטה זו שימשה אותנו ליצירת עשרות אלפי רשומות לוגיות מחושבות, כמו יומני אימון ומדידות גוף (כולל חישובי BMI אוטומטיים).
<p align="center">
  <img src="https://github.com/user-attachments/assets/553bcb60-f615-4712-bcef-c180ffeb5486" width="700" alt="Data Insertion Via Python Scripts" />
</p>
<br/>

### 2. מחולל נתונים חיצוני (Mockaroo)
שימוש בכלי Mockaroo ליצירת מידע אקראי מציאותי. בעזרת מחולל זה יצרנו נתונים אנושיים שקשה לפברק ידנית בכמויות גדולות, כגון שמות מתאמנים, תאריכי לידה והצהרות בריאות.
<p align="center">
  <img src="https://github.com/user-attachments/assets/a45471c0-dfc0-4a4f-a5ee-c5196f63ac7b" width="700" alt="Data Insertion Via Mockaroo Generator" />
</p>
<br/>

### 3. ייבוא נתונים מקבצים (CSV Import)
קליטת נתונים מרוכזת דרך הממשק של מסד הנתונים. יצרנו והכנו מראש קבצי CSV מסודרים המכילים נתוני תשתית ומידע טבלאי, וביצענו להם ייבוא ישיר (Import) לתוך הטבלאות המתאימות במערכת.
<p align="center">
  <img src="https://github.com/user-attachments/assets/1a139102-7e9e-4715-91e7-59a31cb49f6f" width="700" alt="Data Insertion Via CSV" />
</p>

<hr />

## 🛡️ גיבוי ושחזור נתונים

<p align="center">
  <b>תהליך גיבוי מסד הנתונים:</b><br/>
  <img src="https://github.com/user-attachments/assets/241a1901-9aa3-4a82-aa74-038024cee2d7" width="700" alt="Backup Process" />
</p>
<br/>

<p align="center">
  <b>תהליך שחזור מסד הנתונים:</b><br/>
  <img src="https://github.com/user-attachments/assets/190bbfc4-4e47-45b8-adf4-2605f4a4c339" width="700" alt="Restore Process" />
</p>

<hr />

<hr />

# 🔍 שלב ב': שאילתות ואילוצים

## חלק א'1: שאילתות שליפה (SELECT) כפולות - השוואת יעילות

### שאילתה 1: שליפת המדידה העדכנית ביותר (עבור דשבורד מתאמן)
**תיאור השאילתה:** מציגה את המשקל, ה-BMI ואחוזי השומן העדכניים ביותר של מתאמן ספציפי (Trainee_ID = 1).

```sql
-- דרך א': תת-שאילתה (Subquery)
SELECT Weight_Kg, BMI_Score, Fat_Percentage, Measurement_Date 
FROM BODY_MEASUREMENT 
WHERE Trainee_ID = 1 AND Measurement_Date = (SELECT MAX(Measurement_Date) FROM BODY_MEASUREMENT WHERE Trainee_ID = 1);

-- דרך ב': מיון והגבלה (ORDER BY ו-LIMIT)
SELECT Weight_Kg, BMI_Score, Fat_Percentage, Measurement_Date 
FROM BODY_MEASUREMENT 
WHERE Trainee_ID = 1 ORDER BY Measurement_Date DESC LIMIT 1;
```

**צילומי מסך - דרך א':**
<p align="center">
  <img src="https://github.com/user-attachments/assets/15601e4c-7f1b-40d8-b61f-cce2b7cc65c6" width="45%" alt="Q1A Run" />
  <img src="https://github.com/user-attachments/assets/32a6e39c-2eb4-4431-be56-b9a3f6988c94" width="45%" alt="Q1A Result" />
</p>

**צילומי מסך - דרך ב':**
<p align="center">
  <img src="https://github.com/user-attachments/assets/6bf64199-c8bb-4f89-9cc7-b2f2de7aa42b" width="45%" alt="Q1B Run" />
  <img src="https://github.com/user-attachments/assets/32a6e39c-2eb4-4431-be56-b9a3f6988c94" width="45%" alt="Q1B Result" />
</p>

**השוואת יעילות:** דרך ב' (LIMIT) יעילה יותר. בדרך א', מסד הנתונים נדרש לבצע שתי סריקות נפרדות של הטבלה (אחת למציאת תאריך המקסימום ואחת לשליפת הרשומה עצמה). בדרך ב', מסד הנתונים פשוט ממיין ושולף מיד את השורה הראשונה בלבד, מה שחוסך סריקה כפולה ומשפר ביצועים.

<hr />

### שאילתה 2: רשימת תרגילים וציוד בתוכנית (עבור מסך פרטי תוכנית)
**תיאור השאילתה:** שליפת כל שמות התרגילים והציוד הנדרש עבור תוכנית אימון ספציפית (Program_ID = 1).

```sql
-- דרך א': שימוש ב-JOIN
SELECT E.Exercise_Name, E.Equipment_Needed 
FROM EXERCISE E JOIN INCLUDES I ON E.Exercise_ID = I.Exercise_ID 
WHERE I.Program_ID = 1;

-- דרך ב': שימוש ב-IN עם תת-שאילתה
SELECT Exercise_Name, Equipment_Needed 
FROM EXERCISE WHERE Exercise_ID IN (SELECT Exercise_ID FROM INCLUDES WHERE Program_ID = 1);
```

**צילומי מסך - דרך א':**
<p align="center">
  <img src="https://github.com/user-attachments/assets/b6baddc3-b864-4809-b010-262d75817efc" width="45%" alt="Q2A Run" />
  <img src="https://github.com/user-attachments/assets/077e71aa-e309-467e-b43c-e44202ff0894" width="45%" alt="Q2A Result" />
</p>

**צילומי מסך - דרך ב':**
<p align="center">
  <img src="https://github.com/user-attachments/assets/e95c7ed0-5b3f-444a-aa52-0fdb9bd11cbc" width="45%" alt="Q2B Run" />
  <img src="https://github.com/user-attachments/assets/077e71aa-e309-467e-b43c-e44202ff0894" width="45%" alt="Q2B Result" />
</p>

**השוואת יעילות:** דרך א' (JOIN) עוברת אופטימיזציה טובה יותר במנועי SQL. בשימוש ב-IN, במידה ותת-השאילתה מחזירה תוצאות רבות, המנוע עלול לבצע סריקה אטית של הטבלה החיצונית עבור כל ערך. ה-JOIN מיועד לקישור רלציוני כזה ופועל כיחידה אחת יעילה.

<hr />

### שאילתה 3: מתאמנים פעילים החודש
**תיאור השאילתה:** מציאת מתאמנים שביצעו לפחות אימון אחד בחודש פברואר 2024 (פירוק תאריכים).

```sql
-- דרך א': שימוש ב-JOIN ו-DISTINCT
SELECT DISTINCT T.Trainee_ID, T.Gender, T.Join_Date 
FROM TRAINEE_PROFILE T JOIN WORKOUT_LOG W ON T.Trainee_ID = W.Trainee_ID 
WHERE EXTRACT(MONTH FROM W.Log_Date) = 2 AND EXTRACT(YEAR FROM W.Log_Date) = 2024;

-- דרך ב': שימוש ב-EXISTS
SELECT Trainee_ID, Gender, Join_Date 
FROM TRAINEE_PROFILE T WHERE EXISTS (
    SELECT 1 FROM WORKOUT_LOG W WHERE W.Trainee_ID = T.Trainee_ID 
    AND EXTRACT(MONTH FROM W.Log_Date) = 2 AND EXTRACT(YEAR FROM W.Log_Date) = 2024);
```

**צילומי מסך - דרך א':**
<p align="center">
  <img src="https://github.com/user-attachments/assets/4f83a592-ecf4-46d2-891b-ebe5c292738e" width="45%" alt="Q3A Run" />
  <img src="https://github.com/user-attachments/assets/d3d5c16d-f1d5-4a02-9cae-148250335a6f" width="45%" alt="Q3A Result" />
</p>

**צילומי מסך - דרך ב':**
<p align="center">
  <img src="https://github.com/user-attachments/assets/6fd46ba8-c3ae-4a6a-84ff-f8fd4a28fc81" width="45%" alt="Q3B Run" />
  <img src="https://github.com/user-attachments/assets/e71594c5-7969-4b31-ad5e-5dfacaf83988" width="45%" alt="Q3B Result" />
</p>

**השוואת יעילות:** דרך ב' (EXISTS) יעילה משמעותית. בדרך א', ה-JOIN שולף את המתאמן כמספר הפעמים שהתאמן באותו חודש, ורק אז מפעיל DISTINCT כבד למחיקת כפילויות. פקודת EXISTS עוצרת את החיפוש (Short-circuit) עבור מתאמן ברגע שנמצא אימון אחד שמתאים לתנאי, מה שחוסך זמן עיבוד יקר (ניתן לשים לב שהתוצאות ש2 השאילתות נתנו שונות, אבל זה רק הסדר השתנה, התוצאה עצמה - נשארה אותו הדבר, וסימן לכך הוא שב2 התוצאות מוחזרות בדיוק 466 שורות).

<hr />

### שאילתה 4: השוואת משקל נוכחי ליעד (עבור היסטוריית מדידות)
**תיאור השאילתה:** הצגת כל המדידות של מתאמן ספציפי לצד משקל היעד המוגדר שלו בטבלת היעדים.

```sql
-- דרך א': שימוש ב-JOIN
SELECT M.Measurement_Date, M.Weight_Kg, G.Target_Weight_Kg 
FROM BODY_MEASUREMENT M JOIN TRAINEE_GOAL G ON M.Trainee_ID = G.Trainee_ID 
WHERE M.Trainee_ID = 1;

-- דרך ב': תת-שאילתה מקוננת ב-SELECT
SELECT M.Measurement_Date, M.Weight_Kg, 
       (SELECT G.Target_Weight_Kg FROM TRAINEE_GOAL G WHERE G.Trainee_ID = M.Trainee_ID LIMIT 1) AS Target_Weight_Kg
FROM BODY_MEASUREMENT M WHERE M.Trainee_ID = 1;
```

**צילומי מסך - דרך א':**
<p align="center">
  <img src="https://github.com/user-attachments/assets/c05de781-f5fd-4da7-8be2-0f0fa9b1a3dc" width="45%" alt="Q4A Run" />
  <img src="https://github.com/user-attachments/assets/b6d8786e-5046-40e7-bec2-e45c84bd269a" width="45%" alt="Q4A Result" />
</p>

**צילומי מסך - דרך ב':**
<p align="center">
  <img src="https://github.com/user-attachments/assets/1ce0561d-22f7-4214-9b84-2def124b2598" width="45%" alt="Q4B Run" />
  <img src="https://github.com/user-attachments/assets/b6d8786e-5046-40e7-bec2-e45c84bd269a" width="45%" alt="Q4B Result" />
</p>

**השוואת יעילות:** דרך א' (JOIN) היא היעילה והנכונה לארכיטקטורה זו. דרך ב' סובלת מ"בעיית ה-N+1": תת-השאילתה המקוננת ב-SELECT מורצת מחדש עבור כל שורה ושורה שחוזרת מטבלת המדידות. ה-JOIN מבצע את ההתאמה בפעולה אחת רציפה עבור כל קבוצת הנתונים.

<hr />

## חלק א'2: שאילתות שליפה (SELECT) מורכבות

### שאילתה 5: סיכום שריפת קלוריות ודופק לפי חודשים
**תיאור השאילתה:** הצגת סיכום חודשי למתאמן ספציפי הכולל את כמות האימונים, סך הקלוריות שנשרפו וממוצע הדופק בשנת 2024.

```sql
SELECT EXTRACT(MONTH FROM Log_Date) AS Workout_Month, COUNT(Log_ID) AS Total_Workouts, 
       SUM(Total_Calories_Burned) AS Total_Calories, ROUND(AVG(Average_Heart_Rate), 1) AS Avg_Heart_Rate 
FROM WORKOUT_LOG 
WHERE Trainee_ID = 1 AND EXTRACT(YEAR FROM Log_Date) = 2024 
GROUP BY EXTRACT(MONTH FROM Log_Date) ORDER BY Workout_Month;
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/d2901a26-bd7c-48bb-93d1-8e26cf2652b4" width="45%" alt="Q5 Run" />
  <img src="https://github.com/user-attachments/assets/3322af27-2bfb-46cd-a664-62cc10258f48" width="45%" alt="Q5 Result" />
</p>

### שאילתה 6: אפיון תוכניות אימון ארוכות לפי קבוצות שריר
**תיאור השאילתה:** הצגת התוכניות במערכת שאורכן מעל 45 דקות, לצד קבוצת השריר המרכזית וכמות התרגילים בכל תוכנית (שילוב 4 טבלאות).

```sql
SELECT P.Program_Name, M.Group_Name, COUNT(I.Exercise_ID) AS Total_Exercises 
FROM TRAINING_PROGRAM P 
JOIN INCLUDES I ON P.Program_ID = I.Program_ID 
JOIN EXERCISE E ON I.Exercise_ID = E.Exercise_ID 
JOIN MUSCLE_GROUP M ON E.Muscle_Group_ID = M.Muscle_Group_ID 
WHERE P.Estimated_Duration_Minutes > 45 
GROUP BY P.Program_Name, M.Group_Name ORDER BY Total_Exercises DESC;
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/2e579d10-dd50-4683-928f-c3b9f0f066b5" width="45%" alt="Q6 Run" />
  <img src="https://github.com/user-attachments/assets/c239d516-4f51-4921-9a48-488659898a9e" width="45%" alt="Q6 Result" />
</p>

### שאילתה 7: מעקב תנודות משקל למתאמנים
**תיאור השאילתה:** מציאת הפער בין המשקל המקסימלי למינימלי של כל מתאמן, והצגת מתאמנים עם פער של יותר מ-2 ק"ג בלבד.

```sql
SELECT T.Trainee_ID, T.Gender, MAX(M.Weight_Kg) AS Max_Weight, MIN(M.Weight_Kg) AS Min_Weight, 
       (MAX(M.Weight_Kg) - MIN(M.Weight_Kg)) AS Weight_Fluctuation 
FROM TRAINEE_PROFILE T JOIN BODY_MEASUREMENT M ON T.Trainee_ID = M.Trainee_ID 
GROUP BY T.Trainee_ID, T.Gender HAVING (MAX(M.Weight_Kg) - MIN(M.Weight_Kg)) > 2 
ORDER BY Weight_Fluctuation DESC;
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/d6af260a-417f-47f7-ad0d-6eb0a242742a" width="45%" alt="Q7 Run" />
  <img src="https://github.com/user-attachments/assets/c626602e-3046-43ed-b0ec-7f81e376fe1d" width="45%" alt="Q7 Result" />
</p>

### שאילתה 8: פופולריות של תוכניות אימון בפועל
**תיאור השאילתה:** בדיקה אילו תוכניות אימון בוצעו הכי הרבה פעמים בפועל על ידי מתאמנים, כולל תוכניות שלא בוצעו מעולם (שימוש ב-LEFT JOIN).

```sql
SELECT P.Program_Name, P.Workout_Type, COUNT(W.Log_ID) AS Times_Performed, 
       COALESCE(SUM(W.Duration_Minutes), 0) AS Total_Minutes_Spent 
FROM TRAINING_PROGRAM P LEFT JOIN WORKOUT_LOG W ON P.Program_ID = W.Program_ID 
GROUP BY P.Program_ID, P.Program_Name, P.Workout_Type ORDER BY Times_Performed DESC;
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/3fe9ec0e-6f9f-4c8c-b3ab-5e3596de633e" width="45%" alt="Q8 Run" />
  <img src="https://github.com/user-attachments/assets/c13f4d21-ad40-47e5-a322-08510fd2568e" width="45%" alt="Q8 Result" />
</p>

<hr />

## חלק ב': שאילתות עדכון (UPDATE)

### עדכון 1: סימון יעדים שהושגו
**תיאור השאילתה:** מעדכן את סטטוס היעד (`Is_Achieved`) ל-true עבור מתאמנים שהמשקל הנוכחי שלהם (בטבלת המדידות) הגיע למשקל היעד שהוגדר או ירד ממנו.

**קוד העדכון:**
```sql
UPDATE TRAINEE_GOAL
SET Is_Achieved = true
WHERE Trainee_ID IN (
    SELECT G.Trainee_ID FROM TRAINEE_GOAL G
    JOIN BODY_MEASUREMENT M ON G.Trainee_ID = M.Trainee_ID
    WHERE M.Weight_Kg <= G.Target_Weight_Kg AND G.Is_Achieved = false
);
```

**שאילתת בקרה (SELECT להצגת הנתונים לפני ואחרי):**
```sql
SELECT G.Trainee_ID, G.Target_Weight_Kg, M.Weight_Kg AS Current_Weight, G.Is_Achieved
FROM TRAINEE_GOAL G
JOIN BODY_MEASUREMENT M ON G.Trainee_ID = M.Trainee_ID
WHERE M.Weight_Kg <= G.Target_Weight_Kg AND G.Is_Achieved = false;
```

**צילומי מסך:**
<p align="center">
  <b>לפני העדכון:</b><br/>
  <img src="https://github.com/user-attachments/assets/76f28d51-06fa-4aa1-b081-0804662c0ddc" width="600" alt="Update 1 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="https://github.com/user-attachments/assets/640ca25d-e659-4aaf-a500-746bea0ee87c" width="600" alt="Update 1 Run" />
</p>
<p align="center">
  <b>אחרי העדכון (טבלה ריקה):</b><br/>
  <img src="https://github.com/user-attachments/assets/9b77ca70-dafe-4cce-b776-8a8e63bf7a80" width="600" alt="Update 1 After" />
</p>

<hr />

### עדכון 2: סידור אזורי הלוקרים לפי מגדר
**תיאור השאילתה:** מתקנת הקצאות לוקרים שגויות על ידי הבטחה שמתאמנים גברים מועברים לחדר ההלבשה לגברים ומתאמנות נשים מועברות לחדר ההלבשה לנשים.

**קוד העדכון:**
```sql
UPDATE Locker
SET Location_Zone = CASE 
    WHEN Trainee_Profile.Gender = 'Male' THEN 'Men Locker Room'
    WHEN Trainee_Profile.Gender = 'Female' THEN 'Women Locker Room'
END
FROM Trainee_Profile
WHERE Locker.Trainee_ID = Trainee_Profile.Trainee_ID
  AND (
    (Trainee_Profile.Gender = 'Male' AND Locker.Location_Zone = 'Women Locker Room')
    OR 
    (Trainee_Profile.Gender = 'Female' AND Locker.Location_Zone = 'Men Locker Room')
  );
```

**שאילתת בקרה (SELECT להצגת הנתונים לפני ואחרי):**
```sql
SELECT L.Locker_ID, L.Location_Zone AS Current_Zone, TP.Gender AS Trainee_Gender
FROM Locker L
JOIN Trainee_Profile TP ON L.Trainee_ID = TP.Trainee_ID
WHERE (TP.Gender = 'Male' AND L.Location_Zone = 'Women Locker Room')
   OR (TP.Gender = 'Female' AND L.Location_Zone = 'Men Locker Room');
```

**צילומי מסך:**
<p align="center">
  <b>לפני העדכון:</b><br/>
  <img src="https://github.com/user-attachments/assets/6b3c2687-4bd5-4c98-885b-fc4ec2db8c1b" width="600" alt="Update 2 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="https://github.com/user-attachments/assets/57c1ac09-eb7f-4649-a363-78d3b7d97741" width="600" alt="Update 2 Run" />
</p>
<p align="center">
  <b>אחרי העדכון (טבלה ריקה):</b><br/>
  <img src="https://github.com/user-attachments/assets/9b77ca70-dafe-4cce-b776-8a8e63bf7a80" width="600" alt="Update 2 After" />
</p>

<hr />

### עדכון 3: העלאת רמת קושי לתוכניות ארוכות
**תיאור השאילתה:** משנה את רמת הקושי ל-5 עבור תוכניות אימון שמשך הביצוע הממוצע שלהן בפועל (לפי היומנים) גדול מ-70 דקות.

**קוד העדכון:**
```sql
UPDATE TRAINING_PROGRAM
SET Difficulty_Level = 5
WHERE Program_ID IN (
    SELECT Program_ID FROM WORKOUT_LOG GROUP BY Program_ID HAVING AVG(Duration_Minutes) > 70
) AND Difficulty_Level < 5;
```

**שאילתת בקרה (SELECT להצגת הנתונים לפני ואחרי):**
```sql
SELECT Program_ID, Program_Name, Difficulty_Level
FROM TRAINING_PROGRAM
WHERE Program_ID IN (
    SELECT Program_ID FROM WORKOUT_LOG GROUP BY Program_ID HAVING AVG(Duration_Minutes) > 70
) AND Difficulty_Level < 5;
```

**צילומי מסך:**
<p align="center">
  <b>לפני העדכון:</b><br/>
  <img src="https://github.com/user-attachments/assets/06b3f6e0-d39b-4a5c-9208-a6988e6cf96c" width="600" alt="Update 3 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="https://github.com/user-attachments/assets/eae9dd5f-d6ed-4bca-b4bf-a2c51689a345" width="600" alt="Update 3 Run" />
</p>
<p align="center">
  <b>אחרי העדכון (טבלה ריקה):</b><br/>
  <img src="https://github.com/user-attachments/assets/9b77ca70-dafe-4cce-b776-8a8e63bf7a80" width="600" alt="Update 3 After" />
</p>

<hr />

## חלק ג': שאילתות מחיקה (DELETE)

### מחיקה 1: מחיקת יומני אימונים היסטוריים
**תיאור השאילתה:** מוחק מטבלת יומני האימון את כל הרשומות של האימונים שבוצעו במהלך חודש ינואר בשנת 2024.

**קוד המחיקה:**
```sql
DELETE FROM WORKOUT_LOG
WHERE EXTRACT(MONTH FROM Log_Date) = 1 
  AND EXTRACT(YEAR FROM Log_Date) = 2024;
```

**שאילתת בקרה (SELECT להצגת הנתונים לפני ואחרי):**
```sql
SELECT Log_ID, Trainee_ID, Log_Date, Total_Calories_Burned
FROM WORKOUT_LOG
WHERE EXTRACT(MONTH FROM Log_Date) = 1 AND EXTRACT(YEAR FROM Log_Date) = 2024;
```

**צילומי מסך:**
<p align="center">
  <b>לפני המחיקה:</b><br/>
  <img src="https://github.com/user-attachments/assets/6aca4240-60b5-4f78-8d7b-5f6adbf882fb" width="600" alt="Delete 1 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="https://github.com/user-attachments/assets/3b0659be-7459-4328-8441-59fc48b53923" width="600" alt="Delete 1 Run" />
</p>
<p align="center">
  <b>אחרי המחיקה (טבלה ריקה):</b><br/>
  <img src="https://github.com/user-attachments/assets/9b77ca70-dafe-4cce-b776-8a8e63bf7a80" width="600" alt="Delete 1 After" />
</p>

<hr />

### מחיקה 2: הסרת מדידות משקל גבוהות עבור מתאמנים גברים
**תיאור השאילתה:** מוחק את כל רשומות המדידה בהן המשקל שנרשם גדול מ-119 קילוגרמים, אך ורק עבור מתאמנים המוגדרים כגברים.

**קוד המחיקה:**
```sql
DELETE FROM BODY_MEASUREMENT
WHERE Weight_Kg > 119
  AND Trainee_ID IN (
      SELECT Trainee_ID FROM TRAINEE_PROFILE WHERE Gender = 'Male'
  );
```

**שאילתת בקרה (SELECT להצגת הנתונים לפני ואחרי):**
```sql
SELECT M.Measurement_ID, M.Trainee_ID, M.Weight_Kg, T.Gender
FROM BODY_MEASUREMENT M
JOIN TRAINEE_PROFILE T ON M.Trainee_ID = T.Trainee_ID
WHERE M.Weight_Kg > 119 AND T.Gender = 'Male';
```

**צילומי מסך:**
<p align="center">
  <b>לפני המחיקה:</b><br/>
  <img src="https://github.com/user-attachments/assets/96d61a7d-e9e4-4aef-a175-d25c23b793c0" width="600" alt="Delete 2 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="https://github.com/user-attachments/assets/e823d563-7e2b-482c-954b-14072a605546" width="600" alt="Delete 2 Run" />
</p>
<p align="center">
  <b>אחרי המחיקה (טבלה ריקה):</b><br/>
  <img src="https://github.com/user-attachments/assets/9b77ca70-dafe-4cce-b776-8a8e63bf7a80" width="600" alt="Delete 2 After" />
</p>

<hr />

### מחיקה 3: ניקוי היסטוריית מדידות למתאמנים שהשיגו יעד
**תיאור השאילתה:** מוחק את כל מדידות הגוף הישנות של מתאמנים שהוגדר להם במערכת כי הם כבר השיגו את יעד המשקל שלהם (`Is_Achieved = true`).

**קוד המחיקה:**
```sql
DELETE FROM BODY_MEASUREMENT
WHERE Trainee_ID IN (
    SELECT Trainee_ID FROM TRAINEE_GOAL WHERE Is_Achieved = true
);
```

**שאילתת בקרה (SELECT להצגת הנתונים לפני ואחרי):**
```sql
SELECT M.Measurement_ID, M.Trainee_ID, M.Measurement_Date, G.Is_Achieved
FROM BODY_MEASUREMENT M
JOIN TRAINEE_GOAL G ON M.Trainee_ID = G.Trainee_ID
WHERE G.Is_Achieved = true;
```

**צילומי מסך:**
<p align="center">
  <b>לפני המחיקה:</b><br/>
  <img src="https://github.com/user-attachments/assets/0f8da495-eef3-4ca7-9c7d-189ea87395a7" width="600" alt="Delete 3 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="https://github.com/user-attachments/assets/b1c90859-b052-4d77-afac-ea0d7df5c19a" width="600" alt="Delete 3 Run" />
</p>
<p align="center">
  <b>אחרי המחיקה (טבלה ריקה):</b><br/>
  <img src="https://github.com/user-attachments/assets/9b77ca70-dafe-4cce-b776-8a8e63bf7a80" width="600" alt="Delete 3 After" />
</p>

## חלק ה': הוספת עמודות ואילוצים (ALTER TABLE)

### שינוי מבני מקדים: הוספת עמודת שם
לפני הוספת האילוצים, עדכנו את סכמת בסיס הנתונים והוספנו עמודה חדשה עבור שם המתאמן לטבלת הפרופילים.
**קוד ה-ALTER TABLE:**
```sql
ALTER TABLE Trainee_Profile 
ADD COLUMN Name VARCHAR(100);
```

---

### אילוץ 1: תקינות השכרת לוקר (`chk_locker_rental`)
**תיאור השינוי:** הוספנו אילוץ לטבלת `Locker` המוודא שלמות נתונים בעת השכרת לוקר. האילוץ קובע כי לא ניתן להזין תאריך סיום השכרה ללא שיוך למתאמן (Trainee_ID), ולא ניתן לשייך לוקר למתאמן ללא תאריך סיום השכרה.

**קוד ה-ALTER TABLE:**
```sql
ALTER TABLE Locker
ADD CONSTRAINT chk_locker_rental 
CHECK (
  (Trainee_ID IS NULL AND Rental_End_Date IS NULL) OR 
  (Trainee_ID IS NOT NULL AND Rental_End_Date IS NOT NULL)
);
```

**הכנסת נתונים סותרים (בדיקת האילוץ):**
הורצו שתי בדיקות שמפרות את האילוץ בכוונה:
1. ניסיון להזין תאריך ללא מספר מתאמן:
```sql
INSERT INTO Locker (Locker_ID, Location_Zone, Rental_End_Date, Trainee_ID)
VALUES (501, 'VIP Zone', '2026-06-06', NULL);
```
2. ניסיון להזין מספר מתאמן ללא תאריך:
```sql
INSERT INTO Locker (Locker_ID, Location_Zone, Rental_End_Date, Trainee_ID)
VALUES (501, 'VIP Zone', NULL, 1);
```

**צילומי שגיאת הרצה:**
<p align="center">
  <b>הפרה 1 - תאריך ללא מתאמן:</b><br/>
  <img src="https://github.com/user-attachments/assets/6fa146cb-c946-49ef-ade6-5963cb50cf7f" width="700" alt="Locker Constraint Error 1" />
</p>
<p align="center">
  <b>הפרה 2 - מתאמן ללא תאריך:</b><br/>
  <img src="https://github.com/user-attachments/assets/b843cfdd-112c-4ae0-8f0c-cfb6ad2f9310" width="700" alt="Locker Constraint Error 2" />
</p>

---

### אילוץ 2: גיל מינימלי להצטרפות (`chk_trainee_age`)
**תיאור השינוי:** הוספנו אילוץ לטבלת `Trainee_Profile` המוודא כי מתאמן יכול להירשם למכון הכושר רק אם מלאו לו לפחות 14 שנים ביום ההצטרפות.

**קוד ה-ALTER TABLE:**
```sql
ALTER TABLE Trainee_Profile
ADD CONSTRAINT chk_trainee_age 
CHECK (EXTRACT(YEAR FROM AGE(Join_Date, Date_Of_Birth)) >= 14);
```

**הכנסת נתונים סותרים (בדיקת האילוץ):**
ניסיון להזין מתאמן בן 10 (תאריך לידה ב-2015 ותאריך הצטרפות ב-2025):
```sql
INSERT INTO Trainee_Profile (Trainee_ID, Date_Of_Birth, Join_Date, Gender, Main_Goal, Menu_ID, Name)
VALUES (501, '2015-01-01', '2025-01-01', 'Male', 'Flexing & Aura', NULL, 'Yair Ziv');
```

**צילום שגיאת הרצה:**
<p align="center">
  <img src="https://github.com/user-attachments/assets/5f2644ab-f66f-4542-981b-c22bcb48f893" width="700" alt="Age Constraint Error" />
</p>

<hr />

## חלק ו': ניהול עסקאות (Transactions) - COMMIT / ROLLBACK

### תסריט 1: ביטול תהליך בעזרת ROLLBACK
**תיאור התסריט:** פתחנו בלוק פקודות (BEGIN) וביצענו עדכון לתאריך הלידה של מתאמן מספר 1. לאחר שווידאנו שהנתון אכן השתנה באופן זמני בזיכרון, הרצנו פקודת `ROLLBACK` כדי לבטל את התהליך. ניתן לראות כי הנתון חזר למצבו ההתחלתי.

**קוד התהליך:**
```sql
BEGIN;

UPDATE Trainee_Profile 
SET Date_Of_Birth = '2001-01-01' 
WHERE Trainee_ID = 1;

ROLLBACK;
```

**מצב מסד הנתונים בכל שלב:**
<p align="center">
  <b>1. לפני תחילת התהליך (תאריך מקורי: 2007-09-24):</b><br/>
  <img src="https://github.com/user-attachments/assets/d6f8f87f-2d62-4deb-82fa-c8031a8dc49e" width="400" alt="Before Rollback" />
</p>
<p align="center">
  <b>2. בתוך הבלוק, לפני הביטול (התאריך השתנה ל-2001-01-01):</b><br/>
  <img src="https://github.com/user-attachments/assets/de770203-e48d-4e61-9d17-a75bbc22ff2f" width="400" alt="During Rollback" />
</p>
<p align="center">
  <b>3. אחרי ה-ROLLBACK (הנתון חזר לתאריך המקורי):</b><br/>
  <img src="https://github.com/user-attachments/assets/5af6658c-821f-4d4e-af32-841413a9da8f" width="400" alt="After Rollback" />
</p>

<hr />

### תסריט 2: שמירת תהליך בעזרת COMMIT
**תיאור התסריט:** פתחנו בלוק פקודות וביצענו עדכון לתאריך ההצטרפות של מתאמן מספר 2. הפעם, הרצנו פקודת `COMMIT` בסיום. ניתן לראות כי השינוי נשמר במסד הנתונים באופן קבוע וסופי.

**קוד התהליך:**
```sql
BEGIN;

UPDATE Trainee_Profile 
SET Join_Date = '2025-01-01' 
WHERE Trainee_ID = 2;

COMMIT;
```

**מצב מסד הנתונים בכל שלב:**
<p align="center">
  <b>1. לפני תחילת התהליך (תאריך מקורי: 2026-02-01):</b><br/>
  <img src="https://github.com/user-attachments/assets/fb05de79-76a7-49e3-bf48-e098ed425639" width="400" alt="Before Commit" />
</p>
<p align="center">
  <b>2. בתוך הבלוק, לאחר העדכון (התאריך השתנה ל-2025-01-01):</b><br/>
  <img src="https://github.com/user-attachments/assets/e797df24-71d4-46f0-a7cf-a8950139802d" width="400" alt="During Commit" />
</p>
<p align="center">
  <b>3. אחרי ה-COMMIT (הנתון נשמר ונשאר על 2025-01-01):</b><br/>
  <img src="https://github.com/user-attachments/assets/121555b4-9c25-49e3-901d-ab96b99e7e33" width="400" alt="After Commit" />
</p>
