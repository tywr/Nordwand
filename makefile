build:
	python -m generate_font
	python -m scripts.banner
	python -m scripts.specimen_pdf

build-otf:
	python -m generate_font --otf

install-mac:
	cp -r fonts/otf/Nordwand-*.otf ~/Library/Fonts
