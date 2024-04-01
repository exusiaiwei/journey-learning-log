#import "@preview/touying:0.3.3": *

#let s = themes.simple.register()
#let (init, slides) = utils.methods(s)
#show: init

#let (slide, empty-slide) = utils.slides(s)
#show: slides

= Title

== First Slide

Hello, Touying!

#pause

Hello, Typst!