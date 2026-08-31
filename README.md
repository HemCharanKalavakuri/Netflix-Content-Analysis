Netflix Content Strategy Analysis

1. Project Overview

This project analyzes the Netflix Movies and TV Shows dataset using Power BI to understand Netflix's content library, content growth, genre distribution, geographic distribution, ratings, and content characteristics.

The project focuses on transforming raw Netflix data into a clean analytical dataset and building an interactive Power BI dashboard that provides meaningful insights into Netflix's content strategy.

---

2. Project Objectives

The main objectives of this project are:

 Analyze the overall Netflix content catalog.
 Compare Movies and TV Shows.
 Analyze Netflix content additions over time.
 Identify the countries contributing the most content.
 Identify the most common genres on Netflix.
 Analyze the distribution of content ratings.
 Analyze movie duration.
 Analyze the number of seasons in TV Shows.
 Understand how Netflix's content composition has changed over time.
 Build an interactive and professional business intelligence dashboard.

---

3. Dataset

Dataset Name

Netflix Movies and TV Shows

Source

Kaggle

File Format

CSV

Dataset Description

The dataset contains information about Movies and TV Shows available on Netflix, including their titles, content type, directors, cast, countries, release years, ratings, durations, genres, and dates added to Netflix.

Important Columns

| Column         | Description                                    |
| -------------- | ---------------------------------------------- |
| `show_id`      | Unique identifier for each Netflix title       |
| `type`         | Movie or TV Show                               |
| `title`        | Name of the title                              |
| `director`     | Director of the title                          |
| `cast`         | Main cast members                              |
| `country`      | Country or countries associated with the title |
| `date_added`   | Date the title was added to Netflix            |
| `release_year` | Original release year                          |
| `rating`       | Content rating                                 |
| `duration`     | Movie duration or number of TV Show seasons    |
| `listed_in`    | Genre/category of the title                    |
| `description`  | Description of the title                       |

---

4. Data Cleaning

The raw Netflix dataset was inspected and cleaned before building the dashboard.

Cleaning steps performed

 Checked the dataset structure.
 Checked missing values in each column.
 Identified missing values in important fields.
 Removed records with missing values where appropriate.
 Checked for duplicate records.
 Verified that `show_id` values were unique.
 Checked the `type` column for invalid values.
 Removed invalid records from the `type` column.
 Ensured the `type` column contains only:

  * Movie
  * TV Show
 Cleaned unnecessary spaces from text fields.
 Converted `date_added` into a proper date format.
 Extracted year and month information from `date_added`.
 Cleaned the `duration` column.
 Created a numeric movie-duration field.
 Created a TV Show season-count field.
 Split multiple countries into individual country records.
 Split multiple genres into individual genre records.
 Created separate datasets for Movies and TV Shows.

---

5. Data Transformation

Power Query was used to transform the dataset for analysis.

Created supporting datasets

 `netflix_cleaned`
 `Netflix_Movies`
 `Netflix_TV_Shows`
 `Netflix_Countries`
 `Netflix_Genres`
These tables were created to make the dashboard analysis more accurate and easier to manage.

---

6. Tools & Technologies

 Power BI
 Power Query
 DAX
 Python
 Pandas
 CSV
 Kaggle Dataset

---

7. Dashboard KPIs

The dashboard contains the following KPI cards:

Total Titles

Total number of Movies and TV Shows available in the dataset.

Total Movies

Total number of Movies available on Netflix.

Total TV Shows

Total number of TV Shows available on Netflix.

Total Countries

Number of unique countries represented in the Netflix catalog.

Average Movie Duration
Average duration of Netflix Movies in minutes.

---

8. Interactive Filters

The dashboard contains interactive slicers that allow users to explore the data dynamically.

Content Type

 Movie
 TV Show

Release Year

Allows users to filter content by release year.

Rating

Allows users to analyze different content ratings.

Country

Allows users to analyze Netflix content by country.

All relevant charts and KPI cards respond dynamically to these filters.

---

9. Dashboard Visualizations

1. Netflix Content Growth Over Time

Chart Type: Line Chart

Question answered:

> How has Netflix's content library grown over time?

This visualization shows the number of Netflix titles added across different years and allows comparison between Movies and TV Shows.

---

 2. Netflix Catalog Composition

Chart Type: Donut Chart

Question answered:

> What proportion of Netflix's catalog consists of Movies and TV Shows?

This visualization compares the overall distribution of Movies and TV Shows.

---

 3. Global Netflix Content Distribution

Chart Type: Map

Question answered:

> How is Netflix content distributed across different countries?

The map visualizes the geographic distribution of Netflix titles.

---

 4. Top 10 Netflix Genres

Chart Type: Bar Chart


> Which genres dominate Netflix's content catalog?

The visualization identifies the ten most common genres/categories.

---

5. Netflix Content by Rating

Chart Type: Clustered Column Chart

> Which content ratings are most common on Netflix?

This visualization compares the number of titles across different content ratings.

---

6. Netflix Content Additions by Year

Chart Type: Clustered Column Chart



> How do Movie and TV Show additions compare across different years?

The chart displays Movies and TV Shows side-by-side for each year, making it easy to compare Netflix's content additions.

---

### 7. Movie Duration Distribution

**Chart Type:** Histogram / Column Chart

**Question answered:**

> What is the distribution of movie durations on Netflix?

This analysis identifies common movie-length ranges and helps understand Netflix's movie catalog characteristics.

---

## 10. Key Business Questions

This dashboard answers the following business questions:

### Content Strategy

* How large is Netflix's content catalog?
* Is Netflix's catalog dominated by Movies or TV Shows?
* How has Netflix's content library grown over time?
* How does Movie growth compare with TV Show growth?

### Geographic Distribution

* Which countries contribute the most Netflix content?
* How is Netflix content distributed globally?

### Genre Analysis

* What are the most common Netflix genres?
* Which genres dominate the catalog?

### Audience Analysis

* Which content ratings are most common?
* What type of audience does Netflix primarily target?

### Content Characteristics

* What is the typical movie duration?
* How are movie durations distributed?
* How do Movie and TV Show additions differ by year?

---

## 11. Key Findings

The final findings are based on the values obtained from the Power BI dashboard.

### Overall Catalog

* Total Titles: **[YOUR VALUE]**
* Total Movies: **[YOUR VALUE]**
* Total TV Shows: **[YOUR VALUE]**
* Total Countries: **[YOUR VALUE]**
* Average Movie Duration: **[YOUR VALUE] minutes**

### Content Composition

* Movies account for **[YOUR VALUE]%** of the catalog.
* TV Shows account for **[YOUR VALUE]%** of the catalog.

### Content Growth

* The highest number of content additions occurred in **[YEAR]**.
* **[Movie/TV Show]** had the greater number of additions during the peak period.

### Geographic Distribution

* **[COUNTRY]** contributes the largest number of Netflix titles.
* The catalog is concentrated among several major content-producing countries.

### Genre Distribution

* **[GENRE 1]** is one of the most common genres.
* **[GENRE 2]** is another major genre in the Netflix catalog.
* The Top 10 genres account for a significant portion of the available content.

### Rating Distribution

* **[RATING]** is the most common content rating.
* The rating distribution provides an indication of Netflix's major audience segments.

### Movie Duration

* The average movie duration is approximately **[VALUE] minutes**.
* Most movies fall within the **[RANGE] minute** range.

---

## 12. Dashboard Screenshot

---

## 13. Project Structure

```text
Netflix-Content-Analysis/
│
├── data/
│   ├── netflix_titles.csv
│   ├── netflix_cleaned.csv
│   ├── netflix_movies.csv
│   ├── netflix_tv_shows.csv
│   ├── netflix_countries.csv
│   └── netflix_genres.csv
│
├── powerbi/
│   └── Netflix_Dashboard.pbix
│
├── screenshots/
│   └── netflix_dashboard.png
│
├── notebooks/
│   └── netflix_cleaning.ipynb
│
└── README.md
```

---

## 14. How to Use the Dashboard

1. Open the Power BI `.pbix` file.
2. Navigate to the dashboard page.
3. Use the slicers to filter the data.
4. Select Movie or TV Show from the Type slicer.
5. Adjust the Release Year filter.
6. Select a Rating or Country.
7. Observe how the KPI cards and visualizations change dynamically.
8. Hover over charts to view detailed information.

---

## 15. Skills Demonstrated

This project demonstrates practical skills in:

* Data Cleaning
* Data Transformation
* Exploratory Data Analysis
* Power Query
* DAX
* Data Modeling
* Data Visualization
* KPI Development
* Interactive Dashboard Design
* Business Intelligence
* Business Insight Generation

---

## 16. Future Improvements

Possible future improvements include:

* Add Netflix viewership data.
* Add subscriber growth data.
* Add country-level drill-through analysis.
* Add advanced DAX measures.
* Add year-over-year growth calculations.
* Add more detailed genre analysis.
* Add predictive analysis for future content trends.
* Connect the dashboard to a live data source.
* Build a machine learning model to predict content characteristics.

---

17. Conclusion

This project demonstrates how raw Netflix catalog data can be transformed into a structured analytical dataset and an interactive Power BI dashboard.

The dashboard provides insights into Netflix's content composition, growth, geographic distribution, genres, ratings, and content characteristics.

The project demonstrates the complete analytics workflow from data cleaning and transformation to visualization and business insight generation.

---

18. Author

Charan Reddy

Aspiring Data Scientist | Python | SQL | Power BI | Machine Learning
