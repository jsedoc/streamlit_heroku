import streamlit as st
import streamlit.components.v1 as components
import json

PAGE_CONFIG = {"page_title":"More Examples","page_icon":":smiley:",
               "layout":"centered"}
st.set_page_config(**PAGE_CONFIG)




def main():
    st.title("Treemap with Highcharts in Streamlit")

    data = [
        {"id": "A", "name": "Technology", "color": "#434348", "value": 100, "change": 0.15},
        {"id": "A1", "name": "Apple", "parent": "A", "value": 60, "change": 0.30},
        {"id": "A2", "name": "Microsoft", "parent": "A", "value": 40, "change": -0.20},
        {"id": "B", "name": "Financials", "color": "#90ed7d", "value": 200, "change": 0.50},
        {"id": "B1", "name": "JPMorgan", "parent": "B", "value": 120, "change": 0.45},
        {"id": "B2", "name": "Goldman Sachs", "parent": "B", "value": 80, "change": 0.55}
    ]
    html = f"""
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/treemap.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <div id="container" style="height: 400px; min-width: 310px; max-width: 800px; margin: 0 auto"></div>
    <script>
        document.addEventListener('DOMContentLoaded', function () {{
            var data = {json.dumps(data)};
            Highcharts.chart('container', {{
                series: [{{
                    type: 'treemap',
                    layoutAlgorithm: 'squarified',
                    data: data,
                    dataLabels: {{
                        enabled: true,
                        format: '{{point.name}}: {{point.change}}%'
                    }},
                    levels: [{{
                        level: 1,
                        dataLabels: {{
                            enabled: true,
                            align: 'left',
                            verticalAlign: 'top',
                            style: {{
                                fontSize: '15px',
                                fontWeight: 'bold'
                            }}
                        }}
                    }}]
                }}],
                title: {{
                    text: 'Sector Performance'
                }},
                tooltip: {{
                    headerFormat: '',
                    pointFormat: 'The change in {{point.name}} is <b>{{point.change}}%</b>'
                }},
                colorAxis: {{
                    dataClasses: [{{
                        from: -0.1,
                        to: 0,
                        color: '#ff3333',
                        name: 'Negative'
                    }}, {{
                        from: 0.01,
                        to: 0.2,
                        color: '#48CFAD',
                        name: 'Positive'
                    }}]
                }}
            }});
        }});
    </script>
    """
    components.html(html,
        height=600,
    )



    # st.html(html)

if __name__ == "__main__":
    main()
