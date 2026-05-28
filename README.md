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
  * [חלק א': עדכוני סכמה ואילוצים (DDL & Constraints)](#חלק-א-עדכוני-סכמה-ואילוצים-ddl--constraints)
  * [חלק ב': טיוב נתונים ולוגיקה עסקית (UPDATE)](#חלק-ב-טיוב-נתונים-ולוגיקה-עסקית-update)
  * [חלק ג': ניקוי נתונים (DELETE)](#חלק-ג-ניקוי-נתונים-delete)
  * [חלק ד'1: שאילתות שליפה (SELECT) כפולות - השוואת יעילות](#חלק-ד1-שאילתות-שליפה-select-כפולות---השוואת-יעילות)
  * [חלק ד'2: שאילתות שליפה (SELECT) מורכבות](#חלק-ד2-שאילתות-שליפה-select-מורכבות)
  * [חלק ה': ניהול עסקאות (Transactions) - COMMIT / ROLLBACK](#חלק-ה-ניהול-עסקאות-transactions---commit--rollback)
* [🔗 שלב ג': שילוב מערכות (Integration) ויצירת תצוגות (Views)](#-שלב-ג-שילוב-מערכות-integration-ויצירת-תצוגות-views)
  * [חלק 1: החלטות ארכיטקטוניות ותהליך ה-ETL](#חלק-1-החלטות-ארכיטקטוניות-ותהליך-ה-etl)
  * [חלק 2: תצוגות מסד נתונים ושאילתות משולבות](#חלק-2-תצוגות-מסד-נתונים-ושאילתות-משולבות)
* [🧠 שלב ד': תכנות מסד נתונים (PL/pgSQL)](#-שלב-ד-תכנות-מסד-נתונים-plpgsql)
  * [חלק 1: טיוב נתונים מתקדם (Data Cleansing)](#חלק-1-טיוב-נתונים-מתקדם-data-cleansing)
  * [חלק 2: טריגרים (Triggers)](#חלק-2-טריגרים-triggers)
  * [חלק 3: פרוצדורות (Procedures)](#חלק-3-פרוצדורות-procedures)
  * [חלק 4: פונקציות (Functions)](#חלק-4-פונקציות-functions)
  * [חלק 5: תוכניות ראשיות ובדיקות (Main Programs)](#חלק-5-תוכניות-ראשיות-ובדיקות-main-programs)

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

בשלב זה התמקדנו ביישום הלוגיקה העסקית, הבטחת שלמות הנתונים ושליפת מידע מורכב. בחרנו לפעול בצורה מתודולוגית: תחילה הוספנו אילוצי מערכת מתקדמים, לאחר מכן טיבנו וניקינו את הנתונים (UPDATE ו-DELETE), ורק לבסוף ביצענו את שאילתות השליפה (SELECT) על גבי נתונים מדויקים והגיוניים.

## חלק א': עדכוני סכמה ואילוצים (DDL & Constraints)

### שינוי מבני מקדים: הוספת עמודת שם
לפני הוספת האילוצים, עדכנו את סכמת בסיס הנתונים והוספנו עמודה חדשה עבור שם המתאמן לטבלת הפרופילים, והכנסנו ערכים בעזרת שאילתה המגרילה שמות לגברים ונשים מתוך 50 שמות פרטיים ו- 50 שמות משפחה לכל אחד:

```sql
ALTER TABLE Trainee_Profile
ADD COLUMN Name VARCHAR(50);

UPDATE Trainee_Profile
SET name = CASE 
    WHEN gender = 'Male' THEN 
        (ARRAY['David', 'Daniel', 'Omer', 'Amit', 'Itay', 'Yonatan', 'Tom', 'Guy', 'Roy', 'Ido', 'Tomer', 'Ben', 'Adam', 'Michael', 'Eran', 'Gil', 'Lior', 'Nir', 'Roee', 'Ariel', 'Noam', 'Uri', 'Yosef', 'Eitan', 'Itamar', 'Yair', 'Asaf', 'Nadav', 'Matan', 'Shahar', 'Eyal', 'Ohad', 'Barak', 'Gal', 'Peleg', 'Dvir', 'Elad', 'Yaron', 'Aviv', 'Ziv', 'Gabi', 'Yoav', 'Yishai', 'Eli', 'Avi', 'Yigal', 'Dor', 'Maor', 'Or', 'Erez'])[floor(random() * 50 + 1)::int]
        || ' ' ||
        (ARRAY['Cohen', 'Levi', 'Mizrahi', 'Peretz', 'Bitton', 'Dahan', 'Agmon', 'Friedman', 'Malka', 'Azoulay', 'Katz', 'Yosef', 'David', 'Amar', 'Ohayon', 'Hadad', 'Gabbay', 'Ben-David', 'Adler', 'Levin', 'Tal', 'Golan', 'Kadosh', 'Shapira', 'Klein', 'Avraham', 'Yaari', 'Bar', 'Chen', 'Eilon', 'Peled', 'Tzur', 'Segel', 'Naveh', 'Almog', 'Harari', 'Vardi', 'Lavi', 'Manor', 'Dror', 'Ratzon', 'Paz', 'Sadeh', 'Geva', 'Mor', 'Shahaf', 'Gefen', 'Dekel', 'Carmeli', 'Alon'])[floor(random() * 50 + 1)::int]
        
    WHEN gender = 'Female' THEN 
        (ARRAY['Maya', 'Noa', 'Shir', 'Yael', 'Michal', 'Tamar', 'Roni', 'Shira', 'Eden', 'Adi', 'Gal', 'Dana', 'Mor', 'Anna', 'Sarah', 'Nofar', 'Talia', 'Romi', 'Lian', 'Keren', 'Hila', 'Yarden', 'Noya', 'Mika', 'Agam', 'Ella', 'Lihi', 'Maayan', 'Sapir', 'Liron', 'Rotem', 'Inbar', 'Hadar', 'Nitzan', 'Yuval', 'Gefen', 'Tair', 'Avia', 'Gali', 'Carmel', 'Shelly', 'Yifat', 'Lital', 'Einat', 'Efrat', 'Meirav', 'Sigal', 'Orit', 'Ronit', 'Anat'])[floor(random() * 50 + 1)::int]
        || ' ' ||
        (ARRAY['Cohen', 'Levi', 'Mizrahi', 'Peretz', 'Bitton', 'Dahan', 'Agmon', 'Friedman', 'Malka', 'Azoulay', 'Katz', 'Yosef', 'David', 'Amar', 'Ohayon', 'Hadad', 'Gabbay', 'Ben-David', 'Adler', 'Levin', 'Tal', 'Golan', 'Kadosh', 'Shapira', 'Klein', 'Avraham', 'Yaari', 'Bar', 'Chen', 'Eilon', 'Peled', 'Tzur', 'Segel', 'Naveh', 'Almog', 'Harari', 'Vardi', 'Lavi', 'Manor', 'Dror', 'Ratzon', 'Paz', 'Sadeh', 'Geva', 'Mor', 'Shahaf', 'Gefen', 'Dekel', 'Carmeli', 'Alon'])[floor(random() * 50 + 1)::int]
END;
```

### אילוץ 1: תקינות השכרת לוקר (`chk_locker_rental`)
**תיאור השינוי:** הוספנו אילוץ לטבלת `Locker` המוודא שלמות נתונים בעת השכרת לוקר. האילוץ קובע כי לא ניתן להזין תאריך סיום השכרה ללא שיוך למתאמן (Trainee_ID), ולא ניתן לשייך לוקר למתאמן ללא תאריך סיום השכרה.

```sql
ALTER TABLE Locker
ADD CONSTRAINT chk_locker_rental 
CHECK (
  (Trainee_ID IS NULL AND Rental_End_Date IS NULL) OR 
  (Trainee_ID IS NOT NULL AND Rental_End_Date IS NOT NULL)
);
```

**צילומי שגיאת הרצה (בדיקת האילוץ):**
<p align="center">
  <b>הפרה 1 - תאריך ללא מתאמן:</b><br/>
  <b><img width="1521" height="455" alt="Screenshot 2026-03-22 204244" src="https://github.com/user-attachments/assets/ac537927-78fc-4eca-acc0-2fe013bee04d" /></b>
</p>
<p align="center">
  <b>הפרה 2 - מתאמן ללא תאריך:</b><br/>
  <b><img width="1520" height="461" alt="Screenshot 2026-03-22 204316" src="https://github.com/user-attachments/assets/17cfa2ae-1438-43a2-bb3f-4c13ef2b4a22" /></b>
</p>

### אילוץ 2: גיל מינימלי להצטרפות (`chk_trainee_age`)
**תיאור השינוי:** הוספנו אילוץ לטבלת `Trainee_Profile` המוודא כי מתאמן יכול להירשם למכון הכושר רק אם מלאו לו לפחות 14 שנים ביום ההצטרפות.

```sql
ALTER TABLE Trainee_Profile
ADD CONSTRAINT chk_trainee_age 
CHECK (Join_Date >= Date_Of_Birth + INTERVAL '14 years');
```

**צילום שגיאת הרצה (בדיקת האילוץ):**
<p align="center">
  <b><img width="1520" height="457" alt="Screenshot 2026-03-22 204353" src="https://github.com/user-attachments/assets/ce3ee633-37f6-4856-a517-ca4c8f43ede7" /></b>
</p>

<hr />

## חלק ב': טיוב נתונים ולוגיקה עסקית (UPDATE)

בשלב זה ביצענו 6 שאילתות עדכון (Data Cleansing) כדי להפוך את הנתונים האקראיים (Mock Data) להגיוניים עסקית ותואמים למציאות.

### עדכון 1: סידור תאריכי יומני אימון
**תיאור השאילתה:** יישור קו לתאריכי האימונים במערכת. הבטחנו שאף תאריך אימון לא יקדם ליום פתיחת המכון (01.01.2024) או ליום ההצטרפות של המתאמן למכון.

<p align="center">
  <b>1. המאגר לפני העדכון:</b><br/>
  <b><img width="1442" height="624" alt="Screenshot 2026-03-23 155151" src="https://github.com/user-attachments/assets/bcc7e5a5-b847-46b6-abe1-147b82e2234f" /></b><br/><br/>
  <b>2. הרצת השאילתה (כולל הקוד וההשפעה):</b><br/>
  <b><img width="1515" height="328" alt="Screenshot 2026-03-23 155232" src="https://github.com/user-attachments/assets/365491e2-3ce0-45bd-954a-5d7107c460a4" /></b><br/><br/>
  <b>3. המאגר אחרי העדכון:</b><br/>
  <b><img width="1439" height="619" alt="Screenshot 2026-03-23 155258" src="https://github.com/user-attachments/assets/1fc8a87c-db62-472c-afe4-e9239f55aa5f" /></b>
</p>

<hr />

### עדכון 2: סידור תאריכי מדידות גוף
**תיאור השאילתה:** בדומה לאימונים, יישור קו לתאריכי המדידות בטבלת `BODY_MEASUREMENT` כך שלא יהיו מדידות לפני הצטרפות המתאמן או פתיחת המכון.

<p align="center">
  <b>1. המאגר לפני העדכון:</b><br/>
  <b><img width="1417" height="622" alt="Screenshot 2026-03-23 155407" src="https://github.com/user-attachments/assets/3b44c13a-c40c-4ca0-a595-3ceeb17e3069" /></b><br/><br/>
  <b>2. הרצת השאילתה (כולל הקוד וההשפעה):</b><br/>
  <b><img width="1513" height="313" alt="Screenshot 2026-03-23 155434" src="https://github.com/user-attachments/assets/8c5975ca-37ae-4923-989e-699c14d150d1" /></b><br/><br/>
  <b>3. המאגר אחרי העדכון:</b><br/>
  <b><img width="1419" height="622" alt="Screenshot 2026-03-23 155522" src="https://github.com/user-attachments/assets/7482ad9b-acb2-4d46-bdde-7ef46f7d75e0" /></b>
</p>

<hr />

### עדכון 3: סידור תאריכי יצירת יעדים
**תיאור השאילתה:** עדכון תאריכי יצירת היעד (`Creation_Date`) בטבלת `TRAINEE_GOAL` כך שיהיו הגיוניים כרונולוגית ביחס למועד רישום המתאמן.

<p align="center">
  <b>1. המאגר לפני העדכון:</b><br/>
  <b><img width="1438" height="623" alt="Screenshot 2026-03-23 155708" src="https://github.com/user-attachments/assets/0f3531cf-a801-438e-9bab-415240b9db4d" /></b><br/><br/>
  <b>2. הרצת השאילתה (כולל הקוד וההשפעה):</b><br/>
  <b><img width="1516" height="320" alt="Screenshot 2026-03-23 155840" src="https://github.com/user-attachments/assets/5f767e71-e274-48b2-80e6-62e0c2b5b020" /></b><br/><br/>
  <b>3. המאגר אחרי העדכון:</b><br/>
  <b><img width="1438" height="623" alt="Screenshot 2026-03-23 155914" src="https://github.com/user-attachments/assets/ebcb0de9-9dbe-4b09-a440-037134fb9cc7" /></b>
</p>

<hr />

### עדכון 4: חישוב תאריכי יעד סופיים
**תיאור השאילתה:** חישוב דינמי של תאריכי היעד (`Target_Date`) ביחס ישיר לתאריך יצירת המטרה (טווח אקראי של 30 עד 365 ימים קדימה).

<p align="center">
  <b>1. המאגר לפני העדכון:</b><br/>
  <b><img width="1438" height="623" alt="Screenshot 2026-03-23 155914" src="https://github.com/user-attachments/assets/ebcb0de9-9dbe-4b09-a440-037134fb9cc7" /></b><br/><br/>
  <b>2. הרצת השאילתה (כולל הקוד וההשפעה):</b><br/>
  <b><img width="1515" height="225" alt="Screenshot 2026-03-23 160040" src="https://github.com/user-attachments/assets/0fc0c4b8-5758-4408-9c4f-acbbf693c528" /></b><br/><br/>
  <b>3. המאגר אחרי העדכון:</b><br/>
  <b><img width="1439" height="622" alt="Screenshot 2026-03-23 160124" src="https://github.com/user-attachments/assets/2202df2d-6482-40ea-bdb2-48b928ca3ef0" /></b>
</p>

<hr />

### עדכון 5: הקצאת לוקרים לפי מגדר
**תיאור השאילתה:** מתקן הקצאות לוקרים שגויות על ידי הבטחה שמתאמנים גברים מועברים לחדר ההלבשה לגברים, ומתאמנות נשים מועברות לחדר ההלבשה לנשים, תוך הצלבה עם טבלת הפרופילים.

<p align="center">
  <b>1. המאגר לפני העדכון:</b><br/>
  <b><img width="846" height="624" alt="Screenshot 2026-03-23 160447" src="https://github.com/user-attachments/assets/9cc24c35-51f8-475f-acf5-e3fd816a03d8" /></b><br/><br/>
  <b>2. הרצת השאילתה (כולל הקוד וההשפעה):</b><br/>
  <b><img width="1518" height="462" alt="Screenshot 2026-03-23 160510" src="https://github.com/user-attachments/assets/271370c4-ac15-48df-84a2-e8c4556006a9" /></b><br/><br/>
  <b>3. המאגר אחרי העדכון:</b><br/>
  <b><img width="847" height="625" alt="Screenshot 2026-03-23 160555" src="https://github.com/user-attachments/assets/ba142c32-7099-4546-a9ef-200f83a302a4" /></b>
</p>

<hr />

### עדכון 6: חישוב דינמי לעמידה ביעדים
**תיאור השאילתה:** שאילתה מורכבת המשתמשת בתת-שאילתה מתואמת ו-`COALESCE` לבדיקה האם המדידה האחרונה של המתאמן, שבוצעה *לפני* או ביום תאריך היעד שלו, עומדת ביעדי המשקל ואחוז השומן שהציב לעצמו.

<p align="center">
  <b>1. המאגר לפני העדכון:</b><br/>
  <b><img width="1440" height="622" alt="Screenshot 2026-03-23 160739" src="https://github.com/user-attachments/assets/a82bd287-fd96-46a3-900e-3fd632b3591c" /></b><br/><br/>
  <b>2. הרצת השאילתה (כולל הקוד וההשפעה):</b><br/>
  <b><img width="1516" height="562" alt="Screenshot 2026-03-23 163731" src="https://github.com/user-attachments/assets/32d61acc-29b1-489a-a5b8-30324fe9f9d7" /></b><br/><br/>
  <b>3. המאגר אחרי העדכון:</b><br/>
  <b><img width="1439" height="620" alt="Screenshot 2026-03-23 163801" src="https://github.com/user-attachments/assets/c5a4ffa0-76a4-4e51-893b-918d9656be81" /></b>
</p>

<hr />

## חלק ג': ניקוי נתונים (DELETE)

### מחיקה 1: מחיקת אימוני דמו ביום שיפוצים
**תיאור השאילתה:** מחיקת אימונים שהוזנו בטעות ביום בו המכון היה סגור לשיפוצים (15.08.2024), אך ורק למתאמנים שהצטרפו באותה שנה. השאילתה מפרקת תאריך ליום, חודש ושנה בנפרד.

<p align="center">
  <b>1. המאגר לפני המחיקה (הנתונים קיימים):</b><br/>
  <b><img width="1465" height="461" alt="Screenshot 2026-03-23 164109" src="https://github.com/user-attachments/assets/42cd98be-9fdc-44ad-a2ac-6688d50e7e8d" /></b><br/><br/>
  <b>2. הרצת השאילתה (כולל הקוד וההשפעה):</b><br/>
  <b><img width="1515" height="391" alt="Screenshot 2026-03-23 164143" src="https://github.com/user-attachments/assets/b95e61d4-32fc-47c0-ad1d-f8aef38b711e" /></b><br/><br/>
  <b>3. המאגר אחרי המחיקה (הנתונים הוסרו):</b><br/>
  <b><img width="1460" height="507" alt="Screenshot 2026-03-23 164207" src="https://github.com/user-attachments/assets/d7fb7d7a-b198-4f9e-b1ef-df98bb65976f" /></b>
</p>

<hr />

### מחיקה 2: הסרת מדידות חריגות (Outliers)
**תיאור השאילתה:** הסרת מדידות גוף שגויות מעל 115 ק"ג עבור מתאמנות נשים בלבד, לצורך ניקוי רעשים סטטיסטיים והבטחת איכות הנתונים.

<p align="center">
  <b>1. המאגר לפני המחיקה (הנתונים קיימים):</b><br/>
  <b><img width="1513" height="775" alt="Screenshot 2026-03-23 164546" src="https://github.com/user-attachments/assets/c9e9c9de-606c-4f5b-8caa-584ac2d6b692" /></b><br/><br/>
  <b>2. הרצת השאילתה (כולל הקוד וההשפעה):</b><br/>
  <b><img width="1516" height="339" alt="Screenshot 2026-03-23 164631" src="https://github.com/user-attachments/assets/f94e2543-7ab4-4954-b8d7-0036ba37d9c0" /></b><br/><br/>
  <b>3. המאגר אחרי המחיקה (הנתונים הוסרו):</b><br/>
  <b><img width="1514" height="784" alt="Screenshot 2026-03-23 164655" src="https://github.com/user-attachments/assets/6cdbdc80-c5b6-44cd-9eac-f80ccac1dae8" /></b>
</p>

<hr />

### מחיקה 3: ניקוי יעדים למשתמשים לא פעילים
**תיאור השאילתה:** ניהול אחסון חכם - מחיקת יעדים אישיים (מטבלת `TRAINEE_GOAL`) עבור מתאמנים המוגדרים כלא פעילים, כלומר, לא תיעדו אף אימון מתחילת שנת 2026.

<p align="center">
  <b>1. המאגר לפני המחיקה (ישנן 500 רשומות בטבלת היעדים):</b><br/>
  <b><img width="97" height="28" alt="Screenshot 2026-03-23 165257" src="https://github.com/user-attachments/assets/ef3c93f9-f7d8-4175-b3a6-9489288be584" /></b><br/><br/>
  <b>2. הרצת השאילתה (כולל הקוד וההשפעה):</b><br/>
  <b><img width="1518" height="330" alt="Screenshot 2026-03-23 165340" src="https://github.com/user-attachments/assets/753c8ef2-7684-43ce-89d7-020b61223230" /></b><br/><br/>
  <b>3. המאגר אחרי המחיקה (נותרו רק 497 רשומות):</b><br/>
  <b><img width="92" height="30" alt="Screenshot 2026-03-23 165359" src="https://github.com/user-attachments/assets/d418ece4-7034-4a2e-bac9-85918e80c501" /></b>
</p>

<hr />

## חלק ד' 1: שאילתות שליפה (SELECT) כפולות - השוואת יעילות

בפרק זה יצרנו 4 שאילתות בשתי תצורות שונות (Method A ו-Method B) במטרה להשוות ולנתח את היעילות שלהן.

### שאילתה 1: חילוץ מדידת המשקל הנמוכה ביותר 
**תיאור השאילתה:** מציאת המדידה הטובה ביותר של מתאמן ספציפי (לפי ה-ID שלו).

* **דרך א' (תת-שאילתה עם MIN):** פחות יעילה. מסד הנתונים מבצע שתי סריקות נפרדות - אחת למציאת משקל המינימום ואחת לשליפת הרשומה עצמה.
* **דרך ב' (מיון ORDER BY ו-LIMIT) - המנצחת:** יעילה משמעותית. מסד הנתונים ממיין את התוצאות ושולף מיד את השורה הראשונה, מה שחוסך את הסריקה הכפולה.

<p align="center">
  <b>הרצה ותוצאה - דרך א':</b><br/>
  <b><img width="1522" height="441" alt="Screenshot 2026-03-23 165537" src="https://github.com/user-attachments/assets/a8635086-6533-4636-ac0e-e16bd4738457" /></b><br/><br/>
  <b>הרצה ותוצאה - דרך ב':</b><br/>
  <b><img width="1520" height="301" alt="Screenshot 2026-03-23 165610" src="https://github.com/user-attachments/assets/3b658237-4fd4-4a7b-a2f1-ce532a731b0d" /></b>
</p>

<hr />

### שאילתה 2: רשימת תרגילים בתוכנית 
**תיאור השאילתה:** שליפת כל התרגילים, הסטים והחזרות עבור תוכנית אימון מסוימת.

* **דרך א' (שימוש ב-JOIN) - המנצחת:** פועלת כפעולה אחת ממוטבת היטב.
* **דרך ב' (שימוש ב-IN עם תת-שאילתות):** מציגה Anti-Pattern. עבור כל תרגיל המערכת מריצה 2 תת-שאילתות נפרדות, מה שיוצר עומס אדיר לעומת פעולת `JOIN` פשוטה.

<p align="center">
  <b>הרצה ותוצאה - דרך א':</b><br/>
  <b><img width="1521" height="502" alt="Screenshot 2026-03-23 181517" src="https://github.com/user-attachments/assets/883b3c9e-4181-4e83-b33e-46717369b8c6" /></b><br/><br/>
  <b>הרצה ותוצאה - דרך ב':</b><br/>
  <b><img width="1521" height="599" alt="Screenshot 2026-03-23 181652" src="https://github.com/user-attachments/assets/03df1180-35f2-4572-8991-a499844b51be" /></b>
</p>

<hr />

### שאילתה 3: מתאמנים פעילים בחודש ספציפי
**תיאור השאילתה:** איתור מתאמנים שביצעו לפחות אימון אחד בפברואר 2025.

* **דרך א' (שימוש ב-JOIN ו-DISTINCT):** פחות יעילה. יוצרת טבלה זמנית ענקית עם כפילויות לפני הסינון.
* **דרך ב' (שימוש ב-EXISTS) - המנצחת:** מתוכננת לעצירה מוקדמת (Short-circuit). ברגע שנמצא אימון אחד, המנוע עובר מיד למתאמן הבא וחוסך זמן עיבוד יקר.

<p align="center">
  <b>הרצה ותוצאה - דרך א':</b><br/>
  <b><img width="1522" height="462" alt="Screenshot 2026-03-23 181739" src="https://github.com/user-attachments/assets/a92c90c3-6f7d-42e6-95b6-087722224c6b" /></b><br/><br/>
  <b>הרצה ותוצאה - דרך ב':</b><br/>
  <b><img width="1518" height="575" alt="Screenshot 2026-03-23 182142" src="https://github.com/user-attachments/assets/6f38670b-e750-4795-bd2e-3ee732ac50bc" /></b>
</p>


<hr />

### שאילתה 4: כמות לוקרים למתאמני VIP
**תיאור השאילתה:** סופרת כמה לוקרים בסך הכל מוחזקים על ידי מתאמנים שיש להם לפחות לוקר VIP אחד.

* **דרך א' (JOIN, GROUP BY, ותת-שאילתת IN) - המנצחת:** מייצרת רשימה מסוננת אחת מראש ומבצעת חיבור ממוטב.
* **דרך ב' (תת-שאילתות מתואמות):** מדגימה את בעיית ה-"N+1" – עבור כל מתאמן בטבלה, מורצות תת-שאילתות נפרדות שוב ושוב לבדיקת הרשאת ה-VIP ולספירת הלוקרים.

<p align="center">
  <b>הרצה ותוצאה - דרך א':</b><br/>
  <b><img width="1520" height="700" alt="Screenshot 2026-03-23 183023" src="https://github.com/user-attachments/assets/60f05c16-9140-4bdc-bd9a-8c80d6ce93b4" /></b><br/><br/>
  <b>הרצה ותוצאה - דרך ב':</b><br/>
  <b><img width="1517" height="686" alt="Screenshot 2026-03-23 183101" src="https://github.com/user-attachments/assets/2c5b756c-8130-429b-88ba-a1b65bfd59d4" /></b>
</p>

<hr />

## חלק ד' 2: שאילתות שליפה (SELECT) מורכבות

### שאילתה 5: סיכום שריפת קלוריות ודופק לפי חודשים
**תיאור השאילתה:** אנליזה חודשית המציגה כמות אימונים, סך קלוריות וממוצע דופק בשנת 2026 בעזרת קיבוץ (`GROUP BY`) ופונקציות צבירה.

<p align="center">
  <b>השאילתה והתוצאה:</b><br/>
  <b><img width="1521" height="526" alt="Screenshot 2026-03-23 183650" src="https://github.com/user-attachments/assets/5de3e63f-b294-4442-88b1-1515a94a0e1b" /></b>
</p>

<hr />

### שאילתה 6: חשיפה לתביעות (ניהול סיכונים משפטי)
**תיאור השאילתה:** איתור מתאמנים עם לוקר פעיל אך עם הצהרת בריאות שפגת תוקף. עושה שימוש ב-JOIN משולש וחיסור תאריכים להצגת "ימים בסיכון".

<p align="center">
  <b>השאילתה והתוצאה:</b><br/>
  <b><img width="1513" height="693" alt="Screenshot 2026-03-23 185223" src="https://github.com/user-attachments/assets/1422ce8d-de7d-4d24-8610-3472224c0f1b" /></b>
</p>

<hr />

### שאילתה 7: ציר זמן - התקדמות מדידות גוף
**תיאור השאילתה:** שליפת ההיסטוריה המלאה של המתאמן, ממוינת מהעדכני ביותר לישן ביותר, לצורך בניית גרף התקדמות.

<p align="center">
  <b>השאילתה והתוצאה:</b><br/>
  <b><img width="1519" height="620" alt="Screenshot 2026-03-23 185306" src="https://github.com/user-attachments/assets/62e8480c-8fef-4fc8-9b9d-cc69a04370d1" /></b>
</p>

<hr />

### שאילתה 8: פופולריות של תוכניות אימון בפועל
**תיאור השאילתה:** דירוג תוכניות אימון לפי כמות הביצועים וסך הדקות. שימוש ב-`LEFT JOIN` להצגת תוכניות שלא בוצעו מעולם, ו-`COALESCE` להמרת ערכי עמודות ריקות ל-0.

<p align="center">
  <b>השאילתה והתוצאה:</b><br/>
  <b><img width="1521" height="602" alt="Screenshot 2026-03-23 185349" src="https://github.com/user-attachments/assets/f24cea2f-918d-470f-96db-7704e7875b56" /></b>
</p>

<hr />

## חלק ה': ניהול עסקאות (Transactions) - COMMIT / ROLLBACK

במערכות מידע, קריטי לוודא שעדכונים מתבצעים בשלמותם כדי למנוע השחתת נתונים. השתמשנו בבלוקים של עסקאות כדי לבחון שינויים "על יבש".

### תסריט 1: ביטול תהליך בעזרת ROLLBACK
**תיאור:** עדכון תאריך לידה למתאמן בתוך טרנזקציה. לאחר שווידאנו שהנתון השתנה בזיכרון הזמני, הפעלנו פקודת `ROLLBACK` כדי לבטל את התהליך ולהחזיר את המסד למצבו התקין.

<p align="center">
  <b>1. לפני התהליך (הנתון המקורי):</b><br/>
  <b><img width="375" height="321" alt="Screenshot 2026-03-22 160812" src="https://github.com/user-attachments/assets/f19d9569-b825-4c5d-93cd-5cd823c04c51" /></b><br/><br/>
  <b>2. בתוך הבלוק, לפני הביטול (הנתון השתנה זמנית):</b><br/>
  <b><img width="378" height="383" alt="Screenshot 2026-03-22 160912" src="https://github.com/user-attachments/assets/fd32ff8f-49de-49cc-b9a5-6eba6db447a3" /></b><br/><br/>
  <b>3. אחרי ה-ROLLBACK (חזר למצב המקורי):</b><br/>
  <b><img width="374" height="288" alt="Screenshot 2026-03-22 160950" src="https://github.com/user-attachments/assets/94c20e3b-204b-4283-b0ff-f1667c1f184b" /></b>
</p>

<hr />

### תסריט 2: שמירת תהליך בעזרת COMMIT
**תיאור:** עדכון תאריך הצטרפות למתאמן בתוך טרנזקציה. הפעם, הרצנו פקודת `COMMIT` בסיום כדי לאשר סופית את השינוי ולצרוב אותו במסד הנתונים.

<p align="center">
  <b>1. לפני התהליך (הנתון המקורי):</b><br/>
  <b><img width="339" height="242" alt="Screenshot 2026-03-22 163458" src="https://github.com/user-attachments/assets/62c262cf-192c-46fe-b086-8e3baed31666" /></b><br/><br/>
  <b>2. בתוך הבלוק, לאחר העדכון:</b><br/>
  <b><img width="347" height="381" alt="Screenshot 2026-03-22 163656" src="https://github.com/user-attachments/assets/4d634b04-1971-404d-b687-ca967cb0af3f" /></b><br/><br/>
  <b>3. אחרי ה-COMMIT (הנתון נשמר סופית):</b><br/>
  <b><img width="345" height="295" alt="Screenshot 2026-03-22 163908" src="https://github.com/user-attachments/assets/56856dd2-25f4-423d-a1ba-65a2f322529a" /></b>
</p>


# 🔗 שלב ג': שילוב מערכות (Integration) ויצירת תצוגות (Views)

## חלק 1: החלטות ארכיטקטוניות ותהליך ה-ETL

### 1.1 החלטות ארכיטקטוניות מרכזיות בשילוב
במהלך השילוב של שתי המערכות הישנות (**מערכת א' - ניהול פיננסי** ו-**מערכת ב' - ניהול כושר ואימונים**), התקבלו מספר החלטות ארכיטקטוניות קריטיות כדי להבטיח סקלאביליות, נרמול (Normalization) ותחזוקה לטווח ארוך.

#### 1. אסטרטגיית שילוב Greenfield (אפשרות ג')
במקום למזג מערכת אחת ישירות לתוך השנייה, אימצנו גישת **Greenfield** - עיצוב סכמה מאוחדת וחדשה לחלוטין וייבוא הנתונים לתוכה.
החלטה זו עזרה לנו:
* למנוע חוב טכני מצטבר.
* לתקן חוסר עקביות לוגית מהמערכות הישנות.
* להסיר תלויות בעייתיות (כמו הצימוד הישן בין ניהול לוקרים לתפריטי תזונה).
* ליצור מבנה מסד נתונים מנורמל ונקי יותר.

#### 2. הפרדת תחומי אחריות משתמשים (Single Responsibility Principle)
במקום לתחזק טבלת משתמשים אחת עמוסה ("מפלצתית"), ישות המשתמש פוצלה לשתי טבלאות ייעודיות ביחס של **1:1**:
* `core_user`: שומרת נתוני זהות ופרטי קשר בלבד.
* `trainee_metadata`: שומרת מידע ביולוגי, דמוגרפי ומידע הקשור לאימונים.
הפרדה זו שיפרה משמעותית את התחזוקה והנרמול במערכת.

#### 3. המערכת הפיננסית כמקור האמת (Source of Truth)
במקרי התנגשות נתונים בין המערכות, **מערכת א' (פיננסית)** נבחרה כמקור הסמכות:
* מתאמנים שהיו קיימים במערכת ב' ללא רישום פיננסי תואם סוננו החוצה.
* תאריכי תחילת מנוי נגזרו בעיקר מתאריך הרכישה החוקי המוקדם ביותר.
* נמנעה לחלוטין יצירת רשומות יתומות (Orphan records) במהלך המיגרציה.

#### 4. תאריך עוגן קבוע לחישובי זמן
מכיוון שנתוני הדמו משתרעים על השנים **2020-2024**, קבענו תאריך עוגן קבוע לפרויקט:
```sql
DATE '2024-01-01'
```
במקום להסתמך על התאריך הנוכחי. זה מבטיח ש:
* בדיקות פקיעת מנוי יישארו רלוונטיות.
* חישובי גיל יפיקו תוצאות הגיוניות ומציאותיות.
* הפלטים של נתוני הדמו יישארו עקביים והדירים לאורך זמן ללא תלות ביום בדיקת הפרויקט.

---

### 1.2 סקירת תהליך ה-ETL (Extract, Transform, Load)
תהליך השילוב פעל לפי מתודולוגיית **ETL מבוססת Staging** מובנית וחולק לשלושה שלבים עיקריים:

#### א. שלב ה-Staging (השהייה)
ייצוא CSV גולמי משתי מערכות המקור יובא לטבלאות זמניות (Staging tables) שקיבלו את הקידומת:
```sql
temp_
```
מאפייני הטבלאות הזמניות:
* ללא מפתחות זרים (Foreign Keys).
* ללא אילוצי מערכת (Constraints).
* נתונים גולמיים לחלוטין ללא אימות.
הדבר איפשר עיבוד מקדים ובטוח לפני ההכנסה של הנתונים לסכמה הסופית.

#### ב. שלב ההתמרה והטעינה (Transform & Load)
סקריפטים להתמרת נתונים יושמו באמצעות פעולות אצווה של `INSERT INTO ... SELECT`.

**התמרות עיקריות שבוצעו:**
* **המרת תאריכים מפורשת (`::DATE`):** שימשה להמרת ערכי טקסט שיובאו באופן שגוי לשדות תאריך חוקיים.
* **פתרון קונפליקטים בעזרת `COALESCE()`:** פונקציה זו שימשה לתיעדוף ערכים חוקיים ותקינים בין שתי המערכות במקרה של שדות חסרים (NULL).
* **איחוד מפתחות זרים:** המזהים מהמערכות הישנות (`Customer_ID`, `Trainee_ID`) אוחדו למפתח רציף, אחיד וחדש בשם: `User_ID`.

#### ג. שלב הניקוי (Cleanup)
לאחר מיגרציה ואימות מוצלחים, כל טבלאות ה-Staging הזמניות הוסרו לחלוטין מן המסד באמצעות פקודת:
```sql
DROP TABLE
```
זה הבטיח שמסד הנתונים בסביבת הייצור יישאר נקי, קל וממוטב.

<hr />

## חלק 2: תצוגות מסד נתונים ושאילתות משולבות

### תצוגה 1: מחלקת כספים (מערכת א')
**תיאור התצוגה:** תוכננה במיוחד עבור מחלקת הכספים וניהול המנויים. היא מציגה מנויים פעילים בלבד, פרטי קשר, פרטי חוזה, וחישוב דינמי של ימי המנוי הנותרים. 
**שילוב טבלאות:** התצוגה משלבת את הטבלאות `core_user` ו-`subscription`.

**קוד SQL ליצירת התצוגה:**
```sql
CREATE OR REPLACE VIEW vw_active_subscriptions AS
SELECT
    cu.user_id,
    cu.first_name || ' ' || cu.last_name AS full_name,
    cu.phone_number,
    s.contract_number,
    s.purchase_date,
    s.expiration_date,
    s.total_cost,
    (s.expiration_date - DATE '2024-01-01') AS days_remaining
FROM public.core_user cu
JOIN public.subscription s
    ON cu.user_id = s.user_id
WHERE s.expiration_date >= DATE '2024-01-01';
```

**שאילתה 1: פקיעת מנויים קרובה**
שליפת לקוחות שהמנוי שלהם יפוג ב-30 הימים הקרובים. מאפשר למחלקת המכירות של המכון ליצור קשר יזום לחידוש המנוי.
```sql
SELECT
    full_name,
    phone_number,
    days_remaining
FROM vw_active_subscriptions
WHERE days_remaining <= 30
  AND days_remaining >= 0
ORDER BY days_remaining ASC;
```

**שאילתה 2: תחזית הכנסות מחידושים חודשיים**
קיבוץ מנויים פעילים לפי חודש פקיעה וחישוב הערך הכולל הצפוי מחידושים, לטובת בניית תחזית הכנסות להנהלה.
```sql
SELECT
    EXTRACT(MONTH FROM expiration_date) AS expiration_month,
    COUNT(contract_number) AS total_active_contracts,
    SUM(total_cost) AS total_value
FROM vw_active_subscriptions
GROUP BY EXTRACT(MONTH FROM expiration_date)
ORDER BY expiration_month;
```

<hr />

### תצוגה 2: מחלקת כושר ואימונים (מערכת ב')
**תיאור התצוגה:** ריכוז כל המידע הקריטי הנדרש למאמני חדר הכושר. משלבת מידע דמוגרפי, יעדי כושר, חישוב גיל נוכחי ונתוני אישור רפואי.
**שילוב טבלאות:** התצוגה מאחדת את `core_user`, `trainee_metadata`, ו-`health_declaration`.

**קוד SQL ליצירת התצוגה:**
```sql
CREATE OR REPLACE VIEW vw_trainee_fitness_profile AS
SELECT
    cu.user_id,
    cu.first_name,
    cu.last_name,
    tm.gender,
    tm.main_goal,
    EXTRACT(YEAR FROM AGE(DATE '2024-01-01', tm.date_of_birth)) AS age,
    hd.doctor_name,
    hd.limitations_notes,
    hd.is_valid AS medical_clearance
FROM public.core_user cu
JOIN public.trainee_metadata tm
    ON cu.user_id = tm.user_id
LEFT JOIN public.health_declaration hd
    ON cu.user_id = hd.user_id;
```

**שאילתה 1: פילוח קהל יעד (תוכנית הרזיה)**
איתור מתאמנים בני 40 ומעלה שהיעד המרכזי שלהם הוא ירידה במשקל (Weight Loss) ובעלי אישור רפואי בתוקף. משמש להזמנת מועמדים לתוכניות ייעודיות.
```sql
SELECT
    first_name,
    last_name,
    age,
    main_goal
FROM vw_trainee_fitness_profile
WHERE age >= 40
  AND main_goal = 'Weight Loss'
  AND medical_clearance = 1;
```

**שאילתה 2: אכיפת בטיחות רפואית**
שאילתת בקרת בטיחות קריטית. שולפת מתאמנים שהצהרת הבריאות שלהם חסרה או אינה בתוקף, במטרה למנוע פעילות אימון מסכנת חיים.
```sql
SELECT
    user_id,
    first_name,
    last_name,
    limitations_notes
FROM vw_trainee_fitness_profile
WHERE medical_clearance = 0
   OR medical_clearance IS NULL;
```

<hr />

### תצוגה 3: תפעול ולוגיסטיקה (שילוב מערכות מלא)
**תיאור התצוגה:** מדגימה את אחד היתרונות הגדולים של שילוב המערכות - היכולת לחבר תשתית ציוד פיזית עם נתוני זהות הלקוח. מציגה מידע על לוקרים, מיקומם, ושם/אימייל של המתאמן.
**שילוב טבלאות:** התצוגה משלבת את `locker` ו-`core_user`.

**קוד SQL ליצירת התצוגה:**
```sql
CREATE OR REPLACE VIEW vw_locker_utilization AS
SELECT
    l.locker_id,
    l.location_zone,
    l.rental_end_date,
    cu.user_id,
    cu.first_name || ' ' || cu.last_name AS occupant_name,
    cu.email
FROM public.locker l
LEFT JOIN public.core_user cu
    ON l.user_id = cu.user_id;
```

**שאילתה 1: לוקרים זמינים באזור הבריכה**
איתור כל הלוקרים הפנויים (ללא מתאמן מוקצה) הממוקמים באזור הבריכה (Pool Area), לשירות צוות הקבלה.
```sql
SELECT
    locker_id,
    location_zone
FROM vw_locker_utilization
WHERE occupant_name IS NULL
  AND location_zone = 'Pool Area';
```

**שאילתה 2: אכיפת השכרת לוקרים שפגה תוקף**
מזהה לוקרים שתקופת ההשכרה שלהם הסתיימה ביחס לתאריך העוגן של הפרויקט. שולפת את כתובות האימייל של הלקוחות הרלוונטיים כדי לאפשר פנייה ישירה בנושא פינוי הציוד.
```sql
SELECT
    locker_id,
    occupant_name,
    email,
    rental_end_date
FROM vw_locker_utilization
WHERE rental_end_date < DATE '2024-01-01'
AND occupant_name IS NOT NULL;
```

# 🧠 שלב ד': תכנות מסד נתונים (PL/pgSQL)

בשלב זה מימשנו לוגיקה עסקית מורכבת ישירות בתוך מסד הנתונים באמצעות שפת **PL/pgSQL**. הקוד מכסה את כל האלמנטים הנדרשים: סמנים מפורשים ומובלעים, Ref Cursor, פקודות DML, הסתעפויות, לולאות, חריגות ורשומות.

<hr />

## 🛠️ טיוב נתונים — AlterTable.sql

קובץ זה מכיל **6 שאילתות SQL** המנקות לוגית את כל הנתונים שהגיעו מתהליך האינטגרציה, ומייצרות בסיס נתוני אמין לפני הרצת קוד ה-PL/pgSQL.

### עדכון 1: סנכרון תאריכי יומן אימון

מעדכן את `log_date` בטבלת `workout_log` כך שכל תאריך אימון יהיה לאחר תאריך עוגן המערכת (`2024-01-01`) ולאחר תאריך ההצטרפות של המתאמן. השאילתה מחשבת מחדש תאריך הגיוני תוך שימור הפיזור היחסי המקורי בין הרשומות.

```sql
UPDATE public.workout_log wl
SET log_date = GREATEST(DATE '2024-01-01', cu.join_date) + 
               ((wl.log_date - DATE '2020-01-01')::int % 365) * INTERVAL '1 day'
FROM public.core_user cu
WHERE wl.user_id = cu.user_id
  AND (wl.log_date < DATE '2024-01-01' OR wl.log_date < cu.join_date);
```

### עדכון 2: סנכרון תאריכי מדידות גוף

אותו עיקרון על טבלת `body_measurement`. מבטיח שאף מדידה לא תקדם להצטרפות המתאמן או לפתיחת המכון.

```sql
UPDATE public.body_measurement bm
SET measurement_date = GREATEST(DATE '2024-01-01', cu.join_date) + 
                       ((bm.measurement_date - DATE '2020-01-01')::int % 365) * INTERVAL '1 day'
FROM public.core_user cu
WHERE bm.user_id = cu.user_id
  AND (bm.measurement_date < DATE '2024-01-01' OR bm.measurement_date < cu.join_date);
```

### עדכון 3: סנכרון תאריכי יעדים

מעדכן את `creation_date` ו-`target_date` בטבלת `trainee_goal` עבור כל שורה שתאריכיה קדומים לתאריך ההצטרפות או לתאריך העוגן. `target_date` מוגדר כ-180 יום לאחר תאריך הגיוני של יצירת היעד.

```sql
UPDATE public.trainee_goal tg
SET creation_date = GREATEST(DATE '2024-01-01', cu.join_date),
    target_date   = GREATEST(DATE '2024-01-01', cu.join_date) + INTERVAL '180 days'
FROM public.core_user cu
WHERE tg.user_id = cu.user_id
  AND (tg.creation_date < DATE '2024-01-01' OR tg.creation_date < cu.join_date);
```

### עדכון 4: יציבות גובה (Height Stabilization)

נתוני הגובה של אותו מתאמן יכולים להשתנות ברשומות שונות (כשגיאת ייצוא). השאילתה מחשבת גובה ממוצע לכל מתאמן ומשווה את כל שורותיו לאותו הגובה היציב.

```sql
WITH height_anchor AS (
    SELECT
        user_id,
        ROUND(AVG(height_cm), 1) AS stable_height
    FROM public.body_measurement
    GROUP BY user_id
)
UPDATE public.body_measurement bm
SET height_cm = ha.stable_height
FROM height_anchor ha
WHERE bm.user_id = ha.user_id
  AND bm.height_cm <> ha.stable_height;
```

### עדכון 5: החלקת משקלים (Weight Stabilization)

הנתונים מכילים קפיצות משקל בלתי הגיוניות בין מדידות עוקבות. שימוש בפונקציות חלון `ROW_NUMBER()` ו-`FIRST_VALUE()` ליצירת ירידה הדרגתית וחלקה של 0.3% בין כל מדידה ומדידה.

```sql
WITH ordered_measurements AS (
    SELECT
        measurement_id,
        user_id,
        measurement_date,
        weight_kg,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY measurement_date) AS rn,
        FIRST_VALUE(weight_kg) OVER (PARTITION BY user_id ORDER BY measurement_date) AS first_weight
    FROM public.body_measurement
),
smoothed AS (
    SELECT
        measurement_id,
        ROUND(
            first_weight * POWER(0.997, rn - 1)::numeric,
            2
        ) AS smoothed_weight
    FROM ordered_measurements
)
UPDATE public.body_measurement bm
SET weight_kg = s.smoothed_weight
FROM smoothed s
WHERE bm.measurement_id = s.measurement_id
  AND bm.weight_kg <> s.smoothed_weight;
```

### עדכון 6: סנכרון BMI (BMI Synchronization)

לאחר ייצוב המשקל והגובה, מחשבים מחדש את `bmi_score` לפי הנוסחה הרפואית הסטנדרטית `משקל / (גובה_במטרים)^2`. השאילתה מעדכנת רק שורות שבהן ה-BMI אינו תואם את הערכים המעודכנים.

```sql
UPDATE public.body_measurement
SET bmi_score = ROUND(
    weight_kg / POWER(height_cm / 100.0, 2),
    1
)
WHERE height_cm > 0
  AND bmi_score IS DISTINCT FROM ROUND(
    weight_kg / POWER(height_cm / 100.0, 2),
    1
  );
```

<hr />

## ⚡ טריגר 1: אימות תאריך השכרת לוקר

**קובץ:** `trigger1.sql` | **טבלה:** `locker` | **אירוע:** `BEFORE INSERT OR UPDATE`

טריגר זה מגן על שלמות נתוני ההשכרה בטבלת `locker`. בכל הכנסה או עדכון של שורה, מתבצעות הבדיקות הבאות:

- **אימות קיום משתמש:** שליפת `join_date` מטבלת `core_user` באמצעות Implicit Cursor (`SELECT INTO`). אם המשתמש לא קיים — `RAISE EXCEPTION`.
- **אימות עתידיות תאריך:** `rental_end_date` חייב להיות לאחר `2024-01-01`.
- **אימות ביחס לתאריך הצטרפות:** `rental_end_date` חייב להיות לאחר `join_date` של המשתמש.

האלמנטים של PL/pgSQL שמשמשים: Implicit Cursor, Record, Branching (IF/THEN), Exception.

```sql
CREATE OR REPLACE FUNCTION public.trg_func_locker_rental_future_date()
RETURNS trigger
LANGUAGE plpgsql
AS $$
DECLARE
    v_join_date DATE;
BEGIN
    IF NEW.user_id IS NOT NULL AND NEW.rental_end_date IS NOT NULL THEN
        SELECT join_date INTO v_join_date
        FROM public.core_user
        WHERE user_id = NEW.user_id;

        IF v_join_date IS NULL THEN
            RAISE EXCEPTION 'Locker assignment failed: user_id % does not exist in core_user.', NEW.user_id;
        END IF;

        IF NEW.rental_end_date <= DATE '2024-01-01' THEN
            RAISE EXCEPTION 'Locker assignment failed: rental_end_date (%) must be after the system anchor date 2024-01-01.', NEW.rental_end_date;
        END IF;

        IF NEW.rental_end_date <= v_join_date THEN
            RAISE EXCEPTION 'Locker assignment failed: rental_end_date (%) cannot be on or before the user join_date (%).', NEW.rental_end_date, v_join_date;
        END IF;
    END IF;

    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_locker_rental_future_date ON public.locker;

CREATE TRIGGER trg_locker_rental_future_date
BEFORE INSERT OR UPDATE ON public.locker
FOR EACH ROW
EXECUTE FUNCTION public.trg_func_locker_rental_future_date();
```

**בדיקה מוצעת — הפרת האילוץ:**
```sql
UPDATE public.locker
SET rental_end_date = '2020-01-01', user_id = 1
WHERE locker_id = 3;
```

**תוצאה צפויה:** `ERROR: Locker assignment failed: rental_end_date (2020-01-01) must be after the system anchor date 2024-01-01.`

<hr />

## ⚡ טריגר 2: אימות יומן אימון

**קובץ:** `trigger2.sql` | **טבלה:** `workout_log` | **אירוע:** `BEFORE INSERT OR UPDATE`

טריגר המגן על אמינות נתוני יומן האימון. בכל הכנסה או עדכון:

- שולף נתוני המשתמש לתוך **Record** (`v_user_rec`) באמצעות Implicit Cursor.
- בודק שה-`log_date` אינו קדמוני לתאריך ההצטרפות ולתאריך העוגן.
- מאמת שציון הפידבק (`trainee_feedback_rating`) בין 1 ל-10.

האלמנטים של PL/pgSQL שמשמשים: Implicit Cursor, Record, Branching (IF/THEN/ELSIF), Exception.

```sql
CREATE OR REPLACE FUNCTION public.trg_func_workout_log_date_check()
RETURNS trigger
LANGUAGE plpgsql
AS $$
DECLARE
    v_join_date DATE;
    v_user_rec  RECORD;
BEGIN
    SELECT user_id, join_date INTO v_user_rec
    FROM public.core_user
    WHERE user_id = NEW.user_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Workout log rejected: user_id % does not exist.', NEW.user_id;
    END IF;

    v_join_date := v_user_rec.join_date;

    IF NEW.log_date < v_join_date THEN
        RAISE EXCEPTION 'Workout log rejected: log_date (%) is before the user join_date (%) for user_id %.', NEW.log_date, v_join_date, NEW.user_id;
    END IF;

    IF NEW.log_date < DATE '2024-01-01' THEN
        RAISE EXCEPTION 'Workout log rejected: log_date (%) is before the system anchor date 2024-01-01.', NEW.log_date;
    END IF;

    IF NEW.trainee_feedback_rating < 1 OR NEW.trainee_feedback_rating > 10 THEN
        RAISE EXCEPTION 'Workout log rejected: trainee_feedback_rating (%) must be between 1 and 10.', NEW.trainee_feedback_rating;
    END IF;

    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_workout_log_date_check ON public.workout_log;

CREATE TRIGGER trg_workout_log_date_check
BEFORE INSERT OR UPDATE ON public.workout_log
FOR EACH ROW
EXECUTE FUNCTION public.trg_func_workout_log_date_check();
```

**בדיקה מוצעת — הפרת האילוץ:**
```sql
INSERT INTO public.workout_log
  (log_id, log_date, duration_minutes, total_calories_burned,
   average_heart_rate, trainee_feedback_rating, coach_notes, program_id, user_id)
VALUES
  (99999, '2019-06-01', 60, 400, 130, 7, 'Test', 1, 1);
```

**תוצאה צפויה:** `ERROR: Workout log rejected: log_date (2019-06-01) is before the system anchor date 2024-01-01.`

<hr />

## 📦 פרוצדורה 1: הארכת חוזי לוקרים פגי תוקף

**קובץ:** `procedure1.sql` | **פקודה:** `CALL public.proc_extend_expiring_lockers();`

פרוצדורה המבצעת עדכון המוני של לוקרים שתאריך פקיעתם נמצא בתוך 90 הימים הראשונים מתאריך העוגן. לכל לוקר כזה מחושב תאריך הארכה חדש בהתאם לקרבת הפקיעה.

**אלמנטים של PL/pgSQL:**

| אלמנט | יישום |
| :--- | :--- |
| Explicit Cursor | `CURSOR FOR SELECT` הסורק לוקרים עם תאריך פקיעה בחלון זמן מוגדר |
| Loop | `LOOP / FETCH / EXIT WHEN NOT FOUND` — איטרציה רשומה-רשומה |
| Branching | `IF / ELSIF / ELSE` — קביעת משך הארכה (365 / 180 / 90 יום) |
| DML | `UPDATE public.locker SET rental_end_date = ...` לכל רשומה |
| Record | `v_locker_rec RECORD` לשמירת נתוני כל לוקר |

```sql
CREATE OR REPLACE PROCEDURE public.proc_extend_expiring_lockers()
LANGUAGE plpgsql
AS $$
DECLARE
    v_locker_rec RECORD;
    v_cursor CURSOR FOR
        SELECT l.locker_id, l.user_id, l.rental_end_date, cu.join_date
        FROM public.locker l
        JOIN public.core_user cu ON l.user_id = cu.user_id
        WHERE l.rental_end_date IS NOT NULL
          AND l.rental_end_date BETWEEN DATE '2024-01-01' AND DATE '2024-01-01' + INTERVAL '90 days';
    v_count INT := 0;
    v_new_end_date DATE;
BEGIN
    OPEN v_cursor;
    LOOP
        FETCH v_cursor INTO v_locker_rec;
        EXIT WHEN NOT FOUND;

        IF v_locker_rec.rental_end_date < DATE '2024-01-01' + INTERVAL '30 days' THEN
            v_new_end_date := v_locker_rec.rental_end_date + INTERVAL '365 days';
        ELSIF v_locker_rec.rental_end_date < DATE '2024-01-01' + INTERVAL '60 days' THEN
            v_new_end_date := v_locker_rec.rental_end_date + INTERVAL '180 days';
        ELSE
            v_new_end_date := v_locker_rec.rental_end_date + INTERVAL '90 days';
        END IF;

        UPDATE public.locker
        SET rental_end_date = v_new_end_date
        WHERE locker_id = v_locker_rec.locker_id;

        v_count := v_count + 1;
        RAISE NOTICE 'Locker % (user %): extended from % to %',
            v_locker_rec.locker_id, v_locker_rec.user_id,
            v_locker_rec.rental_end_date, v_new_end_date;
    END LOOP;
    CLOSE v_cursor;

    RAISE NOTICE 'proc_extend_expiring_lockers complete: % lockers updated.', v_count;
END;
$$;
```

<hr />

## 📦 פרוצדורה 2: זיהוי ועדכון יעדים שהושגו

**קובץ:** `procedure2.sql` | **פקודה:** `CALL public.proc_award_achieved_goals();`

פרוצדורה העוברת על כל היעדים הלא-מושגים ובודקת אם המדידה האחרונה לפני תאריך היעד עומדת ביעדי המשקל ואחוז השומן. אם כן — מסמנת את היעד כמושג.

**אלמנטים של PL/pgSQL:**

| אלמנט | יישום |
| :--- | :--- |
| Implicit Cursor | לולאת `FOR v_goal_rec IN SELECT ...` |
| Record | `v_goal_rec RECORD` לשמירת נתוני כל יעד |
| Exception | בלוק `BEGIN / EXCEPTION WHEN OTHERS / END` בתוך כל איטרציה |
| Branching | `IF NOT FOUND` ו-`IF v_last_weight <= ...` |
| DML | `UPDATE public.trainee_goal SET is_achieved = 1` |

```sql
CREATE OR REPLACE PROCEDURE public.proc_award_achieved_goals()
LANGUAGE plpgsql
AS $$
DECLARE
    v_goal_rec   RECORD;
    v_last_weight   numeric(5,2);
    v_last_fat      numeric(4,1);
    v_updated_count INT := 0;
    v_error_count   INT := 0;
BEGIN
    FOR v_goal_rec IN
        SELECT tg.goal_id, tg.user_id, tg.target_date,
               tg.target_weight_kg, tg.target_fat_percentage, tg.is_achieved
        FROM public.trainee_goal tg
        WHERE tg.is_achieved = 0
          AND tg.target_date <= DATE '2024-01-01' + INTERVAL '365 days'
    LOOP
        BEGIN
            SELECT bm.weight_kg, bm.fat_percentage
            INTO v_last_weight, v_last_fat
            FROM public.body_measurement bm
            WHERE bm.user_id = v_goal_rec.user_id
              AND bm.measurement_date <= v_goal_rec.target_date
            ORDER BY bm.measurement_date DESC
            LIMIT 1;

            IF NOT FOUND THEN
                RAISE EXCEPTION 'No measurement found for user % before target_date %',
                    v_goal_rec.user_id, v_goal_rec.target_date;
            END IF;

            IF v_last_weight <= v_goal_rec.target_weight_kg AND
               v_last_fat <= v_goal_rec.target_fat_percentage THEN
                UPDATE public.trainee_goal
                SET is_achieved = 1
                WHERE goal_id = v_goal_rec.goal_id;

                v_updated_count := v_updated_count + 1;
                -- התיקון בוצע בשורה הבאה: נוסף % עבור המשתנה לפני ה-%%
                RAISE NOTICE 'Goal % for user % ACHIEVED (weight: %, fat: % %%)',
                    v_goal_rec.goal_id, v_goal_rec.user_id, v_last_weight, v_last_fat;
            END IF;

        EXCEPTION
            WHEN OTHERS THEN
                v_error_count := v_error_count + 1;
                RAISE NOTICE 'Skipping goal % for user %: %',
                    v_goal_rec.goal_id, v_goal_rec.user_id, SQLERRM;
        END;
    END LOOP;

    RAISE NOTICE 'proc_award_achieved_goals done. Updated: %, Skipped: %.', v_updated_count, v_error_count;
END;
$$;
```

<hr />

## 🔢 פונקציה 1: סטטיסטיקות אימון למשתמש

**קובץ:** `function1.sql` | **קריאה:** `SELECT * FROM public.fn_user_workout_stats(1);`

פונקציה המחשבת ומחזירה שורת סיכום אחת עם כל הסטטיסטיקות של משתמש מיומני האימון שלו.

**אלמנטים של PL/pgSQL:**

| אלמנט | יישום |
| :--- | :--- |
| Implicit Cursor | `SELECT ... INTO` עם פונקציות צבירה (`COUNT`, `SUM`, `AVG`, `MAX`) |
| Branching | `IF v_total_sessions = 0 THEN RAISE NOTICE` |
| Record Variables | 7 משתני `DECLARE` נפרדים המאוכלסים בשאילתה אחת |
| RETURNS TABLE | מבנה טבלאי עם 7 שדות מוגדרים |

```sql
CREATE OR REPLACE FUNCTION public.fn_user_workout_stats(p_user_id INT)
RETURNS TABLE(
    total_sessions     INT,
    total_minutes      numeric(10,2),
    total_calories     BIGINT,
    avg_heart_rate     numeric(6,2),
    avg_rating         numeric(4,2),
    best_rating        INT,
    most_recent_log    DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_total_sessions  INT;
    v_total_minutes   numeric(10,2);
    v_total_calories  BIGINT;
    v_avg_heart_rate  numeric(6,2);
    v_avg_rating      numeric(4,2);
    v_best_rating     INT;
    v_most_recent     DATE;
BEGIN
    SELECT
        COUNT(*)::INT,
        COALESCE(SUM(duration_minutes), 0),
        COALESCE(SUM(total_calories_burned)::BIGINT, 0),
        COALESCE(ROUND(AVG(average_heart_rate), 2), 0),
        COALESCE(ROUND(AVG(trainee_feedback_rating), 2), 0),
        COALESCE(MAX(trainee_feedback_rating), 0),
        MAX(log_date)
    INTO
        v_total_sessions, v_total_minutes, v_total_calories,
        v_avg_heart_rate, v_avg_rating, v_best_rating, v_most_recent
    FROM public.workout_log
    WHERE user_id = p_user_id;

    IF v_total_sessions = 0 THEN
        RAISE NOTICE 'No workout logs found for user_id %.', p_user_id;
    END IF;

    total_sessions  := v_total_sessions;
    total_minutes   := v_total_minutes;
    total_calories  := v_total_calories;
    avg_heart_rate  := v_avg_heart_rate;
    avg_rating      := v_avg_rating;
    best_rating     := v_best_rating;
    most_recent_log := v_most_recent;

    RETURN NEXT;
END;
$$;
```

<hr />

## 🔢 פונקציה 2: היסטוריית מדידות גוף (Ref Cursor)

**קובץ:** `function2.sql` | **קריאה:** ראה `main_program2.sql`

פונקציה המחזירה **Ref Cursor** המכיל את כל היסטוריית המדידות של מתאמן, כולל חישוב הפרש המשקל בין מדידה ומדידה באמצעות פונקציית חלון `LAG()`.

**אלמנטים של PL/pgSQL:**

| אלמנט | יישום |
| :--- | :--- |
| Explicit Cursor | לולאה פנימית הסורקת מדידות ומדפיסה הודעה עבור מדידות מעל 100 ק"ג |
| Record | `v_meas_rec RECORD` בתוך הלולאה הפנימית |
| Branching | `IF v_meas_rec.weight_kg > 100 THEN RAISE NOTICE` |
| Ref Cursor | `OPEN v_ref FOR SELECT ...` עם `LAG()` — מוחזר לקורא |

```sql
CREATE OR REPLACE FUNCTION public.fn_trainee_progress_cursor(p_user_id INT)
RETURNS refcursor
LANGUAGE plpgsql
AS $$
DECLARE
    v_ref refcursor := 'trainee_progress_cursor';
    v_meas_rec  RECORD;
    v_explicit_cursor CURSOR FOR
        SELECT measurement_id, measurement_date, weight_kg
        FROM public.body_measurement
        WHERE user_id = p_user_id
        ORDER BY measurement_date;
BEGIN
    FOR v_meas_rec IN v_explicit_cursor LOOP
        IF v_meas_rec.weight_kg > 100 THEN
            RAISE NOTICE 'Measurement % on % is heavy: % kg',
                v_meas_rec.measurement_id,
                v_meas_rec.measurement_date,
                v_meas_rec.weight_kg;
        END IF;
    END LOOP;

    OPEN v_ref FOR
        SELECT
            bm.measurement_date,
            bm.weight_kg,
            bm.fat_percentage,
            bm.muscle_mass_kg,
            bm.bmi_score,
            bm.waist_circumference_cm,
            LAG(bm.weight_kg) OVER (ORDER BY bm.measurement_date) AS prev_weight,
            ROUND(bm.weight_kg - LAG(bm.weight_kg) OVER (ORDER BY bm.measurement_date), 2) AS weight_delta
        FROM public.body_measurement bm
        WHERE bm.user_id = p_user_id
        ORDER BY bm.measurement_date;

    RETURN v_ref;
END;
$$;
```

<hr />

## 🚀 תוכנית ראשית 1

**קובץ:** `main_program1.sql` | **הרצה:** הדבקה ישירה ב-Supabase SQL Editor

בלוק אנונימי (`DO $$`) המשמש כ"מנהל תהליכים" הקורא לפרוצדורה ולפונקציה ומדפיס דוח מסכם.

**זרימת הביצוע:**

1. קריאה ל-`proc_extend_expiring_lockers` באמצעות `CALL`.
2. קריאה ל-`fn_user_workout_stats` עבור `user_id = 1`, שמירת התוצאה ב-`RECORD`.
3. הסתעפות `IF/ELSIF/ELSE` הקובעת רמת פעילות: `INACTIVE` / `BEGINNER` / `REGULAR` / `VETERAN`.
4. הדפסת דוח מפורט באמצעות `RAISE NOTICE`.

**אלמנטים של PL/pgSQL:** DML (CALL), Record, Branching (IF/ELSIF/ELSE), Implicit Cursor (SELECT INTO), Raise Notice.

```sql
DO $$
DECLARE
    v_stats_rec RECORD;
    v_target_user_id INT := 1;
    v_label TEXT;
BEGIN
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Running procedure: proc_extend_expiring_lockers';
    RAISE NOTICE '========================================';

    CALL public.proc_extend_expiring_lockers();

    RAISE NOTICE '';
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Running function: fn_user_workout_stats for user_id = %', v_target_user_id;
    RAISE NOTICE '========================================';

    SELECT * INTO v_stats_rec
    FROM public.fn_user_workout_stats(v_target_user_id);

    IF v_stats_rec.total_sessions = 0 THEN
        v_label := 'INACTIVE';
    ELSIF v_stats_rec.total_sessions < 5 THEN
        v_label := 'BEGINNER';
    ELSIF v_stats_rec.total_sessions < 20 THEN
        v_label := 'REGULAR';
    ELSE
        v_label := 'VETERAN';
    END IF;

    RAISE NOTICE 'User % Workout Summary:', v_target_user_id;
    RAISE NOTICE '  Status         : %', v_label;
    RAISE NOTICE '  Total Sessions : %', v_stats_rec.total_sessions;
    RAISE NOTICE '  Total Minutes  : %', v_stats_rec.total_minutes;
    RAISE NOTICE '  Total Calories : %', v_stats_rec.total_calories;
    RAISE NOTICE '  Avg Heart Rate : %', v_stats_rec.avg_heart_rate;
    RAISE NOTICE '  Avg Rating     : %', v_stats_rec.avg_rating;
    RAISE NOTICE '  Best Rating    : %', v_stats_rec.best_rating;
    RAISE NOTICE '  Last Workout   : %', v_stats_rec.most_recent_log;
    RAISE NOTICE '========================================';
    RAISE NOTICE 'main_program1 finished successfully.';
END;
$$;
```

<hr />

## 🚀 תוכנית ראשית 2

**קובץ:** `main_program2.sql` | **הרצה:** הדבקה ישירה ב-Supabase SQL Editor

בלוק אנונימי שני המדגים עיבוד מלא של **Ref Cursor** בתוך לולאה.

**זרימת הביצוע:**

1. קריאה ל-`proc_award_achieved_goals` באמצעות `CALL`.
2. קריאה ל-`fn_trainee_progress_cursor` עבור `user_id = 1`, קבלת `refcursor`.
3. לולאת `LOOP / FETCH / EXIT WHEN NOT FOUND` — איטרציה שורה-שורה על תוצאות הסמן.
4. הסתעפות המפרשת את `weight_delta` לסטטוס: `FIRST RECORD` / `LOSING` / `GAINING` / `STABLE`.
5. בלוק `BEGIN / EXCEPTION / END` סביב כל עיבוד הסמן לטיפול בשגיאות.
6. סגירת הסמן `CLOSE v_ref` בסיום מוצלח.

**אלמנטים של PL/pgSQL:** DML (CALL), Ref Cursor, Record, Loop (FETCH), Branching, Exception Handling, Raise Notice.

```sql
DO $$
DECLARE
    v_ref        refcursor;
    v_row        RECORD;
    v_row_count  INT := 0;
    v_target_user_id INT := 1;
    v_trend TEXT;
BEGIN
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Running procedure: proc_award_achieved_goals';
    RAISE NOTICE '========================================';

    CALL public.proc_award_achieved_goals();

    RAISE NOTICE '';
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Running function: fn_trainee_progress_cursor for user_id = %', v_target_user_id;
    RAISE NOTICE '========================================';

    BEGIN
        v_ref := public.fn_trainee_progress_cursor(v_target_user_id);

        LOOP
            FETCH v_ref INTO v_row;
            EXIT WHEN NOT FOUND;

            v_row_count := v_row_count + 1;

            IF v_row.weight_delta IS NULL THEN
                v_trend := 'FIRST RECORD';
            ELSIF v_row.weight_delta < 0 THEN
                v_trend := 'LOSING';
            ELSIF v_row.weight_delta > 0 THEN
                v_trend := 'GAINING';
            ELSE
                v_trend := 'STABLE';
            END IF;

            -- התיקון בוצע כאן: Fat: % %%
            RAISE NOTICE '[Row %] Date: % | Weight: % kg | Fat: % %% | BMI: % | Delta: % kg | Trend: %',
                v_row_count,
                v_row.measurement_date,
                v_row.weight_kg,
                v_row.fat_percentage,
                v_row.bmi_score,
                COALESCE(v_row.weight_delta::TEXT, 'N/A'),
                v_trend;
        END LOOP;

        CLOSE v_ref;

    EXCEPTION
        WHEN OTHERS THEN
            RAISE NOTICE 'Error while processing refcursor for user %: %', v_target_user_id, SQLERRM;
    END;

    IF v_row_count = 0 THEN
        RAISE NOTICE 'No body measurements found for user_id %.', v_target_user_id;
    ELSE
        RAISE NOTICE 'Total measurement rows processed: %', v_row_count;
    END IF;

    RAISE NOTICE '========================================';
    RAISE NOTICE 'main_program2 finished successfully.';
END;
$$;
```
