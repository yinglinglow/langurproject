# -*- coding: utf-8 -*-
import dash

app = dash.Dash()
server = app.server

print('hello world!!!!!!')

if __name__ == '__main__':
    app.run_server(debug=True)
