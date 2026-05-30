import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_review_report(context):
    try:
        model = genai.GenerativeModel('gemini-flash-lite-latest')
        
        prompt = f"""
You are an expert technical document reviewer.

Your task is to analyze the provided text and produce a "TECHNICAL REVIEW REPORT".
Identify the following elements from the text:
1. Unsupported Claims
2. Missing Assumptions
3. Weak Evidence
4. Overgeneralization

Finally, assign an "Overall Risk Score" (LOW, MEDIUM, HIGH) based on your findings.

Text to analyze:
{context}

Format your output exactly as follows:

```
TECHNICAL REVIEW REPORT

1. Unsupported Claims:
- [claim] -> [reason]

2. Missing Assumptions:
- [missing assumption]

3. Weak Evidence:
- [weak evidence found]

4. Overgeneralization:
- [overgeneralization found]

Overall Risk Score: [SCORE]
```

Keep your points concise. If no issue is found for a category, explicitly write "None detected."
"""

        response = model.generate_content(prompt)
        try:
            return response.text.strip()
        except ValueError:
            return "No review could be generated from the provided document."

    except Exception as e:
        return f"Error: {str(e)}"
