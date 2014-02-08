all:  jslint 

jslint:
		cat fulljslint.js rhino.js > fulljslint_rhino.js
		java -jar ../yuicompressor-2.4.2.jar fulljslint_rhino.js > jslint.js
