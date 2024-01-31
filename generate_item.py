markdown_type = "complex" # complex or simple
    
paper_name = ''
paper_url = ''
github_url = ''
author_name = ''
image_path = 'figures/{}.png'.format('')
conference = ""


star_format = '[![Star](https://img.shields.io/github/stars/{}.svg?style=social&label=Star)](https://github.com/{})'
conference_format = "[![Publish](https://img.shields.io/badge/Conference-{}-blue)]()"

if markdown_type == 'simple':
    final_str = "* "
    if len(conference) > 0:
        conference_item = conference_format.format(conference)
        final_str += conference_item
        final_str += " "
    if len(github_url) > 0:
        github_item = '/'.join(github_url.split('/')[-2:])
        final_str += star_format.format(github_item, github_item)
        final_str += " "
    final_str += "[{}]({}). {}. [[Paper]]({})".format(paper_name, paper_url, author_name, paper_url)
    if len(github_url) > 0:
        final_str += "[[Github]]({})".format(github_url)
    print(final_str)
else:
    main_item_format = '[{}]({}) <br> {} |'
    image_format = '<img width="1002" alt="image" src="{}"> |'
    github_format = '[Github]({}) <br> '
    paper_format = '[Paper]({})'
    publish = 'https://img.shields.io/badge/Conference-{}-blue'.format(conference)

    final_str = "|"
    flag = False
    if len(github_url) > 0:
        github_item = '/'.join(github_url.split('/')[-2:])
        final_str += star_format.format(github_item, github_item)
        flag = True
    if len(conference) > 0:
        conference_item = conference_format.format(conference)
        final_str += conference_item
        flag = True
    if flag:
        final_str += '<br>'

    final_str += main_item_format.format(paper_name, paper_url, author_name)
    final_str += image_format.format(image_path)

    if len(github_url) > 0:
        final_str += github_format.format(github_url)
    final_str += paper_format.format(paper_url)

    final_str += '|'
    print(final_str)