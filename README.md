<div align="center">
  <h1>🏋️‍♂️ PowerGym Pro - Database Project</h1>
  <p><b>מערכת מתקדמת לניהול מתאמנים, מדדי גוף ותוכניות אימון</b></p>
  
  <img src="https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge&logo=supabase" alt="Supabase" />
  <img src="https://img.shields.io/badge/Scripts-Python-3776AB?style=for-the-badge&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/SQL-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql" alt="PostgreSQL" />
</div>

<br />

## 📋 פרטי ההגשה

| שם מגיש | תעודת זהות | תפקיד/חלק בפרויקט |
| :--- | :---: | :--- |
| **ישראל ישראלי** | 3553 | ארכיטקטורת נתונים וכתיבת סקריפטים (Python) |
| **משה כהן** | 4459 | עיצוב מסד הנתונים, ERD ואילוצי SQL |

* **היחידה הנבחרת מתוך המערכת:** ניהול ומעקב אישי - מתאמנים, מדדי גוף, תוכניות ויומני אימון.

<hr />

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
  <img src="LINK_TO_DASHBOARD_IMAGE" width="600" alt="Trainee Dashboard" />
  <br />
  <i>מסך דשבורד מתאמן המציג את תמונת המצב העדכנית</i>
</p>

<details>
  <summary><b>לחץ כאן לצפייה בשאר מסכי המערכת</b></summary>
  <br/>
  <p align="center">
    <img src="LINK_TO_MEASUREMENTS_IMAGE" width="45%" alt="Measurements" />
    <img src="LINK_TO_PROGRAM_IMAGE" width="45%" alt="Workout Program" />
  </p>
</details>

<hr />

## 🗺️ תרשימי אפיון

### תרשים ERD (מושגי)
<p align="center">
  <img src="LINK_TO_ERD_IMAGE" width="800" alt="ERD Diagram" />
</p>

### תרשים DSD (לוגי)
<p align="center">
  <img src="LINK_TO_DSD_IMAGE" width="800" alt="DSD Diagram" />
</p>

<hr />

## 🧠 החלטות עיצוב וארכיטקטורה
1. **קישור ישיר לקבוצות שריר:** החלטנו לפשט את מבנה התרגילים ולוותר על טבלת קשר מיותרת. במקום זאת, ישות ה-`MUSCLE_GROUP` מקושרת ישירות כישות אב לטבלת ה-`EXERCISE`.
2. **ניהול מרובה סרטונים:** אפשרנו קשר של יחיד לרבים (1:N) בין תרגיל לסרטוני הדרכה, מתוך הבנה שלתרגיל מורכב עשויות להיות מספר וריאציות.
3. **אבטחת איכות נתונים (Constraints):** הוגדרו אילוצי `CHECK` קשיחים (כמו ווידוא ציון BMI בטווח הגיוני של 10-60).

<hr />

## ⚙️ שיטות הכנסת נתונים
כדי למלא את מסד הנתונים בכמויות המידע הנדרשות (מעל 40,000 שורות סך הכל), השתמשנו ב-3 שיטות שונות:

1. **תכנות (Python Scripts):** יצירת יומני אימון ומדידות גוף בעזרת סקריפטים שמייצאים קבצי CSV.
2. **מחולל נתונים חיצוני (Mockaroo):** יצירת מידע אקראי מציאותי כמו שמות והצהרות בריאות.
3. **הכנסה ידנית ב-SQL:** כתיבת שאילתות ידניות עבור טבלאות תשתית קטנות.

<p align="center">
  <img src="LINK_TO_DATA_INSERT_IMAGE" width="600" alt="Data Insertion" />
</p>

<hr />

## 🛡️ גיבוי ושחזור נתונים
<details>
  <summary><b>הצג צילומי מסך של תהליך הגיבוי והשחזור</b></summary>
  <br/>
  <p align="center">
    <b>גיבוי:</b><br/>
    <img src="LINK_TO_BACKUP_IMAGE" width="600" alt="Backup Process" />
    <br/><br/>
    <b>שחזור:</b><br/>
    <img src="LINK_TO_RESTORE_IMAGE" width="600" alt="Restore Process" />
  </p>
</details>
