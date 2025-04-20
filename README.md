Data Engineering Projects 
---------------------------------------------------------------------------------------------

### ⚽ Premier League 2023/24 Dashboard (Power BI) - Data Engineering Project - 1

**Tools:** Python, PostgreSQL, Power BI  
**Focus:** Data pipeline + Visualization

**What I did:**
- Pulled live EPL data from a football API using Python
- Transformed it with Pandas and stored in PostgreSQL
- Connected Power BI to the database
- Built a branded, interactive dashboard showing team stats, standings, and KPIs

This project helped me apply both data engineering and data visualization skills in a real-world scenario — powered by my passion for football!

**Dataset details:**

API - https://www.thesportsdb.com/free_sports_api

📊 Key Columns Overview
strTeam	-> Team name (e.g., Manchester City, Arsenal)

intPlayed -> Total matches played (all are 38)

intWin -> Total wins per team

intLoss	-> Total losses per team

intDraw	-> Total draws per team

intGoalsFor	-> Total goals scored by each team

intGoalsAgainst	-> Total goals conceded

intGoalDifference -> Difference between goals for and against

intPoints -> Total points earned (W=3, D=1, L=0)

strForm	-> Recent form (last 5 matches, e.g., "WWDLW")

strDescription	-> Contains promotion/relegation tags for some teams

strBadge -> URL of each team’s logo for visual use in dashboards

---------------------------------------------------------------------------------------------
### Tech Job Analysis - Data Engineering Project - 2

**Tools:** Python
**Libraries** Pandas, MatplotLib
**Focus:** Data Engineering + Visualization

**What I did:**
- Job Type Analysis – Categorized job types into Full-Time, Contract, and Part-Time, and visualized using a horizontal bar chart.
- Job Location Insights – Split location into City, State, and Country, standardized country values, and plotted with a horizontal bar chart.
- Pay Range Categorization – Removed null pay values, classified into three pay bands, and visualized with a vertical bar chart.
- Job Portal Distribution – Filtered out negligible values and displayed job portal distribution using a donut chart.

**Dataset details:**
Collected between October and December 2024, this dataset contains 100,000+ tech job listings from fields like Cyber Security, Software Engineering, IT, Product Management, and Data Science.
Jobs were scraped using JobsPy from major portals like Indeed, ZipRecruiter, and Glassdoor — then consolidated into one dataset for analysis.
