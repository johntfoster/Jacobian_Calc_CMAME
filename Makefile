#==============================================================================================
# Important note: converting to pdf seems to loose the top space of the
# cover page.  This is due to the tex installation using the European A4 page size by default.
# fix this and the problem will go away.  The -t letter seems to fix this.
#==============================================================================================

REPORT = jacobian_calc_CMAME

#COMMON_FILES = Introduction Kinematics LinearIsotropicModel PlasticityModel

BIB_FILE = all

LATEX = latex -shell-esc
BIBTEX = bibtex
MAKEINDEX = makeindex
DVIPS = dvips
PS2PDF = ps2pdf

.PHONY: dvi ps pdf all clean

$(REPORT).pdf: $(REPORT).tex $(REPORT).ps 
	$(PS2PDF) $(REPORT).ps

$(REPORT).ps: $(REPORT).dvi
	$(DVIPS) $(REPORT).dvi

$(REPORT).dvi: $(REPORT).tex
	$(LATEX) $(REPORT).tex
	$(LATEX) $(REPORT).tex
	$(LATEX) $(REPORT).tex
	$(BIBTEX) $(REPORT)
	$(LATEX) $(REPORT).tex
	$(LATEX) $(REPORT).tex
#$(REPORT).dvi: $(REPORT).tex $(addsuffix .tex, $(COMMON_FILES))

clean:
	rm -f $(REPORT).{aux,toc,ids,ind,ilg,log,out,bbl,blg,lof,lot,ps,pdf,dvi,pyg,snm,nav,spl}
	#rm -f $(COMMON_FILES:=.aux)
