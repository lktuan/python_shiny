# Reactive dashboard with Shiny for Python

1. Create `.venv` environment, active it, install **Shiny** with: `pip install shiny`;
2. Get the template: `shiny create --template dashboard --mode express --github posit-dev/py-shiny-templates`;
3. Install deps: `pip install -r .\dashboard\requirements.txt`;
4. Click the *RUN* button on `app.py` or run: `shiny run .\dashboard\app.py` (I noticed then dashboard will be exposed to port `8000` of the localhost while it was a random port if we clicked the button);
5. Play a bit with the sample dashboard, then delete everything and start over from the scratch.



# Sources:

1. <https://training.talkpython.fm/courses/details/reactive-web-dashboards-with-shiny-for-data-science>;
2. <https://talkpython.github.io/reactive-web-dashboards-with-shiny-course/>;
3. <https://shiny.posit.co/py/>;
4. <https://shiny.posit.co/py/templates/dashboard/index.html>;
5. <https://medium.com/berk-orbay/deploying-shinypy-0fa449a019e0>

