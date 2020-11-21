## Translations
### Compile a translation file
`msgfmt de.po --output-file de.mo`
### Create new locale
`msginit --locale=xx --input=name.pot`
### Update Template
` find . -iname "*.py" | xargs  xgettext -L Python -d schoolbot -s --keyword=_ -o ../locales/base.pot`

### Update Locale from Template
`msgmerge --update locales/de/LC_MESSAGES/base.po locales/base.pot`