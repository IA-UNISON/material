(TeX-add-style-hook
 "continua_6_2019"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "onecolumn" "letter" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("amsmath" "sumlimits") ("babel" "spanish")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "fourier"
    "inputenc"
    "amsmath"
    "graphicx"
    "babel"
    "amsfonts"
    "amssymb"
    "amsthm"
    "geometry"))
 :latex)

