__author__ = 'Kevin Schreiber'

# Do I have any classes I need to define?

#Lets do a title screen

print(
    """

;+'++;#:#'##;#'#+:#'++'@:#++#'#++#+#;+;+#;+;#++';';+';;;+;@';+'+'#'+';+'+''';';+'#';';+;#''':+;+:++;+;++;++#'#++++@'#;#'#++#'+'#+##'#'@'@;#+###++
;':''++:+;+',+'+''+#'''+;#'@#'#+@+++'#''++++:++:;;;;++:;:'+'+''+'+++;+;+':#'+,''#+'+,+''+'#''+'''+''+'++';'+;++''#+;':+;++++:+,+'#+:#:+:#,+#+@'@'
;';#'':;+;#;'#+#+';'#'+#'';++':;#'++'''::''+:+';'+++'';'++++'#'#++#'''####'#'+###'''++++';';+++''+:+:;+'+';#'''#'+#'+;+'#+++;';;'#+''::;':'';';;:
+''+''''++#++#'##'#+##'#;#'+#'#'++'+:':+':;:''';:+,'+::;+';';;:''+''':+;+';::';#;;+:+:'+++'+'#'#+;;';'';+'+'';'+:#+++'+'+;#'+;'''+'++'+'+'+'#++':
;#;#@#@;+;@+:#;##:#'++'#:+:++;':+''';';+';+:+'+;'';++';;+;#+'':+;+'+;:',#;';:';+':+:+:''+#;#;@;++++;#;++'''+'++''++;#++++'++;:';:#'++'''+'+:+'+''
,':+;#;'+;+;:+'#';+;@'#+;+'#++#'#+@#'#''++;;;'+'#';''+#;''+;#''+'#'#''+'+''+;';#;+';+'#;++:+:+:+;'+;':+@;@;#'#+:#;#;#'+++#'#:#;#+++'@'@'###+;#;#'
;+'#'#++;+';',;':;.::++';;;+;';;++++;+:++;'.'+#'++,#++;'+;+++#;@;#'+':+'++++:;'''#;';++'+;;;;'+';#''''++++'#;+#'++#'++#'++;+;':++'#:+;+';+;+;#;@;
';''+#+++;#+;#++#'#;+++#'@;#++#:##'#:#;#+:+:+;'+;':#+:+:+:++'+;+:+;;+:+:'+;+;+;'#'#:+'+#+#'#:#+++;:;';''';:;;'+:;:+'''+'#+'+'''++++;+'#+#'++:+;':
'#:#;+#'@'##;':+''';+:'+:+:+'++;#:#';+:+';''+'#+'+''+++;+'+'##'#'+''+;+'#+'';+:'':+;+,++'+:';##'#++'#++#+#++''++'++++'#'#'+:;';::#'+'++'+'#;''+++
:':+:#'#';#+++'';::,,:;'''+++#+####++'':;+:',++'+;;';';;:;'++;'#+#+##;'+#'+;';+#+++;'+++@+++'##++++;;;:,,.,,.::,;:';';'#:@'@+##+'++#++'+'+';+''#'
++'''+'@++''@:.````````````````````````````,'#++'+++++++,`````````````````````````````+'#;';'#++'#',``````` ` ```````````````````:;:'+:::+,+,+'+#
'#+#+##+++#@'.````` ````````````````````````.;+;'':++'#'.``````````````````````````````+:+:'+##'#';.``````````` ` ```````````````.+;##:;:':',+''#
'#;#;#;++'#@'.`` `` `````````````````````````'+'#+'###''.`````````````````````` ```````''+'+;+#+'''.``````.#@@@@@@@@@@@#@@@```````+'''#+''++'#+++
''+';#+#++@+'`````````````:,:`````````````` `+''+;;;,+';.````````` ```` ``````  ```````:+;'''#+#''',`````.#,@@@@@@@@#@#++@,#.`````@#+@'#;+'+:+'+'
+++'++#+'+++'.```````````;+''++```````````` `'#++''#+++'```  `  ``  ````  ```````   ```.+';':+'+''',`````.#;:.':```````@,.@:;`````@+;#:@'+#'#'+;#
'#+++#+##+@#;``` ` ```````.'''``````` ````` `;+++#;+#++'.`       ``:@```:++`````     ``.'#'++'##''',`````.+,@;``` ` ` ```##,+`````##++:+;#++';;:'
#++#'#;+'+@#'.``    ```````''++'';``` ```````;#'#';++++'.``   `  `'##+;++.:+#,`   `  ```'''++'++''',`````.#,@`````    ````#,#.````;''''''+;+;';'+
+'++;#'#++@+'```   ``''+;++'++:,''''.`````` `'+;;:;+;+''.``   `` ``##.`.#+#```````  ````':;''#+#'';:``  ``@,@`` ``     ` `@,#`````+#+@###++':''+'
''@'#+'+''#';`````````'''`.'',``.'''++````` `'+#+#'##+''.``   ``''#+``'.`.,@,+```    ```'+#+#+++''':``   `@.@`      ``` ``@,#.````:+,+:+';#:#:@;+
+:+#';'++'@+:````   ``.+''''';+';'+```````  `;;;+';'++''.``   ``.#;##@,+':#,+#' @,`` ` `;':+++#+''':`    `#.@``       ````#,#`````,#;#;++:+;':+;+
+,++;+:+;+@+:``   ``````;,.'''+''```    `````++'+#+++#+',`   ``;#.:,++.#,##':``:,.`    `;':++'''''':``   `#.@``        ```+:@.``` .''++#'+;'''++#
#;####+''+@',```  ``   ````''.``  `  ` `  ` `+;+;;;':#'',`   `,,``.+#'.:+#@;``  `     ``';;;''''''';``  ``#,#````     ````+:+``````#+@##+++;;;+;+
':#'+':#'#@+,```    ``````.''``       ` `  ` ;@;@#+###+':`      `:@.##.#'+#,` `       ``;#+#+##++'';``  ``+,#.```     ````;''.`````+;+#'#;+;#+##'
#;+++@;+'+@',```       ` `.''``        ` `  `;+;++;++++':`      `+.`+:.'#@@.+``        `:++++:#'''';``   `;,#+ `    ``````:#;.`````#'#+'';':;+,+:
+:#'+';+;#@',```         `.'+``              '#'#+;++++':``     `.#+::#+````##.`       `,+'#+'';+';;.    `::#,#@`` `````,@.#,:`````+'+'++'''#'##'
''+##++:+'#+,``          `.;'``        ``   `+''+;+''@+';``                `           `,''+'+'++'';.`    ,+@#` #@````,#`..#,;`````@+#+#+';:#;''+
'+#+######@+.``          `.':`             ``'+'##:+#;+';`      `      `      ``       `.+++;++++';;.`     +#.``` `....,,,::@``````'+;#;@;#+'''#'
;,+:':;#;##',``          ```               ``:+'#;;+++'';`                              `#+:''@++'';.`                 ``.````` ```#+;+:';+#:+,#:
''''+'+;+'@+.`                             ``'+++'+';+'';`                              `+#;':+;+'';.`     `            `  ` `   ``''++'++#+'+'+;
+'#+@+++###+,`                             ``+#'''++';'''``                            `.+''#'#+''';,``               `          ``#+++,'';:':;';
+:+,++:+;##':,.```````````  ``            ``,;'@+#'##;'';:.````````````````````````````.'#+#+;+;#'';;;;;;;;;;;:;:;:;;;:;;;;::::::;'##:@;#@++:':++
+;+'##+:'+#'';';'';';';;';';;;;;;;;;:::::,::++#+#+'+#+'';;;;;;;;;;;;;;;;;;;';;;;;;;;;;;;+'':';+#;+;;;';;;;;;';;';;;;;;;;;;'';;'''@+++;+:'#;#,+,#+
','+++''+###';;;;;;'';';'''';';;';;'';;;;';';##;+;+;;;'';;;;;;;';;;;;;;;';;;';';;;;;';'#;++;+'#':+;+;;',+;++;#;+:+;;#;@;#;##:+,:;':##;#++#:+:','+
#;+,'@:+,+#:'.++:',+',+,+''#:#:+@+++##;@;+#:+;#++#'##;+;++;+,@:#++#:##:+,#+++;':#;;+:+:+;;;::'+'';;+''+;+'+'';,+;+':','.'+;@'#+''''+''''#+'''#;+'
';';#+;+;+'++;+''+;#';':#'#+:+:+';+'+',':+':':'''':+':',+;';,'.;;:',+;.;.+':+`','':+:++;#;++##++'+'+;''+:'+'+';+'#''+;+;'':.:,:'+;#;@+#+';+;'+;#'
;+:';+;.+,+','''':'''''';;+:'.;+'';'+:':'+'';'#+':'#;;''#;';'';#+'';#+:';#+':,::';,,:+'..,;,;+:'.+++#:@'+''+;+'+++'';;;;#';';+'++;#,##@#'###@;;'#
#'+;+''+'##++;#@;#:++;#;#;++;+;'#'+#++;#+##'+++'++:+:;''':;:+''+'+:;:,+;++'#,;,;+:';;+''+:+;++;+:+';',+:'#;+;####;#:#';',:.';;':,;';#+#';''++:;:'
::',++,';+;;+,++,',',;;,+;+',''+',';'+:+:'+:'';+:+:++;#,+''#;+++#;#++';+'++,+:++::.':,;.:,;:;';#'++'#;+'@':',+;+':',;:'+:+:#+#+;+;+:#'+;:,:;:''++
##';+#+;';++.''#;'';++''''++;;'##++'@';#;##;#'+';+'+';',';:',';;',+''',+;:+;+:';++:#++#:#;++++;#+#+:#;++#;,:;';';;'++;#+++'@+#';':+:'#'@+#'+;''';
;';:'';+:++';;+#,#:#++#;#:+#:''#+'';+::;;+;;'';:',;,,,:'+,:;;'++';;;':';;##'''''+';+##';++@+'''':'+,'.'::+;#++#'#'#++';;':'#+#+;''+'+'.':#+;#+#'#
+;+;'+:':+',+:++,;,++:','+,+,';;@:;#:#:#'+#'+#;#;#+##;#+++;#;+#;#:#++#'++++'+++++:++'';':'+:'''+++#;+'@+;+,+:'',+,++'#;+:###+++:';+;'::;'#+#++++#
'##'+#';'#++:;'#''+##++;'''+'+;++'+'++:#:++;+;:':+;+':+:+',':+','.+',',++:':+:;#;+'+#;#;++++;#:+''''';',;,;:'#+'+;#+'+:':'+''.+,++'@'##+++:;:'+'+
'';;;';:';;;:,';:''++'':+'+';:++''''+:;;'#:'''+:':;+,''+#;;:;++'';++'''#';+;+;#+;+;+',';'+;+;#;++;+'+#+#''+''';'''+'''''++''':;;+';::;''++#'+#+'#
"""
)

print("Welcome to Mahjong for Python!\n\n")


#call main menu

def mainmenu():
    print("1. New Game")
    print("2. Load Game")
    print("3. Exit\n",)
    choice = input("Please make a selection\n>")
    if choice == "1":
        print("non-functional\n\n")
        mainmenu()
    if choice == "2":
        print("non-functional as well\n\n")
        mainmenu()
    if choice == "3":
        exit()
    if choice == "4":
        print("Debug mode enabled\n\n\n")
    else:
        print("Invalid choice\n\n")
        mainmenu()


mainmenu()


#lets get into newgame I guess

#we will need to create a class for a tile...

class Tile(object):

    VALUES = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
              "East", "South", "West", "North",
              "White", "Red", "Green"]

    SUITS = ["Bamboo", "Dots", "Numbers", "Wind", "Dragon"]

    def __init__(self, suit, value, unique, location):
        self.suit = suit
        self.value = value
        self.__unique = unique
        self.__location = location

    def __str__(self):
        rep = "A " + self.value + "tile of " + self.suit
        return rep

#so lets try creating a tile (everything from here down is a bit messy and needs to be redone)

B11 = Tile("Bamboo","1","1","Table")


#lets create our hand --> This needs to be a class object instead of a list, since we can have 4 players

playerhand = []


#put that in our hand?
#we need to define a moving action

def addtohand(the_tile, hand):
    the_tile.location = hand
    hand.append (the_tile)

addtohand(B11, playerhand)

print(playerhand)

print(B11)

exit()