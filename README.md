# Menéame News Filter

Filter news from Menéame (https://www.meneame.net/)

Given a file containing a list of words, filters out news from Menéame if at least there is one of those words in its title.

## Requirements

	- Python 2.x
	- a .txt file called `words` containing one string per line
	- Chrome installed

## Process

1. Write in terminal `python meneame_news_filter.py`
2. A Chrome page will be opened, with the filtered news. At the end of the page you can see how many news where filtered
3. If you want to add/edit the words used to remove news, just edit the contents of `words.txt` (obs. do not let a line break at the end)
4. If you want to filter more/less pages from Menéame, add/remove `read_and_select("pageN")`

I hope you enjoy it!