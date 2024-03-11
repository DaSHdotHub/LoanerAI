## Build with
* [GitHub](https://www.github.com/)
* [GitPod](https://www.gitpod.io/)
* [Heroku](https://www.heroku.com/)
* [Streamlit](https://www.streamlit.io/)
* [Jupyter Notebooks](https://jupyter.org/)

## Dataset Content
The initial dataset, curated by Prof. Hofmann, comprises 1000 records, each detailed with 20 categorical/symbolic attributes. 
* E.g. for one dataset:

   A11 6 A34 A43 1169 A65 A75 4 A93 A101 4 A121 67 A143 A152 2 A173 1 A192 A201 1

The dataset is very abstract and was derived for better understanding into a less abstract *.csv file and is available on [kaggle.com](https://www.kaggle.com/code/kabure/predicting-credit-risk-model-pipeline/input).
This collection represents individuals who have obtained loans from a bank. Based on these attributes, each individual is assessed and labeled as either a good or bad credit risk applicant.

| Variable          | Meaning                                                     | Units                                                                                |
|-------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Age               | Applicant age                                               | numerical                   |
| Sex               | Applicant gender                                            | categerocial: male, female  |
| Job               | Applicant job level                                         | numeric: 0 - unskilled and non-resident, 1 - unskilled and resident, 2 - skilled, 3 - highly skilled |
| Housing           | Applicant living situation                                  | categerocial:  own, rent, or free                  |
| Saving accounts   | Applicant savings                                           | categerocial:  little, moderate, quite rich, rich  |
| Checking account  | Applicant has dependents or not                             | numerical                                          |
| Credit amount     | Applied loan                                                | numerical                                          |
| Duration          | Applied lann period                         | numerical: between 0 and 72                                                                           |
| Purpose           | Loan purpose                                                | categerocial: car, furniture/equipment, radio/TV, domestic appliances, repairs, education, business, vacation/others|
| Risk              | Applicant should be loaned = 0, risk for defualt to high = 0| Value target - Good or Bad Risk|

The data about the job is special, in the derived dataset, numerical and categeroical properties were mixed up. In this project the job variable will be handled as a categorical feature.

## Business Requirements

### Improve Loan Approval Process 
Requirement: Enhance the accuracy and efficiency of the loan approval process by identifying applicants who are likely to be good credit risks and streamlining their approval.

Rationale: By accurately identifying applicants who pose a lower risk, the company can expedite the approval process for these individuals, improving customer satisfaction and reducing the workload on manual review teams. This could also reduce the financial risk associated with default rates.

Implementation Strategy:

Develop a **predictive model** that classifies loan applicants as "good" or "bad" credit risks based on their application data.
Validate the model's accuracy through testing and ensure it meets predefined performance metrics (e.g., precision, recall).
Integrate the model into the loan application process to provide real-time risk assessments.

For the ease of this project this shall be a simple caluclator in a streamlit app.

### Identify Key Factors Influencing Credit Risk

Requirement: **Determine the most significant factors** that influence an applicant's likelihood of being a good or bad credit risk to inform risk mitigation strategies and policy adjustments.

Rationale: Understanding which factors most strongly predict credit risk can help the company tailor its loan products, adjust its criteria for loan approvals.

Implementation Strategy:

**Conduct exploratory data analysis** and feature importance analysis to identify the most predictive factors of credit risk.
Use insights from the data to revise loan application assessments and consider policy changes that might include offering financial guidance or alternative products to applicants with higher risk factors.
Monitor the impact of these changes on loan performance and customer outcomes, adjusting strategies as needed.


## Hypothesis and how to validate?
### Age and Credit Risk

**Hypothesis:** 

Older applicants are less likely to be classified as bad credit risks compared to younger applicants.

**Validation:**

Perform a logistic regression analysis with "Risk" as the dependent variable and "Age" as an independent variable. Additionally, a visualization (e.g., boxplot) showing the distribution of ages for good vs. bad credit risks could provide initial insights. The significance of the age coefficient in the regression model would indicate the impact of age on credit risk.

### Relationship Between Job Skill Level and Credit Risk


**Hypothesis:**

 Applicants with higher job skill levels (3 - highly skilled) are less likely to be classified as bad credit risks.

**Validation:** 

Use a chi-square test of independence to examine the relationship between job skill levels and credit risk categories. A multinomial logistic regression could further quantify the relationship, using "Risk" as the dependent variable and "Job" (encoded categorically) as an independent variable.

### Impact of Savings and Checking Account Balances on Credit Risk

**Hypothesis:**

 Applicants with little savings or checking account balances are more likely to be classified as bad credit risks.

**Validation:**

Conduct logistic regression analysis with "Risk" as the dependent variable and categorical encodings of "Saving accounts" and "Checking account" as independent variables. An ANOVA test could be used if transforming account balances into numerical categories or bins to see if there are statistically significant differences in risk classification across different levels of savings and checking account balances.

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).



## Unfixed Bugs
* None

## Deployment
### Heroku

* The App live link is: [Heroku/LoanerAI](https://loanerai-a6ec3ddb707c.herokuapp.com/)
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version. **OR**
* Add an app.json with the key-value pair:

    <code>{
            "stack": "heroku-20"
    }</code>
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

### GitPod
1. Create a new workspace
2. Paste the repository link <code>https://github.com/DaSHdotHub/LoanerAI.git</code>
3. E.g. select VS Code (Browser) and Standard, click Continue
4. For this project to run python v3.18.8 or equal should be installed.
<code>
#python installation
pyenv install 3.8.18
pyenv local 3.8.18
python3 -m venv venv
source venv/bin/activate
pip3 -r install requirements.txt
</code>


## Main Data Analysis and Machine Learning Libraries
| Library | Description |
|---------|-------------|
| numpy | Fundamental package for scientific computing with Python. Supports arrays, mathematical operations, and more. |
| pandas | Provides high-performance, easy-to-use data structures and data analysis tools. Alos loading and saving data.|
| matplotlib | Plotting library for Python and NumPy, offering a variety of static, animated, and interactive visualizations. |
| seaborn | Data visualization library based on matplotlib, providing a high-level interface for drawing attractive statistical graphics. |
| ydata-profiling | Tool for comprehensive automated data profiling. Gives insights into data quality, distribution, and relationships. Note: The correct name might be `pandas-profiling`. |
| plotly | Interactive graphing library for making interactive plots and dashboards across multiple programming languages. |
| ppscore | Calculates the Predictive Power Score (PPS) as an alternative to the correlation coefficient. |
| streamlit | Open-source app framework for Machine Learning and Data Science projects. Simplifies the creation of apps. |
| feature-engine | Library for feature engineering in machine learning, supporting transformations, selections, and encodings. |
| imbalanced-learn | Offers solutions to deal with imbalanced datasets, including resampling techniques. |
| scikit-learn | Machine learning library featuring various classification, regression, and clustering algorithms. |
| xgboost | Optimized distributed gradient boosting library designed for efficiency, flexibility, and portability. |
| yellowbrick | Visual diagnostic tools built on matplotlib to facilitate machine learning model selection and tuning. |
| Jinja2 | Modern and designer-friendly templating language for Python, widely used for web applications. |
| MarkupSafe | Ensures string representation is safe for HTML and XML, often used with web development libraries. |
| protobuf | Protocol Buffers, Google's data interchange format, useful for serializing structured data. |
| ipywidgets | Provides interactive HTML widgets for Jupyter notebooks and the IPython kernel. |
| altair | Declarative statistical visualization library for Python, designed for building a wide range of visualizations. |
| joblib | Set of tools for lightweight pipelining in Python, mainly used for saving and loading objects that use NumPy data structures. |


## Credits 

### Resources - Code and General Idea

The foundation of this project was provided by the *CodeInstitute Walkthrough 2 project* - "Churnometer". Leveraging its groundwork, I integrated numerous custom functions to streamline model selection, hyperparameter tuning, and evaluation processes. These functions were adapted to enhance their versatility and centralized accessibility. Key modifications included:

* Adapt imputation principles: This involves refining the strategies for handling missing data within the dataset, ensuring more accurate and reliable imputation techniques are utilized.

* Adapt numerical encodings for a better pipeline and therefore more accurate ML model: This entails optimizing the encoding methods for categorical variables to enhance the efficiency and accuracy of the ML pipeline, resulting in improved predictive performance.



### Content 

- Kaggle.com for providing the dataset(s)
- Kaggle.com | [Insigths for Encoding on a Notebook example](https://www.kaggle.com/code/aimack/how-to-encode-numerical-categorical-data)
- Medium.com | [Feature Encoding](https://medium.com/@denizgunay/feature-encoding-f099a6c1abe8)
- Medium.com | [Numerical Encoding](https://medium.com/@pp1222001/the-ultimate-guide-to-encoding-numerical-features-in-machine-learning-440c0e7752d#:~:text=Encoding%20numerical%20features%20refers%20to,suitable%20for%20machine%20learning%20algorithms.&text=However%2Cthere%20are%20scenarios%20where,performance%20of%20machine%20learning%20models.)


### Media

- None

## Acknowledgements (optional)
* Thank the people that provided support through this project.

