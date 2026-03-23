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
