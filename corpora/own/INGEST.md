# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 300 (the final check needs at least 200)
- Words: 55,617
- Estimated tokens (words times 1.4): 77,863 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 19

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `adrian-dantley` | 116 | - | - | - |
| `adrian-smith-basketball` | 130 | - | - | - |
| `al-horford` | 151 | - | - | - |
| `alex-english` | 226 | - | - | - |
| `alex-groza` | 73 | - | - | - |
| `allan-houston` | 109 | - | - | - |
| `alonzo-mourning` | 170 | - | - | - |
| `alvan-adams` | 82 | - | - | - |
| `alvin-robertson` | 99 | - | - | - |
| `amar-e-stoudemire` | 287 | - | - | - |
| `andre-iguodala` | 285 | - | - | - |
| `andrew-toney` | 432 | - | - | - |
| `antawn-jamison` | 169 | - | - | - |
| `anthony-davis` | 377 | - | - | - |
| `anthony-edwards-basketball` | 164 | - | - | - |
| `antonio-davis` | 89 | - | - | - |
| `austin-carr` | 60 | - | - | - |
| `b-j-armstrong` | 57 | - | - | - |
| `bailey-howell` | 77 | - | - | - |
| `bam-adebayo` | 120 | - | - | - |
| `baron-davis` | 133 | - | - | - |
| `bernard-king` | 111 | - | - | - |
| `bill-bradley` | 397 | - | - | - |
| `bill-bridges-basketball` | 61 | - | - | - |
| `bill-russell` | 609 | - | - | - |
| `bill-sharman` | 303 | - | - | - |
| `bill-walton` | 334 | - | - | - |
| `billy-knight` | 153 | - | - | - |
| `bob-cousy` | 354 | - | - | - |
| `bob-dandridge` | 48 | - | very short (48 words) | - |
| `bob-davies` | 129 | - | - | - |
| `bob-mcadoo` | 198 | - | - | - |
| `bob-rule` | 91 | - | - | - |
| `bobby-wanzer` | 156 | - | - | - |
| `brad-daugherty` | 94 | - | - | - |
| `brandon-ingram` | 166 | - | - | - |
| `brook-lopez` | 133 | - | - | - |
| `buck-williams` | 143 | - | - | - |
| `cade-cunningham` | 168 | - | - | - |
| `calvin-murphy` | 116 | - | - | - |
| `calvin-natt` | 111 | - | - | - |
| `campy-russell` | 50 | - | - | - |
| `carlos-boozer` | 75 | - | - | - |
| `cazzie-russell` | 49 | - | very short (49 words) | - |
| `cedric-ceballos` | 49 | - | very short (49 words) | - |
| `charles-oakley` | 82 | - | - | - |
| `charlie-scott-basketball` | 75 | - | - | - |
| `chauncey-billups` | 236 | - | - | - |
| `chet-walker` | 233 | - | - | - |
| `chris-bosh` | 365 | - | - | - |
| `chris-gatling` | 46 | - | very short (46 words) | - |
| `chris-mullin` | 236 | - | - | - |
| `chris-paul` | 428 | - | - | - |
| `chris-webber` | 216 | - | - | - |
| `christian-laettner` | 192 | - | - | - |
| `chuck-noble` | 69 | - | - | - |
| `clifford-robinson-basketball-born-1966` | 100 | - | - | - |
| `clyde-drexler` | 161 | - | - | - |
| `clyde-lee` | 300 | - | - | - |
| `clyde-lovellette` | 62 | - | - | - |
| `d-angelo-russell` | 152 | - | - | - |
| `dale-ellis` | 88 | - | - | - |
| `dan-issel` | 140 | - | - | - |
| `dan-majerle` | 78 | - | - | - |
| `dan-roundfield` | 137 | - | - | - |
| `dana-barros` | 77 | - | - | - |
| `danny-ainge` | 246 | - | - | - |
| `danny-granger` | 119 | - | - | - |
| `danny-manning` | 140 | - | - | - |
| `darius-garland` | 180 | - | - | - |
| `darrall-imhoff` | 71 | - | - | - |
| `dave-bing` | 294 | - | - | - |
| `dave-debusschere` | 125 | - | - | - |
| `david-lee-basketball` | 139 | - | - | - |
| `david-robinson` | 234 | - | - | - |
| `david-thompson-basketball` | 166 | - | - | - |
| `david-west-basketball` | 91 | - | - | - |
| `de-aaron-fox` | 121 | - | - | - |
| `deandre-jordan` | 252 | - | - | - |
| `dejounte-murray` | 109 | - | - | - |
| `deni-avdija` | 250 | - | - | - |
| `dennis-johnson` | 193 | - | - | - |
| `dennis-rodman` | 380 | - | - | - |
| `deron-williams` | 107 | - | - | - |
| `derrick-rose` | 417 | - | - | - |
| `devin-booker` | 192 | - | - | - |
| `devin-harris` | 78 | - | - | - |
| `dick-barnett` | 84 | - | - | - |
| `dick-garmaker` | 91 | - | - | - |
| `dick-mcguire` | 278 | - | - | - |
| `dick-van-arsdale` | 250 | - | - | - |
| `dikembe-mutombo` | 272 | - | - | - |
| `dirk-nowitzki` | 368 | - | - | - |
| `doc-rivers` | 234 | - | - | - |
| `dolph-schayes` | 170 | - | - | - |
| `domantas-sabonis` | 192 | - | - | - |
| `dominique-wilkins` | 235 | - | - | - |
| `don-barksdale` | 71 | - | - | - |
| `don-buse` | 64 | - | - | - |
| `don-ohl` | 48 | - | very short (48 words) | - |
| `don-sunderlage` | 81 | - | - | - |
| `draymond-green` | 300 | - | - | - |
| `dwyane-wade` | 406 | - | - | - |
| `earl-monroe` | 118 | - | - | - |
| `eddie-johnson-basketball-born-1955` | 216 | - | - | - |
| `eddie-miles` | 178 | - | - | - |
| `elgin-baylor` | 295 | - | - | - |
| `elton-brand` | 87 | - | - | - |
| `elvin-hayes` | 410 | - | - | - |
| `fat-lever` | 49 | - | very short (49 words) | - |
| `frank-selvy` | 88 | - | - | - |
| `fred-brown-basketball` | 73 | - | - | - |
| `fred-vanvleet` | 178 | - | - | - |
| `gary-payton` | 174 | - | - | - |
| `gene-shue` | 328 | - | - | - |
| `geoff-petrie` | 70 | - | - | - |
| `george-mcginnis` | 113 | - | - | - |
| `george-yardley` | 57 | - | - | - |
| `gerald-wallace` | 48 | - | very short (48 words) | - |
| `giannis-antetokounmpo` | 407 | - | - | - |
| `glen-rice` | 124 | - | - | - |
| `glenn-robinson` | 92 | - | - | - |
| `grant-hill` | 412 | - | - | - |
| `gus-johnson-basketball` | 390 | - | - | - |
| `gus-williams-basketball` | 81 | - | - | - |
| `hal-greer` | 96 | - | - | - |
| `horace-grant` | 92 | - | - | - |
| `isaiah-thomas-basketball` | 223 | - | - | - |
| `isiah-thomas` | 273 | - | - | - |
| `ja-morant` | 239 | - | - | - |
| `jack-george-basketball` | 140 | - | - | - |
| `jack-molinas` | 128 | - | - | - |
| `jalen-duren` | 102 | - | - | - |
| `jalen-johnson` | 75 | - | - | - |
| `jalen-williams` | 78 | - | - | - |
| `jamaal-magloire` | 147 | - | - | - |
| `jamal-murray` | 92 | - | - | - |
| `jameer-nelson` | 119 | - | - | - |
| `james-donaldson-basketball` | 64 | - | - | - |
| `james-harden` | 396 | - | - | - |
| `jason-kidd` | 420 | - | - | - |
| `jaylen-brown` | 157 | - | - | - |
| `jayson-tatum` | 201 | - | - | - |
| `jeff-malone` | 67 | - | - | - |
| `jeff-mullins-basketball` | 171 | - | - | - |
| `jeff-ruland` | 78 | - | - | - |
| `jeff-teague` | 107 | - | - | - |
| `jermaine-o-neal` | 196 | - | - | - |
| `jerry-lucas` | 212 | - | - | - |
| `jerry-stackhouse` | 78 | - | - | - |
| `jim-king-basketball-born-1941` | 130 | - | - | - |
| `jim-pollard` | 107 | - | - | - |
| `joakim-noah` | 89 | - | - | - |
| `joe-barry-carroll` | 60 | - | - | - |
| `joe-caldwell` | 86 | - | - | - |
| `joe-dumars` | 140 | - | - | - |
| `joe-fulks` | 49 | - | very short (49 words) | - |
| `joe-johnson-basketball` | 133 | - | - | - |
| `joel-embiid` | 204 | - | - | - |
| `john-block-basketball` | 122 | - | - | - |
| `john-havlicek` | 245 | - | - | - |
| `john-starks` | 63 | - | - | - |
| `john-stockton` | 173 | - | - | - |
| `john-wall` | 144 | - | - | - |
| `johnny-kerr` | 286 | - | - | - |
| `josh-howard` | 56 | - | - | - |
| `julius-erving` | 478 | - | - | - |
| `julius-randle` | 130 | - | - | - |
| `juwan-howard` | 301 | - | - | - |
| `karl-anthony-towns` | 168 | - | - | - |
| `karl-malone` | 386 | - | - | - |
| `kawhi-leonard` | 279 | - | - | - |
| `kelly-tripucka` | 103 | - | - | - |
| `kemba-walker` | 137 | - | - | - |
| `kenyon-martin` | 106 | - | - | - |
| `kevin-duckworth` | 118 | - | - | - |
| `kevin-durant` | 460 | - | - | - |
| `kevin-garnett` | 356 | - | - | - |
| `kevin-johnson-basketball-player` | 278 | - | - | - |
| `kevin-love` | 326 | - | - | - |
| `kevin-willis` | 213 | - | - | - |
| `khris-middleton` | 198 | - | - | - |
| `kiki-vandeweghe` | 40 | - | very short (40 words) | - |
| `klay-thompson` | 338 | - | - | - |
| `kobe-bryant` | 560 | - | - | - |
| `kyle-korver` | 280 | - | - | - |
| `kyle-lowry` | 316 | - | - | - |
| `kyrie-irving` | 357 | - | - | - |
| `lamelo-ball` | 294 | - | - | - |
| `larry-bird` | 555 | - | - | - |
| `larry-foust` | 95 | - | - | - |
| `larry-nance` | 160 | - | - | - |
| `latrell-sprewell` | 105 | - | - | - |
| `lauri-markkanen` | 230 | - | - | - |
| `lebron-james` | 440 | - | - | - |
| `lee-shaffer` | 169 | - | - | - |
| `lenny-wilkens` | 300 | - | - | - |
| `lionel-hollins` | 66 | - | - | - |
| `lou-hudson` | 44 | - | very short (44 words) | - |
| `lucious-jackson` | 75 | - | - | - |
| `luka-doncic` | 331 | - | - | - |
| `luol-deng` | 211 | - | - | - |
| `manu-ginobili` | 356 | - | - | - |
| `marques-johnson` | 142 | - | - | - |
| `maurice-cheeks` | 80 | - | - | - |
| `maurice-lucas` | 199 | - | - | - |
| `maurice-stokes` | 112 | - | - | - |
| `mehmet-okur` | 139 | - | - | - |
| `michael-finley` | 84 | - | - | - |
| `michael-redd` | 107 | - | - | - |
| `micheal-ray-richardson` | 169 | - | - | - |
| `mike-conley-basketball` | 159 | - | - | - |
| `mitch-richmond` | 95 | - | - | - |
| `mo-williams` | 232 | - | - | - |
| `mookie-blaylock` | 39 | - | very short (39 words) | - |
| `moses-malone` | 425 | - | - | - |
| `nat-clifton` | 44 | - | very short (44 words) | - |
| `nate-archibald` | 146 | - | - | - |
| `nate-thurmond` | 142 | - | - | - |
| `neil-johnston` | 122 | - | - | - |
| `norm-nixon` | 71 | - | - | - |
| `norm-van-lier` | 277 | - | - | - |
| `norman-powell` | 140 | - | - | - |
| `otis-birdsong` | 118 | - | - | - |
| `otis-thorpe` | 45 | - | very short (45 words) | - |
| `pascal-siakam` | 243 | - | - | - |
| `paul-arizin` | 81 | - | - | - |
| `paul-george` | 248 | - | - | - |
| `paul-pierce` | 259 | - | - | - |
| `paul-seymour-basketball` | 87 | - | - | - |
| `paul-silas` | 145 | - | - | - |
| `paul-westphal` | 166 | - | - | - |
| `peja-stojakovic` | 373 | - | - | - |
| `penny-hardaway` | 85 | - | - | - |
| `pete-maravich` | 223 | - | - | - |
| `phil-chenier` | 41 | - | very short (41 words) | - |
| `phil-smith-basketball` | 53 | - | - | - |
| `ralph-beard` | 58 | - | - | - |
| `rasheed-wallace` | 318 | - | - | - |
| `ray-felix` | 66 | - | - | - |
| `reggie-miller` | 238 | - | - | - |
| `richard-hamilton-basketball` | 233 | - | - | - |
| `richie-guerin` | 380 | - | - | - |
| `rickey-green` | 212 | - | - | - |
| `ricky-pierce` | 53 | - | - | - |
| `rolando-blackman` | 70 | - | - | - |
| `rudy-larusso` | 44 | - | very short (44 words) | - |
| `rudy-tomjanovich` | 252 | - | - | - |
| `russell-westbrook` | 367 | - | - | - |
| `sam-cassell` | 169 | - | - | - |
| `sam-lacey` | 208 | - | - | - |
| `scott-wedman` | 59 | - | - | - |
| `scottie-barnes` | 220 | - | - | - |
| `sean-elliott` | 127 | - | - | - |
| `shai-gilgeous-alexander` | 327 | - | - | - |
| `shaquille-o-neal` | 409 | - | - | - |
| `shareef-abdur-rahim` | 270 | - | - | - |
| `shawn-kemp` | 120 | - | - | - |
| `shawn-marion` | 108 | - | - | - |
| `sidney-wicks` | 90 | - | - | - |
| `stephen-curry` | 488 | - | - | - |
| `stephon-marbury` | 137 | - | - | - |
| `steve-francis` | 99 | - | - | - |
| `steve-johnson-basketball` | 33 | - | very short (33 words) | - |
| `steve-mix` | 53 | - | - | - |
| `steve-smith-basketball` | 161 | - | - | - |
| `terrell-brandon` | 60 | - | - | - |
| `terry-cummings` | 57 | - | - | - |
| `tim-duncan` | 343 | - | - | - |
| `tim-hardaway` | 107 | - | - | - |
| `tom-chambers-basketball` | 305 | - | - | - |
| `tom-gola` | 367 | - | - | - |
| `tom-heinsohn` | 195 | - | - | - |
| `tom-meschery` | 123 | - | - | - |
| `tony-parker` | 318 | - | - | - |
| `tracy-mcgrady` | 264 | - | - | - |
| `trae-young` | 151 | - | - | - |
| `truck-robinson` | 210 | - | - | - |
| `tyler-herro` | 114 | - | - | - |
| `tyrese-maxey` | 238 | - | - | - |
| `tyrone-hill` | 294 | - | - | - |
| `tyson-chandler` | 167 | - | - | - |
| `vern-mikkelsen` | 126 | - | - | - |
| `victor-oladipo` | 275 | - | - | - |
| `vin-baker` | 42 | - | very short (42 words) | - |
| `vince-boryla` | 266 | - | - | - |
| `vlade-divac` | 264 | - | - | - |
| `wally-szczerbiak` | 66 | - | - | - |
| `walt-bellamy` | 474 | - | - | - |
| `walt-hazzard` | 118 | - | - | - |
| `wayne-embry` | 102 | - | - | - |
| `wes-unseld` | 187 | - | - | - |
| `willie-naulls` | 188 | - | - | - |
| `willis-reed` | 189 | - | - | - |
| `wilt-chamberlain` | 530 | - | - | - |
| `woody-sauldsberry` | 42 | - | very short (42 words) | - |
| `world-b-free` | 56 | - | - | - |
| `xavier-mcdaniel` | 40 | - | very short (40 words) | - |
| `zelmo-beaty` | 383 | - | - | - |
| `zydrunas-ilgauskas` | 146 | - | - | - |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
