import json
from jsondiff import diff
from difflib import HtmlDiff
from html import escape  # Escape special characters for safe HTML output


def generate_html_diff(json1, json2):

    # diff_result = jsondiff.diff(json1, json2)
    # html_diff = HtmlDiff().make_file(json1, json2, context=True)
    from jsondiff import diff
    return diff(json1, json2)
