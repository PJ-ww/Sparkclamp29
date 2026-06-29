# Data Specification – Part 1

## Complete Data Dictionary

### A. Traceability & Identity

| Column        | Data Type | Description                      | Business Rule                 | Target Layer |
| ------------- | --------- | -------------------------------- | ----------------------------- | ------------ |
| record_type   | String    | ประเภทของข้อมูล                  | ต้องไม่เป็นค่าว่าง            | Raw, Staging |
| entity_id     | String    | รหัสประจำ Record                 | Primary Business Key, ห้ามซ้ำ | ทุก Layer    |
| snapshot_date | Date      | วันที่ Snapshot                  | ต้องเป็นวันที่ถูกต้อง         | ทุก Layer    |
| student_no    | String    | รหัสนักศึกษา                     | ต้องไม่ซ้ำ                    | Trusted      |
| citizen_id    | String    | เลขประจำตัวประชาชน (ข้อมูลจำลอง) | ใช้เพื่ออ้างอิง               | Raw          |
| email         | String    | อีเมล                            | รูปแบบ Email                  | Trusted      |
| mobile        | String    | เบอร์โทรศัพท์                    | ตัวเลข 10 หลัก                | Trusted      |
| student_name  | String    | ชื่อ–นามสกุล                     | ต้องไม่เป็นค่าว่าง            | Trusted      |

---

### B. Academic Information

| Column             | Data Type | Description      | Business Rule            | Target    |
| ------------------ | --------- | ---------------- | ------------------------ | --------- |
| level              | String    | ระดับการศึกษา    | Undergraduate / Graduate | Analytics |
| faculty_or_school  | String    | คณะหรือสำนัก     | ใช้จัดกลุ่ม              | Analytics |
| program_id         | String    | รหัสหลักสูตร     | ต้องไม่ว่าง              | Trusted   |
| program_name       | String    | ชื่อหลักสูตร     | ใช้แสดงผล                | Analytics |
| discipline_cluster | String    | กลุ่มสาขาวิชา    | ใช้แบ่งประเภท            | Analytics |
| campus             | String    | วิทยาเขต         | ใช้วิเคราะห์ตาม Campus   | Analytics |
| year_of_study      | Integer   | ชั้นปี           | 1–8                      | Analytics |
| admission_channel  | String    | ช่องทางรับเข้า   | ใช้จัดกลุ่ม              | Analytics |
| status             | String    | สถานะนักศึกษา    | Active / Inactive        | Analytics |
| gpa                | Decimal   | เกรดเฉลี่ย       | 0.00–4.00                | Trusted   |
| credit_earned      | Integer   | หน่วยกิตสะสม     | ≥ 0                      | Trusted   |
| is_international   | Boolean   | นักศึกษาต่างชาติ | True / False             | Analytics |

---

### C. Analytics Dataset

| Column         | Type    | Description                |
| -------------- | ------- | -------------------------- |
| fact_category  | String  | หมวดข้อมูลสำหรับ Analytics |
| metric_or_item | String  | ตัวชี้วัด                  |
| value          | Decimal | ค่าของตัวชี้วัด            |
| unit           | String  | หน่วย                      |
| year_or_as_of  | String  | ปีหรือช่วงเวลาของข้อมูล    |

---

### D. Document Information

| Column      | Type   | Description   |
| ----------- | ------ | ------------- |
| doc_title   | String | ชื่อเอกสาร    |
| doc_section | String | หมวดเอกสาร    |
| doc_text    | Text   | เนื้อหาเอกสาร |
| doc_type    | String | ประเภทเอกสาร  |

---

### E. Operational Metadata

| Column                    | Type    | Description             |
| ------------------------- | ------- | ----------------------- |
| batch_date                | Date    | วันที่ประมวลผล          |
| source_system             | String  | ระบบต้นทาง              |
| protection_classification | String  | ระดับการจัดประเภทข้อมูล |
| required_action           | String  | การดำเนินการที่ต้องทำ   |
| task_hint                 | String  | คำแนะนำสำหรับผู้ใช้     |
| source_url                | String  | URL แหล่งข้อมูล         |
| source_row_no             | Integer | ลำดับแถวในไฟล์ต้นฉบับ   |

---

### F. Behavior & Career

| Column                  | Type    | Description                | Analytics |
| ----------------------- | ------- | -------------------------- | --------- |
| behavior_profile        | String  | ลักษณะพฤติกรรม             | ✓         |
| teamwork_style          | String  | รูปแบบการทำงานเป็นทีม      | ✓         |
| learning_preference     | String  | รูปแบบการเรียนรู้          | ✓         |
| career_interest         | String  | อาชีพที่สนใจ               | ✓         |
| expected_salary_thb     | Integer | เงินเดือนที่คาดหวัง        | ✓         |
| salary_expectation_note | Text    | หมายเหตุเกี่ยวกับเงินเดือน | ✓         |
| internship_interest     | String  | ความสนใจฝึกงาน             | ✓         |
| mock_interview_note     | Text    | หมายเหตุการสัมภาษณ์        | ✓         |

---

### G. RAG Document

| Column                   | Type   | Description          | Used For   |
| ------------------------ | ------ | -------------------- | ---------- |
| rag_document_title       | String | ชื่อเอกสารสำหรับ RAG | Retrieval  |
| rag_document_text        | Text   | เนื้อหาหลัก          | Embedding  |
| rag_keywords             | String | คำสำคัญ              | Search     |
| rag_sample_question      | Text   | ตัวอย่างคำถาม        | Testing    |
| rag_expected_answer_hint | Text   | แนวคำตอบที่คาดหวัง   | Evaluation |


# Data Specification – Part 2

## Source to Target Mapping

### Pipeline Overview

```
Excel File
      │
      ▼
Raw Layer
(raw_workshop_data)
      │
      ▼
Staging Layer
(stg_student_snapshot)
      │
      ▼
Trusted Layer
(trusted_student_snapshot)
      │
      ├────────► Analytics
      │
      └────────► RAG
```

---

# 1. Identity & Traceability Mapping

| Source Column | Raw | Staging | Trusted | Analytics | RAG | Transformation  |
| ------------- | :-: | :-----: | :-----: | :-------: | :-: | --------------- |
| record_type   |  ✓  |    ✓    |    ✓    |     ✓     |  -  | No Change       |
| entity_id     |  ✓  |    ✓    |    ✓    |     ✓     |  ✓  | Primary Key     |
| snapshot_date |  ✓  |    ✓    |    ✓    |     ✓     |  ✓  | Date Validation |
| source_row_no |  ✓  |    ✓    |    ✓    |     -     |  ✓  | No Change       |
| student_no    |  ✓  |    ✓    |    ✓    |     ✓     |  ✓  | Trim            |

---

# 2. Student Profile Mapping

| Source       | Raw | Staging | Trusted | Analytics | Transformation |
| ------------ | :-: | :-----: | :-----: | :-------: | -------------- |
| citizen_id   |  ✓  |    ✓    |    ✓    |     -     | Trim           |
| student_name |  ✓  |    ✓    |    ✓    |     ✓     | Trim           |
| email        |  ✓  |    ✓    |    ✓    |     -     | Lowercase      |
| mobile       |  ✓  |    ✓    |    ✓    |     -     | Remove Space   |

---

# 3. Academic Mapping

| Source             | Raw | Staging | Trusted | Analytics | Rule         |
| ------------------ | :-: | :-----: | :-----: | :-------: | ------------ |
| level              |  ✓  |    ✓    |    ✓    |     ✓     | No Change    |
| faculty_or_school  |  ✓  |    ✓    |    ✓    |     ✓     | No Change    |
| program_id         |  ✓  |    ✓    |    ✓    |     ✓     | No Change    |
| program_name       |  ✓  |    ✓    |    ✓    |     ✓     | No Change    |
| discipline_cluster |  ✓  |    ✓    |    ✓    |     ✓     | No Change    |
| campus             |  ✓  |    ✓    |    ✓    |     ✓     | No Change    |
| year_of_study      |  ✓  |    ✓    |    ✓    |     ✓     | Integer      |
| admission_channel  |  ✓  |    ✓    |    ✓    |     ✓     | No Change    |
| status             |  ✓  |    ✓    |    ✓    |     ✓     | No Change    |
| gpa                |  ✓  |    ✓    |    ✓    |     ✓     | Decimal(3,2) |
| credit_earned      |  ✓  |    ✓    |    ✓    |     ✓     | Integer      |
| is_international   |  ✓  |    ✓    |    ✓    |     ✓     | Boolean      |

---

# 4. Behavior Mapping

| Column                  | Trusted | Analytics | RAG |
| ----------------------- | :-----: | :-------: | :-: |
| behavior_profile        |    ✓    |     ✓     |  ✓  |
| teamwork_style          |    ✓    |     ✓     |  ✓  |
| learning_preference     |    ✓    |     ✓     |  ✓  |
| career_interest         |    ✓    |     ✓     |  ✓  |
| internship_interest     |    ✓    |     ✓     |  ✓  |
| expected_salary_thb     |    ✓    |     ✓     |  ✓  |
| salary_expectation_note |    ✓    |     -     |  ✓  |
| mock_interview_note     |    ✓    |     -     |  ✓  |

---

# 5. Document Mapping

| Column      | Trusted | Analytics | RAG |
| ----------- | :-----: | :-------: | :-: |
| doc_title   |    ✓    |     -     |  ✓  |
| doc_section |    ✓    |     -     |  ✓  |
| doc_text    |    ✓    |     -     |  ✓  |
| doc_type    |    ✓    |     -     |  ✓  |

---

# 6. RAG Mapping

| Source                   | Chunk Metadata | Retrieval  |
| ------------------------ | -------------- | ---------- |
| rag_document_title       | ✓              | ✓          |
| rag_document_text        | ✓              | ✓          |
| rag_keywords             | ✓              | ✓          |
| rag_sample_question      | ✓              | Testing    |
| rag_expected_answer_hint | ✓              | Evaluation |

---

# 7. Metadata Mapping

| Column                    | Purpose       |
| ------------------------- | ------------- |
| batch_date                | Partition     |
| source_system             | Audit         |
| source_url                | Citation      |
| task_hint                 | User Guidance |
| protection_classification | Governance    |

---

# 8. New Metadata Generated by Pipeline

| Column              | Generated By |
| ------------------- | ------------ |
| run_id              | Pipeline     |
| load_timestamp      | Pipeline     |
| business_date       | Pipeline     |
| input_file_name     | Pipeline     |
| input_file_checksum | Pipeline     |
| record_status       | Pipeline     |
