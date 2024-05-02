

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

