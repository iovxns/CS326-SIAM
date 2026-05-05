# KPI Metrics Report

This report summarizes actual measurements collected from application logs.

---

## Raw Data Summary

### Registration
- Total attempts: 2
- Successful: 2
- Failed: 0

---

### Login
- Total attempts: 4
- Successful: 2
- Failed: 2

Breakdown:
- Invalid credentials failures: 2

---

### Profile Update
- Total attempts: 2
- Successful: 0
- Failed: 2
- Failure reason: Name too short

---

## KPI Results

### 1. Login Success Rate
= 2 / 4 × 100  
= **50%**

---

### 2. Registration Success Rate
= 2 / 2 × 100  
= **100%**

---

### 3. Profile Update Failure Rate
= 2 / 2 × 100  
= **100%**

---

### 4. Invalid Credential Rate
= 2 / 4 × 100  
= **50%**

---

##  Analysis

- Login system shows moderate success (50%), with failures caused by invalid credentials.
- Registration system is stable with no observed failures.
- Profile update validation is strict, causing all attempts to fail due to short input ("a").
- System usage is consistent across sessions, indicating repeated user interaction patterns.

---

## Suggested Improvements

- Improve login UX by distinguishing between wrong password vs non-existent user.
- Add password strength or username validation during registration.
- Improve profile update validation feedback (show minimum length requirements clearly).
- Consider logging user session IDs for more detailed KPI segmentation.