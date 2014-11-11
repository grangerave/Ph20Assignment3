Ph20Assignment4.pdf:Ph20Assignment4.tex gitlog.txt Assignment3Full.pdf
gitlog.txt:
	git log > gitlog.txt
Assignment3Full.pdf:Ph20Assignment3Full.tex Grapher.py Ph20Assignment3.py

	python Ph20Assignment3.py
	pdflatex -interaction=batchmode Ph20Assignment3Full.tex
	pdflatex -interaction=batchmode Ph20Assignment4.tex
	open Ph20Assignment4.pdf