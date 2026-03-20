# Job Market Data Collection & Analysis

## Overview

Built an automated pipeline that scrapes real job listings from company career pages, extracts structured data, and runs analysis to find hiring trends. The system uses two tools working together — Selenium for browser automation and Scrapy for data extraction.

---

## Data Sources

| Company | Platform | URL |
|---------|----------|-----|
| Stripe | Greenhouse | https://boards.greenhouse.io/stripe |
| Hubspot | Greenhouse | https://boards.greenhouse.io/hubspot |
| Squarespace | Greenhouse | https://boards.greenhouse.io/squarespace |

All three sources are public career pages. No accounts, logins, or authentication was needed.

---

## How the Two Tools Work Together

First, Selenium opens a real browser window, loads each career page, and saves all the job listing URLs into a file called job_links.csv. This step is needed because career pages load their content dynamically with JavaScript, which regular scrapers cannot handle.

Second, Scrapy reads those URLs one by one, visits each job page, pulls out all the details like title, location, salary, and skills, then saves everything into jobs.csv and jobs.json.

---

## Folder Structure
```
Job_scrapper_0045/
├── selenium/
│   └── job_scraper.py
├── scrapy_project/
│   ├── spiders/
│   │   └── job_spider.py
│   ├── items.py
│   ├── pipelines.py
│   └── settings.py
├── data/
│   ├── raw/
│   │   └── job_links.csv
│   └── final/
│       ├── jobs.csv
│       └── jobs.json
├── analysis/
│   ├── analyze_jobs.py
│   ├── summary.json
│   ├── top_skills.png
│   ├── top_companies.png
│   ├── top_titles.png
│   ├── top_locations.png
│   └── experience_levels.png
├── docs/
│   └── report.md
├── scrapy.cfg
├── .gitignore
└── README.md
```

---

## Steps to Run

Install required libraries:
```bash
pip install selenium scrapy itemadapter matplotlib pandas
```

Run Selenium to collect job URLs:
```bash
python selenium/job_scraper.py
```

Run Scrapy to extract job details:
```bash
scrapy crawl job_spider
```

Run the analysis:
```bash
python analysis/analyze_jobs.py
```

---

## Fields Collected

| Field | Description |
|-------|-------------|
| job_title | Title of the job posting |
| company_name | Company that posted the job |
| location | City or Remote |
| department | Team or department name |
| employment_type | Full-time, Part-time, Contract, Internship |
| posted_date | Date the job was posted |
| job_url | Direct link to the job page |
| job_description | Full job description text |
| required_skills | Skills extracted from the description |
| experience_level | Entry-level, Mid-level, Senior, Management |
| salary | Salary range if listed publicly |

---

## Results from 558 Job Listings

- Top skills employers want: Communication, SQL, Python, Collaboration, Go
- Most active hiring company: Stripe with 516 open roles
- Most common locations: Dublin, Bengaluru, New York City
- Majority of roles are Senior or Management level
- 498 out of 558 jobs are full-time positions

---

## Branch Structure

| Branch | What it contains |
|--------|-----------------|
| main | Final working version |
| develop | Testing and integration |
| feature/selenium-search | Selenium scraper code |
| feature/scrapy-job-parser | Scrapy spider code |
| feature/analysis-report | Analysis and charts |

---

## Ethics

- All scraped pages are publicly accessible
- No login or authentication bypass was used
- Delays added between requests to avoid overloading servers
- robots.txt rules followed throughout
- No private or personal data was collected