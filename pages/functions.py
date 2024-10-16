from datetime import datetime
import numpy as np
import pandas as pd
from plotly import graph_objects as go
import plotly.express as px


def process_times(time_list, adjust=False):
    '''
    Process the times to completion

    Parameters:
    -----------
    time_list : list of lists
        List of 2-item lists where first element is time-to-completion in
        minutes and second element is name of the item
    adjust : string
        Name of item to reset to np.nan (used when want line to extend to when
        stopped reproduction, without it marking it as another item complete).
        Default is False (which means nothing is adjusted).

    Returns:
    --------
    plt_times: dataframe
        Processed dataframe of times, ready for plotting
    '''
    # Create times dataframe...

    # Convert to dataframe
    times = pd.DataFrame(time_list, columns=['time', 'item'])

    # Sort the DataFrame by 'time' to correctly plot the ECDF
    times_clean = times.sort_values(by='time').reset_index(drop=True)

    # Compute the ECDF values
    times_clean['ecdf'] = np.arange(
        1, len(times_clean) + 1) / len(times_clean) * 100

    # Amend item to set as np.nan (so time extends to that point)
    if adjust is not False:
        times_clean.loc[times_clean['item'] == adjust, 'ecdf'] = np.nan

    # Insert the starting point (0, 0) in the ECDF
    times_clean.loc[-1] = [0, 'Start', 0]
    times_clean.index = times_clean.index + 1
    times_clean = times_clean.sort_index()

    # Convert time to hours
    times_clean['hours'] = times_clean['time']/60

    # Add points for the 90 degree turns in the line...

    # Adjust index so it goes 0 2 4 6...
    times_original = times_clean.copy()
    times_original.index = times_clean.index*2

    times_extra = times_clean.copy()

    # Get result from row 1 to final, and add another row with np.nan
    next_result = times_clean['time'][1:].reset_index(drop=True)
    next_result[len(next_result)] = np.nan
    # Replace time with those values (i.e. the value from the row below)
    times_extra['time'] = next_result
    times_extra['item'] = np.nan
    # Then adjust index so it goes 1 3 5 7...
    times_extra.index = (times_extra.index*2)+1

    # Combine (so have alternating rows from each due to odd and even indexes)
    plt_times = pd.concat([times_original, times_extra]).sort_index()

    # Convert time to hours
    plt_times['hours'] = plt_times['time']/60

    return plt_times


def success_interactive(times_df, fig, label, colour):
    '''
    Create interactive plot of time-to-completion

    Parameters:
    -----------
    times_df : dataframe
        Dataframe of times processed for plotting by process_times()
    fig : go.figure object
        To plot on
    label : string
        Label for the line
    colour : string
        Colour of line
    '''
    # Line
    fig.add_trace(go.Scatter(
        x=times_df['hours'],
        y=times_df['ecdf'],
        mode='lines',
        hoverinfo='skip',
        line_color=colour,
        name=label,
        legendgroup=label))
    # Scatter
    items_only = times_df[times_df['item'].notna()].copy()
    fig.add_trace(go.Scatter(
        x=items_only['hours'],
        y=items_only['ecdf'],
        mode='markers',
        marker=dict(color=colour, size=6),
        name=label,
        legendgroup=label,
        showlegend=False,
        hovertext=items_only['item'],
        hoverlabel=dict(namelength=0),
        hovertemplate=(
            '%{hovertext}<br>Time: %{x:.1f} hours<br>Completion: %{y:.1f}%')))


def success_static(times_df, ax, label, colour):
    '''
    Create static/non-interactive plot of time-to-completion

    Parameters:
    -----------
    times_df : dataframe
        Dataframe of times processed for plotting by process_times()
    ax : matplotlib axis
        To plot lines on
    label : string
        Label for the line
    colour : string
        Colour of line
    '''
    ax.plot(times_df['hours'], times_df['ecdf'], marker='.', markevery=2,
            label=label.replace('<br>', '\n'), color=colour)


def eval_chart(df):
    '''
    Create a stacked bar chart presenting the results from evaluation for
    each study.

    Parameters:
    -----------
    df : dataframe
        Wide dataframe where columns are result of evaluation, and rows
        are the study
    '''
    eval = (df
            .melt(ignore_index=False)
            .reset_index()
            .rename(columns={'index': 'guideline',
                             'variable': 'result',
                             'value': 'count'}))

    # Add percentages
    eval['total'] = eval['count'].groupby(eval['guideline']).transform('sum')
    eval['percent'] = eval['count'] / eval['total']
    eval['percentage'] = round(eval['percent']*100, 1).astype(str) + '%'

    # Create stacked bar visualisation
    fig = px.bar(
        eval,
        x='percent',
        y='guideline',
        color='result',
        color_discrete_map={'fully': '#06a94d',
                            'partially': '#ffd68c',
                            'not': '#ff9999',
                            'na': '#d1dcea'},
        orientation='h',
        hover_data={
            'count': True,
            'percent': False,
            'percentage': True,
            'guideline': False,
            'result': False})

    # Amend x axis label and ticks
    fig.update_layout(xaxis=dict(
        range=[0, 1],
        tickmode='array',
        tickvals=[0, 0.2, 0.4, 0.6, 0.8, 1],
        ticktext=['0%', '20%', '40%', '60%', '80%', '100%'],
        title=''))

    # Amend y axis label and order, and add space between ticks and plot
    fig.update_layout(yaxis=dict(
        autorange='reversed',
        title=''))
    fig.update_yaxes(ticksuffix='  ')

    # Relabel legend
    fig.update_layout(legend_title_text='Result')
    newnames = {'fully': 'Fully met', 'partially': 'Partially met',
                'not': 'Not met', 'na': 'Not applicable'}
    fig.for_each_trace(lambda t: t.update(name=newnames[t.name]))

    # Show without toolbar
    fig.show(config={'displayModeBar': False})


def min_hour(time):
    '''
    Creates a string with time in minutes, or hours and minutes

    Parameters:
    -----------
    time: int
        Time in minutes

    Returns:
    --------
    string : str
        String stating the time in minutes, or hours and minutes
    '''
    return f'{int(time)}m, or {int(time)//60}h {int(time)%60}m'


def calculate_times(used_to_date, times, limit=True):
    '''
    Calculates the time used today, total time used, and time remaining.

    Parameters:
    -----------
    used_to_date : int
        Total time used prior to that day in minutes
    times : list
        List of tuples with 24h times
        Example: [('11.01', '12.13'), ('14.45', '14.59')]
    limit : boolean
        Whether there is a 40h time limit (and hence, whether to return
        proportion of time used, and time remaining)
    '''
    FMT = '%H.%M'
    total_min = 0
    for t in times:
        # Convert to datetime object
        h0 = datetime.strptime(t[0], FMT)
        h1 = datetime.strptime(t[1], FMT)
        # Find difference in minutes and add to total
        total_min += (h1 - h0).total_seconds() / 60

    # Time in hours and minutes
    print(f'Time spent today: {min_hour(total_min)}')

    # Total time used
    total_used = total_min + used_to_date
    print(f'Total used to date: {min_hour(total_used)}')

    if limit:
        # Find time remaining
        max = 40*60
        remain_min = max - total_used
        print(f'Time remaining: {min_hour(remain_min)}')

        # Find proportion out of 40 hours
        prop = round((total_min+used_to_date)/max*100, 1)
        print(f'Used {prop}% of 40 hours max')


def plot_scatter(var, sho, hua, lim, kim, ana, her, woo):
    '''
    Create scatter plot of variable against reproduction success, with dot size
    from time taken.

    Parameters:
    -----------
    var: string
        Name of variable to plot
    sho: number
        Value for Shoaib and Ramamohan 2021
    hua: number
        Value for Huang et al. 2019
    lim: number
        Value for Lim et al. 2020
    kim: number
        Value for Kim et al. 2021
    ana: number
        Value for Anagnostou et al. 2022
    her: number
        Value for Hernandez et al. 2015
    woo: number
        Value for Wood et al. 2021
    '''
    # Create data frame with columns for study, % items reproduced,
    # time (minutes) spent on reproduction, and the input variable
    df = pd.DataFrame({
        'Shoaib and Ramamohan 2021': [94, 1694, sho],
        'Huang et al. 2019': [37.5, 1450, hua],
        'Lim et al. 2020': [100, 747, lim],
        'Kim et al. 2021': [100, 875, kim],
        'Anagnostou et al. 2022': [100, 130, ana],
        # 'Johnson et al. 2021': [],
        'Hernandez et al. 2015': [12.5, 1076, her],
        'Wood et al. 2021': [100, 230, woo]
    }).T.reset_index()
    df.columns = ['study', 'reproduce', 'time', var]

    # Create plot
    fig = px.scatter(df, x=var, y='reproduce', size='time',
                     hover_data={'study': True})
    fig.update_layout(xaxis_range=[-10, 110],
                      yaxis_range=[-10, 110],
                      yaxis_title='Items reproduced',
                      xaxis_ticksuffix='%',
                      yaxis_ticksuffix='%')
    fig['data'][0]['showlegend'] = True
    fig['data'][0]['name'] = ('<b>Dot size:</b><br>Time spent<br>on ' +
                              'reproduction<br>(smaller=quicker)')
    return fig
