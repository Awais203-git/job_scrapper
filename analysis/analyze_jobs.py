import os
import json
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA_PATH  = os.path.join("data", "final", "jobs.csv")
OUTPUT_DIR = "analysis"


def load_data():
    if not os.path.exists(DATA_PATH):
        print(f"File not found: {DATA_PATH}")
        return None
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded {len(df)} job records")
    return df


def plot_bar(series, title, filename, color="steelblue"):
    fig, ax = plt.subplots(figsize=(10, 5))
    series.plot(kind="bar", ax=ax, color=color)
    ax.set_title(title)
    ax.set_xlabel("")
    ax.set_ylabel("Count")
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path)
    plt.close()
    print(f"Chart saved: {path}")


def analyze(df):
    print("=" * 60)
    print("        JOB MARKET ANALYSIS REPORT")
    print("=" * 60)
    print(f"Total job records: {len(df)}")

    print("\n── 1. TOP SKILLS ──")
    skills = df["required_skills"].dropna()
    skills = skills[skills != "Not specified"]
    skill_counts = pd.Series(
        [s.strip() for row in skills for s in row.split(",")]
    ).value_counts().head(10)
    print(skill_counts)
    plot_bar(skill_counts, "Top 10 In-Demand Skills", "top_skills.png", "steelblue")

    print("\n── 2. TOP COMPANIES ──")
    companies = df["company_name"].value_counts().head(10)
    print(companies)
    plot_bar(companies, "Top Hiring Companies", "top_companies.png", "coral")

    print("\n── 3. TOP LOCATIONS ──")
    locations = df["location"].value_counts().head(10)
    print(locations)
    plot_bar(locations, "Top Locations", "top_locations.png", "mediumseagreen")

    print("\n── 4. EXPERIENCE LEVELS ──")
    exp = df["experience_level"].value_counts()
    print(exp)
    plot_bar(exp, "Experience Level Distribution", "experience_levels.png", "mediumpurple")

    print("\n── 5. EMPLOYMENT TYPES ──")
    emp = df["employment_type"].value_counts()
    print(emp)

    print("\n── 6. TOP JOB TITLES ──")
    titles = df["job_title"].value_counts().head(10)
    print(titles)
    plot_bar(titles, "Top Job Titles", "top_titles.png", "darkorange")

    summary = {
        "total_jobs": len(df),
        "top_skills": skill_counts.to_dict(),
        "top_companies": companies.to_dict(),
        "top_locations": locations.to_dict(),
        "experience_levels": exp.to_dict(),
        "employment_types": emp.to_dict(),
    }
    with open(os.path.join(OUTPUT_DIR, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print("\nSummary saved to analysis/summary.json")
    print("=" * 60)


if __name__ == "__main__":
    df = load_data()
    if df is not None:
        analyze(df)