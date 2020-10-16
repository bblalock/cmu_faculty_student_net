import plotly.express as px
import plotly.graph_objects as go

def community_bar(community_df, **kwargs):
    community_df = community_df[community_df['community'] > 0].rename(columns={'count':'size'})
    community_df['community'] = community_df['community'].astype(str)
    fig = px.bar(community_df,
                 y='size',
                 x='community',
                 text='ID: ' + community_df['community'].astype(str),
                 color='community',
                 log_x=False,
                 hover_name='Community ID: ' + community_df['community'].astype(str),
                 hover_data=['community', 'size'],
                 color_discrete_sequence=community_df.community_color.tolist(),
                 **kwargs
                 )

    fig.update_traces(textposition='auto',
                      insidetextanchor="end",
                      textangle=0,
                      hovertemplate="<b>Community ID: %{x}</b><br>Size: %{y}"
                      )

    fig.update_layout(
        hovermode="x",
        showlegend=False,
        # title_text="Community Size",
        # title_x=.5,
        uniformtext_minsize=12,
        # height=100,
        # width=500,
        font=dict(
            family="News Cycle, Arial Narrow Bold, sans-serif",
            size=12,
            color="white"
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(
            # title='Size of Community',
            title=None,
            constrain="domain",
            showgrid=True,
            gridcolor='rgba(0,0,0,0.2)',
            zeroline=False,
            showticklabels=False,
            tickformat=','
        ),
        xaxis=dict(
            title=None,
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            ticks='',
        ),
        legend=dict(
            title='Community',
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=go.layout.Margin(
            t=0,
            l=0,  # left margin
            r=0,  # right margin
            b=0,  # bottom margin
        )
    )
    return fig