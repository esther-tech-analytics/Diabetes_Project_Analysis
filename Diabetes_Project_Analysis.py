
# DIABETES CAPSTONE PROJECT

# This project answers 15 research questions about diabetes
# using Python, Pandas, and Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# LOAD DATASET

df = pd.read_csv("diabetes_012_health_indicators_BRFSS2015.csv")

print(df.head())

# QUESTION 1
# BMI: What is the average BMI for patients with no diabetes,
# prediabetes, and diabetes?

average_bmi = df.groupby("Diabetes_012")["BMI"].mean()

plt.figure(figsize=(8,6))

ax = average_bmi.plot(
    kind="bar",
    color=["green", "orange", "red"]
)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.3,
        round(bar.get_height(), 2),
        ha="center",
        fontsize=11
    )

plt.title("Average BMI by Diabetes Status")
plt.xlabel("Diabetes Group")
plt.ylabel("Average BMI")

plt.tight_layout()
plt.savefig("Q1_BMI.png")
plt.show()

# QUESTION 2
# Physical Health: What is the average number of physically unhealthy
# days per month for each diabetes group?

physical_health = df.groupby("Diabetes_012")["PhysHlth"].mean()

plt.figure(figsize=(8,6))

physical_health.plot(
    kind="line",
    marker="o",
    linewidth=3,
    color="blue"
)

plt.title("Average Physically Unhealthy Days")
plt.xlabel("Diabetes Group")
plt.ylabel("Average Days")

plt.tight_layout()
plt.savefig("Q2_PhysicalHealth.png")
plt.show()

# QUESTION 3
# Mental Health: What is the average number of poor mental health
# days for each diabetes group?

mental_health = df.groupby("Diabetes_012")["MentHlth"].mean()

plt.figure(figsize=(8,6))

mental_health.plot(
    kind="line",
    marker="o",
    linewidth=3,
    color="purple"
)

plt.title("Average Poor Mental Health Days")
plt.xlabel("Diabetes Group")
plt.ylabel("Average Days")

plt.tight_layout()
plt.savefig("Q3_MentalHealth.png")
plt.show()

# QUESTION 4
# Age: Is the average age higher for patients with diabetes
# compared to those without?

average_age = df.groupby("Diabetes_012")["Age"].mean()

plt.figure(figsize=(8,6))

ax = average_age.plot(
    kind="bar",
    color=["skyblue", "orange", "darkred"]
)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.2,
        round(bar.get_height(), 2),
        ha="center",
        fontsize=11
    )

plt.title("Average Age by Diabetes Status")
plt.xlabel("Diabetes Group")
plt.ylabel("Average Age")

plt.tight_layout()
plt.savefig("Q4_Age.png")
plt.show()

# QUESTION 5
# Difficulty Walking: What percentage of patients in each diabetes
# group have difficulty walking or climbing stairs?

walking = df.groupby("Diabetes_012")["DiffWalk"].mean() * 100

plt.figure(figsize=(8,6))

plt.pie(
    walking,
    labels=["No Diabetes", "Prediabetes", "Diabetes"],
    autopct="%1.1f%%",
    colors=["green", "orange", "red"]
)

plt.title("Difficulty Walking by Diabetes Status")

plt.savefig("Q5_Walking.png")
plt.show()

# QUESTION 6
# General Health: What is the most common self-rated general health
# score for each diabetes group?

general_health = df.groupby("Diabetes_012")["GenHlth"].median()

plt.figure(figsize=(8,6))

ax = general_health.plot(
    kind="bar",
    color=["darkgreen", "gold", "red"]
)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.1,
        round(bar.get_height(), 2),
        ha="center",
        fontsize=11
    )

plt.title("General Health Score")
plt.xlabel("Diabetes Group")
plt.ylabel("Health Score")

plt.tight_layout()
plt.savefig("Q6_GeneralHealth.png")
plt.show()

# QUESTION 7
# Heart Disease: What percentage of patients with diabetes have also
# had a heart disease or heart attack?

heart_disease = df.groupby("Diabetes_012")["HeartDiseaseorAttack"].mean() * 100

plt.figure(figsize=(8,6))

plt.pie(
    heart_disease,
    labels=["No Diabetes", "Prediabetes", "Diabetes"],
    autopct="%1.1f%%",
    colors=["green", "orange", "darkred"]
)

plt.title("Heart Disease by Diabetes Status")

plt.savefig("Q7_HeartDisease.png")
plt.show()

# QUESTION 8
# Stroke: Do patients with diabetes have a higher rate of previous strokes?

stroke = df.groupby("Diabetes_012")["Stroke"].mean() * 100

plt.figure(figsize=(8,6))

ax = stroke.plot(
    kind="bar",
    color=["green", "orange", "red"]
)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.3,
        str(round(bar.get_height(),2)) + "%",
        ha="center",
        fontsize=11
    )

plt.title("Stroke Rate by Diabetes Status")
plt.xlabel("Diabetes Group")
plt.ylabel("Percentage")

plt.tight_layout()
plt.savefig("Q8_Stroke.png")
plt.show()

# QUESTION 9
# Healthcare Access: Is there a difference in healthcare access
# between diabetes groups?

healthcare = df.groupby("Diabetes_012")["AnyHealthcare"].mean() * 100

plt.figure(figsize=(8,6))

plt.pie(
    healthcare,
    labels=["No Diabetes", "Prediabetes", "Diabetes"],
    autopct="%1.1f%%",
    colors=["blue", "purple", "darkblue"]
)

plt.title("Healthcare Access")

plt.savefig("Q9_Healthcare.png")
plt.show()

# QUESTION 10
# Doctor Costs: Do more patients with diabetes report not being able
# to see a doctor because of the cost?

doctor_cost = df.groupby("Diabetes_012")["NoDocbcCost"].mean() * 100

plt.figure(figsize=(8,6))

ax = doctor_cost.plot(
    kind="bar",
    color=["green", "gold", "red"]
)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.3,
        str(round(bar.get_height(),2)) + "%",
        ha="center",
        fontsize=11
    )

plt.title("Doctor Cost Problems")
plt.xlabel("Diabetes Group")
plt.ylabel("Percentage")

plt.tight_layout()
plt.savefig("Q10_DoctorCost.png")
plt.show()

# QUESTION 11
# Education: Is there a pattern between a patient's education level
# and their diabetes status?

education = df.groupby("Education")["Diabetes_012"].mean()

plt.figure(figsize=(10,6))

education.plot(
    kind="line",
    marker="o",
    linewidth=3,
    color="purple"
)

plt.title("Education Level and Diabetes")
plt.xlabel("Education Level")
plt.ylabel("Average Diabetes Score")

plt.tight_layout()
plt.savefig("Q11_Education.png")
plt.show()

# QUESTION 12
# Income: Does average income level differ between the diabetes groups?

income = df.groupby("Diabetes_012")["Income"].mean()

plt.figure(figsize=(8,6))

ax = income.plot(
    kind="bar",
    color=["blue", "orange", "crimson"]
)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.05,
        round(bar.get_height(),2),
        ha="center",
        fontsize=11
    )

plt.title("Average Income by Diabetes Status")
plt.xlabel("Diabetes Group")
plt.ylabel("Income Level")

plt.tight_layout()
plt.savefig("Q12_Income.png")
plt.show()


# QUESTION 13
# High BP & Cholesterol: What is the proportion of patients with high
# blood pressure and high cholesterol in each diabetes group?

proportions = df.groupby("Diabetes_012")[["HighBP", "HighChol"]].mean() * 100

plt.figure(figsize=(10,6))

ax = proportions.plot(
    kind="bar",
    color=["red", "orange"]
)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.5,
        str(round(bar.get_height(),2)) + "%",
        ha="center",
        fontsize=10
    )

plt.title("High BP and High Cholesterol")
plt.xlabel("Diabetes Group")
plt.ylabel("Percentage")

plt.tight_layout()
plt.savefig("Q13_BP_Chol.png")
plt.show()


# QUESTION 14
# Smoking: Do smokers have higher diabetes rates than non-smokers?

smoking = df.groupby("Smoker")["Diabetes_012"].mean()

plt.figure(figsize=(7,6))

ax = smoking.plot(
    kind="bar",
    color=["green", "darkred"]
)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.01,
        str(round(bar.get_height(),2)),
        ha="center",
        fontsize=11
    )

plt.title("Smoking and Diabetes")
plt.xlabel("Smoking Status")
plt.ylabel("Average Diabetes Score")

plt.xticks([0,1], ["Non-Smoker", "Smoker"])

plt.tight_layout()
plt.savefig("Q14_Smoking.png")
plt.show()


# QUESTION 15
# Fruits & Veggies: Do patients who eat fruits and vegetables daily
# have lower diabetes rates?

fruit = df.groupby("Fruits")["Diabetes_012"].mean()
veggie = df.groupby("Veggies")["Diabetes_012"].mean()

plt.figure(figsize=(8,6))

plt.plot(
    fruit.index,
    fruit.values,
    marker="o",
    linewidth=3,
    label="Fruits"
)

plt.plot(
    veggie.index,
    veggie.values,
    marker="o",
    linewidth=3,
    label="Vegetables"
)

plt.title("Fruits and Vegetables vs Diabetes")
plt.xlabel("Daily Consumption")
plt.ylabel("Average Diabetes Score")

plt.legend()

plt.tight_layout()
plt.savefig("Q15_FruitsVeggies.png")
plt.show()

print("ALL 15 QUESTIONS ANSWERED!")
print("All charts saved successfully.")