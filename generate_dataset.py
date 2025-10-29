# generate_dataset.py
import pandas as pd
import numpy as np

np.random.seed(42)
n = 10000

# ----------------------
# Indian names
# ----------------------
first_names = [
    "Aarav", "Vivaan", "Aditya", "Sai", "Krishna", "Ananya", "Isha", "Priya", "Diya", "Meera",
    "Rohan", "Aryan", "Neha", "Shreya", "Kavya", "Ankit", "Ritika", "Siddharth", "Tanvi", "Rahul"
]
last_names = [
    "Sharma", "Verma", "Gupta", "Patel", "Singh", "Reddy", "Chatterjee", "Nair", "Kumar", "Iyer",
    "Das", "Mehta", "Joshi", "Kapoor", "Bose", "Malhotra", "Khan", "Mishra", "Chauhan", "Agarwal"
]

names = [np.random.choice(first_names) + " " + np.random.choice(last_names) for _ in range(n)]

# ----------------------
# Skills
# ----------------------
skills_pool = [
    "Python", "Java", "C++", "SQL", "Data Analysis", "Machine Learning", "Deep Learning",
    "Web Development", "React", "CSS", "HTML", "UI/UX Design", "Figma", "Photoshop",
    "Marketing", "Content Writing", "SEO", "Cloud Computing", "AWS", "DevOps",
    "Cybersecurity", "Networking", "Finance", "Excel", "Accounting",
    "Statistics", "Artificial Intelligence", "Data Science"
]

skills_list = ["; ".join(np.random.choice(skills_pool, size=np.random.randint(3, 7), replace=False)) for _ in range(n)]

# ----------------------
# Education Levels (exact labels from your screenshot)
# ----------------------
education_levels = [
    "High School",
    "Certificate from ITI",
    "Diploma from Polytechnic Institute",
    "Bachelor Degree"
]
# probabilities - adjust if you want different distribution
edu_list = np.random.choice(education_levels, size=n, p=[0.15, 0.10, 0.25, 0.50])

# ----------------------
# Ability Scores
# ----------------------
ability_scores = np.random.randint(50, 101, size=n)

# ----------------------
# Sectors & Locations
# ----------------------
sectors = [
    "IT", "Finance", "Marketing", "Design", "Healthcare", "Education",
    "Engineering", "Data Science", "Cybersecurity", "Cloud"
]
locations = [
    "Delhi", "Mumbai", "Bengaluru", "Hyderabad", "Chennai",
    "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow"
]

sector_list = np.random.choice(sectors, size=n)
location_list = np.random.choice(locations, size=n)

# ----------------------
# Final Dataset
# ----------------------
applicants = pd.DataFrame({
    "applicant_id": range(1, n+1),
    "name": names,
    "skills": skills_list,
    "education_level": edu_list,
    "ability_score": ability_scores,
    "preferred_sector": sector_list,
    "preferred_location": location_list
})

# Save to CSV
applicants.to_csv("10000_indian_students.csv", index=False)
print("✅ Dataset with 10,000 Indian students (with sector & location) generated.")
