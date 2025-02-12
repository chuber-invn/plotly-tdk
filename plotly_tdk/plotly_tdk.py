import plotly.graph_objects as go
import plotly.io as pio
from PIL import Image

tdk_logo = Image.open('tdk_logo.png')
tdk_link = f'<a href="https://trustedpositioning.tdk.com/">TDK Logo</a>'

tdk_template = go.layout.Template()

# Show the logo on the top left
tdk_template.layout = go.Layout(
    font_family='arial',  # TDK Font
    plot_bgcolor='#FFFFFF',
    paper_bgcolor='#F0F0F0',  # Grey colors for paper and dashes
    xaxis=dict(gridcolor='#D0D0D0', griddash='dot'),
    yaxis=dict(gridcolor='#D0D0D0', griddash='dot'),
    images=[
        dict(
            name='logo',
            source=tdk_logo,
            xref='paper',
            yref='paper',
            x=0,
            y=1.02,
            sizex=0.2,
            sizey=0.2,
            xanchor='left',
            yanchor='bottom',
        )
    ]
)

# Trick to make the logo a hyperlink, use an invisible annotation
tdk_template.layout.annotations = [dict(
    name='hyperlink',
    text=tdk_link,
    showarrow=False,
    x=0,
    y=1.02,
    font=dict(size=70),
    xref='paper',
    yref='paper',
    xanchor='left',
    yanchor='bottom',
    opacity=0,
)]

# Set the template
pio.templates["tdk"] = tdk_template