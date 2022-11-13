title_article = input()
content_article = input()
comment_article = input()
list_of_comments = []

print(f'<h1>\n\t{title_article}\n</h1>')
print(f'<article>\n\t{content_article}\n</article>')

while comment_article != 'end of comments':
    list_of_comments.append(comment_article)
    comment_article = input()

for comment in list_of_comments:
    print(f'<div>\n\t{"".join(comment)}\n</div>')
