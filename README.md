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
| **יאיר חיים זיו** | 3553 |
| **אמיתי אברהם יושעי** | 4459 |

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
  <img src="https://github.com/user-attachments/assets/1261cfd8-0f36-48ce-a40d-3353fee654e3" width="600" alt="Trainee Dashboard" />
  <br />
  <i>מסך דשבורד מתאמן המציג את תמונת המצב העדכנית</i>
</p>

<details>
  <summary><b>לחץ כאן לצפייה בשאר מסכי המערכת</b></summary>
  <br/>
  <p align="center">
    <img src="https://github.com/user-attachments/assets/fde4bbc7-9786-4aeb-a1b3-44e712f4b2cb" width="45%" alt="Measurements" />
    <img src="https://github.com/user-attachments/assets/f71a9f0d-6a92-42eb-8e79-240615bc0415" width="45%" alt="Workout Program" />
    <img src="https://github.com/user-attachments/assets/ddb79232-1b82-41d2-9846-554a4f93cb30" width="45%" alt="Workout Log" />
  </p>
</details>

<hr />

## 🗺️ תרשימי אפיון

### תרשים ERD (מושגי)
<p align="center">
  <img src="https://github.com/user-attachments/assets/8b04b38b-1800-4935-a9b4-71bf9b871be8" width="800" alt="ERD Diagram" />
</p>

### תרשים DSD (לוגי)
<p align="center">
  <img src="https://github.com/user-attachments/assets/e8915f6c-a453-4dd4-a8cd-f64af687adcf" width="800" alt="DSD Diagram" />
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
  <img src="https://github.com/user-attachments/assets/553bcb60-f615-4712-bcef-c180ffeb5486" width="600" alt="Data Insertion Via Python Scripts" />
</p>
<br/>


### 2. מחולל נתונים חיצוני (Mockaroo)
שימוש בכלי Mockaroo ליצירת מידע אקראי מציאותי. בעזרת מחולל זה יצרנו נתונים אנושיים שקשה לפברק ידנית בכמויות גדולות, כגון שמות מתאמנים, תאריכי לידה והצהרות בריאות.
<p align="center">
  <img src="https://github.com/user-attachments/assets/a45471c0-dfc0-4a4f-a5ee-c5196f63ac7b" width="600" alt="Data Insertion Via Mockaroo Generator" />
</p>
<br/>

### 3. ייבוא נתונים מקבצים (CSV Import)
קליטת נתונים מרוכזת דרך הממשק של מסד הנתונים. יצרנו והכנו מראש קבצי CSV מסודרים המכילים נתוני תשתית ומידע טבלאי, וביצענו להם ייבוא ישיר (Import) לתוך הטבלאות המתאימות במערכת.
<p align="center">
  <img src="https://github.com/user-attachments/assets/1a139102-7e9e-4715-91e7-59a31cb49f6f" width="600" alt="Data Insertion Via CSV" />
</p>

<hr />

## 🛡️ גיבוי ושחזור נתונים
<details>
  <summary><b>הצג צילומי מסך של תהליך הגיבוי והשחזור</b></summary>
  <br/>
  <p align="center">
    <b>גיבוי:</b><br/>
    <img src="https://github.com/user-attachments/assets/241a1901-9aa3-4a82-aa74-038024cee2d7" width="600" alt="Backup Process" />
    <br/><br/>
    <b>שחזור:</b><br/>
    <img src="https://github.com/user-attachments/assets/190bbfc4-4e47-45b8-adf4-2605f4a4c339" width="600" alt="Restore Process" />
  </p>
</details>
