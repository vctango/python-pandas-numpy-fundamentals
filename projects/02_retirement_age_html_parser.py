# Parses retirement age information from HTML tables using Pandas and transforms the data into a structured DataFrame for analysis.

import pandas as pd

retirement_html = """
<table>
<tr>
    <th>Year of Birth</th>
    <th>Normal Retirement Age</th>
</tr>
<tr>
    <td>1937 and prior</td>
    <td>65</td>
</tr>
<tr>
    <td>1938</td>
    <td>65 and 2 months</td>
</tr>
<tr>
    <td>1939</td>
    <td>65 and 4 months</td>
</tr>
<tr>
    <td>1940</td>
    <td>65 and 6 months</td>
</tr>
<tr>
    <td>1941</td>
    <td>65 and 8 months</td>
</tr>
<tr>
    <td>1942</td>
    <td>65 and 10 months</td>
</tr>
<tr>
    <td>1943-54</td>
    <td>66</td>
</tr>
<tr>
    <td>1955</td>
    <td>66 and 2 months</td>
</tr>
<tr>
    <td>1956</td>
    <td>66 and 4 months</td>
</tr>
<tr>
    <td>1957</td>
    <td>66 and 6 months</td>
</tr>
</table>
"""

retirement_age_df = pd.read_html(
    retirement_html
)[0]

print(retirement_age_df)
