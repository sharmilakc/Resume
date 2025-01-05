import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Interactive Resume - Sharmila KC",
    page_icon="📄",
    layout="centered",
)

# Upload and display profile picture
st.sidebar.header("Upload Your Picture")
uploaded_file = st.sidebar.file_uploader("Choose a profile picture", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    profile_pic = Image.open(uploaded_file)
    st.image(profile_pic, width=200, caption="Sharmila KC")
else:
    st.write("Upload your picture using the sidebar!")

# Resume Header
st.markdown(
    f"""
    <h1 style="text-align: center; color: #4CAF50;">Sharmila KC</h1>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.header("Navigation")
sections = ["Objective", "Education", "Professional Experience", "Capstone Projects", "Technical Skills"]
selection = st.sidebar.radio("Go to", sections)

# Content Sections
if selection == "Objective":
    st.header("Objective")
    st.write(
        """
        Results-driven Business Analyst with expertise in Python, SQL, R, Tableau, Power BI, and Excel. Proven ability 
        to analyze complex datasets, develop data-driven insights, and present actionable recommendations. Experienced in 
        logistics optimization, data visualization, and statistical analysis, with a strong foundation in business analytics and hands-on project experience.
        """
    )

elif selection == "Education":
    st.header("Education")
    st.markdown(
        """
        - **MBA in Business Analytics**, Stanislaus State University, Turlock, CA (01/2023 - 12/2024)
        - **BBA in Accounting**, San Jose State University, San Jose, CA (07/2017 - 12/2021)
        """
    )

elif selection == "Professional Experience":
    st.header("Professional Experience")
    st.markdown(
        """
        **Business Analyst, Empire Xpress Inc.** (05/2022 – 10/2024)
        - Analyzed logistics datasets using SQL and Excel, leveraging advanced functions (VLOOKUP, HLOOKUP, Pivot Tables) to reduce fuel consumption by 12% and increase delivery efficiency by 15%.
        - Built R-based visualizations and dashboards to monitor key operational metrics, enabling strategic decision-making and process improvements.
        - Designed and maintained relational databases in SQL, performing data cleaning, updating, and insertion tasks to streamline reporting processes and enhance data accuracy.
        """
    )

elif selection == "Capstone Projects":
    st.header("MBA Capstone Projects")
    st.markdown(
        """
        **Retail Sales Optimization Using Data Analytics**
        - Tools Used: Python, R, SQL Workbench, Tableau
        - Cleaned and analyzed retail sales data to identify key trends, seasonal patterns, and top-performing product categories.
        - Developed interactive Tableau dashboards to present insights, enabling actionable strategies for revenue growth.
        - Conducted hypothesis testing in R to assess the effectiveness of discounting strategies, improving profitability by 10%.

        **Customer Churn Analysis**
        - Tools Used: Python, Power BI, Excel
        - Built a predictive churn model using Python, achieving 85% accuracy by analyzing customer demographics and engagement patterns.
        - Created Power BI dashboards to visualize churn drivers, helping stakeholders implement targeted retention strategies.
        """
    )

elif selection == "Technical Skills":
    st.header("Technical Skills")
    st.markdown(
        """
        - **Programming & Data Analysis:** Python, SQL, R, VBA, dplyr, ggplot2, Pandas, NumPy
        - **Data Visualization:** Tableau, Power BI, ggplot2, Matplotlib, Seaborn
        - **Database Management:** MySQL, SQL Workbench
        - **Business Tools:** Advanced Excel (Pivot Tables, VLOOKUP, HLOOKUP), Power Query, Power Pivot
        - **Statistical Analysis:** Hypothesis Testing, ANOVA, Regression Analysis
        """
    )

# Contact Information - Displayed at the bottom of the page
st.markdown(
    f"""
    <hr style="border:2px solid #4CAF50;">
    <h4 style="text-align: center;">California | (669) 246-2883 | <a href="mailto:sharmilakc631@gmail.com">sharmilakc631@gmail.com</a></h4>
    """,
    unsafe_allow_html=True,
)

# Footer
st.markdown(
    """
    <p style="text-align: center; color: gray;">Designed with ❤️ using Streamlit</p>
    """,
    unsafe_allow_html=True,
)

