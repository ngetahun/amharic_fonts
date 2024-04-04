NAME          = amharic_fonts
VERSION       = $(shell bash -c "cat amharic_fonts.spec | sed -n 's/^Version:\s*\(.*\)/\1/p'")
DIST          = $(NAME)-$(VERSION)

all: package

package:
	@echo "Building package..."
	@rm -rf dist-$(DIST)
	@mkdir dist-$(DIST)
	@cp -r $(shell git ls-files) dist-$(DIST)
	@echo "Zipping files."
	@tar cfvj $(DIST).tar.xz dist-$(DIST)
	@rm -r dist-$(DIST)
