title_article, content_article, comment_article = input(), input(), input()
list_of_comments = []

print(f'<h1>\n\t{title_article}\n</h1>')
print(f'<article>\n\t{content_article}\n</article>')

while comment_article != 'end of comments':
    print(f'<div>\n\t{comment_article}\n</div>')
    comment_article = input()
