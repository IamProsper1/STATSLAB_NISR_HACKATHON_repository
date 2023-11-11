#__IMPORTING NEEDED PACKAGES_____
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import openpyxl
import plotly.graph_objects as go
import time
from streamlit_option_menu import option_menu

#___IMPORTING DATAFRAMES FROM EXCEL_____
#_(1)_GDP at Current prices DF___
excel_file_GDPCP = 'GDPdata.xlsx'
sheet_name = 'CYGDP CP'
df_GDPCP = pd.read_excel(excel_file_GDPCP,
                   sheet_name=sheet_name,
                   usecols='D:AD',
                   header=4)
#___Dropping unnecessary rows & columns___
rows_to_drop_GDPCP = [0, 39, 41, 42, 43]
df_GDPCP = df_GDPCP.drop(rows_to_drop_GDPCP)

column_to_drop_GDPCP = 'Unnamed: 5'
df_GDPCP = df_GDPCP.drop(column_to_drop_GDPCP, axis=1)

#_(2)_GDP at constant 2017 prices
excel_file_GDPKP = 'GDPdata.xlsx'
sheet_name = 'CYGDP KP'
df_kp = pd.read_excel(excel_file_GDPKP,
                   sheet_name=sheet_name,
                   usecols='D:AD',
                   header=4)
#___Dropping unnecessary rows & columns___
rows_to_drop_kp = [0, 39, 41, 42, 43]
df_kp = df_kp.drop(rows_to_drop_kp)

column_to_drop_kp = 'Unnamed: 5'
df_kp = df_kp.drop(column_to_drop_kp, axis=1)


#_(3)_GDP by Expenditure
excel_file_GDPexp = 'GDPdata.xlsx'
sheet_name = 'T3 GDP CY'
df_expenditure = pd.read_excel(excel_file_GDPexp,
                   sheet_name=sheet_name,
                   usecols='D:AD',
                   header=5)

#___Dropping unnecessary rows & columns___
rows_to_drop_GDPexp = [0,6,12,20,21,22,23,24,25,26,27,28,29,30,
                       31,32,33,34,35,36,37,38,39,40,41,42,43,44,
                       45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]
df_expenditure = df_expenditure.drop(rows_to_drop_GDPexp)

column_to_drop_GDPexp = 'Unnamed: 4'
df_expenditure = df_expenditure.drop(column_to_drop_GDPexp, axis=1)


#_(4)_CPI Rwanda, Urban & Rural
excel_file_CPIURBAN = 'CPIdata.xlsx'
sheet_name = 'Urban'
df_cpiurban = pd.read_excel(excel_file_CPIURBAN,
                   sheet_name=sheet_name,
                   usecols='D:FO',
                   header=3)

excel_file_CPIRURAL = 'CPIdata.xlsx'
sheet_name = 'Rural'
df_cpirural = pd.read_excel(excel_file_CPIRURAL,
                   sheet_name=sheet_name,
                   usecols='D:FO',
                   header=3)

excel_file_CPIRDA = 'CPIdata.xlsx'
sheet_name = 'All Rwanda'
df_cpirda = pd.read_excel(excel_file_CPIRDA,
                   sheet_name=sheet_name,
                   usecols='D:FO',
                   header=3)

#___TITLES___
st.set_page_config(page_title="Rwanda's GDP 2022,",
                   page_icon=":bar_chart:",
                   layout="centered")

st.header("Rwanda's 2022 GROSS DOMESTIC PRODUCT AND CONSUMER PRICE INDEX")

  #___GDP growth by quater data__
quarters = ['First Quarter', 'Second Quarter', 'Third Quarter', 'Fourth Quarter']
values_quaters = [7.9, 7.5, 10, 7.3]
fig_GDP_growth_by_quater = go.Figure(data=[go.Bar(x=quarters, y=values_quaters, text=values_quaters,
                                                  textposition='auto', textfont=dict(size=30))])
fig_GDP_growth_by_quater.update_layout(title='2022 GDP growth by quater',
                  xaxis_title='Quarter',
                  yaxis_title='% increase')









   #___OPTION-MENU


#1. as a sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data", "More statistics"],
        icons=["house", "folder", "plus-lg"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#1D3347"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#5A7264",
            },
            "nav-link-selected": {"background-color": "darkgray"}
        },
    )

st.sidebar.write("Designed by;")
if st.sidebar.checkbox("STATSLAB"):
    st.sidebar.caption("AYINEBYONA Prosper")
    st.sidebar.caption("HANGU Dieu Merci")
if selected == "Home":

    # space_function
    st.write('#        ')
    # __Part 2.Important Economic Indicators___
    st.info("### 2022 IMPORTANT ECONOMIC INDICATORS")

    st.caption("Gross Domestic Product")
    target_number = 13716
    step = 4
    placeholder = st.empty()
    # __Simulate the counting animation for float numbers
    current_number = 0
    while current_number <= target_number:
        time.sleep(0.000000000000000001)  # Adjust the sleep time to control the speed of the animation
        placeholder.success(f'### {current_number:.2f} billions Rwf')
        current_number += step
    # __Display the final number
    placeholder.success(f'### {target_number} billions Rwf')

    st.caption("GDP per Capita (average income)")
    # ___Seting the target number
    target_number = 1035
    placeholder = st.empty()
    # ___Simulating the counting animation
    for i in range(target_number + 1):
        time.sleep(0.0001)  # Adjust the sleep time to control the speed of the animation
        placeholder.success(f'### {i} Thousands Rwf')

    st.caption("Gross National Income")
    target_number = 13428
    step = 4
    placeholder = st.empty()
    # __Simulate the counting animation for float numbers
    current_number = 0
    while current_number <= target_number:
        time.sleep(0.000000000000000001)  # Adjust the sleep time to control the speed of the animation
        placeholder.success(f'### {current_number:.2f} billions Rwf')
        current_number += step
    # Display the final number
    placeholder.success(f'### {target_number} billions Rwf')

    st.caption("Consumer Price Index [Index(Feb 2014=100)]")
    # __Set the target number
    target_number = 180.9
    step = 0.1
    placeholder = st.empty()
    # __Simulate the counting animation for float numbers
    current_number = 0.0
    while current_number <= target_number:
        time.sleep(
            0.000000000000000000000000000000000000001)  # Adjust the sleep time to control the speed of the animation
        placeholder.success(f'### {current_number:.2f}')
        current_number += step
    # Display the final number
    placeholder.success(f'### {target_number}')

    st.caption("Total population")
    target_number = 13.3
    step = 0.01
    placeholder = st.empty()
    # __Simulate the counting animation for float numbers
    current_number = 0.0
    while current_number <= target_number:
        time.sleep(0.0001)  # Adjust the sleep time to control the speed of the animation
        placeholder.success(f'### {current_number:.2f} millions')
        current_number += step
    # Display the final number
    placeholder.success(f'### {target_number} millions')

    # space_function
    st.write('#        ')
    st.write('       ')

    # __Part 3. GDP and Economic Growth___
    st.info("### GDP AND ECONOMIC GROWTH")

    # ___GDP by Kind of Activity (pie chart)___
    selected_rows = df_GDPCP.iloc[[2, 8, 22, 38], [0, -1]]  # Selecting rows by index and columns by name
    # Renaming the columns for better labeling
    selected_rows.columns = ['Activities description', '2022']
    # Create a pie chart
    # Create a pie chart with custom width and height
    fig_DPPbyactivities = px.pie(selected_rows, values='2022', names='Activities description',
                                 title='GDP by Kind of Activity(% contributions) in Rwf billions',
                                 width=600, height=600)
    # Show the pie chart
    st.write(" ##### 1. Gross Domestic product by Kind of Activity (at current prices)")
    st.markdown("Rwanda's GDP is mainly influenced by the service sector which was measured at 6,377 Frw billions,"
                "and the agriculture and industry sectors contributing almost equally with 3,415 Frw billions"
                " and 2,913 Frw billions respectively, while Adjustment for taxes less subsidies was measured at 1,012 Frw billions")
    st.plotly_chart(fig_DPPbyactivities)
    st.caption("The above chart depicts the percentage contribution by kind of activities to GDP,"
               "with Service sector contributing almost a half of Rwanda's GDP")

    # ___GDP by Expenditure___
    st.write(" ##### 2. Gross Domestic product by Expenditure (at current prices)")

    # __Select specific rows for creating bargraphs___
    selected_rows_GDPexpenditure = df_expenditure.iloc[
        [3, 4, 5, 11, 14, 10], [0, -1]]  # Selecting rows by index and columns by name

    # __Renaming the columns for better labeling___
    selected_rows_GDPexpenditure.columns = ['Expenditure', '2022']

    # __Ploting the bar graphs with text labels___
    # Create a bar graph with custom colors
    figEx = px.bar(selected_rows_GDPexpenditure, x='Expenditure', y='2022', text='2022',
                   title='2022 GDP by Expenditure',
                   color=selected_rows_GDPexpenditure['Expenditure'])

    # __Updating layout for text orientation and size__
    figEx.update_layout(yaxis_title='Expenditure in Frw billions', xaxis_title='Expenditure by category',
                        font=dict(size=17))

    # Show the plot
    st.markdown("Total final consumption (Government, Households and NGOs) Contributed the most to GDP (91%)")
    st.plotly_chart(figEx)
    st.caption("Due to higher imports than exports the Resource balance was negative")

    # __Economic growth__
    st.write(" ##### 3. Economic growth")

    # ____Extracting the 'Item' and the data for plotting the line graphs
    item_cp = df_GDPCP.iloc[0, 0]
    x_values_cp = df_GDPCP.columns[2:].astype(int)
    y_values_cp = df_GDPCP.iloc[0, 2:].astype(float)

    item_kp = df_kp.iloc[0, 0]
    x_values_kp = df_kp.columns[2:].astype(int)
    y_values_kp = df_kp.iloc[0, 2:].astype(float)

    # ____Creating the line graph
    fig_GDPgrowthrate = go.Figure()

    # ____Adding the first line from the df_GDPcp dataframe
    fig_GDPgrowthrate.add_trace(go.Scatter(x=x_values_cp, y=y_values_cp, mode='lines', name='GDP at Current prices'))

    # ____Adding the second line from the df_kp dataframe
    fig_GDPgrowthrate.add_trace(
        go.Scatter(x=x_values_kp, y=y_values_kp, mode='lines', name='GDP at Constant 2017 prices'))

    # ____Updating the layout
    fig_GDPgrowthrate.update_layout(title='Economic growth at different prices',
                                    xaxis_title='Year',
                                    yaxis_title='Total GDP in Frw billions')

    # __Show the line graph
    st.markdown(
        "The recent year has seen Economic growth, with the GDP rising by 25.5% when measured at current prices"
        " and 8.2% when measured at constant 2017 prices. The Economic growth when evaluated at constant 2017 prices, "
        "the growth rate appears comparatively lower, reflecting the adjustments made for inflationary effects. "
        "This adjustment accounts for changes in price levels, presenting a more accurate depiction of the actual increase "
        "in the quantity of goods and services produced, independent of inflation."
    )
    st.plotly_chart(fig_GDPgrowthrate)
    st.caption("Use the slider below to select the specific range of your choice to see its Economic growth rate")

    # __Economic growth rate slider__
    # ____Adding a slider to select the range of years
    selected_years_GDPgrowthrate = st.slider('Select Range of Years', min_value=1999, max_value=2022,
                                             value=(1999, 2022))

    # ____Finding the corresponding indices for the selected years in the first dataframe (df_cp)
    start_year_cp, end_year_cp = selected_years_GDPgrowthrate
    start_index_cp = df_GDPCP.columns.get_loc(start_year_cp)
    end_index_cp = df_GDPCP.columns.get_loc(end_year_cp)

    # _____Calculate the percentage change for the selected range of years in the first dataframe (df_cp)
    percentage_change_GDPCP = ((df_GDPCP.iloc[0, end_index_cp] - df_GDPCP.iloc[0, start_index_cp]) / df_GDPCP.iloc[
        0, start_index_cp]) * 100

    # ____Finding the corresponding indices for the selected years in the second dataframe (df_kp)
    start_year_kp, end_year_kp = selected_years_GDPgrowthrate
    start_index_kp = df_kp.columns.get_loc(start_year_kp)
    end_index_kp = df_kp.columns.get_loc(end_year_kp)

    # ____Calculating the percentage change for the selected range of years in the second dataframe (df_kp)
    percentage_change_kp = ((df_kp.iloc[0, end_index_kp] - df_kp.iloc[0, start_index_kp]) / df_kp.iloc[
        0, start_index_kp]) * 100

    # ____Displaying the percentage change for GDP at Current prices and GDP at Constant 2017 prices
    st.write(f'Economic growth at Current pricesㅤwas ㅤ{percentage_change_GDPCP:.2f}%')
    st.write(f'Economic growth at Constant 2017 pricesㅤwasㅤ {percentage_change_kp:.2f}%')

    # __Growth rate by kund of activity
    # _____Define the rows to plot
    rows_to_plot_kp = [2, 8, 22, 38]

    # _____Create a single line graph for all rows
    fig_GDPgrowthrate_by_activity = go.Figure()

    # ____Adding a line for each row to the graph
    for row_index in rows_to_plot_kp:
        item_kp = df_kp.iloc[row_index, 0]
        x_values_kp = df_kp.columns[2:].astype(int)
        y_values_kp = df_kp.iloc[row_index, 2:].astype(float)

        # ____Adding the line to the graph
        fig_GDPgrowthrate_by_activity.add_trace(go.Scatter(x=x_values_kp, y=y_values_kp, mode='lines', name=item_kp))

        # _____Updating the layout
    fig_GDPgrowthrate_by_activity.update_layout(title='Growth by Activity (at constant 2017 prices)',
                                                xaxis_title='Year',
                                                yaxis_title='GDP by activity in Frw billions')

    # ____Showing the line graph
    st.plotly_chart(fig_GDPgrowthrate_by_activity)
    st.caption("Use the slider below to select the specific range of your choice to see its growth rate by activity")


    # _____Function to calculate the percentage change for a specific row and selected years
    def calculate_percentage_change(data, start_year, end_year, row_index):
        start_index = data.columns.get_loc(start_year)
        end_index = data.columns.get_loc(end_year)
        percentage_change = ((data.iloc[row_index, end_index] - data.iloc[row_index, start_index]) / data.iloc[
            row_index, start_index]) * 100
        return percentage_change

        # _____Add a slider to select the range of years


    selected_years_all = st.slider('Select Range of Years', min_value=1999, max_value=2022, value=(1999, 2020))

    # _____Define new row names
    row_names = {2: 'AGRICULTURE, FORESTRY & FISHING', 8: 'INDUSTRY', 22: 'SERVICES',
                 38: 'TAXES LESS SUBSIDIES ON PRODUCTS'}

    # _____Display percentage changes for each renamed row below the slider
    for row_index, new_row_name in row_names.items():
        percentage_change = calculate_percentage_change(df_kp, selected_years_all[0], selected_years_all[1], row_index)
        st.write(f'Growth rate for {new_row_name}ㅤwas ㅤ {percentage_change:.2f}%')

        # ___Activies' contribution to GDP growth
    # __Define the items and their values
    items = ["Agriculture", "Industry", "Services", "Adjustment"]
    values = [0.4, 0.9, 5.7, 1.1]

    # ___Create comparison circles
    fig = go.Figure()

    for i, (item, value) in enumerate(zip(items, values)):
        fig.add_trace(go.Indicator(
            mode="number+gauge",
            value=value,
            title={'text': f"{item}: {value}"},
            gauge={'axis': {'range': [0, 8.2], 'tickwidth': 1, 'tickcolor': "white"},
                   'bar': {'color': 'blue'},
                   'shape': 'angular'},
            domain={'row': 1, 'column': i}))

    fig.update_layout(grid={'rows': 4, 'columns': len(items)})

    # ___Display the plot using Streamlit
    st.write("##### ")
    st.write("##### ")
    st.write("##### Activies' contribution to GDP growth")
    st.caption(
        "Contributing to an overall 8.2% GDP growth, the collective impact of four key sectors can be seen below.")
    st.plotly_chart(fig)


    # __NOMINAL VS REAL GDP
    # ____Function to convert nominal value to real value and vice versa
    def convert_values(input_value, is_nominal_to_real=True):
        if is_nominal_to_real:
            return float(input_value) * (10593 / 13716)
        else:
            return float(input_value) / (10593 / 13716)

        # ____Seting up the layout


    st.write('##### 4. Nominal vs Real GDP')
    st.markdown(
        "by looking at the Nominal GDP(13,716 Frw billions) and Real GDP [measured at constant 2017 prices(10,593 Frw billions)]"
        " you can see the impact of inflation on the overall value of goods and services produced within Rwanda.")
    st.caption("The below Nominal/Real GDP converter lets you input and convert different economic values."
               "You can compute and compare the nominal(current Frw prices) and real(measured at constant 2017 Frw prices) GDP")

    # ____Creating two input boxes for nominal and real values
    nominal_value = st.text_input(label='Nominal/Current price', key='nominal')
    if nominal_value:
        try:
            real_value = convert_values(nominal_value, is_nominal_to_real=True)
            st.write(f"Converted Real Value: ㅤ{real_value}")
        except ValueError:
            st.write("Real Value:")

    real_value = st.text_input(label='Real/2017 price', key='real')
    if real_value:
        try:
            nominal_value = convert_values(real_value, is_nominal_to_real=False)
            st.write(f"Converted Nominal Value: ㅤ{nominal_value}")
        except ValueError:
            st.write("Nominal Value:")

    # __CONSUMER PRICE INDEX___
    st.write("###   ")
    st.write("###   ")
    st.info("### CONSUMER PRICE INDEX")

    # __Change in CPI
    # _____Extract data for the line graphs
    x = list(df_cpirda.columns[2:])
    y1 = df_cpirda.iloc[1, 2:].values
    y2 = df_cpiurban.iloc[1, 2:].values
    y3 = df_cpirural.iloc[1, 2:].values

    # ____Create traces for each line graph
    trace1 = go.Scatter(x=x, y=y1, mode='lines', name='RWANDA GENERAL INDEX (CPI)')
    trace2 = go.Scatter(x=x, y=y2, mode='lines', name='URBAN GENERAL INDEX (CPI)')
    trace3 = go.Scatter(x=x, y=y3, mode='lines', name='RURAL GENERAL INDEX (CPI)')

    # ____Create layout
    layout = go.Layout(xaxis=dict(title='Year(s)'), yaxis=dict(title='GENERAL INDEX (CPI)', range=[80, 200]))

    # ____Create figure and plot
    fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

    # ____Display the plot using Streamlit
    st.write('##### 1. Change in General CPI over time (Reference: February 2014=100)')
    st.plotly_chart(fig)
    st.caption("On average, prices for consumer goods and services in Rwanda have increased by 80.9% since 2014")

    # __COMPONENTS OF RWANDA CPI
    st.write('##### 2. components of Rwanda CPI')
    st.markdown("These components collectively represent Rwanda basket of goods and services, "
                "with Food and non-alcoholic beverages contributing the most (39%) to the national basket of goods and services.")

    st.markdown("In the box below you can see and select specific CPI components to see their weights, "
                "each bar graph will display the component's relative weights in the Rwanda's basket of goods and services.")

    # _____Add a multiselect box to select items for the bar graph
    selected_items = st.multiselect('Select Items to Display', list(df_cpirda.iloc[3:19, 0]))

    # _____Extract data for the bar graph based on the selected items
    filtered_data = df_cpirda[df_cpirda.iloc[:, 0].isin(selected_items)]

    # _____Extract data for the bar graph
    items = filtered_data.iloc[:, 0].values
    values = filtered_data.iloc[:, 1].values

    # _____Create a bar graph
    fig2 = go.Figure([go.Bar(x=values, y=items, orientation='h')])

    # _____Customize the layout
    fig2.update_layout(title_text='Weights of the selected components', xaxis_title='Weights', yaxis_title='Components')

    st.plotly_chart(fig2)

    st.info("### DATA SETs")
    # Display the CPI data in Streamlit
    if st.checkbox('Show Dataset'):
        st.write('GDP at current prices')
        st.write(df_GDPCP)
        st.write('GDP at constant 2017 prices')
        st.write(df_kp)
        st.write('GDP by Expenditure')
        st.write(df_expenditure)
        st.write('RWANDA CPI data')
        st.write(df_cpirda)
        st.write('URBAN CPI data')
        st.write(df_cpiurban)
        st.write('RURAL CPI data')
        st.write(df_cpirural)



if selected == "Data":
    # space_function
    st.write('#        ')
    # DATA
    # __Part last.Data sets___
    st.info("### DATA SETs")
    # Display the CPI data in Streamlit
    st.write('GDP at current prices')
    st.write(df_GDPCP)
    st.write('GDP at constant 2017 prices')
    st.write(df_kp)
    st.write('GDP by Expenditure')
    st.write(df_expenditure)
    st.write('RWANDA CPI data')
    st.write(df_cpirda)
    st.write('URBAN CPI data')
    st.write(df_cpiurban)
    st.write('RURAL CPI data')
    st.write(df_cpirural)


if selected == "More statistics":
    # MORE
    # __ADDITIONAL STATISTICS ON SIDEBAR__
    st.info('### Additional Statistics')
    if st.checkbox("#### Other Consumer Price Indices in Nov-2022(Urban only)"):
        st.markdown("Base: 2014; Reference: February 2014=100")
        st.caption("Local Goods Index")
        st.success(' #### 154.9')
        st.caption(" Imported Goods Index")
        st.success(' #### 168')
        st.caption("Fresh Products index")
        st.success(' #### 217.3')
        st.caption("Energy index")
        st.success(' #### 162.9')
        st.caption("General Index excluding fresh Products and energy")
        st.success(' #### 144.7')

    if st.checkbox("#### Exchange rate"):
        st.caption("Exchange rate (per US dollar)")
        st.success(' #### 1,031 Rwf')

    if st.checkbox("#### GDP Deflator"):
        st.caption("2022 GDP Deflator (Based on 2017=100)")
        st.success(' #### 129')

    if st.checkbox("#### National income and expenditure (Rwf billions)"):
        st.caption("Gross National Disposible Income (GNI + Current transfers, net)")
        st.success(' #### 14,437')
        st.caption(
            "Gross National Saving (Gross National Disposible Income Less Final consumption expenditure)")
        st.success(' #### 1,966')
        st.caption("Net lending to the rest of the world (Gross National Saving Less Gross capital formation)")
        st.success(' #### -1,393')

    if st.checkbox("#### 2022 GDP growth by quarters"):
        st.caption("Measured at constant 2017 prices the year 2022 to grow by 8.2 % when compared to 2021. "
                           "                                           below are 2022 GDP growth by each quarter")
        st.plotly_chart(fig_GDP_growth_by_quater)




#ENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDENDEND
st.write("#                                        ")
st.write("#                                        ")
st.write("#                                        ")

st.caption("_________________________________________________________________________________________________________")




# Add an image to the sidebar
col1, col2, col3 = st.columns(3)
image1 = Image.open('images/NISR.png')
image3 = Image.open('images/statslab logo a.jpg')
col1.image(image1,
         caption= 'NISR',
         width=75)

col3.image(image3,
         caption= 'STATSLAB',
         width=75)


st.caption("### Source links")
st.caption("Gross Domestic Product 2022 (GDP) and Consumer Price Index 2022 (CPI). Accessed from www.statistics.gov.rw")
st.caption("GDP National Accounts, 2022: https://www.statistics.gov.rw/publication/1914")
st.caption("Consumer Price Index (CPI) - November 2022: https://www.statistics.gov.rw/publication/1873")