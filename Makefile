# IAA Repository Makefile
# Manages slides compilation and repository operations

# Slides directory and chapter files
SLIDES_DIR = Slides
CHAPTERS = chp0 chp1 chp2 chp3 chp4 chp5 chp6 chp7 chp9.1-2 chp9.3 chp9.4 chp9.5 chp9appendix chp10
TEX_FILES = $(CHAPTERS:%=$(SLIDES_DIR)/%.tex)
PDF_FILES = $(CHAPTERS:%=$(SLIDES_DIR)/%.pdf)

# Default target - compile only changed slides
.PHONY: all changed clean git slides

all: slides

# Compile all slides (only changed ones)
slides:
	@echo "Compiling slides in $(SLIDES_DIR)..."
	@cd $(SLIDES_DIR) && for chp in $(CHAPTERS); do \
		if [ $$chp.tex -nt $$chp.pdf ] || [ ! -f $$chp.pdf ]; then \
			echo "Compiling $$chp.tex (changed or missing PDF)..."; \
			pdflatex $$chp; \
			pdflatex $$chp; \
			pdflatex $$chp; \
		else \
			echo "Skipping $$chp.tex (PDF is up to date)"; \
		fi; \
	done

# Force compile all slides
force-slides:
	@echo "Force compiling all slides in $(SLIDES_DIR)..."
	@cd $(SLIDES_DIR) && for chp in $(CHAPTERS); do \
		echo "Force compiling $$chp.tex..."; \
		pdflatex $$chp; \
		pdflatex $$chp; \
		pdflatex $$chp; \
	done

# Git operations for entire repository
git:
	@echo "Performing git operations on entire IAA repository..."
	git add .
	git commit -m "Updated IAA repository: $(shell date '+%Y-%m-%d %H:%M:%S')"
	git push

# Clean compiled files in slides directory
clean:
	@echo "Cleaning compiled files in $(SLIDES_DIR)..."
	cd $(SLIDES_DIR) && rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

# Show status of repository
status:
	@echo "Repository status:"
	git status