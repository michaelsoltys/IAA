# After doing:
#		git add .
#		git commit .
# do this command:
# 	make git
# this will create an updated 
#		.git/gitHeadInfo.gin
# from which the title page version info (Git Version) is taken
REMOTE='184.169.244.79:~/Prof/wp-content/uploads/archive/Slides/'
CHP=chp4

# List of all chapter files
CHAPTERS = chp0 chp1 chp2 chp3 chp4 chp5 chp6 chp7 chp9.1-2 chp9.3 chp9.4 chp9.5 chp9appendix chp10
TEX_FILES = $(CHAPTERS:%=%.tex)
PDF_FILES = $(CHAPTERS:%=%.pdf)

# Default target - compile only changed files
.PHONY: all changed clean git upload

all: $(PDF_FILES)

# Rule to build individual PDF files only if tex file is newer
%.pdf: %.tex
	@if [ $< -nt $@ ] || [ ! -f $@ ]; then \
		echo "Compiling $< (changed or missing PDF)..."; \
		pdflatex $*; \
		pdflatex $*; \
		pdflatex $*; \
	else \
		echo "Skipping $< (PDF is up to date)"; \
	fi

# Compile only files that have changed
changed:
	@for chp in $(CHAPTERS); do \
		if [ $$chp.tex -nt $$chp.pdf ] || [ ! -f $$chp.pdf ]; then \
			echo "Compiling $$chp.tex (changed or missing PDF)..."; \
			pdflatex $$chp; \
			pdflatex $$chp; \
			pdflatex $$chp; \
		else \
			echo "Skipping $$chp.tex (PDF is up to date)"; \
		fi; \
	done

# Original single chapter build (backwards compatibility)
$(CHP).pdf : *.tex
	pdflatex $(CHP); \
	pdflatex $(CHP); \
	pdflatex $(CHP);

git: $(CHP).tex
	pdflatex $(CHP); \
	pdflatex $(CHP); \
	git add .; \
	git commit .; \
	.git/hooks/post-checkout; \
	pdflatex $(CHP);
	pdflatex $(CHP);
	git push;

upload:
	rsync -avz -e 'ssh -l ec2-user' chp[0-9].pdf chp10.pdf $(REMOTE)

# Force compile all chapters (original behavior)
force-all:
	@for chp in $(CHAPTERS); do \
		echo "Force compiling $$chp.tex..."; \
		pdflatex $$chp; \
		pdflatex $$chp; \
		pdflatex $$chp; \
	done

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb