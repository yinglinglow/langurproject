# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
server = app.server

print('heya')

if __name__ == '__main__':
    app.run_server(debug=True)
