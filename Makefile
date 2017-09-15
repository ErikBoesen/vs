PREFIX=/usr/local
DESTDIR=

INSTDIR=$(DESTDIR)$(PREFIX)
INSTBIN=$(INSTDIR)/bin
INSTMAN=$(INSTDIR)/share/man/man7

SCRIPT=vs
MANPAGE=$(SCRIPT).7

all:
	@echo did nothing. try targets: install, or uninstall.

install:
	pip3 install -r requirements.txt

	test -d $(INSTDIR) || mkdir -p $(INSTDIR)
	test -d $(INSTBIN) || mkdir -p $(INSTBIN)
	test -d $(INSTMAN) || mkdir -p $(INSTMAN)

	install -m 0755 $(SCRIPT) $(INSTBIN)
	install -m 0644 doc/$(MANPAGE) $(INSTMAN)

uninstall:
	rm -f $(INSTBIN)/$(SCRIPT)
	rm -f $(INSTMAN)/$(MANPAGE)

.PHONY: all install uninstall
