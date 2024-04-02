from IPython.core.display import HTML
import inspect

"""
    Custom error messages. error(...) will display a nice css-styled
    error message and abort the current cell execution by raising a
    (quiet) exception.
"""
class StopExecution(Exception):
    def _render_traceback_(self):
        pass

def error(title, msg):
    display(HTML(f"""
        <div class="error">
            <div class="title"><b>Error:</b> {title}</div>
            <div class="msg">{msg}</div>
        </div>
    """))
    raise StopExecution

def okay(title, msg):
    display(HTML(f"""
        <div class="okay">
            <div class="title">{title}</div>
            <div class="msg">{msg}</div>
        </div>
    """))

def check_variable(name, msg):
    globs = inspect.stack()[1][0].f_globals
    # if not globs:
    #     globs = globals()
    if name in globs and globs[name] != None:
        return
    else:
        error(f"Variable <code>{name}</code> undefined.", msg)

def check_passed(msg):
    print(f"✓ {msg}")

def test_passed(msg):
    okay("All tests passed!", msg)

def test_failed(msg):
    error("Not all tests passed", msg)








##     ## ######## ##     ## ##          ##     ## ########
##     ##    ##    ###   ### ##          ##     ## ##    ##
##     ##    ##    #### #### ##          ##     ##     ##
#########    ##    ## ### ## ##          ##     ##    ##
##     ##    ##    ##     ## ##           ##   ##    ##
##     ##    ##    ##     ## ##            ## ##     ##
##     ##    ##    ##     ## ########       ###      ##


# HTML output for juypter notebooks version 7
html_v7 = r"""
<style>

/* Hide first two cells */
div.jp-Cell:nth-child(1),
div.jp-Cell:nth-child(2) { display: none; 
                                       / * border: 5px solid red !important; */} 

.jp-WindowedPanel-window:before {
  content: 'FDS style loaded succesfully.';
  display: block;
  font-size: 9pt;
  margin-left: 2em;
  color: #999;
}

.jp-Notebook h1 { margin-top: 3em !important; }
.jp-Notebook h2 { margin-top: 2em !important; }

.jp-WindowedPanel-inner {
    width: 80% !important;
    min-width: 50em;
    font-size: 12pt;
    line-height: 18pt;
    margin: 0px auto;
}

/*
    Apply color scheme
*/

/* Changes color of strip shown for selected cells */
div.jp-Cell.jp-mod-selected div.jp-Collapser {
    background-color: #45cc37 !important;
}

/*
    Custom error and okay messages (see error(...) above)
*/
.jp-OutputArea-output .error {
    border: 2px solid #ff4a6e;
    border-radius: 5px;
    text-align: left;
}

.jp-OutputArea-output .okay {
    border: 2px solid #45cc37;
    border-radius: 5px;
    text-align: left;
}

.error .title {
    background-color: #ff4a6e;
    padding-top: 5px;
    text-indent: 1ex;
}

.okay .title {
    background-color: #45cc37;
    padding-top: 5px;
    text-indent: 1ex;
}
.error .title b, .okay .title b { color: #fff; }

.error .msg, .okay .msg {
    margin: 1ex;
}


/*
    Custom markup
*/

.note {
    font-size: 11pt;
    line-height: 12pt;
    font-style: italic;
    margin: 1ex 2ex;
}

.advanced { background-color: #ff0066; color: #001a33; padding: 6px 6px 3px 6px; border-radius: 4px }

.test {
    font-size: 14pt;
    color: #0077b5;
    display: flex;
    align-items: center;
    text-align: center;
}
.test::before, .test::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid #0077b5;
}
.test::before {
    margin-right: .25em;
}
.test::after {
    margin-left: .25em;
}


.task .no {
    font-size: 25pt;
    line-height: 35pt;
    text-align: center;
    color: #fff;
    flex: 0 0 35pt;
    margin: 10pt 10pt 10pt 5pt;
    position: relative;
    z-index: 10;
}

.task .no:after {
    content: '';
    background-color: #0077b5;
    border-radius: 50%;
    display: block;
    float: left;
    width: 35pt;
    height: 35pt;
    margin-right: -35pt;
    position: relative;
    bottom: 0;
    z-index: -1;
}

.task .text {
    flex-grow: 1;
    align-self: center;
    padding-right: 20pt;
}

.task {
    font-size: 110%;
    line-height: 115%;
    display: flex;
    flex-wrap: nowrap;
    align-items: start;
    margin: 1em 0em 0em 0em;
}

/*
  Hints environment
*/

.hints li { margin-bottom: 1ex; }

.hints li button {
    background-color: #727377;
    border: 0;
    padding: 2pt 8pt;
    color: #fff;
    border-radius: 5px;
}
.hints li button:hover { background-color: #ff4a6e ; }

</style>
"""

##     ## ######## ##     ## ##          ##     ##  #######
##     ##    ##    ###   ### ##          ##     ## ##     ##
##     ##    ##    #### #### ##          ##     ## ##
#########    ##    ## ### ## ##          ##     ## ########
##     ##    ##    ##     ## ##           ##   ##  ##     ##
##     ##    ##    ##     ## ##            ## ##   ##     ##
##     ##    ##    ##     ## ########       ###     #######

# HTML output for juypter notebooks below version 7
html_v6 = r"""
<style>

/* Hide first two cells */
#notebook-container > div.cell:nth-child(1),
#notebook-container > div.cell:nth-child(2) { display: none} 

#notebook-container:before {
  content: 'FDS style loaded succesfully.';
  display: block;
  font-size: 9pt;
  color: #999;
}

h1 { margin-top: 3em !important; }
h2 { margin-top: 2em !important; }

#notebook-container {
    width: 55% !important;
    min-width: 40em;
    font-size: 12pt;
    line-height: 18pt;
}

div.prompt {
    /* Decrease width of left sidebar */
    min-width: 10ex !important; 
    font-size: 10pt; 
}


/*
    Apply color scheme
*/
.edit_mode div.cell.selected::before {
    background-color: #45cc37;
}

.edit_mode div.cell.selected {
    border-color: #45cc37;
}

div.cell.selected::before,
div.cell.selected.jupyter-soft-selected::before {
    background-color: #0077b5;
}

div.input_prompt { color: #0077b5; }
div.output_prompt { color: #ff4a6e; }

/*
  Adjust widget look 
*/

.widget-hslider { height: auto !important; }

.jupyter-widgets:not(.widget-interact) {
    padding: 10px;
    border: 1px solid #ced1db;
    border-radius: 2px;
    margin: 10px auto;
    background-color: #f5f6fa;
}

.jupyter-widgets label, .jupyter-widgets .widget-readout {
    font-size: 14pt;
}

.jupyter-widgets .widget-radio-box label {
    font-size: 12pt;
}

.jupyter-widgets label {
    width: auto !important;
}

.jupyter-widgets .widget-readout {
    background-color: #fff;
}


/*
    Custom error and okay messages (see error(...) above)
*/
.output_area .error {
    border: 2px solid #ff4a6e;
    border-radius: 5px;
    text-align: left;
}

.output_area .okay {
    border: 2px solid #45cc37;
    border-radius: 5px;
    text-align: left;
}

.error .title {
    background-color: #ff4a6e;
    padding-top: 5px;
    text-indent: 1ex;
}

.okay .title {
    background-color: #45cc37;
    padding-top: 5px;
    text-indent: 1ex;
}
.error .title b, .okay .title b { color: #fff; }

.error .msg, .okay .msg {
    margin: 1ex;
}


/*
    Custom markup
*/

.note {
    font-size: 11pt;
    line-height: 12pt;
    font-style: italic;
    margin: 1ex 2ex;
}

.advanced { background-color: #ff0066; color: #001a33; padding: 6px 6px 3px 6px; border-radius: 4px }

.test {
    font-size: 14pt;
    color: #0077b5;
    display: flex;
    align-items: center;
    text-align: center;
}
.test::before, .test::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid #0077b5;
}
.test::before {
    margin-right: .25em;
}
.test::after {
    margin-left: .25em;
}


.task .no {
    font-size: 25pt;
    line-height: 40pt;
    text-align: center;
    color: #fff;
    flex: 0 0 35pt;
    margin: 10pt 10pt 10pt 5pt;
    position: relative;
    z-index: 10;
}

.task .no:after {
    content: '';
    background-color: #0077b5;
    border-radius: 50%;
    display: block;
    float: left;
    width: 35pt;
    height: 35pt;
    margin-right: -35pt;
    position: relative;
    bottom: 0;
    z-index: -1;
}

.task .text {
    flex-grow: 1;
    align-self: center;
    padding-right: 20pt;
}

.task {
    font-size: 110%;
    line-height: 115%;
    display: flex;
    flex-wrap: nowrap;
    align-items: start;
    margin: 1em 0em 0em 0em;
}

/*
  Hints environment
*/

.hints li { margin-bottom: 1ex; }

.hints li button {
    background-color: #727377;
    border: 0;
    padding: 2pt 8pt;
    color: #fff;
    border-radius: 5px;
}
.hints li button:hover { background-color: #ff4a6e ; }

/* .dst-modified { border: 1px solid red !important; } */
</style>
"""

# This attempts to keep some backwards compatibility with notebooks v6
import notebook
html = html_v7
try:
    major_version = int(notebook.__version__.split('.')[0])
    print(f"Notebook version {major_version}")
    if major_version < 7:
        html = html_v6
except: 
    pass
display(HTML(html))
