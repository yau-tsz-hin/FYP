from sqlalchemy import create_engine, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import Boolean, Column, ForeignKey, BigInteger, Integer, String, TIMESTAMP, Table, MetaData, update, text, UniqueConstraint
from dotenv import load_dotenv

# 開一個 .env file 去存取敏感資料
from os import getenv as env

# .env file 的內容示範
"""
HOST = host.docker.internal:5432
DATABASE = postgres
USER = postgres
PASSWORD = postgres
"""

# Load .env 的資料
load_dotenv()
db_user = env("USER")
db_password = env("PASSWORD")
db_hostname = env("HOST")
db_database_name = env("DATABASE")

# 連接資料庫URL (此為postgres的預設URL, 使用其他資料庫請更改URL)
engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_hostname}/{db_database_name}", future=True)

metadata = MetaData()
conn = engine.raw_connection()
cursor = conn.cursor()
print(engine)

# 建立 Database Table 示範
# Table名: users
# Column: Column名 (資料類型)
# Column: id (int)
# Column: username (str)
# Column: displayname (str)
# Column: email (str)
# Column: password (str)
# Column: role (str)
# Column: img (str)

"""

1. **Users (使用者)**
   - UserID (使用者ID, PK)
   - Username (使用者名稱)
   - Password (密碼)
   - Email (電子郵件)
   - RoleID (角色ID, FK)

2. **Roles (角色)**
   - RoleID (角色ID, PK)
   - RoleName (角色名稱)

3. **JobSeekers (求職者)**
   - JobSeekerID (求職者ID, PK)
   - UserID (使用者ID, FK)
   - FirstName (名字)
   - LastName (姓氏)
   - Address (地址)
   - Phone (電話)

4. **Employers (雇主)**
   - EmployerID (雇主ID, PK)
   - UserID (使用者ID, FK)
   - CompanyName (公司名稱)
   - Address (地址)
   - Phone (電話)

5. **JobCategories (職位類別)**
   - CategoryID (類別ID, PK)
   - CategoryName (類別名稱)

6. **Jobs (職位)**
   - JobID (職位ID, PK)
   - EmployerID (雇主ID, FK)
   - CategoryID (類別ID, FK)
   - Title (職位標題)
   - Description (職位描述)
   - Requirements (職位要求)
   - Location (工作地點)
   - Salary (薪水)
   - PostedDate (發佈日期)

7. **Applications (申請)**
   - ApplicationID (申請ID, PK)
   - JobSeekerID (求職者ID, FK)
   - JobID (職位ID, FK)
   - ApplicationDate (申請日期)
   - Status (狀態)

8. **Resumes (履歷)**
   - ResumeID (履歷ID, PK)
   - JobSeekerID (求職者ID, FK)
   - ResumeTitle (履歷標題)
   - ResumeContent (履歷內容)
   - LastUpdated (最後更新日期)

9. **Education (教育背景)**
   - EducationID (教育ID, PK)
   - JobSeekerID (求職者ID, FK)
   - Degree (學位)
   - Major (主修)
   - School (學校)
   - GraduationDate (畢業日期)

10. **Experiences (工作經驗)**
    - ExperienceID (經驗ID, PK)
    - JobSeekerID (求職者ID, FK)
    - Title (職稱)
    - Company (公司)
    - Location (工作地點)
    - StartDate (開始日期)
    - EndDate (結束日期)
    - Description (工作描述)

11. **Skills (技能)**
    - SkillID (技能ID, PK)
    - JobSeekerID (求職者ID, FK)
    - SkillName (技能名稱)
    - ProficiencyLevel (熟練程度)

12. **Certificates (證書)**
    - CertificateID (證書ID, PK)
    - JobSeekerID (求職者ID, FK)
    - CertificateName (證書名稱)
    - IssuingOrganization (頒發機構)
    - IssueDate (頒發日期)

13. **Languages (語言能力)**
    - LanguageID (語言ID, PK)
    - JobSeekerID (求職者ID, FK)
    - LanguageName (語言名稱)
    - ProficiencyLevel (熟練程度)

14. **Reviews (評論)**
    - ReviewID (評論ID, PK)
    - UserID (使用者ID, FK)
    - Comment (評論)
    - Rating (評分)
    - Date (日期)

15. **Messages (訊息)**
    - MessageID (訊息ID, PK)
    - SenderID (發送者ID, FK)
    - ReceiverID (接收者ID, FK)
    - MessageContent (訊息內容)
    - Date (日期)
    - Status (狀態)

16. **Reports (檢舉)**
    - ReportID (檢舉ID, PK)
    - ReporterID (檢舉者ID, FK)
    - ReportedUserID (被檢舉者ID, FK)
    - Reason (原因)
    - Date (日期)
    - Status (狀態)

17. **Notifications (通知)**
    - NotificationID (通知ID, PK)
    - UserID (使用者ID, FK)
    - NotificationContent (通知內容)
    - Date (日期)
    - Status (狀態)

18. **Subscriptions (訂閱)**
    - SubscriptionID (訂閱ID, PK)
    - UserID (使用者ID, FK)
    - PlanID (方案ID, FK)
    - StartDate (開始日期)
    - EndDate (結束日期)
    - Status (狀態)

19. **Plans (方案)**
    - PlanID (方案ID, PK)
    - PlanName (方案名稱)
    - Description (描述)
    - Price (價格)

20. **Payments (付款)**
    - PaymentID (付款ID, PK)
    - UserID (使用者ID, FK)
    - PlanID (方案ID, FK)
    - PaymentDate (付款日期)
    - Amount (金額)
    - Status (狀態)

21. **Feedback (回饋)**
    - FeedbackID (回饋ID, PK)
    - UserID (使用者ID, FK)
    - FeedbackContent (回饋內容)
    - Date (日期)
    - Status (狀態)

22. **Events (活動)**
    - EventID (活動ID, PK)
    - EventName (活動名稱)
    - Description (描述)
    - Location (地點)
    - Date

 (日期)

23. **EventRegistrations (活動報名)**
    - RegistrationID (報名ID, PK)
    - EventID (活動ID, FK)
    - UserID (使用者ID, FK)
    - RegistrationDate (報名日期)
    - Status (狀態)

24. **Chats (聊天)**
    - ChatID (聊天ID, PK)
    - SenderID (發送者ID, FK)
    - ReceiverID (接收者ID, FK)
    - Message (訊息)
    - Timestamp (時間戳)

25. **BookmarkJobs (書籤職位)**
    - BookmarkID (書籤ID, PK)
    - JobSeekerID (求職者ID, FK)
    - JobID (職位ID, FK)
    - Date (日期)

26. **FavoriteEmployers (收藏雇主)**
    - FavoriteID (收藏ID, PK)
    - JobSeekerID (求職者ID, FK)
    - EmployerID (雇主ID, FK)
    - Date (日期)

27. **ReportedJobs (檢舉職位)**
    - ReportID (檢舉ID, PK)
    - JobID (職位ID, FK)
    - ReporterID (檢舉者ID, FK)
    - Reason (原因)
    - Date (日期)
    - Status (狀態)

28. **Invitations (邀請)**
    - InvitationID (邀請ID, PK)
    - SenderID (發送者ID, FK)
    - ReceiverID (接收者ID, FK)
    - JobID (職位ID, FK)
    - Date (日期)
    - Status (狀態)

29. **Interviews (面試)**
    - InterviewID (面試ID, PK)
    - JobID (職位ID, FK)
    - JobSeekerID (求職者ID, FK)
    - EmployerID (雇主ID, FK)
    - Date (日期)
    - Status (狀態)

30. **Testimonials (推薦)**
    - TestimonialID (推薦ID, PK)
    - UserID (使用者ID, FK)
    - TestimonialContent (推薦內容)
    - Date (日期)
    - Status (狀態)

31. **Advertisements (廣告)**
    - AdID (廣告ID, PK)
    - AdvertiserID (廣告商ID, FK)
    - AdContent (廣告內容)
    - AdType (廣告類型)
    - StartDate (開始日期)
    - EndDate (結束日期)
    - Status (狀態)

32. **FeedbackReplies (回饋回覆)**
    - ReplyID (回覆ID, PK)
    - FeedbackID (回饋ID, FK)
    - UserID (使用者ID, FK)
    - ReplyContent (回覆內容)
    - Date (日期)
    - Status (狀態)

"""
users = Table(
    "users", metadata,
    Column("UserID", Integer, primary_key=True, autoincrement=True),
    Column("Username", String, unique=True),
    Column("Password", String),
    Column("Email", String),
    Column("RoleID", None, ForeignKey("roles.RoleID")),
)

roles = Table(
    "roles", metadata,
    Column("RoleID", Integer, primary_key=True, autoincrement=True),
    Column("RoleName", String),
)

job_seekers = Table(
    "job_seekers", metadata,
    Column("JobSeekerID", Integer, primary_key=True, autoincrement=True),
    Column("UserID", None, ForeignKey("users.UserID")),
    Column("FirstName", String),
    Column("LastName", String),
    Column("Address", String),
    Column("Phone", String),
)

employers = Table(
    "employers", metadata,
    Column("EmployerID", Integer, primary_key=True, autoincrement=True),
    Column("UserID", None, ForeignKey("users.UserID")),
    Column("CompanyName", String),
    Column("Address", String),
    Column("Phone", String),
)

job_categories = Table(
    "job_categories", metadata,
    Column("CategoryID", Integer, primary_key=True, autoincrement=True),
    Column("CategoryName", String),
)

jobs = Table(
    "jobs", metadata,
    Column("JobID", Integer, primary_key=True, autoincrement=True),
    Column("EmployerID", None, ForeignKey("employers.EmployerID")),
    Column("CategoryID", None, ForeignKey("job_categories.CategoryID")),
    Column("Title", String),
    Column("Description", String),
    Column("Requirements", String),
    Column("Location", String),
    Column("Salary", String),
    Column("PostedDate", TIMESTAMP, server_default=text("now()")),
)

applications = Table(
    "applications", metadata,
    Column("ApplicationID", Integer, primary_key=True, autoincrement=True),
    Column("JobSeekerID", None, ForeignKey("job_seekers.JobSeekerID")),
    Column("JobID", None, ForeignKey("jobs.JobID")),
    Column("ApplicationDate", TIMESTAMP, server_default=text("now()")),
    Column("Status", String),
)

resumes = Table(
    "resumes", metadata,
    Column("ResumeID", Integer, primary_key=True, autoincrement=True),
    Column("JobSeekerID", None, ForeignKey("job_seekers.JobSeekerID")),
    Column("ResumeTitle", String),
    Column("ResumeContent", String),
    Column("LastUpdated", TIMESTAMP, server_default=text("now()")),
)

education = Table(
    "education", metadata,
    Column("EducationID", Integer, primary_key=True, autoincrement=True),
    Column("JobSeekerID", None, ForeignKey("job_seekers.JobSeekerID")),
    Column("Degree", String),
    Column("Major", String),
    Column("School", String),
    Column("GraduationDate", TIMESTAMP),
)

experiences = Table(
    "experiences", metadata,
    Column("ExperienceID", Integer, primary_key=True, autoincrement=True),
    Column("JobSeekerID", None, ForeignKey("job_seekers.JobSeekerID")),
    Column("Title", String),
    Column("Company", String),
    Column("Location", String),
    Column("StartDate", TIMESTAMP),
    Column("EndDate", TIMESTAMP),
    Column("Description", String),
)

skills = Table(
    "skills", metadata,
    Column("SkillID", Integer, primary_key=True, autoincrement=True),
    Column("JobSeekerID", None, ForeignKey("job_seekers.JobSeekerID")),
    Column("SkillName", String),
    Column("ProficiencyLevel", String),
)

certificates = Table(
    "certificates", metadata,
    Column("CertificateID", Integer, primary_key=True, autoincrement=True),
    Column("JobSeekerID", None, ForeignKey("job_seekers.JobSeekerID")),
    Column("CertificateName", String),
    Column("IssuingOrganization", String),
    Column("IssueDate", TIMESTAMP),
)

languages = Table(
    "languages", metadata,
    Column("LanguageID", Integer, primary_key=True, autoincrement=True),
    Column("JobSeekerID", None, ForeignKey("job_seekers.JobSeekerID")),
    Column("LanguageName", String),
    Column("ProficiencyLevel", String),
)

reviews = Table(
    "reviews", metadata,
    Column("ReviewID", Integer, primary_key=True, autoincrement=True),
    Column("UserID", None, ForeignKey("users.UserID")),
    Column("Comment", String),
    Column("Rating", Integer),
    Column("Date", TIMESTAMP),
)

messages = Table(
    "messages", metadata,
    Column("MessageID", Integer, primary_key=True, autoincrement=True),
    Column("SenderID", None, ForeignKey("users.UserID")),
    Column("ReceiverID", None, ForeignKey("users.UserID")),
    Column("MessageContent", String),
    Column("Date", TIMESTAMP),
    Column("Status", String),
)

reports = Table(
    "reports", metadata,
    Column("ReportID", Integer, primary_key=True, autoincrement=True),
    Column("ReporterID", None, ForeignKey("users.UserID")),
    Column("ReportedUserID", None, ForeignKey("users.UserID")),
    Column("Reason", String),
    Column("Date", TIMESTAMP),
    Column("Status", String),
)

notifications = Table(
    "notifications", metadata,
    Column("NotificationID", Integer, primary_key=True, autoincrement=True),
    Column("UserID", None, ForeignKey("users.UserID")),
    Column("NotificationContent", String),
    Column("Date", TIMESTAMP),
    Column("Status", String),
)

subscriptions = Table(
    "subscriptions", metadata,
    Column("SubscriptionID", Integer, primary_key=True, autoincrement=True),
    Column("UserID", None, ForeignKey("users.UserID")),
    Column("PlanID", None, ForeignKey("plans.PlanID")),
    Column("StartDate", TIMESTAMP),
    Column("EndDate", TIMESTAMP),
    Column("Status", String),
)

plans = Table(
    "plans", metadata,
    Column("PlanID", Integer, primary_key=True, autoincrement=True),
    Column("PlanName", String),
    Column("Description", String),
    Column("Price", String),
)

payments = Table(
    "payments", metadata,
    Column("PaymentID", Integer, primary_key=True, autoincrement=True),
    Column("UserID", None, ForeignKey("users.UserID")),
    Column("PlanID", None, ForeignKey("plans.PlanID")),
    Column("PaymentDate", TIMESTAMP),
    Column("Amount", String),
    Column("Status", String),
)

feedback = Table(
    "feedback", metadata,
    Column("FeedbackID", Integer, primary_key=True, autoincrement=True),
    Column("UserID", None, ForeignKey("users.UserID")),
    Column("FeedbackContent", String),
    Column("Date", TIMESTAMP),
    Column("Status", String),
)

events = Table(
    "events", metadata,
    Column("EventID", Integer, primary_key=True, autoincrement=True),
    Column("EventName", String),
    Column("Description", String),
    Column("Location", String),
    Column("Date", TIMESTAMP),
)

event_registrations = Table(
    "event_registrations", metadata,
    Column("RegistrationID", Integer, primary_key=True, autoincrement=True),
    Column("EventID", None, ForeignKey("events.EventID")),
    Column("UserID", None, ForeignKey("users.UserID")),
    Column("RegistrationDate", TIMESTAMP),
    Column("Status", String),
)

chats = Table(
    "chats", metadata,
    Column("ChatID", Integer, primary_key=True, autoincrement=True),
    Column("SenderID", None, ForeignKey("users.UserID")),
    Column("ReceiverID", None, ForeignKey("users.UserID")),
    Column("Message", String),
    Column("Timestamp", TIMESTAMP),
)

bookmark_jobs = Table(
    "bookmark_jobs", metadata,
    Column("BookmarkID", Integer, primary_key=True, autoincrement=True),
    Column("JobSeekerID", None, ForeignKey("job_seekers.JobSeekerID")),
    Column("JobID", None, ForeignKey("jobs.JobID")),
    Column("Date", TIMESTAMP),
)

favorite_employers = Table(
    "favorite_employers", metadata,
    Column("FavoriteID", Integer, primary_key=True, autoincrement=True),
    Column("JobSeekerID", None, ForeignKey("job_seekers.JobSeekerID")),
    Column("EmployerID", None, ForeignKey("employers.EmployerID")),
    Column("Date", TIMESTAMP),
)

reported_jobs = Table(
    "reported_jobs", metadata,
    Column("ReportID", Integer, primary_key=True, autoincrement=True),
    Column("JobID", None, ForeignKey("jobs.JobID")),
    Column("ReporterID", None, ForeignKey("users.UserID")),
    Column("Reason", String),
    Column("Date", TIMESTAMP),
    Column("Status", String),
)

invitations = Table(
    "invitations", metadata,
    Column("InvitationID", Integer, primary_key=True, autoincrement=True),
    Column("SenderID", None, ForeignKey("users.UserID")),
    Column("ReceiverID", None, ForeignKey("users.UserID")),
    Column("JobID", None, ForeignKey("jobs.JobID")),
    Column("Date", TIMESTAMP),
    Column("Status", String),
)

interviews = Table(
    "interviews", metadata,
    Column("InterviewID", Integer, primary_key=True, autoincrement=True),
    Column("JobID", None, ForeignKey("jobs.JobID")),
    Column("JobSeekerID", None, ForeignKey("job_seekers.JobSeekerID")),
    Column("EmployerID", None, ForeignKey("employers.EmployerID")),
    Column("Date", TIMESTAMP),
    Column("Status", String),
)

testimonials = Table(
    "testimonials", metadata,
    Column("TestimonialID", Integer, primary_key=True, autoincrement=True),
    Column("UserID", None, ForeignKey("users.UserID")),
    Column("TestimonialContent", String),
    Column("Date", TIMESTAMP),
    Column("Status", String),
)

advertisements = Table(
    "advertisements", metadata,
    Column("AdID", Integer, primary_key=True, autoincrement=True),
    Column("AdvertiserID", None, ForeignKey("users.UserID")),
    Column("AdContent", String),
    Column("AdType", String),
    Column("StartDate", TIMESTAMP),
    Column("EndDate", TIMESTAMP),
    Column("Status", String),
)

feedback_replies = Table(
    "feedback_replies", metadata,
    Column("ReplyID", Integer, primary_key=True, autoincrement=True),
    Column("FeedbackID", None, ForeignKey("feedback.FeedbackID")),
    Column("UserID", None, ForeignKey("users.UserID")),
    Column("ReplyContent", String),
    Column("Date", TIMESTAMP),
    Column("Status", String),
)





# 如果SQL中 Database Table不存在則建立
metadata.create_all(engine)
#[17:47]
# 用SQL語法來新加資料示範
#stmt = text(f"INSERT INTO likes VALUES({like_user_id}, {like_forum_id}, {like_reply_id}, NULL, {like})")
#with engine.connect() as conn:
#    result = conn.execute(stmt)
#    conn.commit()