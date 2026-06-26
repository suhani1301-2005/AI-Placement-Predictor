def get_response(question):

    question = question.lower()

    # -------------------------
    # DSA
    # -------------------------

    if "dsa" in question or "roadmap" in question:

        return """
## 💻 DSA Roadmap

### 1️⃣ Arrays
- Array Traversal
- Prefix Sum
- Two Pointers

### 2️⃣ Strings
- Palindrome
- Anagram
- Sliding Window

### 3️⃣ Hashing
- Frequency Counting
- HashMap Problems

### 4️⃣ Linked List
- Reverse Linked List
- Cycle Detection
- Merge Linked List

### 5️⃣ Stack & Queue
- Monotonic Stack
- Next Greater Element

### 6️⃣ Trees
- DFS
- BFS
- BST
- Tree Traversals

### 7️⃣ Graphs
- BFS
- DFS
- Shortest Path

### 8️⃣ Dynamic Programming
- Knapsack
- Longest Increasing Subsequence (LIS)
- Grid DP

🎯 Practice 3-5 problems daily.
"""

    # -------------------------
    # SQL
    # -------------------------

    elif "sql" in question:

        return """
## 🗄 SQL Roadmap

1. SELECT
2. WHERE
3. ORDER BY
4. GROUP BY
5. HAVING
6. JOINS
7. Subqueries
8. Window Functions
Practice SQL daily on HackerRank.
"""

    # -------------------------
    # Resume
    # -------------------------

    elif "resume" in question:

        return """
## 📄 Resume Tips

• Keep it one page.
• Mention projects.
• Add technical skills.
• Keep GitHub updated.
• Mention certifications.
"""

    # -------------------------
    # Interview
    # -------------------------

    elif "interview" in question:

        return """
## 🎤 Interview Preparation

1. Revise DSA
2. Practice SQL
3. Revise OOP
4. HR Questions
5. Mock Interviews
"""

    # -------------------------
    # Projects
    # -------------------------

    elif "project" in question:

        return """
## 💻 Project Ideas

• AI Placement Predictor
• Student Management System
• Expense Tracker
• Hospital Management System
• Weather Dashboard
"""

    # -------------------------
    # Placement
    # -------------------------

    elif "placement" in question:

        return """
## 🎯 Placement Preparation

✅ Learn DSA
✅ Learn SQL
✅ Build Projects
✅ Practice Aptitude
✅ Mock Interviews

Spend 2-3 hours daily.
"""

    # -------------------------
    # Default
    # -------------------------

    else:

        return "Sorry! I currently answer questions about DSA, SQL, Resume, Projects and Placements."
