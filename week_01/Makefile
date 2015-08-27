BASENAME=week_01
 
all: slides
	

$(BASENAME)-notes.pdf: $(BASENAME)-notes.tex $(BASENAME)-body.tex Makefile 
	pdflatex -halt-on-error $(BASENAME)-notes
	pdflatex -halt-on-error $(BASENAME)-notes

$(BASENAME)-slides.pdf: $(BASENAME)-slides.tex $(BASENAME)-body.tex Makefile 
	pdflatex -halt-on-error $(BASENAME)-slides
	pdflatex -halt-on-error $(BASENAME)-slides
	# Merge with Python slides
	gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=$(BASENAME)-slides.joined.pdf $(BASENAME)-slides.pdf primer_1-2-3_subset.pdf

notes: $(BASENAME)-notes.pdf
	

slides: $(BASENAME)-slides.pdf $(BASENAME)-body.pdf
	

$(BASENAME)-body.pdf:
	

.PHONY: clean
clean:
	rm -f $(BASENAME)-{slides,notes,body}.pdf $(BASENAME)-{slides,notes,body}.dvi $(BASENAME)-{slides,notes,body}.aux $(BASENAME)-{slides,notes,body}.log $(BASENAME)-{slides,notes,body}.bbl $(BASENAME)-{slides,notes,body}.blg $(BASENAME)-{slides,notes,body}.bbl

