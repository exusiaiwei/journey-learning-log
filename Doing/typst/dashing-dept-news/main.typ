#import "@preview/dashing-dept-news:0.1.0": newsletter, article

#show: newsletter.with(
  title: [Chemistry Department],
  edition: [
    March 18th, 2023 \
    Purview College
  ],
  publication-info: [
    The Dean of the Department of Chemistry. \
    Purview College, 17 Earlmeyer D, Exampleville, TN 59341. \
    #link("mailto:newsletter@chem.purview.edu")
  ],
)

= The Sixtus Award goes to Purview
123123123
#quote(block: true, attribution: [Prof. Herzog])[
  Our Lab has synthesized the most elements of them all.
]

123123
= 2

#article[
  = 3
123123
]

#article[
  = Safety first
  Next Tuesday, there will be a Lab Safety Training.

  These trainings are crucial for ensuring that all members of the department are equipped with the necessary knowledge and skills to work safely in the laboratory. *Attendance is mandatory.*
]
#article[
  = 4
  Next Tuesday, there will be a Lab Safety Training.

  These trainings are crucial for ensuring that all members of the department are equipped with the necessary knowledge and skills to work safely in the laboratory. *Attendance is mandatory.*
]
#figure(
  rect(width: 100%, height: 80pt, fill: white, stroke: 1pt),
  caption: [Our new department rectangle],
)

#article[
  = Tigers win big
  #text(weight: "bold", font: "Syne", pad(x: 12pt, grid(
    columns: (1fr, auto, 1fr),
    row-gutter: 8pt,
    text(32pt, align(right)[12]),
    text(32pt)[---],
    text(32pt)[4],
    align(right)[Tigers],
    none,
    [Eagles]
  )))

  Another great game on the path to win the League. \
  Go tigers!
]

== Another Success
#lorem(20)

#lorem(20)
