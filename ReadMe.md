# 👥 Employee Attrition Analysis

## 📌 Problem Statement

Despite having detailed employee data, the organization lacks clear answers to:

- Which departments and job roles experience the highest attrition?
- Is attrition concentrated among specific age groups or tenure bands?
- Do workload factors such as overtime and business travel contribute to attrition?
- Are early-career employees leaving more frequently than experienced ones?

Without this clarity, HR actions remain reactive and generalized rather than targeted and data-driven.

---

## 📊 Dataset Fields Description

| Field Name | Description |
|------------|-------------|
| Age | Age of the employee in years |
| Attrition | Indicates whether the employee left the organization (0 / 1) |
| BusinessTravel | Frequency of business travel (Non-Travel, Travel Rarely, Travel Frequently) |
| DailyRate | Daily compensation rate of the employee |
| Department | Department where the employee works (e.g., R&D, Sales, HR) |
| DistanceFromHome | Distance between employee’s home and workplace |
| Education | Education level (1: Below College, 2: College, 3: Bachelor, 4: Master, 5: Doctor) |
| EducationField | Field of education (e.g., Life Sciences, Medical, Technical) |
| EnvironmentSatisfaction | Satisfaction with the work environment (1 = Low, 4 = High) |
| Gender | Gender of the employee |
| HourlyRate | Hourly wage of the employee |
| JobInvolvement | Level of involvement in work (1 = Low, 4 = High) |
| JobLevel | Job seniority level (1 = Entry level, higher values = senior roles) |
| JobRole | Specific job role or designation of the employee |
| JobSatisfaction | Satisfaction with the job role (1 = Low, 4 = High) |
| MaritalStatus | Marital status of the employee |
| MonthlyIncome | Monthly salary earned by the employee |
| MonthlyRate | Monthly compensation rate (administrative pay metric) |
| NumCompaniesWorked | Number of companies the employee has worked for previously |
| OverTime | Indicates whether the employee works overtime (Yes / No) |
| PercentSalaryHike | Percentage increase in salary during the last appraisal |
| PerformanceRating | Performance evaluation score of the employee |
| RelationshipSatisfaction | Satisfaction with workplace relationships (1 = Low, 4 = High) |
| StockOptionLevel | Level of stock options granted to the employee |
| TotalWorkingYears | Total professional experience across all companies (in years) |
| TrainingTimesLastYear | Number of training programs attended in the last year |
| WorkLifeBalance | Work-life balance rating (1 = Poor, 4 = Excellent) |
| YearsAtCompany | Number of years the employee has worked at the company |
| YearsInCurrentRole | Number of years in the current role |
| YearsSinceLastPromotion | Number of years since the last promotion |
| YearsWithCurrManager | Number of years working with the current manager |

---

## 📈 Key Performance Indicators (KPIs)

| KPI | Description |
|-----|-------------|
| Attrition Rate (%) | Employees who left ÷ total employees |
| Department Attrition Rate | Attrition within each department |
| Role Attrition Rate | Attrition by job role |
| Early-Tenure Attrition | Attrition within first X years |
| Workload Attrition Index | Attrition linked to overtime & travel |

---

## 🎯 Project Objective

This project analyzes employee attrition patterns to identify:
- High-risk departments and roles
- Key behavioral and workload drivers of attrition
- Early-career employee retention issues
- Actionable insights for HR decision-making