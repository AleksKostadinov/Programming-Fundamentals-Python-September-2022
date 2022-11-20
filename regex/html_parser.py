import re

source_code = input()
title_pattern = r'<title>(.*)</title>'
content_pattern = r'<body>(.*)</body>'
remove_tags = r'<[^>]*>|\\n'
match_title = re.search(title_pattern, source_code)
match_content = re.search(content_pattern, source_code)
match_title = match_title[0]
match_content = match_content[0]
remove_match_title = re.findall(remove_tags, source_code)
remove_match_content = re.findall(remove_tags, source_code)
if match_title:
    for match in remove_match_title:
        match_title = match_title.replace(match, '')

if match_content:
    for match in remove_match_content:
        match_content = match_content.replace(match, '')
print(f'Title: {match_title}')
print(f'Content: {match_content}')
