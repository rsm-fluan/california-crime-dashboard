# run " shiny run --reload app.py "

from shiny import App, ui, render
import pandas as pd
import matplotlib.pyplot as plt

# --- Sample Data ---
df = pd.DataFrame(
    {
        "city": ["LA", "LA", "LA", "SD", "SD", "SF"],
        "crime": [120, 130, 110, 90, 100, 95],
        "month": ["Jan", "Feb", "Mar", "Jan", "Feb", "Jan"],
    }
)

# --- UI ---
app_ui = ui.page_fluid(
    ui.h2("Crime Dashboard"),
    ui.layout_sidebar(
        ui.sidebar(ui.input_select("city", "Select City:", ["LA", "SD", "SF"])),
        ui.output_plot("crime_plot"),
    ),
)


# --- Server ---
def server(input, output, session):
    @output
    @render.plot
    def crime_plot():
        sub = df[df["city"] == input.city()]
        fig, ax = plt.subplots()
        ax.bar(sub["month"], sub["crime"])
        ax.set_title(f"Crime Trend — {input.city()}")
        ax.set_ylabel("Crime Count")
        return fig


# --- Run App ---
app = App(app_ui, server)
