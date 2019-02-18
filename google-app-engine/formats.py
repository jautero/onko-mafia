from formatobjects import filter_weekly, filter_daily, format_spec
from icalformat import ical_generator
import os

def get_json_format():
    return format_spec('{ "week" : %(weekresult)s, "day" : %(dayresult)s }',
        {"weekresult":filter_weekly("true","false"), 
         "dayresult":filter_daily("true","false") })
def get_html_format(template_values):
    template_values.update({"weekresult":filter_weekly("on","ei"), "dayresult":filter_daily("on","ei"),
        "weekclass":filter_weekly("on","ei"), "dayclass":filter_daily("on","ei")})
    return format_spec(file(os.path.join(os.path.dirname(__file__),"index.html")).read(),template_values)

def get_badge_format():
    return format_spec(file(os.path.join(os.path.dirname(__file__),"badge.js")).read(),
        {"weekcolor":filter_weekly("#00ff00","#ff0000"),
         "weekword":filter_weekly("on","ei"),
         "daycolor":filter_daily("#00ff00","#ff0000"),
         "dayword":filter_daily("on","ei")})
         
def get_ical_format(upto,event_name):
    return ical_generator(upto,event_name)
