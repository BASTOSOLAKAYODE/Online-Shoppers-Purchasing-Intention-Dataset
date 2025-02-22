# E-commerce Customer Behavior Analysis

## Project Background
This project analyzes online shopping behavior to understand user interactions, improve conversion rates, and optimize marketing strategies. The company operates in the e-commerce industry and has been active for several years, following a direct-to-consumer business model. Key business metrics include user engagement, bounce rates, exit rates, page values, and revenue conversion rates.

As a data analyst, the goal is to extract insights from user behavior data and provide actionable recommendations to enhance user experience and increase sales.

## Key Areas of Analysis

### Category 1: User Engagement
- Identify patterns in page visits (Administrative, Informational, Product-Related) and their durations.
- Assess the impact of different page types on purchase decisions.

### Category 2: Conversion Analysis
- Examine factors influencing revenue conversion, including bounce rates, exit rates, and page values.
- Rank the most influential features contributing to successful purchases.

### Category 3: Seasonal Trends
- Analyze the effect of special days and monthly trends on purchasing behavior.
- Evaluate the significance of high-traffic periods in driving sales.

### Category 4: Customer Segmentation
- Categorize users based on traffic sources, visitor types, and regions.
- Identify high-value customer segments for targeted marketing strategies.

### Data Source and Tools
- The raw dataset can be found [here](data/raw) while the cleaned dataset used used for the analysis task [here](data/cleaned). More info about the origin of the data is available [here](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset)
- Notebook: The notebooks containing preprocessing, EDA and model training process for this case study can be found: [here](notebooks)

# Data Structure & Initial Checks

The main dataset used for this project consists of user browsing behavior on an e-commerce platform, aiming to predict purchasing behavior. The dataset contains various numerical and categorical features, including session details, page visit metrics, user attributes, and transaction indicators.

## Dataset Overview

**Table: Online Shopping Behavior Data**

The dataset contains behavioral metrics related to website visits, including:

- **Administrative & Administrative_Duration**: Number of administrative pages visited and time spent.
- **Informational & Informational_Duration**: Number of informational pages visited and time spent.
- **ProductRelated & ProductRelated_Duration**: Number of product-related pages visited and time spent.
- **BounceRates & ExitRates**: Metrics indicating how often users leave the website.
- **PageValues**: Value assigned to visited pages.
- **SpecialDay**: Proximity to a special event.
- **Month**: Month of the visit.
- **OperatingSystems, Browser, Region, TrafficType**: Technical user attributes.
- **VisitorType**: New or returning visitor.
- **Weekend**: Whether the session occurred on a weekend.
- **Revenue (Target Variable)**: Whether the session resulted in a purchase.

## Dataset Schema

| Feature                  | Data Type   | Description |
|--------------------------|------------|-------------|
| Administrative           | Integer    | Count of administrative pages visited. |
| Administrative_Duration  | Float      | Time spent on administrative pages. |
| Informational           | Integer    | Count of informational pages visited. |
| Informational_Duration  | Float      | Time spent on informational pages. |
| ProductRelated          | Integer    | Count of product-related pages visited. |
| ProductRelated_Duration | Float      | Time spent on product-related pages. |
| BounceRates             | Float      | Percentage of sessions that leave immediately. |
| ExitRates               | Float      | Percentage of sessions that exit the site. |
| PageValues              | Float      | Page value based on user behavior. |
| SpecialDay              | Float      | Closeness to special events (e.g., Black Friday). |
| Month                   | Categorical| Month of the visit (e.g., Jan, Feb, etc.). |
| OperatingSystems        | Integer    | OS used by the visitor. |
| Browser                 | Integer    | Browser used by the visitor. |
| Region                  | Integer    | Region of the visitor. |
| TrafficType             | Integer    | Type of traffic source. |
| VisitorType             | Categorical| Whether the visitor is new or returning. |
| Weekend                 | Boolean    | Whether the visit happened on a weekend. |
| Revenue                 | Boolean    | Target variable: 1 if purchase was made, 0 otherwise. |

## Initial Data Checks

- **Total Rows**: 12,330 records
- **Duplicates**: Removed duplicate rows.
- **Missing Values**: The dataset have no missing values.
- **Class Imbalance**: Revenue class is imbalanced (15.63% purchases vs. 84.37% no purchase). Applied resampling techniques to balance the classes.

## Data Processing Summary
- **Feature Engineering**: Created interaction features, aggregated session behavior.
- **Categorical Encoding**: One-hot encoded categorical variables.
- **Outlier Handling**: Applied log transformation to numerical features with extreme outliers.
- **Feature Importance**: Used tree-based methods to identify key predictors.
- **Model Selection**: Trained a Random Forest Classifier for prediction.

# Repository Structure

```
Ecommerce-Purchase-Prediction/
├── data/
│   ├── raw/                      # Original, unprocessed data files
│   │   ├── online_shoppers_intention.csv
│   ├── processed/                # Cleaned and processed data files
│   │   ├── data_cleaned.csv
│
├── notebooks/
│   ├── 01_preprocessing.ipynb     # Exploratory Data Analysis
│   ├── 02_eda.ipynb    # Data cleaning and feature engineering
│
│
├── model/
│   ├── random_forest_model.pkl # Saved machine learning model
│
├── reports/
│   ├── figures/                    # Visualizations and plots
│   │   ├── Categorical features count plots.png
│   │   ├── Correlation heatmap.png
│   │   ├── Distribution of numerical features.png
│   │   ├── Feature Importance.png
│   │   ├── Pairplot for key numerical features with Revenue.png
│   ├── executive-summary.pptx       # Final analysis report
│
├── .gitignore                      # Files and folders to ignore
├── requirements.txt                 # Python dependencies
└── README.md                        # Project overview and instructions

```

### **Executive Summary**

**Overview of Findings**
This analysis explores key factors influencing online purchasing behavior. Three primary insights emerge:
1. **Page Value is the strongest predictor of purchases**, indicating that pages designed for transactions significantly impact conversion rates.
2. **Exit and Bounce Rates negatively correlate with revenue**, suggesting that reducing premature exits improves sales.
3. **Product-related page interactions play a crucial role in driving purchases**, with their duration and frequency contributing positively to revenue.

   - The python code utilised to inspect these relationships can be found [here](notebooks/)
   - The prediction model can be downloaded [here](model/random_forest_model.pkl/)
   - A one-page PowerPoint executive summary is available for download [here](Reports/executive-summary.pptx)

---

### **Insights Deep Dive**

#### **Category 1: User Engagement**
1. **Product-Related Page Interactions are highly correlated with revenue** (correlation: 0.16). Users who engage longer with product-related pages are more likely to make a purchase.
2. **Administrative and Informational pages have lower correlations with revenue** (0.14 and 0.10, respectively), indicating that these pages contribute less to conversions.
3. **Product-related page duration (0.15 correlation) is almost as significant as visit frequency**, reinforcing the importance of keeping users engaged with detailed product information.
4. **Special Day impact is minimal (-0.08 correlation),** suggesting that promotions tied to specific dates have a limited effect on revenue.
<p align="center">
    <img src="reports/figures/Correlation of Page Interactions with Revenue.png" alt="Red Wine" width="80%">
</p>


#### **Category 2: Exit and Bounce Behavior**
1. **Exit Rates (-0.21 correlation) and Bounce Rates (-0.15 correlation) reduce purchase likelihood**, emphasizing the importance of optimizing user flow.
2. **Bounce and Exit Rates are highly correlated (0.91),** indicating that users who leave early tend to do so without engaging further.
3. **Pages with high Page Values tend to have lower exit rates**, suggesting that structured purchase paths improve retention.
4. **Reducing friction points (e.g., cart abandonment) can increase conversion rates** by improving Page Values and lowering exits.

<p align="center">
    <img src="reports/figures/Correlations of Exit Rates Bounce Rates and Page Value.png" alt="Red Wine" width="80%">
</p>


#### **Category 3: Traffic and Seasonal Trends**
1. **Traffic Type influences purchases, with TrafficType_2 ranking among the top 10 factors**, indicating that certain sources are more effective for conversions.
2. **November sees higher conversions than other months**, supporting seasonal trends in shopping behavior.
3. **Weekend visits show a minor effect on purchases**, implying that weekday traffic is equally important.
4. **Operating Systems and Browsers have relatively low impact**, suggesting that platform-related optimizations may not significantly shift revenue.

<p align="center">
    <img src="reports/figures/Feature Importance.png" alt="Red Wine" width="80%">
</p>

#### **Category 4: Customer Segmentation**  
1. **Traffic sources significantly impact conversions**, with **TrafficType_2 ranking among the top 10 most important features**. This suggests that certain marketing channels are more effective in driving purchases.  
2. **Regional differences in purchasing behavior exist**, though they have a lower impact compared to traffic type and visitor type. This suggests that while location-based targeting may help, other factors play a bigger role.  
3. **Weekday vs. weekend traffic shows minimal variation in conversions**, implying that marketing efforts should be consistent throughout the week rather than heavily focused on weekends.  

<p align="center">  
    <img src="reports/figures/Feature Importance.png" alt="Feature Importance" width="80%">  
</p>

### **Recommendations:**
Based on the insights and findings above, we recommend the **website design and marketing teams** to consider the following actions:

1. **Enhance Product Page Engagement:**
   - Observation: PageValues has the highest correlation with revenue (0.49) and is the most important feature in the model.
   - Recommendation: Optimize product pages with better descriptions, images, and customer reviews to enhance engagement and conversion rates.

2. **Reduce Exit and Bounce Rates:**
   - Observation: High ExitRates (-0.21) and BounceRates (-0.15) are negatively correlated with revenue.
   - Recommendation: Improve navigation, reduce load times, and introduce personalized recommendations to retain users and reduce abandonment.

3. **Leverage Product-Related Pages:**
   - Observation: ProductRelated and ProductRelated_Duration have positive correlations with revenue (0.16 and 0.15, respectively).
   - Recommendation: Prioritize product-related content in user journeys and invest in A/B testing to enhance user experience on these pages.

4. **Target Users Effectively Based on Seasonal Trends:**
   - Observation: SpecialDay has a slight negative correlation (-0.08) with revenue, indicating minimal impact.
   - Recommendation: While seasonal targeting is important, campaigns should focus on other strong predictors like PageValues and ExitRates for better ROI.

5. **Optimize for Traffic Type & Device Usage:**
   - Observation: TrafficType_2 and OperatingSystems_2 appear among the top 15 most important features.
   - Recommendation: Identify high-value traffic sources and optimize the user experience for specific devices and operating systems.

---

### **Assumptions and Caveats:**
Throughout the analysis, multiple assumptions were made to manage challenges with the data. These assumptions and caveats are noted below:

1. **Data Completeness:** It is assumed that all recorded sessions represent valid user interactions, and missing data did not significantly impact the insights.

2. **Correlation Does Not Imply Causation:** While correlations indicate relationships, they do not confirm causation. Further testing (e.g., A/B experiments) is recommended to validate recommendations.

3. **Feature Engineering Impact:** Some categorical features were encoded and combined for analysis, which may influence interpretability.

4. **Traffic Source Consistency:** The classification of traffic types and their impact may vary depending on external factors like marketing campaigns.

5. **Data Representativeness:** It is assumed that the dataset accurately represents user behavior across different time frames and does not have seasonality biases that could skew insights.

Further analysis and testing should be conducted to refine these recommendations and optimize decision-making strategies.


