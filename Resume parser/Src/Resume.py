import re
import json

def parse_resume(resume_text):
    # Example regex patterns (simplified)
    name_pattern = re.compile(r"Name: (.+)")
    email_pattern = re.compile(r"Email: (.+)")
    phone_pattern = re.compile(r"Phone: (.+)")
    address_pattern = re.compile(r"Address: (.+)")
    professional_summary_pattern = re.compile(r"Professional Summary: (.+)")
    # Add more patterns as needed...

    resume_data = {
        "name": name_pattern.search(resume_text).group(1),
        "contact_information": {
            "email": email_pattern.search(resume_text).group(1),
            "phone": phone_pattern.search(resume_text).group(1),
            "address": address_pattern.search(resume_text).group(1)
        },
        "professional_summary": professional_summary_pattern.search(resume_text).group(1),
        "work_experience": [],
        "education": [],
        "skills": [],
        "certifications": [],
        "projects": [],
        "languages": []
    }

    # Example of extracting work experience (simplified)
    work_experience_pattern = re.compile(r"Company: (.+), Position: (.+), Duration: (.+), Responsibilities: (.+)")
    for match in work_experience_pattern.finditer(resume_text):
        resume_data["work_experience"].append({
            "company": match.group(1),
            "position": match.group(2),
            "duration": match.group(3),
            "responsibilities": match.group(4)
        })

    # Add more extraction logic for education, skills, etc...

    return json.dumps(resume_data, indent=4)

# Example usage
resume_text = """
Name: Ranjitsing Jadhav
Email: jadhavranjitsingh561@gmail.com
Phone: 7498495688
Address: Pune
Professional Summary: Done Instership in Frontend Developer
"""

print(parse_resume(resume_text))
