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

## חלק ג': שאילתות עדכון (UPDATE)

### עדכון 1: סימון יעדים שהושגו
**תיאור השאילתה:** מעדכן את סטטוס היעד (`Is_Achieved`) ל-true עבור מתאמנים שהמשקל הנוכחי שלהם (בטבלת המדידות) הגיע למשקל היעד שהוגדר או ירד ממנו.

```sql
UPDATE TRAINEE_GOAL
SET Is_Achieved = true
WHERE Trainee_ID IN (
    SELECT G.Trainee_ID FROM TRAINEE_GOAL G
    JOIN BODY_MEASUREMENT M ON G.Trainee_ID = M.Trainee_ID
    WHERE M.Weight_Kg <= G.Target_Weight_Kg AND G.Is_Achieved = false
);
```

**צילומי מסך:**
<p align="center">
  <b>לפני העדכון:</b><br/>
  <img src="LINK_FOR_UPDATE1_BEFORE_PICTURE" width="600" alt="Update 1 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="LINK_FOR_UPDATE1_RUN_PICTURE" width="600" alt="Update 1 Run" />
</p>
<p align="center">
  <b>אחרי העדכון:</b><br/>
  <img src="LINK_FOR_UPDATE1_AFTER_PICTURE" width="600" alt="Update 1 After" />
</p>

<hr />

### עדכון 2: הארכת שכירות לוקר למתאמנים ותיקים
**תיאור השאילתה:** מוסיף 30 ימים לתאריך סיום ההשכרה של הלוקר עבור מתאמנים שהצטרפו למכון לפני שנת 2024.

```sql
UPDATE LOCKER
SET Rental_End_Date = Rental_End_Date + 30
WHERE Trainee_ID IN (
    SELECT Trainee_ID FROM TRAINEE_PROFILE WHERE EXTRACT(YEAR FROM Join_Date) < 2024
);
```

**צילומי מסך:**
<p align="center">
  <b>לפני העדכון:</b><br/>
  <img src="LINK_FOR_UPDATE2_BEFORE_PICTURE" width="600" alt="Update 2 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="LINK_FOR_UPDATE2_RUN_PICTURE" width="600" alt="Update 2 Run" />
</p>
<p align="center">
  <b>אחרי העדכון:</b><br/>
  <img src="LINK_FOR_UPDATE2_AFTER_PICTURE" width="600" alt="Update 2 After" />
</p>

<hr />

### עדכון 3: העלאת רמת קושי לתוכניות ארוכות
**תיאור השאילתה:** משנה את רמת הקושי ל-5 עבור תוכניות אימון שמשך הביצוע הממוצע שלהן בפועל (לפי היומנים) גדול מ-70 דקות.

```sql
UPDATE TRAINING_PROGRAM
SET Difficulty_Level = 5
WHERE Program_ID IN (
    SELECT Program_ID FROM WORKOUT_LOG GROUP BY Program_ID HAVING AVG(Duration_Minutes) > 70
) AND Difficulty_Level < 5;
```

**צילומי מסך:**
<p align="center">
  <b>לפני העדכון:</b><br/>
  <img src="LINK_FOR_UPDATE3_BEFORE_PICTURE" width="600" alt="Update 3 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="LINK_FOR_UPDATE3_RUN_PICTURE" width="600" alt="Update 3 Run" />
</p>
<p align="center">
  <b>אחרי העדכון:</b><br/>
  <img src="LINK_FOR_UPDATE3_AFTER_PICTURE" width="600" alt="Update 3 After" />
</p>

<hr />

## חלק ד': שאילתות מחיקה (DELETE)

### מחיקה 1: הסרת שיוך לתוכניות עבור מתאמני סיבולת
**תיאור השאילתה:** מוחק מהטבלה המקשרת (`HAS_PROGRAM`) את השיוך לתוכניות אימון עבור כל המתאמנים שהמטרה המרכזית שלהם היא 'Endurance' (סיבולת).

```sql
DELETE FROM HAS_PROGRAM
WHERE Trainee_ID IN (
    SELECT Trainee_ID FROM TRAINEE_PROFILE WHERE Main_Goal = 'Endurance'
);
```

**צילומי מסך:**
<p align="center">
  <b>לפני המחיקה:</b><br/>
  <img src="LINK_FOR_DELETE1_BEFORE_PICTURE" width="600" alt="Delete 1 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="LINK_FOR_DELETE1_RUN_PICTURE" width="600" alt="Delete 1 Run" />
</p>
<p align="center">
  <b>אחרי המחיקה:</b><br/>
  <img src="LINK_FOR_DELETE1_AFTER_PICTURE" width="600" alt="Delete 1 After" />
</p>

<hr />

### מחיקה 2: ניקוי יומני אימון קצרים לתוכניות מתחילים
**תיאור השאילתה:** מוחק רשומות מיומן האימון שבהן נשרפו פחות מ-350 קלוריות, אך ורק אם הן שייכות לתוכנית אימון ברמת קושי של מתחילים (רמה 1).

```sql
DELETE FROM WORKOUT_LOG
WHERE Total_Calories_Burned < 350
  AND Program_ID IN (SELECT Program_ID FROM TRAINING_PROGRAM WHERE Difficulty_Level = 1);
```

**צילומי מסך:**
<p align="center">
  <b>לפני המחיקה:</b><br/>
  <img src="LINK_FOR_DELETE2_BEFORE_PICTURE" width="600" alt="Delete 2 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="LINK_FOR_DELETE2_RUN_PICTURE" width="600" alt="Delete 2 Run" />
</p>
<p align="center">
  <b>אחרי המחיקה:</b><br/>
  <img src="LINK_FOR_DELETE2_AFTER_PICTURE" width="600" alt="Delete 2 After" />
</p>

<hr />

### מחיקה 3: ניקוי היסטוריית מדידות למתאמנים שהשיגו יעד
**תיאור השאילתה:** מוחק את כל מדידות הגוף הישנות של מתאמנים שהוגדר להם במערכת כי הם כבר השיגו את יעד המשקל שלהם (`Is_Achieved = true`).

```sql
DELETE FROM BODY_MEASUREMENT
WHERE Trainee_ID IN (
    SELECT Trainee_ID FROM TRAINEE_GOAL WHERE Is_Achieved = true
);
```

**צילומי מסך:**
<p align="center">
  <b>לפני המחיקה:</b><br/>
  <img src="LINK_FOR_DELETE3_BEFORE_PICTURE" width="600" alt="Delete 3 Before" />
</p>
<p align="center">
  <b>הרצת השאילתה:</b><br/>
  <img src="LINK_FOR_DELETE3_RUN_PICTURE" width="600" alt="Delete 3 Run" />
</p>
<p align="center">
  <b>אחרי המחיקה:</b><br/>
  <img src="LINK_FOR_DELETE3_AFTER_PICTURE" width="600" alt="Delete 3 After" />
</p>
